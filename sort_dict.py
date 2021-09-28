#Assingment 4
#Sort Dict
dic={'One':'Zoo','Two':'One','Four':'Ball','Three':'Alpha'}
print("Before sort ",dic)
so_dic = {}
for i in sorted(dic,key=dic.get):
    so_dic[i]=dic[i]
print("After Sort ",so_dic)

#Assingment 5
#Sort Diff Components(tuple,set,dict,...)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0     
    j = 0     
    k = l    

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


#arr = [12, 11, 13, 5, 6, 7]
#un_so = {12,2,23,1,21,45}
#un_so = {'1':'3','2':'5','3':'9','4':'1','5':'8'}
un_so = ['Zoo', 'Kafka', 'Alpha', 'HDFS']
n = len(un_so)
arr = []
print("Given array is", un_so)
if isinstance(un_so,tuple):
    for i in un_so:
        arr.append(i)
    mergeSort(arr, 0, n-1)
elif isinstance(un_so, set):
    for i in un_so:
        arr.append(i)
    mergeSort(arr, 0, n-1)
elif isinstance(un_so, dict):
    for i in un_so.items():
        arr.append(i[1])
    mergeSort(arr, 0, n-1)
    print(arr)
mergeSort(arr, 0, n-1)
print("\n\nSorted array is", arr)
