import re
import sys
import utils
import heapq


class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        :input: [73, 74, 75, 71, 69, 72, 76, 73]
        :result:[ 1,  1,  4,  2,  1,  1,  0,  0]

        :input:  [55,38,53,81,61,93,97,32,43,78]
        :result: [ 3, 1, 1, 2, 1, 1, 0, 1, 1, 0]
        """
        n = len(temperatures)
        tempDays = {}
        result = [0]*len(temperatures)

        for i in range(n - 1, -1, -1):
            curr = temperatures[i]
            day = 30001
            for j in range(curr + 1, 101):
                if j in tempDays:
                    day = min(day, tempDays[j] - i)

            if day != 30001:
                result[i] = day
            tempDays[curr] = i
        return result

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        n = len(nums)

        for num in nums:
            currSum += num

        expectedSum = n*(n+1)/2

        return int(expectedSum - currSum)

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binStr = bin(n)[2:]
        print(binStr)

        res = re.search(r"/00|11", binStr)
        if res:
            return False
        else:
            return True

    def findInPivoted(self, arr, query):
        pivot = 0

        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                pivot = i + 1

        val1 = utils.binarySearch(arr[:pivot], 0, pivot - 1, query)
        val2 = utils.binarySearch(arr[pivot:], 0, len(arr) - pivot - 1, query)

        if val1 == -1 and val2 == -1:
            return -1
        elif val1 == -1 and val2 != -1:
            return val2
        else:
            return val1

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Either rob this house and 2 house down, or the next house
        R(n) = max(R(n - 2) + nums[n], R(n - 1))
        """
        if not nums:
            return 0

        n = len(nums)
        if n < 2:
            return nums[0]

        robbed = dict.fromkeys(range(n), 0)
        robbed[0] = nums[0]

        robbed[1] = max(nums[1], robbed[0])

        for i in range(2, n):
            val1 = robbed[i - 1]
            val2 = robbed[i - 2] + nums[i]

            robbed[i] = max(val1, val2)

        return robbed[n - 1]

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = dict.fromkeys(nums, 0)
        result = [0]*k

        for i in range(len(nums)):
            freq[nums[i]] += 1

        # maxHeap to get the top 3 values

        return result

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        DP = [[-1 for x in range(len(s))] for y in range(len(s))]
        return self.subPalindrome(DP, s)

    def subPalindrome(self, DP, S):
        count = 0

        for i in range(len(S)):
            for j in range(len(S)):
                if DP[i][j] == -1 and i <= j:
                    substr = S[i:j+1]
                    if self.isPalindrome(substr):
                        count += 1
                    DP[i][j] = 1

        return count

    def isPalindrome(self, str):
        return str == str[::-1]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :input: [7, 1, 5, 3, 6, 4]
        :output: 5 (6-1)
        """
        if not prices:
            return 0

        buy = prices[0]
        maxProfit = 0

        for price in prices:
            buy = min(buy, price)
            profit = price - buy
            maxProfit = max(maxProfit, profit)
        return maxProfit

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        maxSum = -sys.maxsize - 1

        for val in nums:
            currSum = max(val, currSum + val)
            maxSum = max(maxSum, currSum)

        return maxSum

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        resMin = result
        resMax = result

        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = resMin
                resMin = resMax
                resMax = temp

            resMin = min(resMin, resMin*nums[i])
            resMax = max(resMax, resMax*nums[i])

            result = max(result, resMax)

        return result

    def sumOfString(self, str1, str2):
        overflow = False
        lastflow = False
        n = len(str1) - 1
        retStr = ""

        for index in range(n, -1, -1):
            currSum = int(str1[index]) + int(str2[index])
            if overflow:
                currSum += 1
                overflow = False
                if index == 0:
                    lastflow = True

            if currSum > 9:
                overflow = True
                currSum -= 10

            retStr = str(currSum) + retStr

            if lastflow:
                retStr = "1" + retStr

        return retStr

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :input: [2, 7, 11, 15] and 9
        :output: [0, 1]
        """
        hashMap = {}
        n = len(nums)

        for index in range(n):
            hashMap[nums[index]] = index

        for index in range(n):
            minusNum = target - nums[index]
            first = index

            if hashMap.get(minusNum, -1) is not -1 and first is not hashMap[minusNum]:
                return [index, hashMap[minusNum]]

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        :input: [3,2,1,5,6,4] and k = 2
        :output: 5
        """

        # O(nlgn): Regular Sort (MergeSort)
        # return sorted(nums)[len(nums - k]

        # O(n): Quick Select with lth smallest st l = len(nums) - k + 1
        return utils.QuickSelect(nums, len(nums) - k + 1)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        :input: [3,2,2,3], val = 3
        :output: len[2, 2] = 2
        :req: O(1) space
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            if nums[start] is val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1

        return start

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
