class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        cur_node = self.head
        if self.isEmpty():
            self.head = self.tail = new_node
            self._size += 1
            return
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.previous = cur_node
        self.tail = new_node
        self._size += 1

    def addHead(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = self.tail = new_node
            self._size += 1
            return
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert(self, pos, item):
        if pos == 0 or pos < -(self.size()):
            self.addHead(item)
            return
        
        if pos > self.size() or pos == self.size() - 1:
            self.append(item)
            return
        
        if pos < 0 and pos > -(self.size()):
            new_node = Node(item)
            cur_node = self.tail
            i = 0
            while i != pos:
                cur_node = cur_node.previous
                i -= 1
            new_node.previous = cur_node
            new_node.next = cur_node.next
            cur_node.next.previous = new_node
            cur_node.next = new_node
            self._size += 1
            return
        
        if pos > 0 and pos < self.size():
            new_node = Node(item)
            cur_node = self.head
            i = 0
            while i != pos:
                cur = cur.next
                i += 1
            new_node.previous = cur_node.previous
            new_node.next = cur_node
            cur_node.previous.next = new_node
            cur_node.previous = new_node
            self._size += 1
            return

    def search(self, item):
        if self.index(item) != -1:
            return 'Found'
        return 'Not Found'

    def index(self, item):
        if self.isEmpty():
            return -1
        cur_node = self.head
        index = 0
        while cur_node is not None:
            if cur_node.value == item:
                return index
            if cur_node.next is None:
                return -1
            cur_node = cur_node.next
            index += 1

    def size(self):
        return self._size

    def pop(self, pos):
        if pos < 0 or self._size < pos + 1 or self.isEmpty():
            return 'Out of Range'
        elif pos == 0:
            self.head = self.head.next
        elif pos + 1 == self._size:
            self.tail = self.tail.previous
        else:
            cur_node = self.head
            for i in range(pos):
                cur_node = cur_node.next
            cur_node.previous.next = cur_node.next
            cur_node.next.previous = cur_node.previous
        self._size -= 1
        return 'Success'


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())

