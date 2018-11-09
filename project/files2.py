f=open('File2.txt', 'a') #open the file in the append mode
f.write('\nSome appended text') #write to the file
f.close()

f=open('File1.txt')
lines=f.readlines()
for line in lines:
    print(line,end='')


f.close()