"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ints = sorted([[interval.start, interval.end] for intervals in schedule for interval in intervals])
        #print(ints)
        ans = []
        for i in range(len(ints)):
            if not ans or ints[i][0] > ans[-1][1]:
                ans.append(ints[i])
            elif ints[i][1] > ans[-1][1]:
                ans[-1][1] = ints[i][1]
        return [Interval(ans[i][1], ans[i + 1][0]) for i in range(len(ans) - 1)]