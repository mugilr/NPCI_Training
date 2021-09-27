row = 3#int(input("Enter the Rows: "))
diff = 3#int(input("Enter the diff: "))

a = 1
b = 0
flag = True
lst = list()
#PART 1
for i in range(1, row + 1):
    k = 0
    row_ = []
    while k < row  - i:
        print(end = " ")
        k += 1
    for j in range(i):
        if (flag):
            b=a
            flag = False
        print(b, end = " ")
        row_.append(b)
        b+=1
    a += diff
    flag = True
    lst.append(row_)
    print()

#PART 2
print (lst)
i = 1
r_sum  = []
for r in lst:
   print("Row",i,end = " : ")
   sum_ = 0
   for g in r:
      print(g, end=" + ")
      sum_+=g
   r_sum.append(sum_)
   print("=",sum_)
   i+=1
print ("Sum of all row",r_sum," = ", sum(r_sum))

#PART 3
max_r = len(lst[len(lst)-1])
print(max_r)
mat=[]
for i in range(len(lst)-1,-1,-1):
   mat_=[]
   for j in range(len(lst[i])):
      mat_.append(lst[i][j])
   for j in range(max_r-len(lst[i])):
      mat_.append(0)
   mat.append(mat_)
print(mat)

#PART 4
sq_mat = []
sq_mat = [[c*c for c in r] for r in mat]
print(sq_mat)
