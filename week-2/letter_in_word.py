# write a function return a dictionary counting nums of char appear in a word
# key: get() in dictionary can search and find value with key is possible. If
# key isn't exist, we can assign its to 0 to begin counting. get(key, 0).
# We have just used dictionary and using dict[key] (must contains 1 or
# i + 1) to counting.

def letter_in_word(a_word):
    '''
    this function return a dict with key is a char; value is nums of appearing
    of that char.

    '''
    result_dict = {}

    # thuật toán đếm số lần xuất hiện của từng phần tử trong 1 iterator.
    for x in a_word:
        result_dict[x] = result_dict.get(x, 0) + 1

    return result_dict


if __name__ == '__main__':
    myname = 'quanghuy'
    print(letter_in_word((myname)))
