#project number 6
with open("story.txt", "r") as f:
    storry = f.read()

words = set()
start_of_w = -1

targe_start = "<"
targe_end = ">"
for i, char in enumerate(storry):
    if char == targe_start:
        start_of_w = i
    if char == targe_end and start_of_w != -1:
        word = storry[start_of_w: i + 1]
        words.add(word)
answers = {}
for word in words:
    asw = input("Weka kiwakilishi cha " + word + ": ")
    answers[word] = asw
for word in words:
    storry = storry.replace(word, answers[word])

print(storry)