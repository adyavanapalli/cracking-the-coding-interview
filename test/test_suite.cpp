// test_suite.cpp

#include "gtest/gtest.h"

extern "C"
{
    #include <stdbool.h>

    #include "problem-01-01.c"
    #include "problem-01-02.c"
}

TEST(chapter_01_tests, cstring_has_unique_characters_returns_true_if_cstring_has_unique_characters)
{
    // Arrange.
    char* alphanum = (char*)"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN"
                            "OPQRSTUVWXYZ";

    // Act.
    bool is_unique = cstring_has_unique_characters(alphanum);

    // Assert.
    ASSERT_TRUE(is_unique);
}

TEST(chapter_01_tests, cstring_has_unique_characters_returns_false_if_cstring_has_repeated_characters)
{
    // Arrange.
    char* alphanum = (char*)"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN"
                            "oPQRSTUVWXYZ";

    // Act.
    bool is_unique = cstring_has_unique_characters(alphanum);

    // Assert.
    ASSERT_FALSE(is_unique);
}

TEST(chapter_01_tests, cstrings_are_permutations_returns_true_when_strings_are_permutations)
{
    // Arrange.
    char* s1 = (char*)"abcd";
    char* s2 = (char*)"cdab";

    // Act.
    bool are_permutations = cstrings_are_permutations(s1, s2);

    // Assert.
    ASSERT_TRUE(are_permutations);
}

TEST(chapter_01_tests, cstrings_are_permutations_returns_false_when_strings_contain_same_characters_but_are_not_permutations)
{
    // Arrange.
    char* s1 = (char*)"abcd";
    char* s2 = (char*)"cdabb";

    // Act.
    bool are_permutations = cstrings_are_permutations(s1, s2);

    // Assert.
    ASSERT_FALSE(are_permutations);
}

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
