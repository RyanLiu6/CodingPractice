class BigO:
    """
    Additional Problems:
    VI.1: O(b)

    VI.2: O(b)

    VI.3: O(1)

    VI.4:
        Best: O(1)
        Average / Worst: O(a/b)

    VI.5: O(log n)

    VI.6: O(sqrt n)

    VI.7: Unbalanced Search Tree worst case -> O(n)

    VI.8: Looking for specific value in Binary Tree, not a Binary Search Tree (not guaranteed to have order)
        -> time to search is O(n)

    VI.9:
        length of copyArray input array = n

        appendToNew input array length is varied -> call it m
            creates an array of m + 1 and iterates over each element of m
            Runtime -> O(m)

        copyArray runs appendToNew n times, such that the first call m = 0, second call m = 1 ... last is m = n

        Similar to Example 3:
            for i in range(n):
                for j in range(i + 1, n):
                    print(i, j)

            -> Still O(n^2)

        Can think of it as:
            First call -> 0
            Second call -> 1
            Third call -> 2
            ...
            nth call -> n

            O(1 + 2 + 3 ... + n) -> Sum from 1 to n = (n/2)(n + 1) -> O(n^2)

        Total = O(n^2)

    VI.10: O(log n) -> log base 10

    VI.11: what the fuck is this algorithm

        isInOrder operates on input string s -> O(s)

        printSortedStrings(remaining) calls printSortedStrings(remaining, prefix)
            with remaining = remaining and prefix =  ""

        printSortedStrings(remaining, prefix):
            base: remaining == 0, calls isInOrder(prefix)
            else: for each character in the alphabet (26 characters), calls O(1) algo (ithLetter),
                and then calls itself recursively with (remaining = remaining - 1) and prefix = prefix + ithLetter

        Example:
            printSortedStrings(remaining = 1, prefix = "")
                remaining = 1
                i = 0 -> c = a
                printSortedStrings(remaining = 0, prefix = a)
                    remaining = 0
                    isInOrder(a)
                i = 1 -> c = b
                printSortedStrings(remaining = 0, prefix = b)
                    remaining = 0
                    isInOrder(b)
                ...
                i = 25 -> c = z
                printSortedStrings(remaining = 0, prefix = z)
                    remaining = 0
                    isInOrder(z)

            printSortedStrings(remaining = 2, prefix = "")
                remaining = 2
                i = 0 -> c = a
                printSortedStrings(remaining = 1, prefix = a)
                    remaining = 1
                    i = 0 -> c = a
                    printSortedStrings(remaining = 0, prefix = aa)
                        remaining = 0
                        isInOrder(aa)
                    i = 1 -> c = b
                    printSortedStrings(remaining = 0, prefix = ab)
                        remaining = 0
                        isInOrder(ab)
                    ...
                    i = 25 -> c = z
                    printSortedStrings(remaining = 0, prefix = az)
                        remaining = 0
                        isInOrder(az)
                i = 1 -> c = b
                printSortedStrings(remaining = 1, prefix = b)
                    remaining = 1
                    i = 0 -> c = a
                    printSortedStrings(remaining = 0, prefix = ba)
                        remaining = 0
                        isInOrder(ba)
                    i = 1 -> c = b
                    printSortedStrings(remaining = 0, prefix = bb)
                        remaining = 0
                        isInOrder(bb)
                    ...
                    i = 25 -> c = z
                    printSortedStrings(remaining = 0, prefix = bz)
                        remaining = 0
                        isInOrder(bz)

        Total = O(k * (26^k)))

    VI.12:
        length of a = n
        length of b = m

        Assume mergesort on b is O(m log m)

        Assume binary search on b is O(log m)

        sumDigits runs binary search on b for each element in a -> n * log m

        Total = O((m log m) + (n log m)) = O((n + m)(log m))
    """
