class Node:
    """
    Class representing a node in a linked list.

    Attributes:
        item: The value stored in the node.
        next: Reference to the next node in the list.
    """
    def __init__(self, item):
        """
        Initializes a new node with the given item.

        Args:
            item: The value to be stored in the node.
        """
        self.item = item
        self.next = None

class LinkedList:
    """
    Class representing a linked list.

    Attributes:
        size: The number of elements in the list.
        begin: Reference to the first node in the list.
        end: Reference to the last node in the list.
        items: A list to store the items in the linked list (not necessary for the implementation).
    """
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.size = 0
        self.begin = None
        self.end = None

    def isEmpty(self):
        """
        Checks if the linked list is empty.

        Returns:
            True if the linked list is empty, False otherwise.
        """
        return self.size == 0

    def addLast(self, item):
        """
        Adds a new node with the given item at the end of the linked list.

        Args:
            item: The value to be added to the list.

        Returns:
            True if the operation is successful.
        """
        newNode = Node(item)
        if self.isEmpty():
            self.begin = newNode
            self.end = self.begin
        else:
            self.end.next = newNode
            self.end = newNode
        self.size += 1
        return True

    def addFirst(self, item):
        """
        Adds a new node with the given item at the beginning of the linked list.

        Args:
            item: The value to be added to the list.

        Returns:
            True if the operation is successful.
        """
        newNode = Node(item)
        if self.isEmpty():
            self.begin = newNode
            self.end = self.begin
        else:
            newNode.next = self.begin
            self.begin = newNode
        self.size += 1
        return True

    def removeNode(self, item):
        """
        Removes the first occurrence of the node with the given item from the linked list.

        Args:
            item: The value to be removed from the list.
        """
        if self.isEmpty():
            print("Empty list.\n")
            return

        currentNode = self.begin
        prevNode = None

        while currentNode is not None:
            if currentNode.item == item:
                if prevNode is not None:
                    prevNode.next = currentNode.next
                    if currentNode == self.end:
                        self.end = prevNode
                else:
                    self.begin = currentNode.next
                    if currentNode == self.end:
                        self.end = None

                self.size -= 1
                break
            prevNode = currentNode
            currentNode = currentNode.next
        else:
            print(f"Item {item} not found")

    def showList(self):
        """
        Displays the items in the linked list.
        """
        print("LINKED LIST")
        print(f"SIZE:{self.size}")
        currentNode = self.begin
        while currentNode:
            print(currentNode.item, end=" -> ")
            currentNode = currentNode.next

        print("None")

    def search(self, item):
        """
        Searches for the first occurrence of the given item in the linked list.

        Args:
            item: The value to be searched in the list.

        Returns:
            The position of the item if found, or a message indicating the item was not found.
        """
        currentNode = self.begin
        position = 0
        while currentNode:
            if currentNode.item == item:
                return  print(f"Item {item} is in position {position}")
            position += 1
            currentNode = currentNode.next
        return print(f"Item {item} not found")

    def clear(self):
        """Deletes all nodes from the list"""
        currentNode = self.begin
        while currentNode:
            nextNode = currentNode.next
            self.removeNode(currentNode.item)  # Remove the node from memory
            currentNode = nextNode

        self.begin = None
        self.end = None
        self.size = 0


