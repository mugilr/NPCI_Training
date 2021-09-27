
name = ["Ram", "Som", "Raju", "Khan"]
math = [85, 75, 55, 35]
phy = [81, 96, 66, 55]
chi = [91, 99, 88, 63]

def percentage(i, j, k):
   sum = i+j+k
   return (sum/300)*100

for i in range(len(name)):
   cnt=0
   if (math[i] < 50):
      cnt+=1
   if (phy[i] < 50):
      cnt+=1
   if (chi[i] < 50):
      cnt+=1
   if (cnt == 1):
      print(str(name[i]+ "  Re-appearing student"))
   elif (cnt > 1):
      print(str(name[i]+ "  Fail student"))
   else:
      per = 0
      per = percentage(math[i], phy[i], chi[i])
      if (per >= 80):
         print(str(name[i]+ " Distinction"))
      elif (per >= 60):
         print(str(name[i]+ " First Division"))
      elif (per >= 50):
         print(str(name[i]+ " Second Division"))

