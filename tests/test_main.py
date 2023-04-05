import pytest
from main import *

def test_node():
    t_Node = Node(1, None)
    assert t_Node.data == 1
    assert t_Node.next_node == None

def test_node_next_node():
    node1 = Node(1, None)
    node2 = Node(2, node1)
    assert node2.next_node == node1
    assert node2.next_node.data == 1

def test_stack_empty():
    stack = Stack()
    assert stack.top == None

def test_stack_push1():
    stack = Stack()
    stack.push('data1')
    assert stack.top.data == 'data1'

def test_stack_push2():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    assert stack.top.data == 'data2'
    assert stack.top.next_node.data == 'data1'

def test_stack_pop1():
    stack = Stack()
    stack.push('data1')
    data = stack.pop()
    assert stack.top.data == None
    assert data == 'data1'
def test_stack_pop():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()
    assert stack.top.data == 'data1'
    assert data == 'data2'
    assert stack.top.next_node == None
