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

#                              Updated hash function
      def __getitem__(self, key):
        arr_index = self.gethash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.gethash(key)
        found = False
        for ind, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][ind] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self,key):
        h = self.gethash(key)
        for ind,elem in enumerate(self.arr[h]):
            if elem[0] == key:
                del self.arr[h][ind]
#nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
f = open("D:/vs code/Projects/Saanp/alu_kachalu.csv","r")
elements = []
for line in f:
    element = line.split(",")[1].strip()
    elements.append(element)
elements.pop(0)

avg_temp = sum(float(e) for e in elements)
avg_temp/=7
print(avg_temp)
maxi = max(float(ele) for ele in elements)
print(maxi)
# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
f = open("D:/vs code/Projects/Saanp/alu_kachalu.csv","r")
elementss = {}
for line in f:
    element = line.split(",")
    element[1]=element[1].strip()
    elementss[element[0]]=element[1]
elementss.pop("date")
print(elementss.get("Jan 8"))
print(elementss.get("Jan 4"))
# Write a function in python that can reverse a string using stack data structure
from collections import deque
class stack:
    def __init__(self):
        self.container = deque()
    def push(self,data):
        self.container.append(data)
    def pop(self):
        return(self.container.pop())
    def peek(self):
        return(self.container[-1])
    def is_empty(self):
        return(len(self.container)==0)
    def len(self):
        return(len(self.container))

def revstring(a):
    stac = stack()
    l = len(a)
    revstr = ''
    for char in a:
        stac.push(char)
    for i in range(0,l):
        revstr += stac.pop()
    return revstr

print(revstring("alu ke parathe kha ke needh aayi"))

# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial
# nhi aaya

# Design a food ordering system where your python program will run two threads,
# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Pass following list as an argument to place order thread
# orders = ['pizza','samosa','pasta','biryani','burger']
class queue:
    def __init__(self):
        self.buffer = deque()
    def endeque(self,value):
        self.buffer.appendleft(value)
    def deqque(self):
        return(self.buffer.pop())
    def is_empty(self):
        return(len(self.buffer)==0)
    def lenque(self):
        return(len(self.buffer))
    def orpLA(self,arr):
        for val in arr:
            print(f"in {val}")
            self.endeque(val)
            time.sleep(0.5)
    def orserverd(self):
        time.sleep(1)
        while True:
            print(f"out {self.deqque()}")
            time.sleep(2)
queque = queue()
orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target=queque.orpLA,args=(orders,))
t2 = threading.Thread(target = queque.orserverd)
t1.start()
t2.start()
t1.join()
time.sleep(1)
t2.join()
