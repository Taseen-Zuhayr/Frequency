test = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("The original dictionary is : ",test)
x=2
count = 0

for key in test:
    if test[key] == x:
        count += 1
print("The frequency is ",count,"times")

