def is_palindrome(s):
    char_list = [s[i] for i in range(len(s))]
    char_list.reverse()
    s1 = ' '.join(char_list)
    return s == s1

