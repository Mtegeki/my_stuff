a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
b = "Hello, World!"
print(b[5:10])

sta = " Hellow enord  nakupenda"
#print(sta.strip())
#print(sta.replace("e", "a").strip())
x = "nord" in sta
print(x)
x = "nord" not in sta
print(x)
newlist =["orange", "chery", "mango", "Tomato","Kiwi"]
newlist.append("apple")
print(newlist[1:])
tp = ("mango","orange","banana","kiwi")
y = list(tp)
y[1] = "apple"
x = tuple(y)
print(x)
thisset = {"anord","anjelina","mtegeki"}

thisset.update(["Alex","anania","samia"])
thisset.add("Emanuel")
print(thisset)
thisdic = {
    "name" : "anord",
    "nation" : "Tanzania",
    "age" : 23
}
for i in thisdic:
    print(thisdic[i])

for x ,y in thisdic.items():
    print(x,y)



lbd = lambda a : a * 10
print(lbd(5))
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))