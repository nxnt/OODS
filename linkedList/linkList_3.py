class Node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return self.data

def createList(l=[]):
    


def printList(H):
    ### Code Here ###

def mergeOrderesList(p,q):
    ### Code Here ###

#################### FIX comand ####################   
# input only a number save in L1,L2
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)