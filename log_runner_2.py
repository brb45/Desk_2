from collections import Counter, defaultdict
import collections

username = ["u1", "u1", "u1", "u2", "u2", "u2"]
timestamp = [1, 2, 3, 4, 5, 6]
website = ["a", "b", "a", "a", "b", "c"]


def mostVisitedPattern1(username, timestamp, website):
    # 7:35 --> 7:54 10/31/20

    def helper(i, j, website, tmp, dic):
        if i == 3:
            dic[tuple(tmp)] += 1
            return
        if j == len(website):
            return
        for k in range(j, len(website)):
            helper(i + 1, k + 1, website, tmp + [website[k]], dic)

    tmp = []
    dic = Counter()

    helper(0, 0, website, tmp, dic)

    res = dic.most_common()

    print(res)

    for i in range(len(res)):
        if res[i][1] != res[0][1]:
            break
    if res[i][1] != res[0][1]:
        i = i - 1

    a = sorted(res[:i + 1], key=lambda x: (x[0]))
    print(a)
    return a[0][0]


# mostVisitedPattern1(username, timestamp, website)


def mostVisitedPattern(username, timestamp, website):
    # 7:35 --> 7:54 10/31/20

    def helper(i, j, website, tmp, users, dic):
        if i == 3:
            dic[tuple(tmp)].update(users)
            return
        if j == len(website):
            return
        for k in range(j, len(website)):
            helper(i + 1, k + 1, website, tmp + [website[k][2]], users + [website[k][0]], dic)

    tmp = []
    users = []
    website = list(zip(username, timestamp, website))
    dic = defaultdict(set)

    helper(0, 0, website, tmp, users, dic)

    print(dic)

    for i, v in dic.items():
        dic[i] = len(v)
    print(dic)

    dic = collections.Counter(dic)
    res = dic.most_common()

    for i in range(len(res)):
        if res[i][1] != res[0][1]:
            break
    if res[i][1] != res[0][1]:
        i = i - 1

    return sorted(res[:i + 1], key=lambda x: (x[0]))[0][0]


print(mostVisitedPattern(username, timestamp, website))

aa = defaultdict(collections.deque)
print(aa[0])