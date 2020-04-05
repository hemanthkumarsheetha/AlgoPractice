class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
    def append(self,current_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = current_element
        else:
            self.head = current_element

    def Print_Linked_List(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def Insert_between(self,element,pos):
        c=1
        current = self.head
        if pos>0:
            while current.next:
                if c==pos:
                    element.next = current.next
                    current.next= element
                    break
                c+=1
                current = current.next
        else:
            element.next = current
            self.head = element

    def delete(self,pos):
        c=1
        current = self.head
        if pos>0:
            while current.next:
                prev = current
                current = current.next
                if c==pos:
                    prev.next = current.next
                    break
                c+=1
        else:
            n = current.next
            n = self.head
            current.next=None
e1 = Element(1)
e2 = Element(2)
e3 = Element(4)
e4 = Element(5)

l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)
l1.append(e4)

l1.Print_Linked_List()
print("/////////")
e5=Element(6)
l1.Insert_between(e5,3)
l1.Print_Linked_List()

print("########")
l1.delete(3)
l1.Print_Linked_List()