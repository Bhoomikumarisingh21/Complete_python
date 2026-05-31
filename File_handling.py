#write file
f = open("demo.txt","w")
f.write("Hello Python")
f.close()

#read file
f = open("demo.txt","r")
print(f.read())
f.close()