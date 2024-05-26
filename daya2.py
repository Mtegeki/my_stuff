mylist = [12,34,12,10,7,36,90,16]
n = len(mylist)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    min_value = mylist.pop(min_index)
    mylist.insert(i, min_value)
print("sorted array is :", mylist)

prev1 = 0
prev2 = 1
for i in range(18):
    newfbcc = prev1 + prev2
    print(newfbcc)
    prev2 = prev1
    prev1 =  newfbcc
my_array = [12,34,12,10,7,36,90,16]
min_num = my_array[0]
for i in my_array:
    if i < min_num:
        min_num = i
print("min value is : ", min_num)
my_list = [12,34,12,10,7,36,90,16]
n =  len(my_list)
for i in range(n-1):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
print("sorted array : ", my_list)
my_array2 = [64, 34, 25, 12, 22, 11, 90, 5]
n =  len(my_array2)
for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if my_array2[j] < my_array2[min_index]:
            min_index = j
    my_array2[i],my_array2[min_index] = my_array2[min_index],my_array2[i]
print("sorted array is : ", my_array2)
my_array3 = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array3)
for i in range(1,n):
    insert_index = i
    current_value = my_array3.pop(i)
    for j in range(i-1, -1, -1):
        if my_array3[j] > current_value:
            insert_index = j
    my_array3.insert(insert_index, current_value)
print("sorted value is : ", my_array3)
my_array3x = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array3x)
for i in range(1,n):
    insert_index = i
    current_value = my_array3x[i]
    for j in range(i-1, -1, -1):
        if my_array3x[j] > current_value:
            my_array3x[j+1] = my_array3x[j]
            insert_index = j
        else:
            break
    my_array3x[insert_index] = current_value
print(my_array3x)
#q
def patrtion(array,low,high):
    prvot = array[high]
    i = low -1
    for j in range(low,high):
        if array[j] <= prvot:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return i+1
def quikstart(array, low=0, high=None):
    if high == None:
        high = len(array)-1
    if low < high:
        prvot_index = patrtion(array,low,high)
        quikstart(array,low,prvot_index-1)
        quikstart(array,prvot_index+1, high)
my_arrayq = [64, 34, 25, 12, 22, 11, 90, 5,17]
quikstart(my_arrayq)
print(my_arrayq)
def mergeSort(arry):
    if len(arry) <= 1:
        return arry
    mid = len(arry) // 2
    half_arry = arry[:mid]
    half2_arry = arry[mid:]
    sorted_left = mergeSort(half_arry)
    sorted_right = mergeSort(half2_arry)
    return merge(sorted_left, sorted_right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


unsortedArray = [23,89,1,17,-34,8,12,-9,4]
sorted_array = mergeSort(unsortedArray)
print("sorted array values : ", sorted_array)
def binarysearch(arr, targetVal):
    left = 0
    right = len(arr) - 1
    while left <=  right:
        mid = (left + right) // 2
        if arr[mid] == targetVal:
            return mid
        if arr[mid] < targetVal:
                left = mid + 1
        else:
                right = mid -1
    return -1



my_arrayb = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
taragetVal = 1
result2 = binarysearch(my_arrayb, taragetVal)
if result2 != -1:
    print("Value ", taragetVal, " is found at index ", result2)
else:
    print("target not found in array")

# linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node("head")
node2 = Node(8)
node3 = Node(72)
node4 = Node("tial")

node1.next = node2
node2.next = node3
node3.next = node4
current_node = node1
while current_node:
    print(current_node.data, end=" --> ")
    current_node = current_node.next
print("null")


class my_node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


My_node1 = my_node(8)
My_node2 = my_node(14)
My_node3 = my_node(35)
My_node4 = my_node(45)

My_node1.next = My_node2
My_node2.prev = My_node1
My_node2.next = My_node3
My_node3.prev = My_node2
My_node3.next = My_node4
My_node4.prev = My_node3


current_my_node = My_node1
while current_my_node:
    print(current_my_node.data, end="  --> ")
    current_my_node = current_my_node.next
print("null")

then_node = My_node4
while then_node:
    print(then_node.data, end=" <-- ")
    then_node = then_node.prev
print("null")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ") 
currentNode = currentNode.next 

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

print("...")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node1.prev = node4

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1

print("\nTraversing forward:")
currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("...")

print("\nTraversing backward:")
currentNode = node4
startNode = node4
print(currentNode.data, end=" -> ")
currentNode = currentNode.prev

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")

#linked list operation
class point:
    def __init__(self, data):
        self.data = data
        self.next = None
def point_finder(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("nulll")
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
point_finder(node1)

# hash table
def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

print("'A' has hash code:",hash_function('AB'))
my_hash_set = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]

def hash_t(value):
    sum_char = 0
    for char in value:
        sum_char += ord(char)
    return sum_char % 10
def const(name):
    index = hash_t(name)
    return my_hash_set[index] == name

print("name : ",const("Pete"))


my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hash_function(value):
    return sum(ord(char) for char in value) % 10
    
def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)
        
def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    return value in bucket

add('Stuart')

print(my_hash_set)
print('Contains Stuart:',contains('Stuart'))


#trees
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test
print("root.right.left.data:", root.right.left.data)

# binary search in array
binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def get_data(index):
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None

right_child = right_child_index(3)
left_child_of_right_child = left_child_index(right_child)
data = get_data(left_child_of_right_child)

print("root.right.left.data:", data)

#graph
vertexData = ['A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

print('vertexData:',vertexData)
print_adjacency_matrix(adjacency_matrix)