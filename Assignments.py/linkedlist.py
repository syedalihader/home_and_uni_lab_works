class node:
  def __init__(self, data=None, next=None):
    self.data = data      
    self.next = next
          
class Linkedlist:
    def __init__(self) :
     self.head = None
         
def insert_at_begining(self, data):
    node = node(data,self.head)
    self.head = node
    
    
def print(self):
    if self.head is None:
         print("linked list is empty")
         return  
         
    itr= self.head        
    listr = ''



    while itr:
        listr +=str(itr.data)
        itr= itr.next
      
print(Linkedlist)




    
if  __name__=='__main__'  : 
    li=Linkedlist()
    li.insert_at_end(56)   
    li.insert_at_end(66)
    li.print()   

