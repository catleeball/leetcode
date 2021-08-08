# Leetcode question 56: Merge Intervals

from typing import Any, List, Optional


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge all overlapping intervals, consuming the initial list `intervals`."""

        # Edge cases: one or zero intervals. Just return, nothing to merge with.
        if len(intervals) <= 1:
            return intervals

        # Sort time: O(n log n). Allows us to compare and merge intervals in one iteration of the list. Sort descending
        # so that we can pop from the end of the list at O(1) without converting to a deque.
        intervals = sorted(intervals, reverse=True)
        # Accumulate intervals into this new list of consolidated intervals.
        merged_intervals: List[List[int]] = list()
        # Current earliest interval to compare to the next interval for potential merging.
        current_interval: Optional[List[int]] = None

        # Pop intervals off the list, comparing to the current interval. If they overlap, merge them into the new
        # current interval. Popping into the accumulator allows us to save memory overhead of two lists.
        while intervals:
            # First iteration, grab the first two.
            if not current_interval:
                current_interval: List[int] = intervals.pop()
                next_interval:    List[int] = intervals.pop()
            else:
                next_interval:    List[int] = intervals.pop()

            # Validate interval.
            if not current_interval or not next_interval or len(current_interval) != 2 or len(next_interval) != 2:
                raise ValueError('Invalid interval. Must have two ints. '
                                 f'Found:\n  current: {current_interval}\n  next: {next_interval}')

            # Check if intervals overlap. If so, merge into one with the start time of earlier and end time of later and
            # continue popping. Maintain current interval until it's next neighbor can't be merged into it.
            if current_interval[1] >= next_interval[0]:
                current_interval = [current_interval[0], next_interval[1]]
            else:
                merged_intervals.append(current_interval)
                current_interval = next_interval

        # Last iteration we'll still be holding the current interval without having appended it to merged intervals.
        merged_intervals.append(current_interval)
        return merged_intervals
