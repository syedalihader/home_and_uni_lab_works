#a ={ 1, 2,3 ,4 ,5 ,3,1,3,1,}
#print(type(a))
#print(a)
 
 #an empty set can be creatrd by syntex a={}
 
#a={}
#print(type(a))

b=set()
print(type(b))
 
#we can add items b,add(2)
b.add(3)#cannot add
b.add(4)##cannot add
b.add(6)##cannot add

b.add({6,7,3,6,7,4,6,3})
b.add({5,45,34,2}) # dictionary cannot be added
print(b)

#another method
print(len(b))# for lenght
b.remove(6)
b.remove(3)
print(b)


