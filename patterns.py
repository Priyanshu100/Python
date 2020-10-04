# Lets say we want to print a combination of stars as shown below.

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6):
    for j in range(0,i):
        print('*',end = " ")

    for j in range(1,(2*(5-i))+1):
        print(" ",end = "")

    print("")


# Let's say we want to print pattern which is opposite of above:
#  * * * * *
#    * * * *
#      * * *
#        * *
#          *

print(" ")

for i in range(1,6):

    for j in range(0,(2*(i-1))+1):
        print(" ", end="")


    for j in range(0,6-i):
        print('*',end = " ")

    print("")
 
# Let's print star pyramid pattern:
#   *
#  * *
# * * *
#* * * *
size=int(input("Enter the range:"))

for i in range(size):
    for j in range((size-i) - 1):
        print(end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()    
    
 # Now let's print star pyramid pattern in reverse order:
#* * * *
# * * *
#  * *
#   *
size = int(input("Enter the range:"))

for i in range(size,0,-1):
    for j in range(0,size-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()    
