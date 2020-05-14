class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cnode = self.head
        while cnode.next is not None:
            cnode = cnode.next
        cnode.next = new_node

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        while cnode is not None:
            print(cnode.data, end=" ")
            cnode = cnode.next
        print("\n------")

    def insert_at_begining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_pos(self, data, location):
        new_node = Node(data)
        if self.head is None and location == 1:
            self.head = new_node
            return
        cnode = self.head
        pos = 0
        while cnode.next is not None and pos < location:
            cnode = cnode.next
        new_node.next = cnode.next
        cnode.next = new_node

    def insert_after(self, prev_node, data):
        # prev_node = Node(x_node)
        if self.head is None:
            print("list is empty")
            return
        cnode = self.head
        new_node = Node(data)
        while cnode is not None:
            if cnode.data == prev_node:
                new_node.next = cnode.next
                cnode.next = new_node
                return
            cnode = cnode.next

    def insert_before(self, target_node, data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == target_node:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        cnode = self.head
        prev_node = None
        new_node = Node(data)
        while cnode is not None:
            if cnode.data == target_node:
                new_node.next = cnode
                prev_node.next = new_node

                prev_node = new_node
                return
            prev_node = cnode
            cnode = cnode.next
        else:
            print("Node is not in the list")


llist = LinkedList()
llist.insert_at_end("p")
llist.insert_at_end("r")
llist.insert_at_end("s")
llist.traverse()
llist.insert_at_begining("Start")
llist.traverse()

llist.insert_after("p", "q")
llist.traverse()

llist.insert_before("Start", "X")
llist.traverse()

llist.insert_before("s", "S")
llist.traverse()
