import os

f = open("demofile.txt")
print(f.readline())
f.close()

x = open("demofile.txt","a")
x.write("Napenda kuandika vitabu")
x.close()


y = open("demofile.txt", "r")
print(y.read())
y.close() 

#z = open("myfile.html", "w")
if os.path.exists("myfile.html"):
    os.remove("myfile.html")
else:
    print("unajaribu kufuta file ambalo halipo")
#os.remove("myfile.html")
#for x in f:
#   print(x)