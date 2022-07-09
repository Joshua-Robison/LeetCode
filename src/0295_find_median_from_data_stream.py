"""Implement the MedianFinder class."""
import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        elif len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        return -self.small[0]


if __name__ == "__main__":
    pass
