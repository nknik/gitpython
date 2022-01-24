# remove duplicates from linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while start.next != None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def removeDuplicates(self, head):
        # Write your code here
        c = head
        while c is not None and c.next is not None:
            while c.next is not None and c.data is c.next.data:
                c.next = c.next.next
            c = c.next
        return head


mylist = Solution()
