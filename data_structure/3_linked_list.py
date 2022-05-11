# in a node, there are 2 things:
# data and the ref to the address of next data from another node
class Node:
    # create a constructor
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# create the pointer
# which points the head of the LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

# if the data is inserted at [0] just before the original beginning data
    # create a node for the data inserted
    # next of the data inserted will be
    # the head of the original beginning data
    def insert_at_beginning(self, data):
        node = Node(data, self.head) # pass data and next, which is the head of the original data
                                        # which is before the data inserted now
        self.head = node # now, the head becomes the node of data inserted now

    def print(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        itr = self.head # pointer to head becomes the latest ll.insert_at_beginning() called
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next # this will point to the data of the one before the latest ll.insert_at_begnning()called

        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.print() # 2-->1-->
