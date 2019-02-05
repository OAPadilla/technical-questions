# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init_(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def sum_list(self, first, second):

        prev = 0
        temp = 0
        carry = 0

        while first is not None or second is not None:
            sum = first.data + second.data + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0

            temp = Node(sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            first = first.next
            second = second.next

        if carry > 0:
            temp.next = Node(carry)

    def print_list(selfself):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next



