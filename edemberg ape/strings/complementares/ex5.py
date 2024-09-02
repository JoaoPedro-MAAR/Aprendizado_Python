plvr = input('Digite uma palavra: ')

for i in range(len(plvr)):
 
    print(plvr[i] * (i +1) )
 
for j in range(len(plvr) -2 ,-2,-1):
  print(plvr[j] * (j + 1))
