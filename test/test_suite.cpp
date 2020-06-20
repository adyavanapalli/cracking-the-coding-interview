// test_suite.cpp

#include "gtest/gtest.h"

extern "C"
{
    #include <stdbool.h>

    #include "problem-01-01.c"
    #include "problem-01-02.c"
    #include "problem-01-03.c"
    #include "problem-01-04.c"
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

TEST(chapter_01_tests, urlify_returns_url_with_spaces_replaced_by_escaped_characters)
{
    // Arrange.
    char* url_in = (char*)malloc(35 * sizeof(char));
    strncpy(url_in, "www.google.com?search=tupac shakur", 35);

    char* url_out_expected = (char*)"www.google.com?search=tupac%20shakur";

    // Act.
    char* url_out_actual = urlify(url_in);

    // Assert.
    ASSERT_STREQ(url_out_expected, url_out_actual);

    free(url_in);
}

TEST(chapter_01_tests, urlify_returns_same_url_if_there_are_no_spaces)
{
    // Arrange.
    char* url_in = (char*)malloc(35 * sizeof(char));
    strncpy(url_in, "www.google.com?search=tupac_shakur", 35);

    char* url_out_expected = (char*)"www.google.com?search=tupac_shakur";

    // Act.
    char* url_out_actual = urlify(url_in);

    // Assert.
    ASSERT_STREQ(url_out_expected, url_out_actual);

    free(url_in);
}

TEST(chapter_01_tests, is_palindrome_permutation_returns_true_for_a_palindrome)
{
    // Arrange.
    char* palindrome = (char*)"taco cat";

    // Act.
    bool result = is_palindrome_permutation(palindrome);

    // Assert.
    ASSERT_TRUE(result);
}

TEST(chapter_01_tests, is_palindrome_permutation_returns_true_for_a_permuted_palindrome)
{
    // Arrange.
    char* permuted_palindrome = (char*)"tact coa";

    // Act.
    bool result = is_palindrome_permutation(permuted_palindrome);

    // Assert.
    ASSERT_TRUE(result);
}

TEST(chapter_01_tests, is_palindrome_permutation_returns_false_for_a_non_palindrome)
{
    // Arrange.
    char* non_palindrome = (char*)"tack coa";

    // Act.
    bool result = is_palindrome_permutation(non_palindrome);

    // Assert.
    ASSERT_FALSE(result);
}

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
