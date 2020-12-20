
###################################################################################################
#258
def addDigits( num):
    while num >= 10:
        sum = 0
        while num > 0:
            sum += num %10
            num //= 10
        num = sum
    return num
def addDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    if sum < 10:
        return sum
    else:
        return addDigits(sum)
def addDigits(num):
    num_s = str(num)
    if len(num_s) == 1:
        return num
    else:
        sum = 0
        for i in num_s:
            sum += int(i)
        return addDigits(sum)
#443
def compress(chars):
    len_s = len(chars)
    total, cnt = 0, 0
    for i in range(len(chars)):
        if i < len_s - 1:
            if chars[i] == chars[i+1]:
                cnt += 1
            else:
                if cnt == 0:
                    total += 1
                else:
                    total += 1 + len(str(cnt + 1))
                cnt = 0
        else:
            if chars[i] != chars[i-1]:
                total += 1
            else:
                total += 1 + len(str(cnt + 1))
    return total
def compress(chars):
    prev_ch, loc_update, cnt = chars[0], 0, 1
    for i in range(1, len(chars)):
        if chars[i] == prev_ch:
            cnt += 1
        else:
            str_update = prev_ch + str(cnt) if cnt > 1 else ""
            if cnt == 1:
                chars[loc_update] = prev_ch
                loc_update += 1
            else:
                for item in str_update:
                    chars[loc_update] = item
                    loc_update += 1
            prev_ch = chars[i]
            cnt = 1
    str_update = prev_ch + str(cnt) if cnt > 1 else ""
    for item in str_update:
        chars[loc_update] = item
        loc_update += 1

    chars = chars[0:loc_update]
    print(chars)
    print(loc_update)
    return loc_update
def compress(chars):
    prev_ch, loc_update, cnt = chars[0], 0, 1
    for i in range(1, len(chars)):
        if chars[i] == prev_ch:
            cnt += 1
        else:
            str_update = prev_ch + (str(cnt) if cnt > 1 else "")
            for item in str_update:
                chars[loc_update] = item
                loc_update += 1
            prev_ch = chars[i]
            cnt = 1
    str_update = prev_ch + str(cnt) if cnt > 1 else ""
    for item in str_update:
        chars[loc_update] = item
        loc_update += 1

    chars = chars[0:loc_update]
    print(chars)
    print(loc_update)
    return loc_update
#14
#203

def rmtest(head, val):
    if not head:
        return head
    while head and head.val == val:
        head = head.next
    new_head = head
    while head and head.next:
        if head.next.val == val:
            tmp = head.next
            while tmp and tmp.val == val:
                tmp = tmp.next
            head.next = tmp
            head = tmp
    return new_head
def rmtest(head, val):
    if not head:
        return head
    if head.val == val:
        return rmtest(head.next, val)
    head.next = rmtest(head.next, val)
    return head
def rmtest(head, val):
    if not head:
        return head
    cur = head
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head.next if head.val == val else head
def rmtest(head, val):
    new_head = ListNode(0)
    # new_head = head
    pre = new_head

    while head:
        if head.val != val:
            pre.next = head
            pre = head
            head = head.next
        while head and head.val == val:
            head = head.next
        pre.next = head
        pre = head
        head = head.next if not head else None
    return new_head.next
def rmtest(head, val):
    if not head:
        return head
    head.next = rmtest(head.next, val)
    if head.val == val:
        return head.next
    return head
#543
#TreeNode
def diameterofBt(root):
    rst=[0]
    max_diam(root, rst)
    return rst[0]

def max_diam(root, rst):
    if not root:
        return 0
    left_node = max_diam(root.left, max_val)
    right_node =max_diam(root.right, max_val)
    rst[0] = max(rst[0], left_node + right_node)
    max_val = max(left_node, right_node) + 1
    return max_val

#125
def isPal(str):
    i, j = 0, len(str)-1
    str = str.lower()
    while i < j:
        if str[i].isalnum() and str[j].isalnum():
            if str[i] == str[j]:
                i += 1
                j -= 1
            else:
                return False
        elif str[i].isalnum():
            j -= 1
        elif str[j].isalnum():
            i += 1
        else:
            j -= 1
            i += 1
    return True
