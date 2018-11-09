file=open('File55.txt', 'w')
file.write("Line1\n")
file.write("Line2\n")
file.write("Line3\n")
file.write("Last line.")

file.close()

f=open("File55.txt")
print(f.readline(),end='')
print(f.readline(),end='')



