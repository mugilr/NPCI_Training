
lst = [1,3,5,9, 21]
step = 2
print("Missing Num: ")
for i in range(lst[0],lst[-1],step):
    #print(i)
    if i not in lst:
        print(i,", ")
        

