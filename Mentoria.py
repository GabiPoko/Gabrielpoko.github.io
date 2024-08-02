
# lista = [0, 1]

# fibo = lista [-1] + lista [-2]
# lista.append (fibo)
# print (lista)

#-----------------------------------------------

# def fibonacci(num):
# x = [0,1]
# for i in range(num):
# x.append(x[-1]+x[-2])
# return x

#..................-----------------------------------------------

# def fibonacci(n):
#    x = [0,1]
# if n<=0:
# return[]
# elif n==1:
#      return[0]
# elif n==2:
#     return[0,1]
#  else:
#   for i in range(num):
#    x.append(x[-1]+x[-2])
#    return x

#-----------------------------------------------------------------------------------

# def fibo(n):
  
#  fibo_list = [0,1]
#  if n == 1:
#   return fibo_list[n-1]
#  else:
#   for i in range(1,n-1):
   
#    siguiente = fibo_list[i-1] + fibo_list[i]
#   fibo_list.append(siguiente)
#   return fibo_list

#--------------------------------------------------------------------------
def fibonacci(n):
 x = [0,1]
 if n<=0:
   return[]
elif n==1:
return[0]
elif n==2:
return[0,1]
else:
for i in range(n-2):
x.append(x[-1]+x[-2])
return x