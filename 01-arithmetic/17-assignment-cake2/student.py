# write your code here
def cake2(eggs, flour):
   # vb. 11, 750 -> 5, 250
   # #cakes eggs 2
   # #cakes flour 3
   # min()
   # min(#cakes eggs, #cakes flour)
   
   return min((eggs//5),(flour//250))

print(cake2(15,750))
