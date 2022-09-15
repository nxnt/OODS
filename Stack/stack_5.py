# Into the Woods 2
class Stack:
    def __init__(self):
        self.items = list()

    def push(self, value):
        self.items.append(value)

    def pop(self,pos=None):
        return self.items.pop(pos)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

S = Stack()
def ManageStack(commd, data = None):
        if commd == 'A':
            S.push(data)
        if commd == 'B':
            if not S.isEmpty():
                see = 1
                for x in S.items:
                    fs = S.pop(0)
                    if fs > x:
                        see += 1
                    else:
                        if see > 1:
                            see -= 1
                        else:
                            continue
                print(see)
            else:
                print("0")
            

                
inp = input('Enter Input : ').split(',')

for i in inp:
    j = i.split()
    if len(j) == 1:
        ManageStack(j[0]) 
    if len(j) == 2:
        ManageStack(j[0], j[1])
