monexp = [2200,2350,2600,2130,2190]
print(f"The total expence of feb is {monexp[1]-monexp[0]}")
print(f"Expense for first quarter:{monexp[0]+monexp[1]+monexp[2]}")
print("Did I spent 2000$ in any month? ", 2000 in monexp)
monexp.append(1980)
monexp[3]-=200
print(monexp)
                                                       linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertatend(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insertlist(self,data_list):
        self.head = None
        for data in data_list:
            self.insertatend(data)

    def Lellis(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self,index):
        itr = self.head
        ind=0
        while itr:
            if ind == index-1:
                itr.next = itr.next.next
            itr =itr.next
            ind+=1

    def insertat(self,index,data):
        if index==0:
            self.insert_at_begining(data)
            return
        cnt =0
        itr = self.head
        while itr:
            if (cnt == index-1):
                node = Node(data,itr.next)
                itr.next=node
                break
            cnt+=1
            itr = itr.next

    def insertaftervalue(self,data_after,data):
        itr = self.head
        while itr:
            if(itr.data == data_after):
                node = Node(data,itr.next);
                itr.next = node
                break
            itr = itr.next

ll = LinkedList()
ll.insertlist(["ali","subah","school","aaya","bag",'rakhte','hi', "boom"])
ll.Lellis()
ll.insertaftervalue("bag","bomb")
ll.print()

class Hashtable:
    def __init__(self):
        self.max=100
        self.arr = [None for i in range (self.max)]

    def gethash(self,key):
        h=0
        for chr in key:
            h+=ord(chr)
        return(h%self.max)
    def __setitem__(self,key,val):
        h=self.gethash(key)
        self.arr[h]=val
    def __getitem__(self,key):
        h=self.gethash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h = self.gethash(key)
        self.arr[h]=None

t = Hashtable()
t["Ramu Ke bacche"]=15
print(t["Ramu ke bacche"])
