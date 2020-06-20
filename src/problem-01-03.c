// problem-01-03.c

#include <assert.h>
#include <stdlib.h>
#include <string.h>

char* urlify(char* s)
{
    size_t s_strlen = strlen(s);
    
    int number_of_spaces = 0;
    for (size_t i = 0; i < s_strlen; i++)
    {
        if (s[i] == ' ')
        {
            number_of_spaces++;
        }
    }

    size_t length_of_urlified_cstring = s_strlen + 2 * number_of_spaces;

    char* t = (char*)calloc(length_of_urlified_cstring, sizeof(char));
    assert(t != NULL);

    for (size_t s_i = 0, t_i = 0; s_i < s_strlen; s_i++)
    {
        if (s[s_i] == ' ')
        {
            t[t_i] = '%'; t_i++;
            t[t_i] = '2'; t_i++;
            t[t_i] = '0'; t_i++;
        }
        else
        {
            t[t_i] = s[s_i]; t_i++;
        }
    }

    for (size_t i = 0; i < length_of_urlified_cstring; i++)
    {
        s[i] = t[i];
    }

    free(t);
    return s;
}
