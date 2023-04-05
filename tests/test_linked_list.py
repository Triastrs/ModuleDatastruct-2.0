from linked_list import *

t_ex = LinkedList()
def test_insert_beginning():
    t_ex.insert_beginning('1')
    assert t_ex.head.data == '1'
    t_ex.insert_beginning('2')
    assert t_ex.head.data == '2'

def test_insert_at_end():
    t_ex.insert_at_end({'id':3})
    assert t_ex.head.data == '2'

def test_to_list():
    t_ex.to_list()
    assert t_ex.lst == ['2', '1', {'id': 3}]

def test_get_data_by_id():
    t_user_data = t_ex.get_data_by_id(2)
    assert t_user_data == {'id': 3}

    t_user_data = t_ex.get_data_by_id(0)
    assert t_user_data == None