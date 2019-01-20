import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    a = disjoint_intervals
    xlt, xrt = new_interval
    result = []
    n = len(a)
    i = 0
    while i < n:
        if xlt > a[i].left and xlt > a[i].right:
            result.append(a[i])
        elif xlt < a[i].left and xrt > a[i].right:
            pass
        elif (xlt >= a[i].left and xlt <= a[i].right) or (xrt >= a[i].left and xrt <= a[i].right):
            xlt = min(xlt, a[i].left)
            xrt = max(xrt, a[i].right)
        else:
            break
        i += 1
    result.append(Interval(xlt, xrt))
    while i < n:
        result.append(a[i])
        i += 1
    return result


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
