# 🚨 Don't change the code below 👇
list_items = input("Enter numbers: ").split()
for num in range(0, len(list_items)):
  list_items[num] = int(list_items[num])
print(list_items)
  
# 🚨 Don't change the code above 👆
alls_sum = 0
len_list = 0 
for x in list_items:
  alls_sum += x
  len_list+=1
  
result = alls_sum / len_list
print(round(result))
#Write your code below this row 👇



