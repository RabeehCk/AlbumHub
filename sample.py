string = "longest word in a string"
splitstr = string.split(" ")
longest = ""
for i in splitstr:
    if len(i)>len(longest):
        longest = i
print(longest)