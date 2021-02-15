my_header = {'Authorization': 'bearer token_seq'}
import requests

rst = requests.get('https://httpbin.org/headers', headers=my_header)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev_head = None
        while slow:
            node_next = slow.next
            slow.next, rev_head = rev_head, slow.next
            slow = node_next
        cur = dummy = ListNode()
        while rev_head:
            cur.next = head
            head = head.next
            cur.next.next = rev_head
            cur = rev_head
            rev_head = rev_head.next
        if head:
            cur.next = head
            head.next = None
        return dummy.next

