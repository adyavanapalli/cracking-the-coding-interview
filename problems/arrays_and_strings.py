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


# def RotateMatrix(image: List[List[int]]):
#     """Rotates the specified image by 90 degrees.

#     >>> RotateMatrix([[0]])
#     [[0]]

#     >>> RotateMatrix([[0, 1], [2, 3]])
#     [[1, 3], [0, 2]]

#     >>> RotateMatrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#     [[2, 5, 8], [1, 4, 7], [0, 3, 6]]
#     """

#     return image