filename = input("enter your file name")
study = open(filename,'r')
noofwords = 0

for i in study:
    word = i.split()
    print(word)
    noofwords = noofwords + len(word)
    
print(noofwords)
