class Node:
    def __init__(self,data):
        self.data=data #n1.data=5, n2.data=10, n3.data=15, n4.data=20, nb.data=2, ne.data=25, nnb.data=21
        self.next=None #n1.next=None, n2.Next=None, n3.next=None, n4.Next=None, nb.next=None,
                       # ne.next=None, nnb.next=None

class SinglyLL:
    def __init__(self):
        self.head=None #sll.head=None

    def traveral(self):
        if self.head is None: #sll.head=None
            print("LL is empty")
        else:
            a=self.head #a=sll.head
            while a is not None:# a= sll.head=n1, #a=n1.next
                print(a.data, end=" ") #a.data=n1.data, a.data=n2.data
                a=a.next #a=n1.next (which is n2), a=n2.next

    def insert_at_begining(self, data):
        print()
        nb=Node(data) #nb=Node(2)
        nb.next=self.head #nb.next=n1
        self.head=nb #sll.head=nb

    def insert_at_end(self, data):
        print()
        ne=Node(data)
        a=self.head #a=sll.head=nb
        while a.next is not None: #a.next=nb.next=n1, n1.next, n2.next, n3.next n4.next is none hence loop ends
            a=a.next #nb.next=n1,n2.next,
        a.next=ne #n4.next=ne

    def insert_at_specified(self, position,data):
        print()
        nnb=Node(data)
        a=self.head #sll.head=nb
        for i in range(1, position-1):
            a=a.next #nb.next=n1
        nnb.next=a.next #n1.next=n2
        a.next=pnb  #n1.next=nnb

n1=Node(5)
sll=SinglyLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4
sll.traveral()
sll.insert_at_begining(2)
sll.traveral()
sll.insert_at_end(25)
sll.traveral()
sll.insert_at_specified(3,21)
sll.traveral()
