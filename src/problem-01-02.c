// problem-01-02.c

#include <stdbool.h>
#include <string.h>

bool cstrings_are_permutations(char* s1, char* s2)
{
    // We assume here that the alphabet consists of the printing ASCII
    // characters, which total 95 characters.
    int character_frequency[95];
    memset(character_frequency, 0, 95 * sizeof(int));

    size_t s1_strlen = strlen(s1);
    size_t s2_strlen = strlen(s2);

    if (s1_strlen != s2_strlen)
    {
        return false;
    }

    for (size_t i = 0; i < s1_strlen; i++)
    {
        character_frequency[s1[i] - ' ']++;
        character_frequency[s2[i] - ' ']--;
    }

    for (size_t i = 0; i < s1_strlen; i++)
    {
        if (character_frequency[s1[i] - ' '] != 0)
        {
            return false;
        }
    }

    return true;
}
