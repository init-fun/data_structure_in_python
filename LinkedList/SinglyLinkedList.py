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
        return

    def delete_first_node(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_last_node(self):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        while cnode.next.next is not None:
            cnode = cnode.next
        cnode.next = None
        return

    # def del_this_node(self, this_node):
    #     if self.head is None:
    #         print("List is empty")
    #         return
    #     # if the TBD node is the first node
    #     if self.head.data == this_node and self.head.next is None:
    #         self.head = None
    #         return
    #     # if the TBD node is not the first node
    #     cnode = self.head
    #     if cnode.next is not None and cnode.data == this_node:
    #         cnode = cnode.next
    #         self.head = cnode
    #         return

    #     while cnode.next.next is not None:

    #         cnode = cnode.next

    def reverse_it(self):
        if self.head is None:
            print("list is empty")
            return
        cnode = self.head
        prev_node = None
        while cnode is not None:
            next_node = cnode.next
            cnode.next = prev_node
            prev_node = cnode
            cnode = next_node

        self.head = prev_node
        return

    def search_it(self, find_me):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        pos = 1
        while cnode is not None:
            if cnode.data == find_me:
                print(f"{find_me} found at {pos}")
                return
            pos += 1
            cnode = cnode.next
        else:
            print(f"{find_me} not found in the list")

    # sorting! :|

    def bubble_sortByData(self):
        if self.head is None:
            print("List is empty")
            return

        end_node = None
        while end_node != self.head.next:
            cnode = self.head
            while cnode.next != end_node:
                next_node = cnode.next
                if cnode.data > next_node.data:
                    cnode.data, next_node.data = next_node.data, cnode.data
                cnode = cnode.next

            end_node = cnode

    # in-between
    def bubble_sortByLinks(self):
        if self.head is None:
            print("List is empty")
            return

        end_node = None
        while end_node != self.head.next:
            cnode = self.head
            prev_node = self.head
            while cnode.next != end_node:
                next_node = cnode.next

                if cnode.data > next_node.data:
                    # exchange the links
                    cnode.link = prev_node.links
                    next_node.link = cnode

                cnode = cnode.next
            end_node = cnode


llist = LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(5)
llist.insert_at_end(3)
# llist.traverse()
llist.insert_at_begining(19)
# llist.traverse()

llist.insert_after(3, 21)
# llist.traverse()

llist.insert_before(21, 7)
# llist.traverse()

llist.insert_before(21, 9)
print("List is :> ", end=" ")
llist.traverse()

llist.delete_first_node()
# llist.traverse()
llist.delete_last_node()
llist.traverse()

llist.reverse_it()
llist.traverse()

llist.search_it(5)
llist.traverse()

print("sorting\n")
llist.bubble_sortByData()
llist.traverse()
