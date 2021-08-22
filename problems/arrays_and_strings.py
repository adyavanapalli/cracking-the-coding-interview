"""ArraysAndStrings.py"""

from typing import List


def IsUnique(s: str) -> bool:
    """Determines if s has all unique characters.

    >>> IsUnique("")
    True

    >>> IsUnique("abc")
    True

    >>> IsUnique("aa")
    False

    >>> IsUnique("aabc")
    False

    >>> IsUnique("abca")
    False

    >>> IsUnique("abcab")
    False

    >>> IsUnique("giraffe")
    False
    """

    character_exists = 128 * [False]

    for ch in s:
        if character_exists[ord(ch)]:
            return False

        character_exists[ord(ch)] = True

    return True


def CheckPermutation(s1: str, s2: str) -> bool:
    """Determines if s1 is a permutation of s2.

    >>> CheckPermutation("", "")
    True

    >>> CheckPermutation("a", "aa")
    False

    >>> CheckPermutation("ab", "aa")
    False

    >>> CheckPermutation("ab", "ba")
    True

    >>> CheckPermutation("racecar", "carrace")
    True

    >>> CheckPermutation("cars", "scar")
    True

    >>> CheckPermutation("bus", "sub")
    True

    >>> CheckPermutation("bob", "frank")
    False
    """

    character_count = 128 * [0]

    if len(s1) != len(s2):
        return False

    for ch in s1:
        character_count[ord(ch)] += 1

    for ch in s2:
        character_count[ord(ch)] -= 1

    return sum(map(lambda count: abs(count), character_count)) == 0


def URLify(s: str) -> str:
    """Replaces all spaces in a string with "%20".

    >>> URLify("Mr John Smith")
    'Mr%20John%20Smith'

    >>> URLify("MrJohnSmith")
    'MrJohnSmith'

    >>> URLify("Jack and Jill went up the hill")
    'Jack%20and%20Jill%20went%20up%20the%20hill'
    """

    characters = []
    for ch in s:
        characters.append(ch if ch != " " else "%20")

    return "".join(characters)


def PalindromePermutation(s: str) -> bool:
    """Determines if s is a permutation of a palindrome.

    >>> PalindromePermutation("")
    True

    >>> PalindromePermutation("a")
    True

    >>> PalindromePermutation("Tact Coa")
    True

    >>> PalindromePermutation("ace CarR")
    True

    >>> PalindromePermutation("race cars")
    False
    """

    character_count = 128 * [0]

    s_stripped_and_lowercased = "".join([ch for ch in s if ch != " "]).lower()

    for ch in s_stripped_and_lowercased:
        character_count[ord(ch)] += 1

    odd_character_count_allowed = len(s_stripped_and_lowercased) % 2 == 1
    encountered_odd_character_count = False

    for count in character_count:
        if count % 2 == 1:
            if not odd_character_count_allowed or encountered_odd_character_count:
                return False

            encountered_odd_character_count = True

    return True


def OneAway(s1: str, s2: str) -> int:
    """Determines if s1 and s2 are less than one edit away.

    >>> OneAway("pale", "ple")
    True

    >>> OneAway("pales", "pale")
    True

    >>> OneAway("pale", "bale")
    True

    >>> OneAway("pale", "bake")
    False
    """

    def edit_distance(s1: str, s2: str):
        if len(s2) == 0:
            return len(s1)
        elif len(s1) == 0:
            return len(s2)
        elif s1[0] == s2[0]:
            return edit_distance(s1[1:], s2[1:])
        else:
            return 1 + min(
                [
                    edit_distance(s1[1:], s2),
                    edit_distance(s1, s2[1:]),
                    edit_distance(s1[1:], s2[1:]),
                ]
            )

    return edit_distance(s1, s2) <= 1


