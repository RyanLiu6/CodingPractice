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
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1

        maxHeap = []
        for key, value in freqMap.items():
            maxHeap.append((-value, key))

        heapq.heapify(maxHeap)

        retList = []
        for _ in range(k):
            retList.append(heapq.heappop(maxHeap)[1])

        return retList
