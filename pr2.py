class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if head is None or head.next is None:
        return head

    first = head
    second = head.next

    first.next = swapPairs(second.next)
    second.next = first

    return second


def build_list(arr):
    if not arr:
        return None
    node = ListNode(arr[0])
    node.next = build_list(arr[1:])
    return node


def to_array(head):
    if head is None:
        return []
    return [head.val] + to_array(head.next)

head = build_list([1, 2, 3, 4])
new_head = swapPairs(head)
print(to_array(new_head))   

head2 = build_list([])
print(to_array(head2))     

head3 = build_list([1])
print(to_array(head3))      