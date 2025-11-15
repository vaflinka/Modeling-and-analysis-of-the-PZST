class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2
    return dummy.next


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


list1 = build_list([1, 2, 4])
list2 = build_list([1, 3, 4])
merged = mergeTwoLists(list1, list2)
print(list_to_array(merged))

list1 = build_list([])
list2 = build_list([])
print(list_to_array(mergeTwoLists(list1, list2)))

list1 = build_list([])
list2 = build_list([0])
print(list_to_array(mergeTwoLists(list1, list2)))