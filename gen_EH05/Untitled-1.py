array1 =[1,2]  
array2 =[2]     


c = 0
array3 = []
for i in array1:
    for j in range (1,i+1):
        array3.append(array2[c])
    c+=1
sum=0
print(array3)