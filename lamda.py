

lst=list(map(lambda x: int(x),(input("Enter List : ").split(","))))
cut = True
while cut:
    print("1 - Add New Element ")
    print("2 - Create New Dict from list")
    print("3 - Sort in Desc order(Value)")
    s=int(input("Choose One : "))
    cut = False
    if s==1:
        add=int(input("Add Element ? "))
        lst.append(add)
        print(lst)
    elif s==2:
        dic={i:i for i in lst}
        print(dic)
    elif s==3:
        so_lst=sorted(lst,reverse=True)
        dic={i:i for i in so_lst}
        print(dic)
    cut=bool(input("(Press Enter to stop) / (Any key + Enter to countinue) :"))

