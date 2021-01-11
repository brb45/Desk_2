def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:

        start = head
        while True:
            cnt = m
            while head and cnt > 1:
                head = head.next
                cnt -= 1

            if not head:
                break
            cnt = n
            tail = head
            while tail and cnt > 0:
                tail = tail.next
                cnt -= 1

            if not tail or not tail.next:
                head.next = None
                break
            head.next = tail.next
            head = head.next
        return start


