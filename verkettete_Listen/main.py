import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNextNode(self, nextElement):
        self.next = nextElement

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.getNext():
                currentNode = currentNode.getNext()
            currentNode.setNextNode(newNode)
        return

    def deleteNode(self, value):
        currentNode = self.head
        previousNode = None

        while currentNode:
            if currentNode.getValue() == value:
                if previousNode is None:
                    self.head = currentNode.getNext()
                else:
                    previousNode.setNextNode(currentNode.getNext())
                return
            previousNode = currentNode
            currentNode = currentNode.getNext()

    def getLength(self):
        length = 0
        currentNode = self.head
        if currentNode is None:
            return length
        else:
            while currentNode.getNext():
                currentNode = currentNode.getNext()
                length = length + 1
        return length

    def getAllNodes(self):
        nodes = []
        currentNode = self.head
        while currentNode:
            nodes.append(currentNode.getValue())
            currentNode = currentNode.getNext()
        return nodes

    def __iter__(self):
        self.iterNode = self.head
        return self

    def __next__(self):
        if self.iterNode is None:
            raise StopIteration
        value = self.iterNode.getValue()
        self.iterNode = self.iterNode.getNext()
        return value

if __name__ == "__main__":
    ll = LinkedList()
    ll.addNode("test")
    ll.addNode("test1")
    ll.addNode("test2")
    ll.addNode("test3")
    print(ll.getLength())
    for node in ll.getAllNodes():
        print(node)
    ll.deleteNode("test")
    for node in ll.getAllNodes():
        print(node)
    for l in ll:
        print(l)