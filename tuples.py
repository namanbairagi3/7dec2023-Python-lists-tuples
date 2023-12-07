fruits = ('apple',"orange",'''pineapple''','apple') # this is tuple to store multiple fruits in one variable



print('Before change')
for fruit in fruits:
    print(f"I like {fruit}")


print("After change1")
fruits[0] = "banana" # We can not change the items in tuple
for fruit in fruits:
    print(f"I like {fruit}")