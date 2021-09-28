import time

tp=(9,8,7,(9,8,7,(9,2,1,(1,2))))

temp = tp
print(tp)
k = []
k_ = []
cnt =0
while tp:
    k.append(k_)
    k_ = []
    print(k)
    for i in tp:
        print("i",i)
        if isinstance(i,tuple):
            tp=i
            print("ISIN",tp)
            cnt +=1
            print("Level",cnt)
        else:
            k_.append(i)
        print(k_,"Original ", k)
        #time.sleep(1)
        if len(tp) == 2:
            k.append(list(tp))
            print(tp)
            cnt +=1
            print(cnt)
            tp = []
            break
    

print("Total Levels - ", cnt)

print(k)
s = " "
for i in temp:
    for j in k:
        if i in j:
            print(s*(k.index(j)+1),i)
        else:
            print(s*(k.index(j)+1),"-")
            

