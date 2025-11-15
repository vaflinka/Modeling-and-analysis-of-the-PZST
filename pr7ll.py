import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    tail = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

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


lists1 = [build_list([1,4,5]), build_list([1,3,4]), build_list([2,6])]
res1 = mergeKLists(lists1)
print(list_to_array(res1))

lists2 = []
res2 = mergeKLists(lists2)
print(list_to_array(res2))

lists3 = [build_list([])]
res3 = mergeKLists(lists3)
print(list_to_array(res3))