''' Convert BST to an ordered linked list.'''


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class BST_TO_LIST:

    def bst_to_list(self, head):
        self.list = []

        def in_order_traverse(head):
            if head is None:
                return
            value, left, right = head

            if left is not None:
                in_order_traverse(left)

            self.list.append(value)
            if right is not None:
                in_order_traverse(right)

        in_order_traverse(head)

        reversed_list = reversed(self.list)
        linked_list = []
        last = None
        for i in reversed_list:
            n = Node(i,last)
            linked_list.append(n)
            last = n

        return linked_list[-1]

if __name__ == '__main__':
    TREE = (5,(3, (2,(1,None,None),None),(4,None,None)),(8,(7,None,None),(10,(9,None,None),None)))
    solver = BST_TO_LIST()
    print solver.bst_to_list(TREE)
