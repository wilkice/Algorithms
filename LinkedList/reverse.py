class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        """add new node
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        cur = self.head
        l1 = []
        while cur:
            l1.append(cur.data)
            cur = cur.next
        return l1

    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        prev = None
        cur = self.head

        while cur:
            next_node = cur.next
            cur.next = prev

            prev = cur
            cur = next_node

        self.head = prev


head = LinkedList()
head.push(3)
head.push(4)
head.push(5)
head.push(6)
print("Given list is: ", head.print_list())
head.reverse()
print("Reversed list is: ", head.print_list())
