
lst = [1,3,3,5,5,5]
n = 3
m = (2 * n) - 2
ind = 0
k = 0
pro = [0,0,0]

for i in range(n):  
   for j in range(m):  
      print(end=" ")  
   m = m - 1

   for j in range(i + 1):  
      print(lst[ind], end=" ")
      ind +=1
      pro[k]+=1
   print(" ")
   k +=1
for i in range(n):
   print("Row",i,"=",lst[i*2],"*",pro[i],"=",lst[i*2]*pro[i])

