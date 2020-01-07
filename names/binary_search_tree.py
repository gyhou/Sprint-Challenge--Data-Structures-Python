import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if self.value > value:
                if self.left:
                    return self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
            else:
                if self.right:
                    return self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
        else:
            self.value = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target and self.left:
            return self.left.contains(target)
        elif self.value < target and self.right:
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        """Iterative"""
        if self.right:
            while self.right.right:
                self.right = self.right.right
            return self.right.value
        else:
            return self.value
        """Recursion"""
        # if self.right:
        #     return self.right.get_max()
        # else:
        #     return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        """Recursive depth first traversal"""
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        """Iterative depth first traversal"""
        # stack = Stack()
        # stack.push(self)

        # while stack.len() > 0:
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self:
            if node.left:
                node.left.in_order_print(node.left)
            print(node.value)
            if node.right:
                node.right.in_order_print(node.right)
        # if self:
        #     if self.left:
        #         self.left.in_order_print(self.left)
        #     print(self.value)  
        #     if self.right:
        #         self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     queue = Queue()
    #     queue.enqueue(node)

    #     while queue.len() > 0:
    #         current_node = queue.dequeue()
    #         if current_node.right:
    #             queue.enqueue(current_node.right)
    #         if current_node.left:
    #             queue.enqueue(current_node.left)
    #         print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self, node):
    #     stack = Stack()
    #     stack.push(node)

    #     while stack.len() > 0:
    #         current_node = stack.pop()
    #         if current_node.right:
    #             stack.push(current_node.right)
    #         if current_node.left:
    #             stack.push(current_node.left)
    #         print(current_node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if self:
            print(node.value)
            if node.left:
                node.left.pre_order_dft(node.left)
            if node.right:
                node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self:
            if node.left:
                node.left.post_order_dft(node.left)
            if node.right:
                node.right.post_order_dft(node.right)
            print(node.value)
