class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    before_head = ListNode()
    before = before_head

    after_head = ListNode()
    after = after_head

    curr = head
    while curr:
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next

    after.next = None
    before.next = after_head.next

    return before_head.next


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


h1 = build_list([1, 4, 3, 2, 5, 2])
res1 = partition(h1, 3)
print(list_to_array(res1))

h2 = build_list([2, 1])
res2 = partition(h2, 2)
print(list_to_array(res2))