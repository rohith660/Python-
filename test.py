#1

'''n = str(input("eneter number"))

ace = 0
dce = 0

for i in range(len(n)-1):
    if n[i] < n[i+1]:
        ace += 1
    elif n[i] > n[i+1]:
        dce += 1

if ace > 0 and dce == 0:
    print("Ascending")
elif dce > 0 and ace == 0:
    print("Descending")
else:
    print("Mixed")'''

#2

s = "engi456neer34ing coll2ege "
result = ""
num = ""

for ch in s:
    if ch.isdigit():
        num += ch
    else:
        if num != " ":
            result += num[::-1]
            num = ""
        result += ch
        
print(result)






