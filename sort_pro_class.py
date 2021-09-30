
# usr = []
# u1 = {'name':'abc', 'id':1, 'salary':1000}
# u2 = {'name':'bca', 'id':2, 'salary':100}
# u3 = {'name':'cab', 'id':3, 'salary':5000}
# p1 = []
# p1.append(u2)
# p1.append(u1)
# p2 = []
# p2.append(u3)

# pro = []
# pro.append(p1)
# pro.append(p2)
# # pro.append(u3)
# print(pro)
# so_pi = []
# for i in pro:
#     so_pi.append(sorted(i, key=lambda i:i['salary'], reverse=True))
# print(so_pi)

# print("Project 1 ",pro[0])



class user():
    def __init__(self,i,na,s,k,msg):
        self.id = i
        self.name = na
        self.salary = s
        self.des = k
        self.msg=msg
    def get_salary(self):
        print(self.salary)

class project():
    def __init__(self,i,n,usr):
        self.id = i
        self.name = n
        self.user = usr

# class project_efo():
#     def __init__(self,e,):
#         self.ef= e



us = []
us.append(user("U1","ABC",100,"A1","OU"))
us.append(user("U2","BCA",400,"A2","UU"))
us.append(user("U3","CAB",600,"A3","OU"))

pro = []
pro.append(project(1,"ABC",[[us[0],40],[us[2],20]]))
pro.append(project(2,"BCA",[us[1]]))
print("Project class")
for i in pro:
    print(i.id, [[j.id, j.salary]for j in i.user])
# so_us = []
# for i in pro:
#     print(i.id, [[j.id, j.salary]for j in i.user])
#     j=i.user
#     print(j.salary)
#     so_us.append(sorted(j, key=lambda j:j.salary))

# print(so_us)
# for i in so_us:
#     print(i.salary)

def part1(salary, k):
    for i in k:
        if i.salary == salary:
            print("U_ID -",i.id, "Salary -", i.salary)
            pass

for i in pro:
    print("Pro Id -",i.id)
    l = [j.salary for j in i.user]
    for j in sorted(l,reverse=True):
        # print("Pro ID -",i.id)
        part1(j,i.user)

dic = {}
for i in pro:
    for j in i.user:
        dic[i.id,j.name] = j.salary
for i in sorted(dic.values(),reverse=True):
    for k,v in dic.items():
        if v==i:
            print("Pro ID -",k,"Salary",i)

pro_d = {}
def get(s,l):
    for i in l:
        if i.salary == s:
            return [i.id, i.name, i.salary]
for i in pro:
    l1 =[]
    l = [j.salary for j in i.user]
    for j in sorted(l,reverse=True):
        l1.append(get(j,i.user))
    pro_d[i.id,i.name] = l1
for k,v in pro_d.items():
    print(k,v)

