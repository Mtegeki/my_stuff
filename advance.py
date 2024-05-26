'''class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"{self.name}, {self.age}")
    def __del__(self):
        print("object imefutwa kikamilifu")

#p1 = person("Anord", 23)
class vector:
    def __init__(self, y ,x):
        self.y = y
        self.x = x
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"X : {self.x} Y: {self.y}"
v1 = vector(10, 20)
v2 = vector(30, 70)
v2v = vector(50, 50)
v3 = v1 + v2 + v2v
print(v3)
class man_string:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return man_string(self.name + other.name * 10)
cls_1 = man_string(12)
cls_2 = man_string(13)
cls_3 = cls_1 + cls_2
print(cls_3.name)
print(cls_1.name)
x = ["anord", "mtegeki", "anjelina"]
for i in range(1, 13):
    print(i*i)
'''
def my_generatot(n):
    for i in n:
        yield i

list1 = ["anord","mtegeki", "Alex"]
value = my_generatot(list1)
print(next(value))

print(next(value))


def my_funv():
    for x in range(50):
        yield x
        print(next(x))


my_funv()

alph = ['A','B','C','D','E','F','G','H','I','J']
for i in alph:
    x = len(alph)+1
    y = int( x / 2) - 1
    print(i)
    if i == alph[5-1]:
        break
      


print(alph[5-1])