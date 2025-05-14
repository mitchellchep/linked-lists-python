class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def instertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    def printLinkedList(self):
        temp = self.head

        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()

if __name__ == '__main__':
    lList = LinkedList()
    lList.instertAtBeginning("fox")
    lList.printLinkedList()