#680
def helper(str, k):
    i, j = 0, len(str)-1
    while i < j:
        if i == k:
            i += 1
        if j == k:
            j -= 1
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True


def isPal(str):
    for i in range(len(str)+1):
        if helper(str, i):
            return True
    return False

#
#905
def sortA( A):
    arr_len = len(A)
    rst = list(range(arr_len))
    i, j = 0, arr_len - 1
    for item in A:
        if item % 2 == 0:
            rst[i] = item
            i += 1
        else:
            rst[j] = item
            j -= 1
    return rst
#922
def test_sort(A):
    even = 0
    for odd in range(1, len(A), 2):
        if A[odd] & 1:
            continue
        else:
            while not A[even] & 1:
                even += 2
        A[odd], A[even] = A[even], A[odd]
    return A
#202
def ishtest(n):
    rst = set()
    while True:
        str_n = str(n)
        sum = 0
        for i in str_n:
            sum += (int(i))**2
            print ((int(i))**2)
        if sum == 1:
            return True
        elif sum in rst:
            break
        else:
            rst.add(sum)
            n = sum
    return False
#415
def add_str(num1,num2):
    return str(int(num1) + int(num2))
def add_str(num1,num2):
    i, j = len(num1)-1, len(num2)-1
    carry = 0
    rst = ""
    sum = 0
    while i >=0 or j >=0:
        sum += carry
        sum += (int(num1[i]) if i >= 0 else 0) + (int(num2[j]) if j >= 0 else 0)
        #sum += int(num2[j]) if j >= 0 else 0
        carry = sum // 10
        sum %=  10
        rst = str(sum) + rst
        sum = 0
        i -= 1
        j -= 1
    rst = str(carry) + rst if carry > 0 else rst
    print(rst)
    return rst

#438
def fdana(s,p):
    dict_p, dict_s = {}, {}
    for item in p:
        if item in dict_p:
            dict_p[item] += 1
        else:
            dict_p[item] = 1

    len_s, len_p = len(s), len(p)
    rst = []
    i = 0
    while i < len_s:
        if s[i] not in dict_p:
            i += 1
            if not dict_s:
                dict_s.clear()
            continue
        else:
            if s[i] not in dict_s:
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1

            if len(dict_s) == len(dict_p):
                if dict_s == dict_p:
                    start_index = i - len_p + 1
                    rst.append(start_index)
                    i = start_index + 1
                    if dict_s[s[start_index]] > 1:
                        dict_s[s[start_index]] -= 1
                    else:
                        dict_s.pop(s[start_index])
                else:
                    if dict_s[s[i - len_p + 1]] > 1:
                        dict_s[s[i - len_p + 1]] -= 1
                    else:
                        dict_s.pop(s[i - len_p + 1])

                    i += 1
            else:
                i += 1

    print(rst)
    return rst
def fdana1(s,p):
    len_s, len_p = len(s), len(p)
    dict_s, dict_p = {}, {}
    rst = []
    for item in p:
        if item not in dict_p:
            dict_p[item] = 1
        else:
            dict_p[item] += 1
    for i in range(len(p)-1):
        if s[i] in dict_s:
            dict_s[s[i]] += 1
        else:
            dict_s[s[i]] = 1

    for i in range( len_p - 1, len_s):
        if s[i] in dict_s:
            dict_s[s[i]] += 1
        else:
            dict_s[s[i]] = 1
        if dict_s == dict_p:
            rst.append( i - len_p + 1)
        if dict_s[s[i - len_p + 1]] > 1:
            dict_s[s[i - len_p + 1]] -= 1
        else:
            dict_s.pop(s[i - len_p + 1])
    print(rst)
def fdana(s,p):
    dict_s = Counter(s[:len(p)-1])
    dict_p = Counter(p)

    rst = []
    for i in range(len(p)-1, len(s)):
        dict_s[s[i]] += 1
        if dict_p == dict_s:
            rst.append(i - len(p) + 1)
        if dict_s[s[i - len(p) + 1]] > 1:
            dict_s[s[i - len(p) + 1]]  -= 1
        else:
            del dict_s[s[i - len(p) + 1]]
    return rst

