class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def swapNodes(self, x, y):
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY
        if prevY != None:
            prevY.next = currX
        else: 
            self.head = currX
        temp = currX.next
        currX.next = currY.next
        currY.next = temp


    def isEmpty(self):
        return self.head == None

    def insert(self,data):
        new_node = Node(data)
        if self.isEmpty():
            cursor_node = Node('|')
            new_node.next = cursor_node
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next is not None:
            if cur_node.next.data == '|':
                break
            cur_node = cur_node.next
        new_node.pre = cur_node
        new_node.next = cur_node.next
        cur_node.next = new_node

    def mvLeft(self):
        if self.isEmpty():
            return
        cur_node = self.head
        if cur_node.data == '|':
            return
        while cur_node.next != None:
            if cur_node.next.data == '|':
                break
            cur_node = cur_node.next
        self.swapNodes(cur_node.data, cur_node.next.data)

    def mvRight(self):
        if self.isEmpty():
            return
        cur_node = self.head
        while cur_node.next != None:
            if cur_node.data == '|':
                break
            cur_node = cur_node.next
        if cur_node.next == None:
            return
        self.swapNodes(cur_node.data, cur_node.next.data)

    def delLeft(self):
        if self.isEmpty():
            return
        cur_node = self.head
        if cur_node.data == '|':
            return
        while cur_node.next != None:
            if cur_node.next.data == '|':
                break
            cur_node = cur_node.next
        tmp = self.head
        if cur_node == self.head:
            self.head.next = cur_node
            return
        while tmp.next != cur_node:
            tmp = tmp.next
        tmp.next = cur_node.next

    def delRight(self):
        if self.isEmpty():
            return
        cur_node = self.head
        while cur_node.next != None:
            if cur_node.data == '|':
                break
            cur_node = cur_node.next
        if cur_node.next is None:
            return
        cur_node.next = cur_node.next.next

L = LinkedList()
inp = input('Enter Input : ').split(',') 
for i in inp:
    if i[:1] == 'I':
        L.insert(i[2:])
    elif i[:1] == 'L':
        L.mvLeft()
    elif i[:1] == 'R':
        L.mvRight()
    elif i[:1] == 'B':
        L.delLeft()
    elif i[:1] == 'D':
        L.delRight()
print(L)
        