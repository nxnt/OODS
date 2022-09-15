# Color_Crush
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

inp = input('Enter Input : ').split()

S = Stack()
combo = 0
for i in inp:
    S.push(i)
    if S.size() >= 3:
        fr,sc,th = S.pop(),S.pop(),S.pop()
        if fr == sc == th: 
            combo += 1
        else:
            S.push(th),S.push(sc),S.push(fr)
           
print(S.size())
if S.isEmpty(): 
    print("Empty",end='') 
else: 
    for i in reversed(S.items):
        print(i,end='') 
if combo > 1: print(f"\nCombo : {combo} ! ! !")
