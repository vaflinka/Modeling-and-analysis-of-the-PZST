class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head


def find_node(head, value):
    curr = head
    while curr:
        if curr.val == value:
            return curr
        curr = curr.next
    return None


def list_to_array(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr


head = build_list([4, 5, 1, 9])
node = find_node(head, 5)
deleteNode(node)
print(list_to_array(head))

head = build_list([4, 5, 1, 9])
node = find_node(head, 1)
deleteNode(node)
print(list_to_array(head))