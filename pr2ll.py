class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
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


head = build_list([1, 1, 2])
print(list_to_array(deleteDuplicates(head)))

head = build_list([1, 1, 2, 3, 3])
print(list_to_array(deleteDuplicates(head)))