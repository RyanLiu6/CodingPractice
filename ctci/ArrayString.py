import pytest

from typing import List


class ArrayString:
    def is_unique(self, string: str) -> bool:
        """
        Is Unique: Implement an algorithm to determine if a string has all unique characters.

        Approach: Use frequency map and if character c already exists, we return False.

        Runtime: O(n) -> Have to iterate over all characters of string
        Space: O(n) -> string is unique then we have a dictionary of size n

        What if you cannot use additional data structures?

        Approach: Sort input string and then compare neighbours

        Runtime: O(n log n) + O(n) = O(n log n)
        Space: O(1) -> Sort must be in-place sort
        """
        freq_map = {}
        for c in string:
            if c in freq_map:
                return False
            else:
                freq_map[c] = 1

        return True

        # No data structures -> Assume we can just sort
        prev = None
        string = sorted(string)
        for curr in string:
            if curr == prev:
                return False
            prev = curr

        return True

    def check_permutation(self, first: str, second: str) -> bool:
        """
        Given two strings, write a method to decide if one is a permutation of the other.

        Permutation: Same letters and same amounts, just in different order

        Approach: Use frequency map - fill it up with characters from first string, and subtract
            with characters from second string.

            If character from second string isn't in the frequency map, we can return False early.
            Else, check if frequency map is empty at the end.

        Runtime: O(n + m) -> Have to iterate over both strings
        Space: O(n) -> If strings are not permutations of each other and hence unique, store n elements
            and return False
        """
        freq_map = {}
        for item in first:
            if item in freq_map:
                freq_map[item] += 1
            else:
                freq_map[item] = 1

        for item in second:
            if item in freq_map:
                count = freq_map[item]
                lowered = count - 1
                if lowered == 0:
                    del freq_map[item]
                else:
                    freq_map[item] = lowered
            else:
                return False

        # Check if freq_map is empty
        return len(freq_map) == 0

    def urlify(self, string: str) -> str:
        """
        Write a method to replace all spaces in a string with '%20'.

        You may assume that the string has sufficient space at the end to hold the additional characters,
        and that you are given the "true" length of the string.

        (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
        """
        return string.replace(" ", "%20")

    def palindrome_permutation(self, string: str) -> bool:
        """
        Given a string, write a function to check if it is a permutation of a palindrome.

        A palindrome is a word or phrase that is the same forwards and backwards.
        A permutation is a rearrangement of letters.

        The palindrome does not need to be limited to just dictionary words.

        Approach: Rely on counting # of characters. At most one character can have an odd count! That character
        is the middle character.

        Runtime: O(n) -> Have to iterate over string
        Space: O(n) -> Frequency map contains n elements at worst case

        Example:
        Input: Tact Coa
        Output: True (permutations:"taco cat'; "atco cta '; etc.)
        """
        if not string:
            return True

        # First assumption - whitespace and case are not important
        string = string.strip().lower().replace(" ", "")

        freq_map = {}
        for c in string:
            if c.isspace():
                continue
            if c in freq_map:
                freq_map[c] += 1
            else:
                freq_map[c] = 1

        middle = False
        for num in freq_map.values():
            if num % 2 == 1 and not middle:
                middle = True
            elif num % 2 == 1 and middle:
                return False

        return True

    def is_palindrome(self, string: str) -> bool:
        # return string == string[::-1]

        start, end = 0, len(string) - 1
        while start <= end:
            if string[start] != string[end]:
                return False

            start += 1
            end -= 1

        return True

    def one_away(self, first: str, second: str) -> bool:
        """
        There are three types of edits that can be performed on strings:
            insert a character,
            remove a character, or
            replace a character.

        Given two strings, write a function to check if they are one edit (or zero edits) away.

        Approach: Frequency Maps and counting!

        First, we create a frequency map of the first word, then, we iterate over the second word
        and if current letter exists in the frequency map, we lower the count by 1. When count reaches
        0, we delete the record. If the current letter does not exist in the frequency map, we add it in.

        Realistically speaking, we can exit early if we add two letters in the iteration of the second word,
        because we are now 2 edits away (one could be replacing, but two must be replacing + inserting / removing)

        Idea is that at the end of iterating through second, return True iff freq_map contains:
        1. 0 elements - no edits
        2. 1 element and value is 1 - insert or remove
        3. 2 elements, each of value 1 - replacing

        Any other case we return False.

        Runtime: O(n + m) -> Have to iterate over both strings in worst case
        Space: O(n) -> Frequency map contains n elements from first string. For characters of the second string,
            we only add once, and second time it happens we return False.

        Example:
        pale, ple -> true
        pales, pale -> true
        pale, bale -> true
        pale, bae -> false
        """
        freq_map = {}
        for c in first:
            if c in freq_map:
                freq_map[c] += 1
            else:
                freq_map[c] = 1

        added = False
        for c in second:
            if c in freq_map:
                count = freq_map[c]
                lowered = count - 1
                if lowered == 0:
                    del freq_map[c]
                else:
                    freq_map[c] = lowered
            else:
                if added:
                    return False
                freq_map[c] = 1
                added = True

        if len(freq_map) > 2:
            return False

        for value in freq_map.values():
            if value > 1:
                return False

        return True

    def string_compression(self, string: str) -> str:
        """
        Implement a method to perform basic string compression using the counts of repeated characters.


        If the "compressed" string would not become smaller than the original string, your method should return the original string.
        You can assume the string has only uppercase and lowercase letters (a - z).

        Approach: Iterate over the string and count!

        Runtime: O(n) -> Have to iterate over input string in the worst case (assuming string append is constant)
            If string append is not constant, which is a fair assumption -> O(n + k^2) where k is the number of sequences.
        Space: O(n) -> Compressed string can contain at most n - 1 elements before we return False.

        Example:
        aabcccccaaa -> a2b1c5a3.
        """
        compressed = ""
        n = len(string)

        count = 1
        prev = curr = string[0]
        for i in range(1, n):
            curr = string[i]
            if curr != prev:
                to_add = f"{prev}{count}"
                if len(compressed) + len(to_add) >= n:
                    return string
                else:
                    compressed += to_add
                    count = 1
                    prev = curr
            else:
                count += 1

        if count != 0:
            compressed += f"{prev}{count}"

        return compressed if len(compressed) < n else string

    def rotate_matrix(self, matrix: List) -> None:
        """
        Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.

        Can you do this in place?

        Approach: Rotating based on indices! From the below example, we see that
        [0, 0] -> [0, 2]
        [0, 1] -> [1, 2]
        [0, 2] -> [2, 2]

        [1, 0] -> [0, 1]
        [1, 1] -> [1, 1]
        [1, 2] -> [2, 1]

        [2, 0] -> [0, 0]
        [2, 1] -> [1, 0]
        [2, 2] -> [2, 0]

        The pattern we can establish is that:
        [0, 0] -> [0, n], [0, 1] -> [1, n] ... [0, n] -> [n, n]
        [1, 0] -> [0, n - 1] ... [1, n] -> [n, n - 1]
        ...
        [n, n] -> [n, 0]

        Runtime: O(n^2)
        Space: O(1)

        Actual Approach: Transpose and then Reverse. In context of Matrices, Rotation = Transpose * Reverse
            Transpose: reflection along the diagonal axis
            Reverse: reflection along the middle y axis

        Runtime: O(n^2)
        Space: O(1)

        Example:
        [1, 2, 3]          [7, 4, 1]
        [4, 5, 6]    ->    [8, 5, 2]
        [7, 8, 9]          [9, 6, 3]
        """
        n = len(matrix)
        if len(matrix[0]) != n:
            raise ValueError("Matrix is not NxN")

        """
        1. Swap approach
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
        """
        # 2. Manual transpose and reflect
        self.transpose(matrix)
        self.reflect(matrix)

        """
        3. Similar Math approach (reverse first and then transpose)
        matrix.reverse()

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        """

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


    def zero_matrix(self, matrix: List) -> List:
        """
        Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.

        Approach: Want to achieve this with reduced work. We first iterate matrix and mark down rows and columns that are 0.
        Afterwards, we work on those rows and columns to make them all 0.

        Runtime: O(m*n) -> Have to iterate over entire matrix, possibly three times
        Space: O(m + n) -> In the worst case, all rows and columns are 0 and we store that information.

        Can we do this in-place?
        Yes! Take advantage of the fact that if there's any 0s, we set row and column to be 0. This means that we can use
        first row as zero_rows and first column as zero_cols! We just have to first check if the first row / column has
        a 0. If it does, mark it down so that later, we can turn the first row / column to 0 as well.
        """
        zero_cols = []
        zero_rows = []

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)

        for row in zero_rows:
            for j in range(m):
                matrix[row][j] = 0

        for col in zero_cols:
            for i in range(n):
                matrix[i][col] = 0

        return matrix

    def string_rotation(self, first: str, second: str) -> bool:
        """
        Assume you have a method isSubstring which checks if one word is a substring of another.

        Given two strings, first and second, write code to check if second is a rotation of first using only one call to isSubstring

        Approach: String rotation is easy to figure out with a frequency map, since we'd just be looking at the # of characters and if they match.
        However, the question asks us to use is_substring. The solution that comes out of this is simple - string rotation is simply appending
        the string to itself and splicing a new string of length n from that "double" string. Hence, we can do the same backwards.

        Runtime: O(???) -> Depending on implementation of is_substring! Could be O(1) or O(n) where n is input to is_substring -> O(n + m)
        Space: O(2n) = O(n) -> Create a new string by appending first to itself so 2n

        Example:
        "waterbottle" is a rotation of"erbottlewat"
        """
        double = f"{first}{first}"
        return self.is_substring(second, double)

    def is_substring(self, first: str, second: str) -> bool:
        if not first or not second:
            return False
        return first in second