#770
J = "aA"
S = "aAAbbbb"
J1 = "z"
S1 = "ZZ"
def numtone(J, S):
    j_set  = set()
    for j in J:
        if j not in j_set:
            j_set.add(j)
    cnt = 0
    for s in S:
        if s in j_set:
            cnt += 1
    return cnt
#770
J = "aA"
S = "aAAbbbb"
J1 = "z"
S1 = "ZZ"
import time
def numtone(J, S):
    print(type(s in J for s in S))
    print(type(s for s in S))
    return sum([s in J for s in S])
print(numtone(J,S))

print(time.time())
#709
def tolower(str):
    diff = ord('a') - ord("A")
    rst = ""
    for s in str:
        if  "A"<=s<="Z":
            s = chr(ord(s) + diff)
        rst = rst + s
    print(rst)
#
s = "QA test"
ss = (a if a > "A" else "QQ" for a in s)
print(type(ss))

sss = "".join([a if a > "A" else "QQ" for a in s])
print(sss)
#944
def deleteC(A):
    lenA  = len(A)
    lenS = len(A[0])

    cnt = 0
    for i in range(lenS):
        for j in range(lenA-1):
            if A[j][i] > A[j+1][i]:
                cnt += 1
                break
            #continue
    return cnt
#
#700
def  seaBST(root, val):
    if not root:
        return None
    elif root.val == val:
        return root
    elif root.val > val:
        return seaBST(root.left, val)
    else:
        return seaBST(root.right,val)

# 965
def isUni(root):
    if not root:
        return True
    elif root.left and root.right:
        return root.val == root.left.val == root.right.val and isUni(root.left) and isUni(root.right)
    elif root.left:
        return root.val == root.left.val and isUni(root.left)
    else:
        return root.val == root.right.val and isUni(root.right)
#1002
def commonCHars(A):
    dictList = [ Counter(i) for i in A]

    for i in set(A[0]):
        for j in range(1, len(A)):
            if i not in A[j]:
                del dictList[0][i]
                break
            dictList[0][i] = min(dictList[0][i], dictList[j][i])
    return list(dictList[0].elements())
def commonCHars1(A):
    dictList = [ Counter(i) for i in A]

    for i in set(A[0]):
        for j in range(1, len(A)):
            if i not in A[j]:
                del dictList[0][i]
                break
            dictList[0][i] = min(dictList[0][i], dictList[j][i])
    a_list = dictList[0].most_common()
    print(type(dictList[0].most_common()))
    print("dictList[0].most_common()", a_list)
    b_list = dictList[0].elements()
    print("dictList[0].elements()", type(b_list))
    print("dictList[0].elements()", list(b_list))
    dd = dict(dictList[0].most_common())
    print(type(dd), dd)

    print("*"*10)
    cnter = dictList[0]
    print(cnter.items())
    print(cnter.values())

    it_a = dictList[0].elements()
    while True:
        try:
            print(next(it_a))
        except:
            print("end of iterator it_a")
            break
# commonCHars1(b)
###


###
#617
# def mgebt(t1,t2):
#     root = listNode(0)
#     if not t1 and not t2:
#         return None
#     if t1:
#         root.val += t1.val
#     if t2:
#         root.val += t2.val
#     if t1 and t2:
#         root.left  = mgebt(t1.left, t2.left)
#         root.right = mgebt(t1.right, t2.right)
#     elif t1:
#         root.left  = mgebt(t1.left, None)
#         root.right = mgebt(t1.right, None)
#     else:
#         root.left  = mgebt(None, t2.left)
#         root.right = mgebt(None, t2.right)
#     return root
#

# print(abc(a,b))
class a():
    dd = 100
    print("dd is {}".format(dd))
    def test(self):
        print("self.dd is ", self.dd)
        # print("how about dd is ", dd)


aa = a()
aa.test()
# print("a.dd is " a.dd)
class Shark:

    # Class variables
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")
bbb = Shark("jack",100)
bbb.animal_type="Mammel"
ccc = Shark("peter", 3)
print(ccc.animal_type)