def StringCompression(s: str) -> str:
    """Compresses the specified string using counts of repeated characters.

    >>> StringCompression("")
    ''

    >>> StringCompression("a")
    'a'

    >>> StringCompression("ab")
    'ab'

    >>> StringCompression("abc")
    'abc'

    >>> StringCompression("aba")
    'aba'

    >>> StringCompression("aa")
    'a2'

    >>> StringCompression("aab")
    'a2b1'

    >>> StringCompression("aabaa")
    'a2b1a2'

    >>> StringCompression("aabaabbcddeeef")
    'a2b1a2b2c1d2e3f1'

    >>> StringCompression("aabcccccaaa")
    'a2b1c5a3'
    """

    compressed_segments = []

    i = 0
    while i < len(s):
        current_character = s[i]
        count = 1

        while i + 1 < len(s) and current_character == s[i + 1]:
            i += 1
            count += 1

        compressed_segments.append((current_character, count))
        i += 1

    if all(map(lambda x: x[1] == 1, compressed_segments)):
        return s

    compressed_s = "".join(
        [f"{character}{count}" for character, count in compressed_segments]
    )

    return compressed_s


def RotateMatrix(image: List[List[int]]) -> List[List[int]]:
    """Rotates the specified image by 90 degrees.

    >>> RotateMatrix([[0]])
    [[0]]

    >>> RotateMatrix([[0, 1], [2, 3]])
    [[1, 3], [0, 2]]

    >>> RotateMatrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    [[2, 5, 8], [1, 4, 7], [0, 3, 6]]

    >>> RotateMatrix([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    [[3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13], [0, 4, 8, 12]]

    >>> RotateMatrix([[0, 1, 2, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
    [[5, 10, 15, 20, 25], [4, 9, 14, 19, 24], [2, 8, 13, 18, 23], [1, 7, 12, 17, 22], [0, 6, 11, 16, 21]]
    """

    n = len(image)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            image_ij = image[i][j]

            image[i][j] = image[j][n - i - 1]
            image[j][n - i - 1] = image[n - i - 1][n - j - 1]
            image[n - i - 1][n - j - 1] = image[n - j - 1][i]
            image[n - j - 1][i] = image_ij

    return image


def ZeroMatrix(matrix: List[List[int]]) -> List[List[int]]:
    """Sets the element's row and column to zero if the element in the matrix is
    0.

    >>> ZeroMatrix([[0]])
    [[0]]

    >>> ZeroMatrix([[1]])
    [[1]]

    >>> ZeroMatrix([[1, 0]])
    [[0, 0]]

    >>> ZeroMatrix([[1, 2], [0, 4]])
    [[0, 2], [0, 0]]

    >>> ZeroMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    >>> ZeroMatrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
    [[1, 0, 3], [0, 0, 0], [7, 0, 9]]

    >>> ZeroMatrix([[0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    [[0, 0, 0, 0], [0, 6, 7, 8], [0, 10, 11, 12], [0, 14, 15, 16]]
    """

    m = len(matrix)
    n = len(matrix[0])

    zeros = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    for (i, j) in zeros:
        for row_associated_with_col_j in range(m):
            matrix[row_associated_with_col_j][j] = 0

        for col_associated_with_row_i in range(n):
            matrix[i][col_associated_with_row_i] = 0

    return matrix


def StringRotation(s1: str, s2: str) -> bool:
    """Returns whether s2 is a rotation of s1.

    >>> StringRotation("", "")
    True

    >>> StringRotation("a", "")
    False

    >>> StringRotation("", "b")
    False

    >>> StringRotation("a", "a")
    True

    >>> StringRotation("a", "b")
    False

    >>> StringRotation("ab", "ba")
    True

    >>> StringRotation("aba", "bab")
    False

    >>> StringRotation("abc", "acb")
    False

    >>> StringRotation("erbottlewat", "waterbottle")
    True

    >>> StringRotation("kelly", "ellyk")
    True

    >>> StringRotation("erbottlewat", "waterbottle")
    True
    """

    return len(s1) == len(s2) and s2 in (s1 + s1)
