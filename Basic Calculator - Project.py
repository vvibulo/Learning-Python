#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#creating calculator

#operator recognized
operator=["+","-","*","/","^",'**',':']
#input
expression=input("kalkulasi: ")
#loop through 'expression string to find any operator'
match = [s for s in expression if any(xs in s for xs in operator)]
#not necessary but it remove duplicate, it will messed up calculation step
match1 = list(dict.fromkeys(match))
#print(match)

#filter the operator, get the position of operator in the string
#e.g 2+33-1*2, the position will be 1,4,6
char=[]
for x in match1:
    position = ( [pos for pos, char in enumerate(expression) if char == x])
    #print (position)
    for y in position:
        char.append(y)
char.sort()
#print (char)

#get all the available numbers
number=[]
if len(char)==1:
    q=expression[0:y]
    number.append(q)
    p=expression[y+1:]
    number.append(p)
else:
    for index, y in enumerate(char):
        if index==0:
            p=expression[0:y]
            number.append(p)
        elif index==(len(char)-1):
            q=expression[char[index-1]+1:y]
            number.append(q)
            p=expression[y+1:]
            number.append(p)
        else :
            p=expression[char[index-1]+1:y]
            number.append(p)
print(number)

#where the step become mess, should look for alternative.
#power
dummymatch=match.copy()
dummynum=number.copy()
#print(dummymatch)
#print(dummynum)
y1=0
for i, x in enumerate(match):
    if x=='^' or x=='**':
        if y1==0:
            temp=float(number[i])**float(number[i+1])
            dummynum[i]=temp
            print(temp)
            print(dummynum)
            number[i]=temp
            number[i+1]=temp
            del dummynum[i+1]
            print(dummynum)
            del dummymatch[i]
            print(dummymatch)
            y1=1
            print("y1=",y1)
        else:
            temp=float(number[i])**float(number[i+1])
            dummynum[i+1-y1]=temp
            number[i]=temp
            number[i+1]=temp
            print(temp)
            print(dummynum)
            del dummynum[i-y1]
            print(dummynum)
            del dummymatch[i-y1]
            print(dummymatch)
            y1+=1
            
#multiplication
dummymatch1=dummymatch.copy()
dummynum1=dummynum.copy()
#print(dummymatch1)
print(dummynum1)
y1=0
for i, x in enumerate (dummymatch):
    #print(x)
    if x=='*':
        if y1==0:
            temp=float(dummynum[i])*float(dummynum[i+1])
            print(temp)
            dummynum1[i]=temp
            dummynum[i]=temp
            dummynum[i+1]=temp
            print(dummynum1)
            del dummynum1[i+1]
            print(dummynum1)
            del dummymatch1[i]
            print(dummymatch1)
            y1=1
        else:
            temp=float(dummynum[i])*float(dummynum[i+1])
            print(temp)
            dummynum1[i+1-y1]=temp
            dummynum[i]=temp
            dummynum[i+1]=temp
            print(dummynum1)
            del dummynum1[i-y1]
            print(dummynum1)
            del dummymatch1[i-y1]
            print(dummymatch1)
            y1+=1

#division
dummymatch2=dummymatch1.copy()
dummynum2=dummynum1.copy()
#print(dummymatch2)
#print(dummynum2)
y1=0
for i, x in enumerate (dummymatch1):
    if x=='/' or x==':':
        if y1==0:
            temp=float(dummynum1[i])/float(dummynum1[i+1])
            #print(temp)
            dummynum2[i]=temp
            dummynum1[i]=temp
            dummynum1[i+1]=temp
            del dummynum2[i+1]
            del dummymatch2[i]
            y1=1
        else:
            temp=float(dummynum1[i])/float(dummynum1[i+1])
            #print(temp)
            dummynum2[i+1-y1]=temp
            dummynum1[i]=temp
            dummynum1[i+1]=temp
            del dummynum2[i-y1]
            del dummymatch2[i-y1]
            y1+=1
            
#substraction
dummymatch3=dummymatch2.copy()
dummynum3=dummynum2.copy()
#print(dummymatch2)
#print(dummynum2)

y1=0
for i, x in enumerate (dummymatch2):
    if x=='-':
        if y1==0:
            temp=float(dummynum2[i])-float(dummynum2[i+1])
            dummynum3[i]=temp
            dummynum2[i]=temp
            dummynum2[i+1]=temp
            del dummynum3[i+1]
            del dummymatch3[i]
            y1=1
        else:
            temp=float(dummynum2[i])-float(dummynum2[i+1])
            dummynum3[i+1-y1]=temp
            dummynum2[i]=temp
            dummynum2[i+1]=temp
            del dummynum3[i-y1]
            del dummymatch3[i-y1]
            y1+=1
            
#additin
dummymatch4=dummymatch3.copy()
dummynum4=dummynum3.copy()
#print(dummymatch2)
#print(dummynum2)

y1=0
for i, x in enumerate (dummymatch3):
    if x=='+':
        if y1==0:
            temp=float(dummynum3[i])+float(dummynum3[i+1])
            #print(temp)
            dummynum4[i]=temp
            #print(dummynum4)
            dummynum3[i]=temp
            #print(dummynum3)
            dummynum3[i+1]=temp
            #print(dummynum3)
            del dummynum4[i+1]
            #print(dummynum4)
            del dummymatch4[i]
            #print(dummymatch4)
            y1=1
        else:
            temp=float(dummynum3[i])+float(dummynum3[i+1])
            print(temp)
            dummynum4[i+1-y1]=temp
            
            dummynum3[i]=temp
            dummynum3[i+1]=temp
            #print(dummynum4)
            #print(dummynum3)
            del dummynum4[i-y1]
            #print(dummynum4)
            del dummymatch4[i-y1]
            #print(dummymatch4)
            y1+=1
print(dummynum4)