print(time.time())
print(round(time.time()))
print(round(time.time()*1000))
#852
def peakIndexInM(A):
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] < A[i+1]:
            break
    return i
#852
def peakIndexInM(A):
    i, j = 0, len(A)-1
    while i < j:
        mid = (i+j)//2
        if A[mid-1] < A[mid] < A[mid+1]:
            break
        elif A[mid] < A[mid-1]:
            j = mid
        elif A[mid] < A[mid+1]:
            i = mid
    return mid
#509
def fib(N):
    numDict = {}
    return helper(N, numDict)
def helper(N, numDict):
    if N < 2: return N
    if N in numDict:
        return numDict[N]
    total = helper(N-1, numDict) + helper(N-2, numDict)
    numDict[N] = total
    return total
# print(fib(N))
#
def fib(N):
    dp = [0, 1]
    if N < 2: return N
    for i in range(2, N+1):
        cur = dp[i-1] + dp[i-2]
        dp.append(cur)

    return dp[N]
#
def fib(N):
    n, n_nxt = 0, 1
    if N < 2: return N
    for i in range(2, N+1):
        total = n + n_nxt
        n, n_nxt = n_nxt, total
    return total
#
def fib(N):
    if N < 2: return N
    arr = [ i for i in range(N+1)]
    for i in range(2, N+1):
        arr[i]= arr[i-1] + arr[i-2]
    return arr[N]
#590
#276
#141
def hasCycle(head):
    if not head or not head.next:
        return False
    temp = head.next.next
    while head and temp:
        if head == temp:
            return True
        if not temp.next:
            return False
        head = head.next
        temp = temp.next.next
    return False
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
#
#422
def validwdSq(words):
    num_row = len(words)
    for r in range(num_row):
        word_r = words[r]
        for col in range(len(word_r)):
            if col > len(words) - 1 or r > len(words[col])-1 or word_r[col] != words[col][r]:
                return False
    return True
#434
def countSeg(s):
    #return len(s.split(" "))
    cnt = 0
    i = 0
    while i < len(s):
        if s[i].isspace():
            i += 1
            continue
        cnt += 1
        while i < len(s) and not s[i].isspace():
            i += 1
    return cnt
#624
def maxDis(arrays):
    left, right = arrays[0][0], arrays[0][-1]
    rst = 0
    for i in range(1, len(arrays)):
        newLeft, newRight = arrays[i][0], arrays[i][-1]
        rst = max(abs(newRight - left), abs(right - newLeft))
        left, right = min(left, newLeft), max(right, newRight)
    return rst
#441
#5, 2; 8, 3

def arrCoin(n):
    cnt = 0
    return log_helper(cnt, n)

def log_helper(cnt, n):
    if n < cnt:
        return cnt - 1
    return log_helper(cnt + 1, n - cnt)

#67
def addBina(a,b):
    sum_str = ""
    i, carry  = -1,0
    while -i <= len(a) or -i <= len(b):
        if -i <= len(a) and -i <= len(b):
            sum_int = carry + int(a[i]) + int(b[i])
            carry = 1 if sum_int > 1 else 0
            sum_str = str(sum_int % 2) + sum_str
        elif -i <= len(a):
            sum_int = carry + int(a[i])
            carry = 1 if sum_int > 1 else 0
            sum_str = str(sum_int % 2) + sum_str
        elif -i <= len(b):
            sum_int = carry + int(b[i])
            carry = 1 if sum_int > 1 else 0
            sum_str = str(sum_int % 2) + sum_str
        i -= 1
    sum_str = sum_str if carry == 0 else str(carry) + sum_str
    return sum_str
def addBina(a, b):
    sum_str = ""
    i, carry  = -1, 0
    while -i <= len(a) or -i <= len(b):
        if -i <= len(a) and -i <= len(b):
            sum_int = carry + int(a[i]) + int(b[i])
        elif -i <= len(a):
            sum_int = carry + int(a[i])
        elif -i <= len(b):
            sum_int = carry + int(b[i])
        carry = 1 if sum_int > 1 else 0
        sum_str = str(sum_int % 2) + sum_str
        i -= 1
    sum_str = sum_str if carry == 0 else str(carry) + sum_str
    return sum_str
