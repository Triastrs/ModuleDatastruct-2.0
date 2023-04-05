from custom_queue import *

t_Queue = Queue()
def test_enqueue():
    assert t_Queue.enqueue('data1') == None
    assert t_Queue.head.data == 'data1'
    assert t_Queue.tail.data == 'data1'
    assert t_Queue.tail.next_node == None

    t_Queue.enqueue('data2')
    assert t_Queue.head.data == 'data1'
    assert t_Queue.tail.data == 'data2'
    assert t_Queue.tail.next_node == None


def test_dequeue():
    t_Queue.enqueue('data3')
    assert t_Queue.dequeue() == 'data1'
    assert t_Queue.dequeue() == 'data2'
    assert t_Queue.dequeue() == 'data3'
    assert t_Queue.dequeue() == None


