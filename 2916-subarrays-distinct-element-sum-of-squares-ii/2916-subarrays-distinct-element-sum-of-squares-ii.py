
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left > end or right < start:
                return

            if left <= start and end <= right:
                length = end - start + 1
                old_sum = tree_sum[node]
                add = 1

                tree_sq[node] = (
                    tree_sq[node] + 2 * add * old_sum
                    + length * add * add
                ) % MOD

                tree_sum[node] = (old_sum + length * add) % MOD
                lazy[node] += add
                return

            mid = (start + end) // 2
            push(node, start, end)

            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        def push(node, start, end):
            add = lazy[node]
            if add == 0 or start == end:
                return

            mid = (start + end) // 2

            for child, length in (
                (node * 2, mid - start + 1),
                (node * 2 + 1, end - mid)
            ):
                old_sum = tree_sum[child]
                tree_sq[child] = (
                    tree_sq[child] + 2 * add * old_sum
                    + length * add * add
                ) % MOD
                tree_sum[child] = (
                    old_sum + length * add
                ) % MOD
                lazy[child] += add

            lazy[node] = 0

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i)
            ans = (ans + tree_sq[1]) % MOD
            last[x] = i

        return ans
