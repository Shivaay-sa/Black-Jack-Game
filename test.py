class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def takeinputlist():
    inputlist = [int(ele) for ele in input("Enter the list elements: ").split()]
    head = None
    tail = None
    for currdata in inputlist:
        if currdata == -1:
            break
        newnode = Node(currdata)
        if head is None:
            head = newnode
            tail = newnode

        else:
            tail.next = newnode
            tail = newnode

    return head


def reverse(head):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def midpoint(head):
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    print("Midpoint of linked list is --> ", slow.data)
    return


def merge(head1, head2):
    final_head = head1
    final_tail = head1
    while head1 != None and head2 != None:
        if head1.data <= head2.data:
            final_tail.next = head1
            final_tail = final_tail.next
            head1 = head1.next
        else:
            final_tail.next = head2
            final_tail = final_tail.next
            head2 = head2.next

    if head1 != None:
        final_tail.next = head1
    elif head2 != None:
        final_tail.next = head2

    return final_head


def printll(head):
    while head is not None:
        print(head.data, "-->", end=" ")
        head = head.next
    print("None")
    return


print("Enter first linked list element in a sorted manner: ")
head1 = takeinputlist()
print("Enter second linked list element in a sorted manner: ")
head2 = takeinputlist()
final_head = merge(head1, head2)
printll(final_head)