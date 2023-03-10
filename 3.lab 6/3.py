import re
s = str(input("Please enter word: "))
def isPalindrome(s):
	l_pos = 0
	r_pos = len(s) - 1
	
	while r_pos >= l_pos:
		if not s[l_pos] == s[r_pos]:
			return False
		l_pos += 1
		r_pos -= 1
	return True
print(isPalindrome(s)) 