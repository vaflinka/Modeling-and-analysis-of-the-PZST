class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def build_list(arr, pos):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head
    nodes = [head]

    for x in arr[1:]:
        new_node = ListNode(x)
        curr.next = new_node
        curr = new_node
        nodes.append(new_node)

    if pos != -1:
        curr.next = nodes[pos]

    return head


head = build_list([3, 2, 0, -4], 1)
print(hasCycle(head))

head = build_list([1, 2], 0)
print(hasCycle(head))

head = build_list([1], -1)
print(hasCycle(head))