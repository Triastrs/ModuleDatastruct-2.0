class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """класс для хранения односвязного списка"""
    def __init__(self):
        self.head = None
        self.lst = []

    def insert_beginning(self, data: dict):
        """добавляет данные в начало спсика"""
        self.head = Node(data, self.head)

    def insert_at_end(self, data: dict):
        """добавляет данные в конец спсика"""
        if self.head is None:
            self.head = Node(data, None)

        var = self.head
        while var.next_node:
            var = var.next_node

        var.next_node = Node(data, None)

    def to_list(self):
        """возвращает список с данными, содержащимися в односвязном списке"""
        this_node = self.head
        while this_node.next_node != None:
            self.lst.append(this_node.data)
            this_node = this_node.next_node
        self.lst.append(this_node.data)
        return self.lst

    def get_data_by_id(self, id):
        """возвращает первый найденный в LinkedList словарь с ключом id,
        значение которого равно переданному в метод значению, если тип данных подходящий"""
        try:
            if type(self.lst[id]) is dict and 'id' in self.lst[id].keys():
                return self.lst[id]
            else:
                raise TypeError
        except TypeError:
            print('Данные не являются словарем или в словаре нет id')

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f'{str(node.data)} ->'
            node = node.next_node
        ll_string += ' None'
        print(ll_string)


#ll = LinkedList()
#ll.insert_beginning({'id': 1})
#ll.insert_at_end({'id': 2})
#ll.insert_at_end({'id': 3})
#ll.insert_beginning({'id': 0})
#ll.print_ll()

ll = LinkedList()
ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
ll.insert_beginning({'id': 0, 'username': 'serebro'})
ll.print_ll()

lst = ll.to_list()
for item in lst:
    print(item)

user_data = ll.get_data_by_id(3)
print(user_data)

lll = LinkedList()
lll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
lll.insert_at_end('idusername')
lll.insert_at_end([1, 2, 3])
lll.insert_at_end({'id': 2, 'username': 'mosh_s'})

llll_lst = lll.to_list()
user_data = lll.get_data_by_id(1)
print(user_data)
