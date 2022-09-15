class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, data):
        self.items.append(data)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.items)

data, minute = input('Enter people and time : ').split()
mainQ = Queue([e for e in data])

chas1 = Queue()
chas2 = Queue()
time = 0
count1 = 0
count2 = 0 

def print_f(time,mainQ,chas1,chas2):
    print(time, end = ' ')
    print(mainQ.items, end = ' ')
    print(chas1.items, end = ' ')
    print(chas2.items, end = '\n')

for i in range(int(minute)):
    if not chas1.isEmpty() and count1 % 3 == 0:
        chas1.deQueue()
        count1 = 0
    if not chas2.isEmpty() and count2 % 2 == 0:
        chas2.deQueue()
        count2 = 0
    
    if chas1.size() < 5:
        if not mainQ.isEmpty():
            chas1.enQueue(mainQ.deQueue())
            count1 += 1 
        if not chas2.isEmpty():
            count2 += 1
    elif chas2.size() < 5:
        if not mainQ.isEmpty():
            chas2.enQueue(mainQ.deQueue())
            count1 += 1
            count2 += 1
    time += 1
    print_f(time,mainQ,chas1,chas2)
