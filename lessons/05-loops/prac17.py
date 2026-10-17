nums = (1,2,4,16,25,36,49,25)
a = int(input("Enter Number to Search :"))
i = 0 

while i < len(nums):
    if a == nums [i]:
        print (f"Number found in tuple at index {i}")
        break
    else :
        print (f"Number NOT found in tuple at index {i}")
    i +=1 

