def Palindrome(string):
    string=string.lower()
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            break;
        else:
            return "palindrome"
            
    
 
output = Palindrome("malAyaLam")
print(output) 
