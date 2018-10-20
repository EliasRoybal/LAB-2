# Node class
class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None


# This method reads the file where the passwords are stored
def read_passwords(password_list):
    with open('10-million-combos.txt', 'r') as infile:
        for line in infile:
            line = line.split()
            if len(line) > 1:
                add_password(password_list, line[1])


# This method adds all passwords to a linked list
def add_password(password_list, password):
    node = password_list.head
    while node is not None:
        if node.password == password:
            node.count += 1
            return
        node = node.next
    password_list.head = Node(password, 1, password_list.head)
    # print("Password " + "'" + password + "'" + " not found. " + password + " has been added to the list.")


# This method gets the size of the linked list
def get_list_size(password_list):
    node = password_list.head
    linked_list_size = 0
    while node is not None:
        linked_list_size += 1
        node = node.next
    return linked_list_size


# This method displays the linked list of passwords
def display_passwords(password_list):
    node = password_list.head
    limit = 0
    while node is not None and limit < 20:
        print(node.password + ":", node.count)
        node = node.next
        limit += 1


# O(n^2)
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
    password_list = LinkedList()

    read_passwords(password_list)
    linked_list_size = get_list_size(password_list)

    bubble_sort(password_list, linked_list_size)
    display_passwords(password_list)
    print("List size:", linked_list_size)


main()
