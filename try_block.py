try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")

try:
    print("hello world")
except:
    print("something went wrong")
else:
    print("nothing went wrong")

try:
    print(x)
except:
    print("something went wrong")
finally:
    print("try and except block is finished")

try:
    f = open("demox.txt")
    f.write("Hello world")
except:
    print("something went wrong or file you try to accsess is not available")
finally:
    f.close()
x = -1
if x < 0:
    raise Exception("variable x is lower than 0")

y = "hello"
if not type(y) is int:
    raise TypeError("only integes allowed")