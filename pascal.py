# rows = int(input("Enter your number:"))
# k = 1

# for i in range(1,rows+1):
#     for l in range(1,rows-i+1):
#         print(" ",end="")
#     for j in range(0,i):
#         if j == 0 or i == 0:
#             k=1
#         else:
#             k = k*(i-j)//j
#         print(k,end=" ")
#     print()
#first we use factorial

# def facto(a):
#     s=1
#     for i in range(1,a+1):
#         s*=i
#     return s

# rows = int(input("Enter the value: "))
# for i in range(rows+1):


#     for j in range(rows-i+1):
#         print(" ",end="")


#     for k in range(i+1):
#         ele = facto(i)/(facto(k)*facto(i-k))  #we use ncr = n! / ( r! * (n-r)! )
#         print(int(ele),end=" ")
#     print()


#strong number: sum of the factorial of the digit equal to that number


#prime number: only divisibe by 1 and that number

# this will be the prime

#perfect number: sum of the proper diviser equal to that number


#amstrogn number: sum of the power of the lenth of that number equal to that number


