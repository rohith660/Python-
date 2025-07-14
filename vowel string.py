s="python programming"
a=" "
vowels="AaEeIiOoUu"
for i in s:
    if i not in vowels:
        a=a+i
print(a)

#counting vowels
s=input("enter string")
vowels="AaEeIiOoUu"
c,v=0,0
for i in s:
    i.isspace()
    if i in vowels:
        v+=1
    else:
        c+=1
print("vowels is",v)
print("consonents is",c)


#special character
a=input("enter the string")
b="!@#$%^&*"
c=0
for i in a:
    if i in b:
        c+=1
print(c)


#replacing vowels with 
a=input("enter the string")
b="aeiouAEIOU"
c=''
for i in a:
    if i in b:
        c+="#"
    else:
        c+=i
print(c)


def isisomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        map1, map2 = {}, {}
        for i in range(len(str1)):
            ch1, ch2 = str1[i], str2[i]
            if ch1 not in map1:
                map1[ch1] = ch2
            if ch2 not in map2:
                map2[ch2] = ch1
            if map1[ch1] != ch2 or map2[ch2] != ch1:
                return False
    return True


str1 = "abacba"
str2 = "xpxcpx"
print(isisomorphic(str1, str2))












