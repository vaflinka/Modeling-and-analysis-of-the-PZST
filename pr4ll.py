class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow.next
    slow.next = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first = head
    second = prev

    while second:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2

    return head


def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head


def list_to_array(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr


h1 = build_list([1, 2, 3, 4])
reorderList(h1)
print(list_to_array(h1))

h2 = build_list([1, 2, 3, 4, 5])
reorderList(h2)
print(list_to_array(h2))