// problem-01-01.c

#include <stdbool.h>
#include <string.h>

bool cstring_has_unique_characters(char* cstring)
{
    // We assume here that the alphabet consists of the printing ASCII
    // characters, which total 95 characters.
    bool has_seen_character[95];
    memset(has_seen_character, 0, 95 * sizeof(char));

    size_t cstring_strlen = strlen(cstring);
    for (size_t i = 0; i < cstring_strlen; i++)
    {
        if (has_seen_character[cstring[i] - ' '])
        {
            return false;
        }

        has_seen_character[cstring[i] - ' '] = true;
    }

    return true;
}
