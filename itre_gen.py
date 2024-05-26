class Topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
values = Topten()
print(values.__next__())

#for i in values:
 #   print("loop start here ", i)
nums = ["anord", "mtegeki", "anjelina", "alex"]
def gen2():
    for i in range(1, 10):
        sg = i*i
        yield sg
val2 = gen2()
print(next(val2))
print(next(val2))
print(next(val2))
print(next(val2))
print(next(val2))
#print(next(gen2()))
def gen(n):
    for i in n:
        yield i
        
my_values = gen(nums)
print(next(my_values))
print(next(my_values))

#print(next(gen()))
