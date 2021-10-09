# 1762. Buildings With an Ocean View
# ----------------------------------------------------------------------------------------------------------------------
# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the
# buildings in the line.
#
# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without
# obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.
#
# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
# ----------------------------------------------------------------------------------------------------------------------
# Example 1:
#     Input: heights = [4,2,3,1]
#     Output: [0,2,3]
#     Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
#
# Example 2:
#     Input: heights = [4,3,2,1]
#     Output: [0,1,2,3]
#     Explanation: All the buildings have an ocean view.
#
# Example 3:
#     Input: heights = [1,3,2,4]
#     Output: [3]
#     Explanation: Only building 3 has an ocean view.
#
# Example 4:
#     Input: heights = [2,2,2,2]
#     Output: [3]
#     Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.
# ----------------------------------------------------------------------------------------------------------------------
# Constraints:
#     1 <= heights.length <= 10^5
#     1 <= heights[i] <= 10^9
# ----------------------------------------------------------------------------------------------------------------------

from typing import List, Deque, Iterable
from collections import deque
from array import array

# Runtime: 688 ms, faster than 79.26% of Python3 online submissions for Buildings With an Ocean View.
# Memory Usage: 27.3 MB, less than 99.98% of Python3 online submissions for Buildings With an Ocean View.
class Solution2:
    def findBuildings(self, heights: List[int]) -> Iterable[int]:
        # Edge cases where we don't need to do anything.
        if not heights:
            return array('B')
        if len(heights) == 1:
            return array('B', [0])

        answer = array('I')
        tallest: int = 0
        # Required since pop from `heights` as we loop over it to reduce peak memory use.
        num_buildings: int = len(heights)

        # Note that we use a for loop instead of `while heights: heights.pop` so we can preserve indexes more easily.
        for index in reversed(range(num_buildings)):
            current: int = heights.pop()
            # If nothing taller to the right, it has an ocean view, append to answers list.
            if current > tallest:
                answer.append(index)
                tallest = current

        # Like Solution0, appending while we iterate backward over `heights` means it's currently in descending order.
        answer.reverse()
        return answer


# ----------------------------------------------------------------------------------------------------------------------
# Runtime: 676 ms, faster than 89.05% of Python3 online submissions for Buildings With an Ocean View.
# Memory Usage: 27.9 MB, less than 99.92% of Python3 online submissions for Buildings With an Ocean View.
class Solution1:
    def findBuildings(self, heights: List[int]) -> Deque[int]:
        # Edge cases where we don't need to do anything.
        if not heights:
            return deque([])
        if len(heights) == 1:
            return deque([0])

        answer: Deque[int] = deque()
        tallest: int = 0
        # Required since pop from `heights` as we loop over it to reduce peak memory use.
        num_buildings: int = len(heights)

        # Note that we use a for loop instead of `while heights: heights.pop` so we can preserve indexes more easily.
        for index in reversed(range(num_buildings)):
            current: int = heights.pop()
            # If nothing taller to the right, it has an ocean view, append to answers list.
            if current > tallest:
                answer.appendleft(index)
                tallest = current

        return answer

# Runtime: 676 ms, faster than 89.05% of Python3 online submissions for Buildings With an Ocean View.
# Memory Usage: 27.9 MB, less than 99.92% of Python3 online submissions for Buildings With an Ocean View.
class Solution1:
    def findBuildings(self, heights: List[int]) -> Deque[int]:
        # Edge cases where we don't need to do anything.
        if not heights:
            return deque([])
        if len(heights) == 1:
            return deque([0])

        answer: Deque[int] = deque()
        tallest: int = 0
        # Required since pop from `heights` as we loop over it to reduce peak memory use.
        num_buildings: int = len(heights)

        # Note that we use a for loop instead of `while heights: heights.pop` so we can preserve indexes more easily.
        for index in reversed(range(num_buildings)):
            current: int = heights.pop()
            # If nothing taller to the right, it has an ocean view, append to answers list.
            if current > tallest:
                answer.appendleft(index)
                tallest = current

        return answer


# ----------------------------------------------------------------------------------------------------------------------
# Runtime: 684 ms, faster than 82.41% of Python3 online submissions
# Memory Usage: 28.4 MB, less than 99.49% of Python3 online submissions
class Solution0:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Edge cases where we don't need to do anything.
        if not heights:
            return []
        if len(heights) == 1:
            return [0]

        answer: List[int] = []
        tallest = 0
        # Required since pop from `heights` as we loop over it to reduce peak memory use.
        num_buildings = len(heights)

        # Note that we use a for loop instead of `while heights: heights.pop` so we can preserve indexes more easily.
        for index in reversed(range(num_buildings)):
            current = heights.pop()
            # If nothing taller to the right, it has an ocean view, append to answers list.
            if current > tallest:
                answer.append(index)
                tallest = current

        # We iterated `heights` backward, so our current list is descending, but we want ascending.
        answer.reverse()
        return answer
