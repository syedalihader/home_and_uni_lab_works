mydict= {
    
"fan": "fan",
"dabba":  "fan",
"item": "things" ,
"dog": "kutta",
"animal": "janwar",
"cat": "billi",
"dogzi": "my sister",
"car": " gadi",
"boxing": "ladai",
"human": "na shukr insan",
"ganji": "my sister",
"tool": " ozar",
"ustad": "teacher",
"mobile": "bacho ko kharab krny wali cheez ",
"kapry": "clothes",
"chai": "tea",
"balla": "bat",
"toffie": "candy",
"munni": "rubab ek gandi larki"
}
print("options are",mydict.keys())
a=input("enter what you find in dictionary of words\n")
#if words are present in dictionary
#print("the meaning of your words is ", mydict[a])
#below line will not throw an ereor if the key is not present in the dictionary
print("the meaninng of your words is ", mydict.get(a))