class TestArrayString:
    @pytest.fixture
    def solution(self):
        return ArrayString()

    def test_is_unique(self, solution):
        assert solution.is_unique("") == True
        assert solution.is_unique("asdf") == True
        assert solution.is_unique("qwerty") == True
        assert solution.is_unique("aabc") == False

    def test_check_permutation(self, solution):
        assert solution.check_permutation("", "") == True
        assert solution.check_permutation("a", "") == False
        assert solution.check_permutation("asdf", "dsaf") == True
        assert solution.check_permutation("asdf", "qwerty") == False

    def test_palindrome_permutation(self, solution):
        assert solution.palindrome_permutation("") == True
        assert solution.palindrome_permutation("tact coa") == True
        assert solution.palindrome_permutation("tact cota") == False

    def test_is_palindrome(self, solution):
        assert solution.is_palindrome("") == True
        assert solution.is_palindrome("aba") == True
        assert solution.is_palindrome("taco") == False

    def test_one_away(self, solution):
        assert solution.one_away("pale", "ple") == True
        assert solution.one_away("pale", "pales") == True
        assert solution.one_away("pale", "bale") == True
        assert solution.one_away("pale", "bae") == False

    def test_string_compression(self, solution):
        assert solution.string_compression("aabcccccaaa") == "a2b1c5a3"
        assert solution.string_compression("aaabcccccaaa") == "a3b1c5a3"
        assert solution.string_compression("abbb") == "abbb"

    def test_rotate_matrix(self, solution):
        input_matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        expected_matrix = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        solution.rotate_matrix(input_matrix)

        assert input_matrix == expected_matrix

    def test_zero_matrix(self, solution):
        input_matrix = [
            [1,2,3],
            [0,2,1],
            [6,7,0,]
        ]

        n = len(input_matrix)
        m = len(input_matrix[0])

        """
        Rows 1 and 2 are zero
        Cols 0 and 2 are zero

        Thus the elements that are NON-empty:
        [1, 1]
        """
        output_matrix = solution.zero_matrix(input_matrix)

        zero_rows = [1,2]
        for row in zero_rows:
            for j in range(m):
                assert output_matrix[row][j] == 0

        zero_cols = [0,2]
        for col in zero_cols:
            for i in range(n):
                assert output_matrix[i][col] == 0

        non_zero_rows = [i for i in range(n) if i not in zero_rows]
        non_zero_cols = [j for j in range(m) if j not in zero_cols]

        for row in non_zero_rows:
            for col in non_zero_cols:
                assert output_matrix[row][col] != 0

    def test_string_rotation(self, solution):
        assert solution.string_rotation("erbottlewat", "waterbottle")
