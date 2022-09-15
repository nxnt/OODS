class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
#PrintFunction
def print_ans(time,mainQ,q1,q2):
    print(time,end = " ")
    print(mainQ.items,end = " ")
    print(q1.items,end =" ")
    print(q2.items,end ="\n")
    
#Input data
data, minute = input('Enter people and time : ').split(' ')
mainQ = Queue([e for e in data])
    
#Create variables
q1 = Queue()
q2 = Queue()
time = 0
count1 = 0
count2 = 0

#Solve
for i in range(int(minute)):
    #Dequeue1
    if (not q1.isEmpty() and count1 % 3 == 0):
        q1.dequeue()
        count1 = 0
    #Dequeue2
    if (not q2.isEmpty() and count2 % 2 == 0):
        q2.dequeue()
        count2 = 0

    #Enqueue1
    if (q1.size() != 5):
        if not mainQ.isEmpty():
            q1.enqueue(mainQ.dequeue())
        count1 += 1
        if(not q2.isEmpty()): count2 += 1
    #Enqueue2
    elif (q2.size() != 5):
        if not mainQ.isEmpty():
            q2.enqueue(mainQ.dequeue())
        count2 += 1
        count1 += 1

    time += 1
    print_ans(time,mainQ,q1,q2)