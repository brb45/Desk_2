# No.1
# url: emil, password, Button login

# driver = webdriver.Chrome()
# driver.get(url)
# email = driver.find_element_by_id("email")
# passwd = driver.find_element_by_class_name("passwd")
# login = driver.find_element_by_id("login")

# email.send_keys("asa@yahoo.com")
# passwd.send_keys("allajdl")
# login.click()
# assert "Success" in message.text
# driver.execute_script("")


# System design:
# tiny url
# enter long url: link to bugs
# output : tiny url

# redirect to long url
# Design and test

# url:palo.jira.com/aaaaaaaaaaaaasfdsfsfsdffsfsfsfsfdfsfdsfsfsfsfsssfsfss
# out:wwww.paloaltotiny.com/1234567890

# Banking application: customer deposit, witd draw, login .....
# Online banking: test and qualify, automate

# sentence = "Mom asked me to get eggs from shop"
# Palindromes = "Mom"

# def helper(s):
#   n = len(s)
#   i,j = 0, n-1
#   s = s.lower()
#   while i <= j:
#     if s[i] == s[j]:
#       i += 1
#       j -= 1
#     else:
#       return False
#   return True

# def is_palin(s):
#   if not s:
#     return []

#   res = []
#   n = len(s)
#   i = 0
#   start = 0
#   while i < n:
#     if s[i].isspace():
#       i += 1
#     else:
#       start = i
#       while i < n and not s[i].isspace():
#         i += 1
#       if helper(start, i-1):
#         res.append(s[start:i])

#   return res


#     ->1>2>3>4
#     head
#     4>3>2>1
#     reverse linked list

#     head
#     1 > new_head

#     newhead = None
#     while head is not None:

#       val = head.val

#       element = LinkList(head_val)
#       element.next = new_head
#       new_head = element

#       head = head.next
#     return new_head

# No.2
input = "(is (a (long)) sentence with )lot of brackets"
# didn't think through logic and talk too much, get distracted
def find_index(s, k):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(' and i <= k:
            cnt += 1
        if i > k:
            break
    for i in range(len(s)):
        if s[i] == ')':
            cnt -= 1
            if cnt == 0:
                return i
    return -1

    # # if not s:
    # #   return -1
    # l_cnt, r_cnt = 0, 0

    # n = len(s)
    # for i in range(n):
    #   if s[i] != '(' or s[i] != ')':
    #     continue
    #   elif s[i] == '(' and i >= k:
    #     l_cnt += 1
    #   elif s[i] == ')' and i >= k:
    #     r_cnt += 1
    #     if r_cnt == l_cnt :
    #       return i

    # # return -1


print(find_index(input, 0))

# No.3
# Python Program to Reverse a Number:

# 1230->0321

# def rev_num(num):
#   num_str = str(num)
#   num_str = num_str[::-1]
#   return num_str

# print(rev_num(1))

def palin(num):
    num_str = str(num)
    n = len(num_str)

    i, j = 0, n - 1
    while i <= j:
        if num_str[i] == num_str[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


# print(palin(12020))

# tail command

def tail_rd(filename, k):
    s = []
    cnt = 0
    with open(filename, 'r') as fin:
        data = fin.readlines()
        cnt = len(data) - 1
        if len(data) > 1:
            if k > len(data):
                k = len(data)
            for i in range(-k, -2, -1):
                print(data[i])
                s.append(data[i])

    while True:
        with open(filename, 'r') as fin:
            data = fin.readlines()
            for i in range(cnt + 1, len(data)):
                print(data[i])
            cnt = len(data) - 1
# No.4
# 1. CI/CD implementation, deployment
# 2. Docker vs VM
# 3. Authentication: username/passwd vs token
# 4. cookie machanism , and authentication
# 5. Horizontal Scale vs Vertical Scale
# 6.







#####
input = "(is(a(long))sentencewith)lotofbrackets"


def find_index(s, k):


    if not s:
      return -1
    n = len(s)
    if k > n-1 or s[k] != '(':
        return -1
    l_cnt, r_cnt = 0, 0

    n = len(s)
    for i in range(n):
      if s[i] != '(' and s[i] != ')':
        continue
      elif s[i] == '(' and i >= k:
        l_cnt += 1
      elif s[i] == ')' and i >= k:
        r_cnt += 1
        if r_cnt == l_cnt :
          return i

    return -1

def find_index_1(s,k):
    if not s:
        return -1
    cnt = 0
    n = len(s)
    if k > n-1 or s[k] != '(':
        return -1
    for i in range(n):
        if i < k:
            continue
        elif i == k:
            cnt = 1
        else:
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
                if cnt == 0:
                    return i

    return -1




for i in [0,3,5]:
    print(find_index(input, i), end=", ")
# 24, 11, 10,
print()
for i in [0,3,5]:
    print(find_index_1(input, i), end=", ")
# 24, 11, 10,



















































































