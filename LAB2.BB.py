# solution B with dictionary
# Node Class
class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None


# This method reads the file where passwords are stored
def read_passwords(password_list, my_dict):
    with open('10-million-combos.txt', 'r') as infile:
        for line in infile:
            credentials = line.split()
            if len(credentials) > 1:
                add_password(credentials[1], my_dict)


# This method adds every password to a dictionary
def add_password(password, my_dict):
    if password in my_dict:
        my_dict[password] += 1
    else:
        my_dict[password] = 1


# This method inserts all components into a linked list
def dump_dict_linked(password_list, my_dict):
    for password in my_dict:
        node = Node(password, my_dict[password], password_list.head)
        password_list.head = node


# This method displays the passwords
def display_passwords(password_list):
    node = password_list.head
    limit = 0
    while node is not None and limit < 20:
        print(node.password + ":", node.count)
        node = node.next
        limit += 1


# This method runs the bubble sort algorithm
def bubble_sort(password_list, linked_list_size):
    for i in range(linked_list_size):
        cur_node = password_list.head
        nxt_node = cur_node.next

        for j in range(linked_list_size - 1):
            if cur_node.count < nxt_node.count:
                tmp_count = cur_node.count
                cur_node.count = nxt_node.count
                nxt_node.count = tmp_count
                tmp_pass = cur_node.password
                cur_node.password = nxt_node.password
                nxt_node.password = tmp_pass

            cur_node = nxt_node
            nxt_node = nxt_node.next


# Main method
def main():
    linked_list_size = 0
    my_dict = {}
    password_list = LinkedList()
    read_passwords(password_list, my_dict)
    dump_dict_linked(password_list, my_dict)

    linked_list_size = len(my_dict)
    bubble_sort(password_list, linked_list_size)
    display_passwords(password_list)
    print("List size:", linked_list_size)


main()
