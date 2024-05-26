list1 = [12,2,36,87,7]
list2 = [i for i in list1 if i % 2 == 0]
list3 = list1
list_name = ["Anord","Mtegeki","Matako", "Anjelina", "Alex"]
list_name2 = [x for x in list_name if x ==  "Matako"]
print(list_name2)
def gen():
    for i in list_name2:
        yield i
out_r = gen()
#print(next(out_r))
print("kuna lugha za matusi kwenye list na tusi lenyewe ni ",next(out_r))