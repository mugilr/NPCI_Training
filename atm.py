atm_cur = {100:2, 200:3, 500:10}
total = 0

usr_bal = {1:2000,2:30000,3:100}
trans={1:[0,0,0],2:[0,0,0],3:[0,0,0]}
def to_bal():
    sum_ = 0
    for k,v in atm_cur.items():
        sum_ += k*v
    return sum_

def wd_action(usr, amt):
    t_amt = amt
    note100 = 0
    note500 = 0
    note200 = 0
    rem = 0
    while(t_amt):
        if t_amt >= 500:
            rem = t_amt%500
            note500 = (t_amt - rem)/500
            print("note 500 ",note500)
            t_amt = rem
        if t_amt >= 200:
            rem = t_amt%200
            note200 = (t_amt - rem)/200
            print("note 200 ",note200)
            t_amt = rem
        if t_amt:
            rem = t_amt%100
            note100 = (t_amt - rem)/100
            print("note 100 ",note100)
            t_amt = rem
        if t_amt:
            print("Transaction Failed!!")
            print("Precise Currency note not avail, either", amt-rem,"or", amt+(100-rem))
            return -1
    o_sum = note500*500+note200*200+note100*100
    print(o_sum)
    if(o_sum != amt):
        print("Line 34 Not equal")
        return -1
    atm_cur[500] -= note500
    atm_cur[200] -= note200
    atm_cur[100] -= note100
        
    usr_bal[usr] -=amt
    for k,v in trans.items():
        if k is usr:
            v[0]=v[1]
            v[1]=v[2]
            v[2]=amt
    print("Avail. Balance", usr_bal[usr])
    print("ATM Balance", to_bal())
    return 0


while True:
    usr = int(input("User_ID ? "))
    total_bal = to_bal()
    print(total_bal)
    wd_max = (90 * total_bal)/100
    print("1 - Mini Statement")
    print("2 - Withdraw")
    do = int(input("Choice ? "))
    if do == 1:
        for k,v in trans.items():
            if k is usr:
                print ("Mini Statement: ",v)
    elif do == 2:
        wd = int(input("Withdraw amt ? "))
        if wd > usr_bal[usr]:
            print("Insufficient Balance!!")
            break
        if wd > wd_max:
            print("Trans Limited to:",wd_max)
            dis = input("Do you want to countinue? (y/n) ")
            if dis == 'y':
                wd = wd_max
            else:
                break
        wd_action(usr, wd)
