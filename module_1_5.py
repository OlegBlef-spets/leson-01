immutable_var=1,2,3,4,5 ,True,'string'
print(immutable_var)
#immutable_var[0]=200
immutable_var=([1,2],3)
print(type(immutable_var))
immutable_var[0][0]=3
print(immutable_var)