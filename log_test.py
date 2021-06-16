class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 1:46 --> 1:57 4/12/21
        if k == 0 or not head:
            return head
        cur, tail = head, None
        size = 0
        while cur:
            size += 1
            if not cur.next:
                tail = cur
            cur = cur.next

        move = k % size
        if move == 0:  # missed
            return head

        move = size - move - 1
        cur = head
        while move > 0:
            cur = cur.next
            move -= 1
        cur.next, new_head = None, cur.next
        tail.next = head

        return new_head
