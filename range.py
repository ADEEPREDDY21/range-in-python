#The range() function in Python is used to generate a sequence of numbers.
# It is commonly used in for loops to iterate over a sequence of numbers. 
# The function can take one, two, or three arguments:
#   - start: The starting number of the sequence
#   - stop: The end of the sequence
#   - step: The difference between each number in the sequence
print("Example for range function in python")
for numbers in range(5):
    print(numbers)

print("print numbers from 3 to 19")

for numbers in range(3,20):#ramge(Start,end) will print the numbers bitween start and end
    print(numbers)
 

for even in range(0,10,2):#here 2 is the stepping value
    print(even)
print("print odd numbers from 0 to 10")   
for odd in range(1,10,2):
    print(odd)#here 2 is the stepping value    
    
print("print numbers in decending order")    
for numbers in range(10,0,-1):
    print(numbers)#here -1 is the stepping value it step back by 1 each time it prints a number from 10 to 1
    
print("convert range values in list")    
number=list(range(12,34,1))
print(number) 

print("Example for range in nested loop")
print("Tables from 1 to 10 ")
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j}={i*j}")
        
print("Example for range and printing square numbers from 1 to 100")        
square=[i**2 for i in range(1,101)]
print(square)

print("print the numbers which are multiples of 3 ")
for r in range(1,31):
    if r%3==0: 
        print(f"{r} is a multiple of 3")
    elif r%5==0:
        print(f"{r} is a multiple of 5")
    else:
        print(f"{r} is not a multiple of 3")   
        
print("Set countdown from 5 to 1")
import time#import keywork ia used to import libraries from packages
for i in range(5,0,-1):
    print(i)         
    time.sleep(0.5)#here time.sleep(1) will hold the out put for 1 second
print("time is up lights off!!")    

print("print * into 5 times")
for r in range(5):
    print("*"   *   (r+1))

print("skip the 4 divisable numbers between 1 to 40")
for r in range(1,41):
    if r%4==0:
        continue
    print(f"{r} is not divisable by 4")
