class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue(Node):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.losing_head = None
        super().__init__(Node)

    def enqueue(self, data):
        """метод для добавления данных в очередь. """
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return

        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
        return

    def dequeue(self):
        """Метод удаляет из очереди крайний левый элемент (первый добавленный),
        и возвращает данные удаленного экземпляра класса Node."""
        self.losing_head = self.head.data
        self.head.data = self.head.next_node.data
        self.head.next_node.data = self.tail.data
        self.tail.data = self.tail.next_node
        return self.losing_head



#queue = Queue()
#queue.enqueue('data1')
#queue.enqueue('data2')
#queue.enqueue('data3')
#print(queue.head.data)
#print(queue.head.next_node.data)
#print(queue.tail.data)
#print(queue.tail.next_node)
##print(queue.tail.next_node.data)
#print(queue.dequeue())
#print(queue.dequeue())
#print(queue.dequeue())
#print(queue.dequeue())


