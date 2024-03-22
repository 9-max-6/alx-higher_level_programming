#!/usr/bin/python3
"""
A module containing the classes Node and SinglyLinkedList
"""


class Node:
    """
    A class that represents a single node of the linked list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data variable
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        A setter method for the data variable
        """
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        A setter method for the variable next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        A getter method for the variable next node
        """
        if (not isinstance(value, Node)) or value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class SinglyLinkedList that defines a singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        A public method to insert the value at the right position
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            new.next_node = None
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                tmp = temp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """
        Printing the list
        """
        l_list = []
        temp = self.__head
        while temp is not None:
            l_list.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(l_list))
