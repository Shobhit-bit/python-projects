# monexp = [2200,2350,2600,2130,2190]
# print(f"The total expence of feb is {monexp[1]-monexp[0]}")
# print(f"Expense for first quarter:{monexp[0]+monexp[1]+monexp[2]}")
# print("Did I spent 2000$ in any month? ", 2000 in monexp)
# monexp.append(1980)
# monexp[3]-=200
# print(monexp)
#                                                           linked list
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return

#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + '-->'
#             itr = itr.next
#         print(llstr)
    
#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def insertatend(self,data):
#         if self.head is None:
#             self.head = Node(data,None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data,None)

#     def insertlist(self,data_list):
#         self.head = None
#         for data in data_list:
#             self.insertatend(data)

#     def Lellis(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next
#         return count

#     def remove_at(self,index):
#         itr = self.head
#         ind=0
#         while itr:
#             if ind == index-1:
#                 itr.next = itr.next.next
#             itr =itr.next
#             ind+=1

#     def insertat(self,index,data):
#         if index==0:
#             self.insert_at_begining(data)
#             return
#         cnt =0
#         itr = self.head
#         while itr:
#             if (cnt == index-1):
#                 node = Node(data,itr.next)
#                 itr.next=node
#                 break
#             cnt+=1
#             itr = itr.next

#     def insertaftervalue(self,data_after,data):
#         itr = self.head
#         while itr:
#             if(itr.data == data_after):
#                 node = Node(data,itr.next);
#                 itr.next = node
#                 break
#             itr = itr.next


# ll = LinkedList()
# ll.insertlist(["ali","subah","school","aaya","bag",'rakhte','hi', "boom"])
# ll.Lellis()
# ll.insertaftervalue("bag","bomb")
# ll.print()

#                                                                          hash function
# def getvash(key):
#     h=0
#     for char in key:
#         h+=ord(char)
#     return (h%100)

# class HashTable:  
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [[] for i in range(self.MAX)]
        
#     def gethash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
    
#     def __getitem__(self, key):
#         arr_index = self.gethash(key)
#         for kv in self.arr[arr_index]:
#             if kv[0] == key:
#                 return kv[1]
            
#     def __setitem__(self, key, val):
#         h = self.gethash(key)
#         found = False
#         for ind, element in enumerate(self.arr[h]):
#             if len(element)==2 and element[0] == key:
#                 self.arr[h][ind] = (key,val)
#                 found = True
#         if not found:
#             self.arr[h].append((key,val))
        
#     def __delitem__(self,key):
#         h = self.gethash(key)
#         for ind,elem in enumerate(self.arr[h]):
#             if elem[0] == key:
#                 del self.arr[h][ind]

# t = HashTable()
# t["alu"] = 78
# t["ali"]=908
# t["bpn"] = 98
# del t["ali"]
# print(t.arr)

#Q1
# f = open("D:/vs code/Projects/Saanp/alu_kachalu.csv","r")
# elements = []
# for line in f:
#     element = line.split(",")[1].strip()
#     elements.append(element)
# elements.pop(0)

# avg_temp = sum(float(e) for e in elements)
# avg_temp/=7
# print(avg_temp)
# maxi = max(float(ele) for ele in elements)
# print(maxi)

#Q2
# f = open("D:/vs code/Projects/Saanp/alu_kachalu.csv","r")
# elementss = {}
# for line in f:
#     element = line.split(",")
#     element[1]=element[1].strip()
#     elementss[element[0]]=element[1]
# elementss.pop("date")
# print(elementss.get("Jan 8"))
# print(elementss.get("Jan 4"))

#Q3
# w_count = {}
# f = open("D:/vs code/Projects/Saanp/Kavita.txt","r")
# for line in f:
#     words = line.split(" ")
#     for alpha in words:
#         alpha = alpha.replace("\n"," ")
#         alpha = alpha.replace(","," ")
#         if alpha in w_count:
#             w_count[alpha] +=1
#         else:
#             w_count[alpha] = 1
# print(w_count)

#                                  Stack
# from collections import deque
# import time 
# import threading
# class stack:
#     def __init__(self):
#         self.container = deque()
#     def push(self,data):
#         self.container.append(data)
#     def pop(self):
#         return(self.container.pop())
#     def peek(self):
#         return(self.container[-1])
#     def is_empty(self):
#         return(len(self.container)==0)
#     def len(self):
#         return(len(self.container))

