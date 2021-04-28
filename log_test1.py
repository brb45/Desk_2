class NumArray:
    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.arr = list(nums)
        self.n = math.ceil(len(self.arr) / (len(self.arr)) ** 0.5)
        self.block = [0] * self.n
        for i in range(len(self.arr)):
            self.block[i // self.n] += self.arr[i]

    def update(self, i: int, val: int) -> None:
        idx = i // self.n
        self.block[idx] += val - self.arr[i]
        self.arr[i] = val

    def sumRange(self, i: int, j: int) -> int:
        sums = 0
        lt_block, rt_block = i // self.n, j // self.n
        if lt_block == rt_block:
            for k in range(i, j + 1):
                sums += self.arr[i]
        else:
            for k in range(i, (lt_block + 1) * self.n):
                sums += self.arr[k]
            for m_block in range(lt_block + 1, rt_block):
                sums += self.block[m_block]

            for k in range((rt_block) * self.n, j + 1):
                sums += self.arr[k]

        return sums