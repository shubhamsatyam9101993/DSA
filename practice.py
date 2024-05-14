class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return self

    def index_add(self, position, value):
        new_node = Node(value)
        temp_node = self.head
        count = 0
        while temp_node is not None:
            if count == position:
                new_node.next = temp_node.next
                temp_node.next = new_node
                break
            temp_node = temp_node.next
            count += 1
        self.size += 1
        return self

    def index_insert(self, position, value):
        new_node = Node(value)
        temp_node = self.head
        for i in range(position-1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        return self

    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node is not None:
            result += str(temp_node.value) + '->'
            temp_node = temp_node.next
        return result


if __name__ == '__main__':
    l1 = LinkedList()
    n1 = l1.append(10)
    n2 = l1.append(20)
    n3 = l1.append(30)
    n4 = l1.append(40)
    n5 = l1.prepend(50)
    n6 = l1.append(60)
    # new_node3 = LinkedList(30)
    # new_node4 = LinkedList(200)
    # new_node5 = LinkedList(101)
    # new_node6 = LinkedList(102)
    print(l1)
    n7 = l1.index_insert(2, 70)
    print(l1)
