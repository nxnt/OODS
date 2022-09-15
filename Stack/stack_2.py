# Number in Stack
class Stack:
    def __init__(self, list=None):
        if list == None:
            self.list = []
        else:
            self.list = list

    def push(self, i):
        self.list.append(i)

    def pop(self):
        if not self.isEmpty():
            return "Pop = " + str(self.list.pop())
        else:
            return -1

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def delete(self, i):
        if not self.isEmpty():
            tmp = []
            if i in self.list:
                n = self.list.count(i)
                self.list = [x for x in self.list if x != i]
                for x in range(n):
                    tmp.append(f"Delete = {i}")
            return "\n".join(tmp)
        else:
            return "-1"

    def ld(self, i):
        if not self.isEmpty():
            tmp = []
            txt = [x for x in reversed(self.list) if x < i]
            self.list = [x for x in self.list if not x < i]
            for e in txt:
                tmp.append(f"Delete = {e} Because {e} is less than {i}" )
            return "\n".join(tmp)
        else:
            return "-1"

    def md(self, i):
        if not self.isEmpty():
            tmp = []
            txt = [x for x in reversed(self.list) if x > i]
            self.list = [x for x in self.list if not x > i]
            for e in txt:
                tmp.append(f"Delete = {e} Because {e} is more than {i}" )
            return "\n".join(tmp)
        else:
            return "-1"

stack = Stack()

def ManageStack(commd, data = None):
    if commd == 'A':
        stack.push(data)
        print(f"Add = {data}")
    if commd == 'P':
        print(stack.pop())
    if commd == 'D':
        s = stack.delete(data)
        if len(s) > 1:
            print(s)
    if commd == 'LD':
        s = stack.ld(data)
        if len(s) > 1:
            print(s)
    if commd == 'MD':
        s = stack.md(data)
        if len(s) > 1:
            print(s)

x = input("Enter Input : ").split(",")
for i in x:
    j = i.split()
    if len(j) == 1:
        ManageStack(j[0])
    elif len(j) == 2:
        ManageStack(j[0], int(j[1]))
print("Value in Stack =", stack.list)