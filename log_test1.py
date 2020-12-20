def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    # 12:37 11/30/20
    # 4:00 12/1/20

    cur = dummy = ListNode()
    cur.next = head

    cnt = 0

    while cur.next:
        cnt += 1

        if cnt < m:
            cur = cur.next

        elif m <= cnt <= n:
            if cnt == m:
                left_tail = cur
                right_tail = cur.next
                tail = None
            node_next = cur.next.next
            cur.next.next = tail
            tail = cur.next
            cur.next = node_next
            if cnt == n:
                cur.next = tail
                right_tail.next = node_next
                break

    return dummy.next