f=open('File1.txt', 'r+')
print("B4 write\n")
print(f.read())
#print(f.write('Dodat string'))
f.write('\nDodat string')
f.seek(0)
print(f.readline())
print("\nAfter write \n")
print(f.read())
f.close()
