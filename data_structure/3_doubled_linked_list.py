class Node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Double linked list is empty.")
            return

        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.next
        print("In forward order", dllstr)

    def print_backward(self):
        if self.head is None:
            print("Double linked list is empty.")

        last_node = self.get_last_node()
        itr = last_node
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.prev
        print("In reverse order", dllstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(None, data, self.head)
        else:
            node = Node(None, data, self.head)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(itr, data, None)

    def remove_at(self, index):
        if index == 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.prev = itr.prev.prev
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_at_beginning("banana")
    ll.insert_at_beginning("pineapple")
    ll.insert_at_end("strawberry")
    ll.print_backward()
    ll.print_forward()
    ll.remove_at(2)
    ll.print_forward()
    ll.insert_values(["mango", "papaya", "apple"])
    ll.print_forward()
    ll.print_backward()


