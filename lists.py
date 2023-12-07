fruits = ['apple',"orange",'''pineapple''','apple'] # this is lists to store multiple fruits in one variable



print('Before change')
for fruit in fruits:
    print(f"I like {fruit}")


print("After change1")
fruits[0] = "banana" # change the value of list 
for fruit in fruits:
    print(f"I like {fruit}")