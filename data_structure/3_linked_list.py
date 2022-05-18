"""
stock_prices
0x00500                          0x00A1             0x00C5
[ 298  , 0xC702]                [ 305   , 0x00C5] [ 320   , 0x00D7]
                0xC702
                [ 294 , 0x00A1]
"""
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

    def insert_at_end(self, data): # if inserted at the end, it means next must be None
        # suppose if you are inserting the data
        # in a linked_list, then the head must be empty in the first place
        if self.head is None:
            self.head = Node(data, None) # then pass the data to the Node with next as exmpty
                                            # head will point the node
            return # return None

        itr = self.head # if the Linked_list is not empty

        while itr.next: # then iterate till the end of it
            itr = itr.next

        itr.next = Node(data, None) # when it reaches the end, the pass it to the node

    def insert_values(self, data_list):
        # first wipe out all the previous data in the Linked_list
        self.head = None
        for data in data_list:
            self.insert_at_end(data) # bc there is no previous data now, so insert_at_end is used

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

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0: # you are trying to remove the head
            self.head = self.head.next # then shift the head to the next
            return

        count = 0 # else, you have to iterate till you reach the index prior to the one that you actually want to remove
        itr = self.head
        while itr:
            if count == index - 1: # now the index before the index actually wanted to be got rid of
                itr.next = itr.next.next # shift this prior index's next to the next of it
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        """
        if the index is in the middle of the Linked_list
        we need to iterate
        """
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:# the next must be next of the previous element
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None: # data_after not found
            return

        if self.head.data == data_after: # just found
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head # need to iterate
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next: # bc itr.next must be iterated to get data 
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    """
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_end(9)
    ll.insert_at_end(10)
    ll.print() # 2-->1-->9-->10-->
    ll.insert_values(["pineapple", "mango", "papaya"])
    ll.print() # pineapple-->mango-->papaya-->
    print("length:", ll.get_length()) # length: 3
    ll.remove_at(2)
    ll.print() # pineapple-->mango-->
    ll.print() # pineapple-->mango-->
    ll.remove_at(0)
    ll.print() # mango-->
    ll.insert_at(0, "strawberry")
    ll.print() # strawberry-->mango-->
    ll.insert_at(1, "coconut")
    ll.print() # strawberry-->coconut-->mango-->
    """
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print() # banana-->mango-->grapes-->orange-->
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print() # banana-->mango-->apple-->grapes-->orange-->
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print() # banana-->mango-->apple-->grapes-->
    ll.remove_by_value("figs")
    ll.print() # banana-->mango-->apple-->grapes-->
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print() # Linked list is empty.