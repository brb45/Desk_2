def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:



    cur = dummy = ListNode()
    dummy.next = head

    for i in range(m - 1):
        cur = cur.next

    head, tail = cur.next, None
    for i in range(m, n + 1):
        next_node = head.next
        if i == m:
            end = head
        head.next = tail
        tail = head
        head = next_node
    cur.next = tail
    end.next = head

    return dummy.next