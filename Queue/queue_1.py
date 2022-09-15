# Queue
class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, data):
        self.items.append(data)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


def ManageQueue(commd, data=None):
    if commd == 'E':
        q.enQueue(data)
        print(', '.join(q.items))
    if commd == 'D':
        if not q.isEmpty():
            dq = q.deQueue()
            tmp.append(dq)
            if q.isEmpty():
                print(f'{dq} <- Empty')
            else:
                print(f'{dq} <- ' + f', '.join(q.items))
        else:
            print('Empty')


q = Queue()
tmp = []
inp = input('Enter Input : ').split(',')
for i in inp:
    j = i.split()
    if len(j) == 1:
        ManageQueue(j[0])
    if len(j) == 2:
        ManageQueue(j[0], j[1])
if len(tmp) == 0 and len(q.items) == 0:
    print(f'Empty : Empty')
elif len(tmp) == 0 and len(q.items) != 0:
    print(f'Empty : ' + f', '.join(q.items))
elif len(tmp) != 0 and len(q.items) == 0:
    print(f', '.join(tmp) + f' : Empty')
else:
    print(f', '.join(tmp) + ' : ' + f', '.join(q.items))
