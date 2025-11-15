class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def doubleIt(head):
    head = reverseList(head)

    curr = head
    carry = 0

    while curr:
        total = curr.val * 2 + carry
        curr.val = total % 10
        carry = total // 10

        if not curr.next and carry:
            curr.next = ListNode(carry)
            carry = 0
            break

        curr = curr.next

    return reverseList(head)


def build_list(arr):
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


h1 = build_list([1, 8, 9])
res1 = doubleIt(h1)
print(list_to_array(res1))

h2 = build_list([9, 9, 9])
res2 = doubleIt(h2)
print(list_to_array(res2))