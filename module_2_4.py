numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes=[]
for i in range(len(numbers)):
  if numbers[i]<2:
    continue
  is_prime = True
  for j in range(2,numbers[i]):
    if numbers[i] % j == 0:
      is_prime = False
      not_primes.append(numbers[i])
      break
  if is_prime:
    primes.append(numbers[i])
print(not_primes)
print(primes)

#:#0,1,2,3...
#print(numbers[i])
     # print(numbers)
#for i in range(1,15):
 #for j in range(1,15):
     #print(f'{i}/{j}={i/j}')
     #primes = []
     #for i range(1, 15)
         #
         #print(len(numbers))
