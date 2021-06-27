# 1
br = [0]
def y_arr1(arr):
    print(f'arr is {arr}: id is {id(arr)}') # arr is [0]: id is 17450448

    def change_arr(arr):
        print(f'arr is {arr}: id is {id(arr)}') # arr is [0]: id is 17450448
        # arr.append(100)
        arr[0] = 1000
        print(f'arr is {arr}: id is {id(arr)}') # arr is [1000]: id is 17450448

    change_arr(arr)
    print(f"arr is {arr}: id after change is {id(arr)}") # arr is [1000]: id after change is 17450448

print(f"br is {br}; {id(br)}") # br is [0]; 17450448
y_arr1(br)
print(f"br is {br}; {id(br)}") # br is [1000]; 17450448

# 2
br = [0]
def y_arr1(arr):
    print(f'arr is {arr}: id is {id(arr)}') # arr is [0]: id is 23610832
    def change_arr(arr):
        print(f'arr is {arr}: id is {id(arr)}') # arr is [0, 999]: id is 29189464
        # arr.append(100)
        arr[0] = 1000
        print(f'arr is {arr}: id is {id(arr)}') # arr is [1000, 999]: id is 29189464
    change_arr(arr+[999])
    print(f"arr is {arr}: id after change is {id(arr)}") # arr is [0]: id after change is 23610832

print(f"br is {br}; {id(br)}") # br is [0]; 23610832
y_arr1(br)
print(f"br is {br}; {id(br)}") # br is [0]; 30950864

# 3
br = [0]
def y_arr(arr):
    print(f"arr is {arr}, id is {id(arr)}")
    if len(arr) < 3:
        # arr.append(100-len(arr))
        print(f"arr added is {arr}")
        y_arr(arr+[100-len(arr)])
    else:
        return

y_arr(br)
print(f"br is {br} and id is {id(br)}")


# arr is [0], id is 13452752
# arr added is [0]
# arr is [0, 99], id is 13955960
# arr added is [0, 99]
# arr is [0, 99, 98], id is 13955640
# br is [0] and id is 13452752

# 4-- 842. Split Array into Fibonacci Sequence
class Solution:
    def splitIntoFibonacci(self, S):
        # 5:33 4/22

        def splitArray(S, ind, ans, res):
            if ind == len(S) and len(ans) > 2:
                res = ans # Incorrect
                # res += ans
                return True
            for i in range(ind, len(S)):
                p = S[ind:i + 1]
                if int(p) > (1 << 31) - 1:
                    break
                elif len(p) > 1 and p[0] == "0":
                    break;
                if len(ans) >= 2:
                    if int(ans[-2]) + int(ans[-1]) > int(p):
                        continue
                    elif int(ans[-2]) + int(ans[-1]) < int(p):
                        break
                ans.append(p)
                if splitArray(S, i + 1, ans, res):
                    return True
                # if res:
                #     break
                ans.pop()
            return False

        res = []
        ans = []
        splitArray(S, 0, ans, res)
        return (ans, res)

S= "123456579"
(ans, res) = Solution().splitIntoFibonacci(S)
print(f"res is {res}")   # res is []
print(f"ans is  {ans}")  # ans is  ['123', '456', '579']

# 5
class Solution:
    def splitIntoFibonacci(self, S):
        # 5:33 4/22

        def splitArray(S, ind, ans, res):
            if ind == len(S) and len(ans) > 2:
                res += ans
                # res = ans
                return True
            for i in range(ind, len(S)):
                p = S[ind:i + 1]
                if int(p) > (1 << 31) - 1:
                    break
                elif len(p) > 1 and p[0] == "0":
                    break;
                if len(ans) >= 2:
                    if int(ans[-2]) + int(ans[-1]) > int(p):
                        continue
                    elif int(ans[-2]) + int(ans[-1]) < int(p):
                        break
                ans.append(p)
                if splitArray(S, i + 1, ans, res):
                    return True
                # if res:
                #     break
                ans.pop()
            return False

        res = []
        ans = []
        splitArray(S, 0, ans, res)
        return (ans, res)

S= "123456579"
(ans, res) = Solution().splitIntoFibonacci(S)
print(f"res is {res}")   # res is ['123', '456', '579']
print(f"ans is  {ans}")  # ans is  ['123', '456', '579']

