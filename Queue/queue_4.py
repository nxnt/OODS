class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_Empty():
            return ['Empty']
        else:
            return self.queue.pop(0)

    def getsize(self):
        return len(self.queue)

    def is_Empty(self):
        return self.queue == []

    def getData(self):
        return self.queue


inp = input('Enter Input : ').split('/')
comm = inp[0].split(',')
comp = inp[1].split(',')
typeId = []

check = False

Q = Queue()
tempQ = Queue()

for i in comm:
    cm = i.split()
    typeId.append(((cm[1]), (cm[0])))

d = dict(typeId)

for i in comp:
    cm = i.split()
    if cm[0] == 'E':
        if Q.is_Empty():
            Q.enqueue([(cm[1]), int(d[cm[1]])])
        else:
            a = d[cm[1]]

            for i in range(0, Q.getsize()):
                if int(a) == Q.queue[i][1]:
                    index = i+1
                    check = True
            if not check:
                index = Q.getsize()
            check = False

            for i in range(0, index):
                tempQ.enqueue(Q.dequeue())
            tempQ.enqueue([(cm[1]), int(d[cm[1]])])

            while not Q.is_Empty():
                tempQ.enqueue(Q.dequeue())
            while not tempQ.is_Empty():
                Q.enqueue(tempQ.dequeue())

    else:
        print(Q.dequeue()[0])