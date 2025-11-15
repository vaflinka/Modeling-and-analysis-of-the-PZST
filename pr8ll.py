class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head, k):
    curr = head
    count = 0

    while curr and count < k:
        curr = curr.next
        count += 1

    if count < k:
        return head

    prev = None
    curr = head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    head.next = reverseKGroup(curr, k)
    return prev


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


h1 = build_list([1, 2, 3, 4, 5])
res1 = reverseKGroup(h1, 2)
print(list_to_array(res1))

h2 = build_list([1, 2, 3, 4, 5])
res2 = reverseKGroup(h2, 3)
print(list_to_array(res2))