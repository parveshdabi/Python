





#count letters ,spaces, numbers in a string
a= "this is g00gl3.com"

character=0
digit=0
spaces=0
other=0

for i in a:
    if i.isalpha():
        character +=1
    elif i.isnumeric():
        digit +=1
    elif i.isspace():
        spaces +=1
    else:
        other +=1
print("the number of total character in string",len(a))
print("the number of alphabate",character)
print("the number of digit",digit)
print("the number of sspaces",spaces)
print("the number of otherr char",other)



#remove duplicate element
a= [1,198,21,198,21,21,34,21,46,18,18]
b=[]
for i in a:
    if i not in b:
        b.append(i)
#b=set(b)
print(b)


#find max min
a= {24,-2100,0,-19,235,18,356,36000,21,46}

print("largest number:",max(a))
print("smallest number:",min(a))


a=[24,-2100,0,-19,235,18,356,36000,21,46]
def maxmin(a):
    maxi=a[0]
    mini=a[0]
    for i in a:
        if  i >maxi:
            maxi=i
        elif i< mini:
            mini=i
    print(maxi)
    print(mini)
maxmin(a)



list1=[24,-2100,0,-19,235,18,356,36000,21,46]
def find_len(list1):

    list1.sort()
    print("largest number",list1[-1])
    print("smallest number",list1[0])
find_len(list1)


#recursion
n=int(input("enter a number"))
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
print(fact(n))



