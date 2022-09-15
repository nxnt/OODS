class Stack:
    def __init__(self, list=None):
        if list == None:
            self.list = []
        else:
            self.list = list

    def isEmpty(self):
        return False if len(self.list) else True

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop() if not self.isEmpty() else -1

    def size(self):
        return len(self.list)


class Queue:
    def __init__(self, list=None):
        if list == None:
            self.list = []
        else:
            self.list = list

    def enQueue(self, data):
        self.list.append(data)

    def deQueue(self):
        return self.list.pop(0) if not self.isEmpty() else -1

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return False if self.size() else True


x = input("Enter Input (Normal, Mirror) : ").split()
norm = x[0]
mirr = x[1][::-1]

normQueue = Queue()
mirrQueue = Queue()
itemQueue = Queue()
tmp = Stack()

for i in norm:
    normQueue.enQueue(i)
for i in mirr:
    mirrQueue.enQueue(i)
mirrBomb = 0
while not mirrQueue.isEmpty():
    if tmp.size() < 2:
        tmp.push(mirrQueue.deQueue())
    else:
        first = tmp.pop()
        second = tmp.pop()
        now = mirrQueue.deQueue()
        if first == second and second == now:
            itemQueue.enQueue(first)
            mirrBomb += 1
        else:
            tmp.push(second)
            tmp.push(first)
            tmp.push(now)
mirrored = [x for x in tmp.list]
tmp.list.clear()
bomb = 0
failBomb = 0
while not normQueue.isEmpty():
    if tmp.size() < 2:
        tmp.push(normQueue.deQueue())
    else:
        first = tmp.pop()
        second = tmp.pop()
        now = normQueue.deQueue()
        if first == second and second == now:
            if not itemQueue.isEmpty():
                item = itemQueue.deQueue()
                if not (first == second and second == item):
                    tmp.push(second)
                    if item != now:
                        tmp.push(first)
                        tmp.push(item)
                else:
                    failBomb += 1
                tmp.push(now)
            else:
                bomb += 1
        else:
            tmp.push(second)
            tmp.push(first)
            tmp.push(now)

print(f"NORMAL :\n{tmp.size()}")
print("".join(tmp.list[::-1]) if tmp.size() > 0 else "Empty")
print(f"{bomb} Explosive(s) ! ! ! (NORMAL)")
print(f"Failed Interrupted {failBomb} Bomb(s)\n------------MIRROR------------" if failBomb >
      0 else "------------MIRROR------------")
print(": RORRIM")
print(len(mirrored))
print("ytpmE" if len(mirrored) < 1 else "".join(mirrored[::-1]))
print(f"(RORRIM) ! ! ! (s)evisolpxE {mirrBomb}")
