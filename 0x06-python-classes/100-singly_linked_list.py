#!/usr/bin/python3

class Node:
    """Class that defines a node of a singly linked list.

    Attributes:
        __data (int): Data stored in the node.
        __next_node (Node): Reference to the next node in the list.
    """
    def __init__(self, data, next_node=None):
        """Initialization method for the Node class.

        Args:
            data (int): Data to be stored in the node.
            next_node(Node,optional): Reference next node.Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for the data attribute.

        Args:
            value (int): Data value to be set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for the next_node attribute.

        Args:
            value (Node): Reference to the next node.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list."""
    def __init__(self):
        """Initialization method for the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """Method insert Node in correct position in list(increasing order).

        Args:
            value (int): Data value for the new node.
        """
        new_node = Node(value)

        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Method to print the entire list in stdout."""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
###
