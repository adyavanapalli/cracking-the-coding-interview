// problem-01-05.c

#include <stdbool.h>
#include <stdio.h>
#include <string.h>

size_t max(size_t i, size_t j)
{
    return i > j ? i : j;
}

size_t min(size_t i, size_t j)
{
    return i < j ? i : j;
}

size_t min_3(size_t i, size_t j, size_t k)
{
    return min(min(i, j), k);
}

int levenshtein(char* s1, size_t i, char* s2, size_t j)
{
    if (min(i, j) == 0)
    {
        return max(i, j);
    }

    int l1 = levenshtein(s1, i - 1, s2, j    ) + 1;
    int l2 = levenshtein(s1, i    , s2, j - 1) + 1;
    int l3 = levenshtein(s1, i - 1, s2, j - 1) + (s1[i - 1] != s2[j - 1] ? 1 : 0);

    return min_3(l1, l2, l3);
}

bool is_one_or_less_away(char* s1, char* s2)
{
    size_t s1_strlen = strlen(s1);
    size_t s2_strlen = strlen(s2);

    return levenshtein(s1, s1_strlen, s2, s2_strlen) <= 1;
}
