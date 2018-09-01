import collections


class SortSearchSolutions:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Two pass with count
        # red = 0
        # white = 0
        # blue = 0
        #
        # for num in nums:
        #     if num == 0:
        #         red += 1
        #     if num == 1:
        #         white += 1
        #     if num == 2:
        #         blue += 1
        #
        # for i in range(len(nums)):
        #     if red > 0:
        #         nums[i] = 0
        #         red -= 1
        #     elif white > 0:
        #         nums[i] = 1
        #         white -= 1
        #     elif blue > 0:
        #         nums[i] = 2
        #         blue -= 1

        # One pass without space
        i, j = 0, 0

        for k in range(len(nums)):
            curr = nums[k]
            nums[k] = 2
            if curr < 2:
                nums[j] = 1
                j += 1
            if curr == 0:
                nums[i] = 0
                i += 1

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Using FreqMap and MaxHeap
        # freqMap = {}
        # for num in nums:
        #     if num in freqMap:
        #         freqMap[num] += 1
        #     else:
        #         freqMap[num] = 1
        #
        # maxHeap = []
        # for key, value in freqMap.items():
        #     maxHeap.append((-value, key))
        #
        # heapq.heapify(maxHeap)
        #
        # retList = []
        # for _ in range(k):
        #     retList.append(heapq.heappop(maxHeap)[1])
        #
        # return retList

        # Using Python Counter
        c = collections.Counter(nums)

        retArr = []

        for key, value in c.most_common(k):
            retArr.append(key)

        return retArr

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Using sorted
        return sorted(nums)[len(nums) - k]

        # Using minHeap
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)

        for _ in range(len(nums) - k):
            heapq.heappop(minHeap)

        return heapq.heappop(minHeap)

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Peak element is greater than its neighbours
        Assume that nums[-1] = nums[n] = -∞
        """
        # O(n) Solution
        n = len(nums)
        if n < 2:
            return 0

        for i in range(n):
            if i == 0 and nums[i] > nums[i + 1]:
                    return i
            if i == n - 1 and nums[i] > nums[i - 1]:
                    return i
            if nums[i - 1] < nums[i] > nums[i + 1]:
                    return i

        # O(logn) Solution
        n = len(nums)
        if n < 2:
            return 0

        return self.peakHelper(nums, 0, n - 1)

    def peakHelper(self, nums, start, end):
        mid = (start + end) // 2

        if mid == 0 and nums[mid] > nums[mid + 1]:
            return mid
        if mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:
            return mid

        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid + 1]:
            return self.peakHelper(nums, mid + 1, end)
        else:
            return self.peakHelper(nums, start, mid - 1)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        retArr = [-1, -1]
        if not nums:
            return retArr

        n = len(nums)
        start, end = 0, n - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        if nums[start] != target:
            return retArr
        else:
            retArr[0] = start

        end = n - 1
        while start < end:
            mid = (start + end) // 2 + 1
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid

        retArr[1] = end

        return retArr

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        retArr = []
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key = lambda i: i.start)

        start, end = intervals[0].start, intervals[0].end

        for interval in intervals:
            if interval.start <= end:
                end = max(end, interval.end)
            else:
                retArr.append(Interval(start, end))
                start = interval.start
                end = interval.end

        retArr.append(Interval(start, end))
        return retArr

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            comp = nums[mid]

            if (target < nums[0]) == (comp < nums[0]):
                comp = nums[mid]
            else:
                if target < nums[0]:
                    comp = -1 << 31
                else:
                    comp = 1 << 31

            if comp == target:
                return mid
            elif comp < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        i, j = 0, col - 1

        while i < row and j >= 0:
            curr = matrix[i][j]
            if curr == target:
                return True
            elif curr < target:
                i += 1
            else:
                j -= 1

        return False
