// problem-01-04.c

#include <assert.h>
#include <stdbool.h>
#include <string.h>

bool is_palindrome_permutation(char* s)
{
    // We assume here that the alphabet consists of the printing ASCII
    // characters, which total 95 characters.
    int character_frequency[95];
    memset(character_frequency, 0, 95 * sizeof(int));

    size_t s_strlen = strlen(s);
    for (size_t i = 0; i < s_strlen; i++)
    {
        if (s[i] == ' ')
        {
            continue;
        }

        character_frequency[s[i] - ' ']++;
    }

    bool has_seen_single_character = 0;
    for (size_t i = 0; i < 95; i++)
    {
        switch (character_frequency[i])
        {
            case 1:
                if (has_seen_single_character)
                {
                    return false;
                }

                has_seen_single_character = true;
                break;
            case 0:
            case 2:
                // Do nothing.
                break;
            default:
                assert(false);
        }
    }

    return true;
}
