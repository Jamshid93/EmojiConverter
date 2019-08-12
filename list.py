numbers=[2,3,7,4,5,6]
s =0 

for i in range(len(numbers)):
    if numbers[i] % 2 ==0:
        s+= numbers[i]
print(s) 
