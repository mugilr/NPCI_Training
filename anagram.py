st1 = 'hello'
st2 = 'leloh'
st3 = 'ollhe'

if len(st1) == len(st2) == len(st3):
    print("possible")
    if set(st1.lower()) == set(st2.lower()) == set(st3.lower()):
        print("Anagram")

else:
    print("Not Anagram")
