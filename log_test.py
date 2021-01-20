def nextLargerNodes(self, head, G) -> List[int]:

    cnt = 0
    flag = 0
    while head and head.next:
        if head.val in G and head.next.val in G:
            if flag == 0:
                cnt += 2
                flag = 1
            else:
                cnt += 1
        else:
            flag = 0
        head = head.next
    return cnt