#
#224
def calculate(s):
    rst, sign = 0, 1
    len_s = len(s)
    i = 0
    stack = []
    while i < len(s):
        if s[i].isdigit():
            st = i
            while st < len_s and s[st].isdigit():
                st += 1
            rst += sign * int(s[i:st])
            i = st - 1
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == "(":
            stack.extend([rst,sign])
            rst, sign = 0, 1
        elif s[i] == ')':
            rst *= stack.pop()
            rst += stack.pop()
        i += 1
    return rst

ss = '(1+(4+5+2)-3)+(6+8)'
print(calculate(ss))

##6/19/19
#815
from collections import deque
def num_bus(routes, S, T):
    visited = set()
    stop_bus = {}
    deq = deque()

    for bus, stop in enumerate(routes):
        for i in stop:
            if i not in stop_bus:
                stop_bus[i] = set((bus,))
            else:
                stop_bus[i].add(bus)

    if S not in stop_bus or T not in stop_bus:
        return -1

    cnt = 0
    deq.append(S)
    while deq:
        deq_size = len(deq)
        for i in range(deq_size):
            stop = deq.popleft()
            if stop != T:
                visited.add(stop)
                for bus in stop_bus[stop]:
                    for j in routes[bus]:
                        if j not in visited:
                            deq.append(j)
            else:
                return cnt
        cnt += 1
    return -1

routes = [[1,2,7], [3,6,7]]
S , T = 1, 6
print(num_bus(routes, S, T))

##312 Burst Balloons
## 299 Bulls and Cows
## 815 Bus Routes
##1023 Camelcase Matching

#6/21/19
#6/24/19
from collections import deque

# This function returns the minimum cost
def bfs(googleMap, employeeLocation):

    if not googleMap or not googleMap[0] or not employeeLocation:
        return 0

    minCost = 0
    pathToBuilding = []
    rows, cols = len(googleMap), len(googleMap[0])
    # Perform a BFS here
    startX, startY = employeeLocation
    queue = deque([(startX, startY, 0, [])])

    visited = set([(employeeLocation)])

    while queue:
        x, y, currCost, path = queue.popleft()

        if googleMap[x][y] == 'B':  # Destination Reached
            minCost = currCost
            pathToBuilding = path
            break

        for nextX, nextY, dir in [(x, y + 1, 'R'), (x + 1, y, 'D'), (x, y - 1, 'L'), (x - 1, y, 'U')]:
            if 0 <= nextX < rows and 0 <= nextY < cols \
                    and googleMap[nextX][nextY] != '#' \
                    and (nextX, nextY) not in visited:
                visited.add((nextX, nextY))
                queue.append((nextX, nextY, currCost + 1, path + [dir]))

    return (minCost, pathToBuilding)
###
###1057
def assignBikes(self, workers, bikes):
    n, m = len(workers), len(bikes)
    d = []
    for i in range(n):
        for j in range(m):
            d.append((abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]), i, j))
    d.sort(key=lambda x: (x[0], x[1], x[2]))
    ans = [-1] * n
    visited = set()

    for p in d:
        if ans[p[1]] == -1 and p[2] not in visited:
            ans[p[1]] = p[2]
            visited.add(p[2])
    return ans
###

#135 , 7/10/19
ratings = [1,2,2]
def candy(ratings):
    len_kid = len(ratings)
    arr_candy = [1]*len_kid
    i = 1
    while i < len_kid:
        if ratings[i] > ratings[i-1]:
            arr_candy[i] = arr_candy[i-1] + 1
        i += 1
    i = len_kid - 1
    while i > 0:
        if ratings[i-1] > ratings[i]:
            arr_candy[i-1] = max(arr_candy[i-1], arr_candy[i]+1)
        i -= 1

    return sum(arr_candy)


print(candy(ratings))

