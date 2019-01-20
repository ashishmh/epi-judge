import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    k = -1
    for event in A:
        k = max(event.finish, k)
    arr = [0] * (k + 1)
    for event in A:
        start = event.start
        end = event.finish
        for t in range(start, end + 1):
            arr[t] += 1
    numEvents = -1
    for i in arr:
        numEvents = max(numEvents, i)
    return numEvents


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
