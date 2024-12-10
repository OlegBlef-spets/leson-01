first=int(input())
second=int(input())
third=int(input())
if first==second and first==third and second==third:
  print(3)#"все числа равны между собой
elif first==second or first==third or second==third:
   print(2)#"если хотя бы 2 из 3 введённых чисел равны между собой:",
else:
   print(0)#число не подходит:",


