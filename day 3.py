'''def rot_arr(arr,k):
    n=len(arr)
    k=k%n
    arr.reverse()
    arr[:k]=reversed(arr[:k])
    arr[k:]=reversed(arr[k:])
    return arr

arr=[1,2,3,4,5,6,7]
k=12
print(rot_arr(arr,k))'''

'''def rot_arr(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5, 6, 7]
k = 12
print(rot_arr(arr, k))'''


'''a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(a, b):
    s = str(i)
    if len(set(s)) > 1: 
        print(i)'''

def is_pall(s):
    return s==s[::-1]
def split_into_pall(s):
    n=len(s)
    for i in range(1,n):
        for j in range(i+1,n):
            p1=s[:i]
            p2=s[i:j]
            p3=s[j:]
            if is_pall(p1) and is_pall(p2) and is_pall(p3):
                return[p1,p2,p3]
            else :
                return "non"
    return[]
s="malayalambusazeeza"
result=split_into_pall(s)
for part in result:
    print(part)


