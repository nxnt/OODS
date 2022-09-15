class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        final_string = 'link list : '
        current_node = self.head
        if current_node is None:
            return 'List is empty'
            
        while current_node is not None:
            final_string += str(current_node.data)
            if current_node.next is not None:
                final_string += '->'
            current_node = current_node.next
        return final_string

    def isEmpty(self):
        return False if self.size else True

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1

    def insert(self, index, data):
        if int(index) < 0 or int(index) > self.size:
            print('Data cannot be added')
            return
        else:
            print(f'index = {index.strip()} and data = {data}')

        if int(index) == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            insert_node = Node(data)
            current_node = self.head
            current_index = 0
            while current_node is not None:
                if current_index + 1 == int(index):
                    insert_node.next = current_node.next
                    current_node.next = insert_node
                    break
                current_node = current_node.next
                current_index += 1
        self.size += 1


new_ll = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i == inp[0]:
        if i is '':
            print('List is empty')
        else:
            j = i.split()
            for k in j:
                new_ll.append(k)
            print(new_ll)
    else:
        index,data = i.split(':')
        new_ll.insert(index, data)
        print(new_ll)