# def revstring(a):
#     stac = stack()
#     l = len(a)
#     revstr = ''
#     for char in a:
#         stac.push(char)
#     for i in range(0,l):
#         revstr += stac.pop()
#     return revstr

# print(revstring("alu ke parathe kha ke needh aayi"))

# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial
# nhi aaya

# class queue:
#     def __init__(self):
#         self.buffer = deque()
#     def endeque(self,value):
#         self.buffer.appendleft(value)
#     def deqque(self):
#         return(self.buffer.pop())
#     def is_empty(self):
#         return(len(self.buffer)==0)
#     def lenque(self):
#         return(len(self.buffer))
#     def orpLA(self,arr):
#         for val in arr:
#             print(f"in {val}")
#             self.endeque(val)
#             time.sleep(0.5)
#     def orserverd(self):
#         time.sleep(1)
#         while True:
#             print(f"out {self.deqque()}")
#             time.sleep(2)
# queque = queue()
# orders = ['pizza','samosa','pasta','biryani','burger']
# t1 = threading.Thread(target=queque.orpLA,args=(orders,))
# t2 = threading.Thread(target = queque.orserverd)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

#                                           binary tree
# class tree:
#     def __init__(self,data):
#         self.data=data
#         self.children = []
#         self.parent = None
#     def add_child(self,child):
#         child.parent = self
#         self.children.append(child)
#     def get_level(self):
#         lvl = 0
#         par = self.parent
#         while par:
#             lvl +=1
#             par = par.parent
#         return lvl
#     def print_tree(self):
#         lvl = self.get_level()
#         if lvl>0:
#             print(("  " * lvl) + "|__" + (self.data))
#         else:
#             print(self.data)
#         if self.children:
#             for childr in self.children:
#                 childr.print_tree()

# def product_hierarcy():
#     Electronics = tree("electronics")
#     lapitopi = tree("laptop")
#     lapitopi.add_child(tree("Mac"))
#     lapitopi.add_child(tree("Predator"))
#     lapitopi.add_child(tree("Thinkpad"))
#     sumaho = tree("Mobile")
#     sumaho.add_child(tree("Oneplus"))
#     sumaho.add_child(tree("Google"))
#     sumaho.add_child(tree("Samsung"))
#     tv = tree("Teli_vision")
#     tv.add_child(tree("LG"))
#     tv.add_child(tree("Onida"))
#     tv.add_child(tree("Sony"))
#     Electronics.add_child(lapitopi)
#     Electronics.add_child(sumaho)
#     Electronics.add_child(tv)
#     Electronics.print_tree()


# class jobtree:
#     def __init__(self,name,job):
#         self.name=name
#         self.job = job
#         self.children = []
#         self.parent = None
#     def add_child(self,child):
#         child.parent = self
#         self.children.append(child)
#     def get_level(self):
#         lvl = 0
#         par = self.parent
#         while par:
#             lvl +=1
#             par = par.parent
#         return lvl
#     def print_name(self):
#         lvl = self.get_level()
#         if lvl>0:
#             print(("  " * lvl) + "|__" + (self.name))
#         else:
#             print(self.name)
#         if self.children:
#             for childr in self.children:
#                 childr.print_name()
#     def print_job(self):
#         lvl = self.get_level()
#         if lvl>0:
#             print(("  " * lvl) + "|__" + (self.job))
#         else:
#             print(self.job)
#         if self.children:
#             for childr in self.children:
#                 childr.print_job()
#     def print_both(self):
#         lvl = self.get_level()
#         if lvl>0:
#             print(("  " * lvl) + "|__" + (self.name) + "("+(self.job)+")")
#         else:
#             print(self.name  + "("+(self.job)+")")
#         if self.children:
#             for childr in self.children:
#                 childr.print_both()

# def Office_politics():
#     ceo = jobtree("Nilpul","CEO")
#     cto = jobtree("Chinmay","CTO")
#     infra_head = jobtree("Vishwa","Infrastructure Head")
#     infra_head.add_child(jobtree("Dhaaval","Cloud Manager"))
#     infra_head.add_child(jobtree("Abhijit","APP Manager"))
#     cto.add_child(infra_head)
#     cto.add_child(jobtree("Aamir","Application Head"))
#     Hr_head = jobtree("Gels","HR Head")
#     Hr_head.add_child(jobtree("Peter","Recruitement Manager"))
#     Hr_head.add_child(jobtree("Waqas","Policy"))
#     ceo.add_child(cto)
#     ceo.add_child(Hr_head)
#     return ceo
# office = Office_politics()
# office.print_both()

