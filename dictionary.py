import json


data =  json.load(open("dictionary.json"))

def output(word):
    word = word.lower()
    if word in data:
        return data[word]

def output1(word):
    word = word.lower()
    if word in data:
        return data[word]

word = input("enter te word you want to search")
output = output(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
exit = input("to search next word press Y to exit press any key")

while(exit == "Y"):
    word = input("Enter the word you want to search")
    output = output1(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    exit = input("to search next word press Y to exit press any key")