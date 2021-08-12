"""
Leetcode question #1249: Minimum Remove to Make Valid Parentheses

Given a string s of `(` , `)` and lowercase English characters.

Your task is to remove the minimum number of parentheses ( `(` or `)`, in any positions ) so that the resulting
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    - It is the empty string, contains only lowercase characters, or
    - It can be written as `AB` (A concatenated with B), where `A` and `B` are valid strings, or
    - It can be written as `(A)`, where `A` is a valid string.
"""

from typing import Deque, List
from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Edge case, empty string is valid and needs no additional checks.
        if s == '':
            return s

        # Edge case, one char input string.
        if len(s) == 1:
            if s != '(' and s != ')':
                return s
            else:
                return ''

        # Increment balance when passing `(`, decrement when passing `(`.
        balance: int = 0
        # Note for other langs: this can be an unsigned int; we will never decrement it.
        open_parens: int = 0

        # !! This loop fails test_example_4() !!
        #    - Popping rightmost opening parens only means that in example 4, the `(` at index 0 is preserved, but not
        #      needed. Instead `(` at index 4 is removed, pushing `b` and `c` into the grouping.
        #    - Opened bug since this is the sample solution approach 3 describes, but the approach appears flawed, even
        #      when testing with the sample code provided. Test case in leetcode grader for example 4 appears missing.
        #      https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/4458
        #
        # First pass, remove extra end parens. Use deque so we can consume this list with popleft() in the second pass.
        # Doing so will reduce peak memory usage.
        buffer: Deque[str] = deque()
        for c in s:
            if c == '(':
                # Note: In other language solution attempts, see if SIMD can be used to simultaneously increment these.
                #       Store them together in an array.
                balance += 1
                open_parens += 1
            if c == ')':
                # If we see a close paren, but have no open parens waiting to be closed, we know it is invalid and must
                # be discarded. Don't append it to the resulting string, just continue next iter of the for loop.
                if balance == 0:
                    continue
                balance -= 1
            buffer.append(c)

        # Second pass: remove extra '(' from the right side of the string.
        keep_open: int = open_parens - balance
        result: List[str] = []
        while buffer:
            c = buffer.popleft()
            if c == '(':
                keep_open -= 1
                if keep_open < 0:
                    continue
            result.append(c)

        return ''.join(result)
