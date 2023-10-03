class Node:
    def __init__(self,data=None):
         self,data=data
         self,next=None
        
class singlylinkedlist:
   def __init__(self):
     self.first=None
        
   def insertfirst (self,data):
      temp=None,data
      if(self.first==None):
         self.first=temp
      else:
            temp.next=self.first()
            temp=self.first
            
   def removefirst(self):
       if(self.first==None):
          print("list is empty")
       else:
            curr=self.first()
            self.first=self.first.next
            print("the deleted item is:",curr.data)
            
   def display(self):
       if(self.first==None):
          print("list is empty")
          return
       current=self.first()
       while(current):
           print(current.data,end=" ")
           current=current.next
   def search(self,item):
      if(self.first==None):
         print("list is empty")
         return
      current=self.first()
      found=False
      while current!=None:
          if current.data==item:
               found=True
          else:
                current=current.next
                
      if (found):
             print(" item is present in list")
      else:
          print("item is not  present in list")
                
#singlylinkedlist
ll=singlylinkedlist()
while(True):
      c1=input("/n enter your choice 1-insertfirst,2-remove,3-display,4-search,5-exit:")
      if(c1==1):
        item=input("enter the element to insertfirst")
        ll.insertfirst(item)
      elif(c1==2):
        ll.removefirst(item)
      elif(c1==3):
        ll.display(item)
      elif(c1==4):
        item=input("enter the item to search")
        ll.search(item)
      else:
         break
    
    
        
    


        
                
                
        
        