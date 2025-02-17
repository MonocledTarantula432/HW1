class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def get_cycle_length(node):
    slow, fast = node, node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return calculate_cycle_length(slow)

    return 0


def calculate_cycle_length(slow):
    current = slow
    length = 0

    while True:
        current = current.next
        length += 1
        if current == slow:
            break

    return length


def concatenate(h1, h2, len1, len2):
    if len1 < len2:
        head = h1
        current = h1
    else:
        head = h2
        current = h2

    while current.next:
        current = current.next

    if len1 < len2:
        current.next = h2
    else:
        current.next = h1

    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# driver code
head1 = ListNode(5)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(1)
head1.next.next.next.next.next = head1.next

print("Cycle Length:", get_cycle_length(head1))

head2 = ListNode(3)
head2.next = ListNode(4)
head2.next.next = ListNode(5)

head3 = ListNode(1)
head3.next = ListNode(2)

concatenated = concatenate(head2, head3, 3, 2)
print("Concatenated Linked List:")
print_linked_list(concatenated)