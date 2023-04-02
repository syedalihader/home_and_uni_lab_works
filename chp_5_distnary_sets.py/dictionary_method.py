mydict = {
    
"FST" : "in a handwork faster",
"haider": " a hacker",
"marks": [1, 2, 3, 4, 5],
"anotherhaider":{'ali': "commander"}


}
print(list(mydict.keys())) # for kesy printing
print(mydict.values())#for keys printing
print(mydict.items())#print the (key value) of the distnary
print(mydict)

#update mathod
updatedict = {
    
"haider" :  'frineds'
}

mydict.update(updatedict)
print(mydict)
# another method
print(mydict.get("haider"))



 