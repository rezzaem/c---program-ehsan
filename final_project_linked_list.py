
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.down = None 

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
        
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def erase(self, key):
        cur_node = self.head
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == key:
                last_node.next = cur_node.next
                return

file_list= []
f = open("text.txt", "r")
for x in f:
    file_list.append(x)
file_list2= []
for i in file_list:
    i = i.replace(",", " ")
    i = i.replace(".", " ")
    file_list2.append(i)
file_list3 = []
for i in file_list2:
    z=i.split()
    file_list3.append(z)

counter = 0
for i in file_list3:
    counter+=1
    for x in i:
        z = x.upper()
        if len(z) > 3:
            print(z , counter)