##7/11
#723
def candyCrush(board):
    m, n = len(board), len(board[0])
    arr_zero = []
    while True:
        for i in range(m):
            for j in range(n):
                left, right = j, j
                up, down = i, i
                while left >= 0 and j - left < 3 and board[i][left] == board[i][j]:
                    left -= 1
                while right < n and right - j < 3 and board[i][right] == board[i][j]:
                    right += 1
                while up >= 0 and i - up < 3 and board[up][j] == board[i][j]:
                    up -= 1
                while down < m and down - i < 3 and board[down][j] == board[i][j]:
                    down += 1
                if down - up > 3 or right - left > 3:
                    arr_zero.append((i,j))

        if arr_zero:
            for i, j in arr_zero.pop():
                board[i][j]= 0
            for j in range(n):
                bottom = m-1
                while bottom >= 0 :
                    if board[bottom][j] == 0:
                        temp_bottom = bottom
                        while temp_bottom >= 0:
                            if board[temp_bottom][j] !=0 :
                                board[bottom][j] = board[temp_bottom][j]
                                board[temp_bottom][j] = 0
                                break
                            temp_bottom -= 1
                        if temp_bottom < 0:
                            break
                    bottom -= 1
        return board

### 7/12/19
#1011

def helper(weights, D, index, d_load, min_load):
    if D == 0:
        # print(d_load)
        min_load[0] = min(min_load[0], max(d_load))
        # print(min_load[0])
        return
    if index == len(weights):
        return
    if D == 1:
        d_load.append(sum(weights[index:]))
        helper(weights, D - 1, len(weights), d_load, min_load)
        d_load.pop()
        return

    for i in range(index, len(weights) - D + 1):
        addto = sum(weights[index: i + 1])
        # print(addto)
        #print(addto, D)
        d_load.append(addto)
        print(len(d_load))
        helper(weights, D - 1, i + 1, d_load, min_load)
        d_load.pop()
        print(len(d_load))

def shipwithindays(weights, D):
    min_load = [float("inf")]
    d_load = []
    index = 0
    helper(weights, D, index, d_load, min_load)
    return min_load[0]

arr = [1,2,3,1,1]

print(min(arr))
print("rst is {}".format(shipwithindays(arr, 4)))

###
#7/16
#1094
# bool, matrix, int
trips = [[3,7,9],[3,2,7],[8,3,9]]
capacity= 11
def carPooling(trips, capacity):
    routes = []
    for i, v in enumerate(trips):
        routes.extend([(v[1], v[0]), (v[2], -v[0])])
    routes = sorted(routes)

    seats_taken = 0
    for i, v in enumerate(routes):
        seats_taken += v[1]
        if seats_taken > capacity:
            return False
    return True

print(carPooling(trips, capacity))
##
#913
# def cmg(graph): # m1, c2, d0

##7/23
#1003
S=["aabcbc", 'abcabcababcc','abccba', 'cababbc']
ss = [True, True, False, False]
def isValid(S):
    len_before = len(S)
    len_after = len(S)
    while True:
        if S:
            S = S.replace("abc","")
            len_after = len(S)
            if len_after == 0:
                return True
            if len_after == len_before:
                return False
            len_before = len_after
        else:
            break
    return True

sss = []
for s in S:
    sss.append(isValid(s))
print(sss)

##
def isValid(S):
    stk = []
    for i in S:
        if i == 'c':
            if len(stk) > 1:
                ele_b = stk.pop()
                ele_a = stk.pop()

                if ele_b != 'b' or ele_a != 'a':
                    return False
            else:
                return False
        else:
            stk.append(i)
    return len(stk) == 0

## 7/24
#721: cherry pickup
# 3D dp

#457, 7/25/19

### 1006 8/9/19
def clumsy(N):
    op_index = 0
    op_size = 4
    result = N
    index = N - 1
    while index >= 1:
        if op_index == 0:
            result *= index
        elif op_index == 1:
            result //= index
        elif op_index == 2:
            result += index
        else:
            temp_rst = index
            index -= 1
            op_index = (op_index + 1) % op_size
            while index >=1 and op_index < 2:
                if op_index == 0:
                    temp_rst *= index
                else:
                    temp_rst //= index
                index -= 1
                op_index = (op_index + 1) % op_size
            result -= temp_rst
            continue



        index -= 1
        op_index = (op_index + 1 ) % op_size

    return result

for i in [4, 10]:
    print("{}, {}".format(i, clumsy(i)))

# 39 , 8/26/19

#77, 8/29

