from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        """
        Adds elements to the buffer.
        When the ring buffer is full and a new element is 
        inserted, the oldest element in the ring buffer is 
        overwritten with the newest element.
        You may not use a Python List in your implementation 
        of the append method (except for the stretch goal)
        """
        if self.storage.length == self.capacity:
            self.current += 1
            self.storage.remove_from_head()
        else:
            self.current = 0

        self.storage.add_to_tail(item)
        # if self.storage.length == self.capacity:
        #     self.storage.remove_from_head()
        #     self.storage.add_to_head(item)
        #     self.current += 1
        #     loc = self.current % self.capacity
        #     for _ in range(loc):
        #         if loc == i+1:

        #             for h in range(i):
        #                 self.storage.head = self.storage.head.next
        # else:
        #     self.current = 0
        #     self.storage.add_to_tail(item)

    def get(self):
        """
        Returns all of the elements in the buffer 
        in a list in their given order. 
        It should not return any None values in the 
        list even if they are present in the ring buffer.
        """
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        head = self.storage.head
        tail = self.storage.tail

        if self.storage is None:
            return

        if self.storage.length == self.capacity:
            loc = self.current % self.capacity
            for _ in range(loc-1):
                tail = tail.prev
            for _ in range(loc):
                list_buffer_contents.append(tail.value)
                tail = tail.next

        while head and len(list_buffer_contents) != self.capacity:
            list_buffer_contents.append(head.value)
            head = head.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
