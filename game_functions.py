'''Smit Rao's Proprietary Game Functions'''

import random
from typing import List, Dict
import time


def clean_words(string: str) -> str:
    '''Clean the given words, return cleaned version.
    
    >>> clean_words('mr. xyz h.abc')
    'Mr. Xyz H. Abc'
    '''
    final_str = ''
    for substr in string.split():
        final_str += substr.lower().capitalize()
        final_str += ' '
    return final_str.strip()

def clean_time() -> str:
    '''Return time from time.asctime() cleaned.
    
    ### do not doctest this function as it
    ### relies on accurate time for each line.
    
    >>> import time
    >>> time.asctime()
    'Sun Nov 12 12:20:07 2017'
    >>> clean_time()
    'Sunday, Nov. 12 2017, 12:20:07'
    '''
    import time
    list_time = time.asctime().split()
    if 'Sun' in list_time[0]:
        list_time[0] = 'Sunday'
    if 'Mon' in list_time[0]:
        list_time[0] = 'Monday'
    if 'Tue' in list_time[0]:
        list_time[0] = 'Tuesday'
    if 'Wed' in list_time[0]:
        list_time[0] = 'Wednesday'
    if 'Thu' in list_time[0]:
        list_time[0] = 'Thursday'
    if 'Fri' in list_time[0]:
        list_time[0] = 'Friday'
    if 'Sat' in list_time[0]:
        list_time[0] = 'Saturday'
    list_time[0] += ','
    list_time[1] += '.'
    list_time.append(list_time[3])
    list_time[3] = list_time[-2] + ','
    list_time.pop(-2)
    return ' '.join(list_time)