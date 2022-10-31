s = '()'
for char in range(0 ,len(s) ,2):
    if s[char] == '(' and (s[char +1] != ')' or s[char +2] != ')'):
        print(False)
    if s[char] == '{' and (s[char +1] or s[char +2] != '}'):
        print(False)
    if s[char] == '[' and (s[char +1] or s[char +2] != ']'):
        print(False)
    else: print(True)
