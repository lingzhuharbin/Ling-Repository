# test while loop
x = 1;
s = 0
while (x < 10):
     s = s + x
     x = x + 1
     if (x == 5):
          break
else :
     print('The sum of first 9 integers : ',s)        
print('The sum of ',x,' numbers is :',s) 

# break in for loop
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
num_sum = 0
count = 0
for x in numbers:
    num_sum = num_sum + x
    count = count + 1 
    if count == 5:
        break
print("Sum of first ",count,"integers is : ", num_sum)
