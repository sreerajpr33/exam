# L=[1,2,3,4,4]
# ul=[]
# for i in L:
#     if i not in ul:                        #12
#         ul.append(i)
# print(ul)



# a=65
# for i in range(1,5):
#     for j in range(i,0,-1):                 #14
#         print(chr((a-1)+j),end=" ")
#     print()
    

def factorial():
    f=0
    a=int(input('enter a number to print factorial :'))
    if a>=1:
        for i in range(a):
            f=i*i
        print(f)  
    else:
        print('enter a valid number!')     

factorial()