lst = [['Ram','ram@ab.com',12345],
        ['Som','som@ab.com',67890],
        [],
        ['Khan','khan@ab.com',12315,'Hyd'],
        ['Ram','ram@ab.com',12345,'cdm','698291']
        ]

title = ['Name','Mail','Phone']
f = open('file.txt','w')
f.write('')
f.close()
f = open('file.txt','a+',)
f1 = open('file.txt','r',)

for i in title:
    f.write(str(i))
    f.write(',')

print(f.tell())
for i in lst:
    if len(i)>=3:
        f.write('\n')
        for j in range(0,3,1):
            f.write(str(i[j]))
            f.write(',')
f.close()

# re = f1.read()
# print(re)
