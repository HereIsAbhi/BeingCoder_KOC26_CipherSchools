# c= ["red","black","blue","red","red"]
# c.insert(1,"yb")
# c.insert(2,"x")
# c[0:2]= ["yellow","pink"]
# # used to replace 

# cars= ("tata","audi")
# c.extend(cars)
# c.remove("red")
# print(c)
# # we can also add tuple to a list

# for i in range(0,3):
#     c.remove("red")
# print(c)  

# for i in range(len(c)):
#     print(c[i])  
# [ print x: for x in c ]

cars= ["tata","nano","kia","audi","merce"]
# for i in cars:
#     if "a" in i:
#         print(i)
# new_list= []
# for i in cars:
#     if "a" in i:
#         new_list.append(i)  
# print(new_list)  

new_list= [x for x in cars if "a" not in x]
        # expression item list condition
print(new_list)


