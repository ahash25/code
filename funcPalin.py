def isPalindrome(string):
    pal=1
    left_pos=0
    right_pos=len(string)-1
    while(right_pos >= left_pos):
        if string[left_pos] == string[right_pos]:
            left_pos=left_pos+1
            right_pos=right_pos-1
        else:
            pal=0
            break;
    if pal==1:
         print(string,"is a palindrome")
    else:
         print(string,"is not a palindrme")
isPalindrome("mom")
isPalindrome("father")
