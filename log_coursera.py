def com(a,b):
    m,n = len(a), len(b)
    if m < n:
        return False
    i = 0
    while i < m:
        if a[i]==b[0]:
            start = i
            hd = 0
            while hd < n and start < m:
                if a[start] == b[hd]:
                    start += 1
                    hd += 1
                    # if hd == n:
                    #     return True
                else:
                    break
            if hd == n and a[start] == b[n-1]:
                return True

        i += 1
    return False

# print(com('hello world','world'))
# print(com('hello world',' wor'))
# print(com('helloworld',' word'))
print(com('helloworld','worldx'))


#         System.out.println(isSubstring(pri); //true
#         System.out.println(isSubstring("hello world", "world")); //true
#         System.out.println(isSubstring("hello world", " wor")); //true
#         System.out.println(isSubstring("hello world", "word")); //false
#         System.out.println(isSubstring("hello world", "worldx")); //false
#         System.out.println(isSubstring("hello world", "hello world ”)); //false

def com(a, b):
    m, n = len(a), len(b)
    if m < n:
        return False
    i = 0
    while i < m:
        if a[i] == b[0]:
            start = i
            hd = 0
            while hd < n and start < m:
                if a[start] == b[hd]:
                    start += 1
                    hd += 1
                    if hd == n:
                        return True
                else:
                    break
            # if hd == n and a[start] == b[n-1]:
            #     return True
        # else:
        i += 1
    return False


print(com('hello world', 'world'))
print(com('hello world', ' wor'))
print(com('helloworld', ' word'))
print(com('helloworld', 'worldx'))
print(com('hello world', 'hello world '))