# class Bintree:
#     def __init__(self,data):
#         self.data=data
#         self.children = []
#         self.parent = None
#     def add_state(self,child):
#         child.parent = self
#         self.children.append(child)
#     def get_level(self):
#         lvl = 0
#         par = self.parent
#         while par:
#             lvl +=1
#             par = par.parent
#         return lvl
#     def print_tree(self,reqlvl):
#         lvl = self.get_level()
#         if(lvl<=reqlvl):
#             if lvl>0:
#                 print(("  " * lvl) + "|__" + (self.data))
#             else:
#                 print(self.data)
#             if self.children:
#                 for childr in self.children:
#                     childr.print_tree(reqlvl)

# def bharat():
#     Glob = Bintree("Global")
#     india = Bintree("India")
#     Guju = Bintree("Gujrat")
#     Guju.add_state(Bintree("Ahemdabad"))
#     Guju.add_state(Bintree("Baroda"))
#     karn = Bintree("Karnataka")
#     karn.add_state(Bintree("Banguluru"))
#     karn.add_state(Bintree("Mysore"))
#     usa = Bintree("USA")
#     New_jersey = Bintree("New Jersey")
#     New_jersey.add_state(Bintree("priceton"))
#     New_jersey.add_state(Bintree("Trenton"))
#     california = Bintree("California")
#     california.add_state(Bintree("San fransico"))
#     california.add_state(Bintree("Mountain View"))
#     california.add_state(Bintree("Palo Alto"))
#     usa.add_state(New_jersey)
#     usa.add_state(california)
#     india.add_state(Guju)
#     india.add_state(karn)
#     Glob.add_state(india)
#     Glob.add_state(usa)
#     return(Glob)

# akhand_bharat = bharat()
# akhand_bharat.print_tree(3)

# class BinaryTreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#     def add_child(self,data):
#         if(self.data==data):
#             return
#         elif(self.data>data):
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left = BinaryTreeNode(data)
#         else:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = BinaryTreeNode(data)
#     def in_order_trivalsal(self):
#         elements=[]
#         if self.left:
#             elements += self.left.in_order_trivalsal()
#         elements.append(self.data)
#         if self.right:
#             elements += self.right.in_order_trivalsal()
#         return elements
#     def search_node(self,eli):
#         if(self.data==eli):
#             return True
#         elif(self.data>eli):
#             if self.left:
#                 return self.left.search_node(eli)
#             else:
#                 return False
#         elif(self.data<eli):
#             if self.right:
#                 return self.right.search_node(eli)
#             else:
#                 return False
#     def find_min(self):
#         if self.left:
#             return self.left.find_min()
#         else:
#             return self.data
#     def find_max(self):
#         if self.right:
#             return self.right.find_max()
#         else:
#             return self.data
#     def find_sum(self):
#         left_sum = self.left.find_sum() if self.left else 0
#         right_sum = self.right.find_sum() if self.right else 0
#         return (self.data + left_sum + right_sum)
#     def pre_triversal(self):
#         element = [self.data]
#         if self.left:
#             element += self.left.pre_triversal()
#         if self.right:
#             element +=self.right.pre_triversal()
#         return element
#     def post_triversal(self):
#         element = []
#         if self.left:
#             element += self.left.post_triversal()
#         if self.right:
#             element +=self.right.post_triversal()
#         element.append(self.data)
#         return element
#     def delete(self,val):
#         if self.data>val:
#             if self.left:
#                 self.left = self.left.delete(val)
#         elif self.data<val:
#             if self.right:
#                 self.right =  self.right.delete(val)
#         else:
#             if self.left == None and self.right == None:
#                 return None
#             if self.left == None:
#                 return self.right
#             if self.right == None:
#                 return self.left
#             min_val = self.find_min()
#             self.data = min_val
#             self.right = self.right.delete(min_val)
#         return self

# def Bintree(arr):
#     rot = BinaryTreeNode(arr[0])
#     for i in range(1,len(arr)):
#         rot.add_child(arr[i])
#     return rot

# num = [5,6,223,21,4,89,56,34,24,14]
# rot = Bintree(num)
# rot.delete(5)
# print(rot.in_order_trivalsal())

class graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths
    def short_path(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.short_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path = sp
        return shortest_path

routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
ROu = graph(routes) 
print(ROu.short_path("Paris","New York"))