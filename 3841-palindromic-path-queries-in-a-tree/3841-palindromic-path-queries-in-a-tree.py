class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n

        timer = 0
        stack = [(0, -1, False)]

        while stack:
            node, par, exiting = stack.pop()

            if exiting:
                tout[node] = timer - 1
                continue

            parent[node] = node if par == -1 else par

            if par != -1:
                depth[node] = depth[par] + 1
                prefix[node] = (
                    prefix[par] ^ (1 << (ord(s[node]) - ord('a')))
                )
            else:
                prefix[node] = 1 << (ord(s[node]) - ord('a'))

            tin[node] = timer
            timer += 1

            stack.append((node, par, True))

            for child in reversed(graph[node]):
                if child != par:
                    stack.append((child, node, False))

        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]
        up[0] = parent[:]

        for k in range(1, LOG):
            for node in range(n):
                up[k][node] = up[k - 1][up[k - 1][node]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        bit = [0] * (n + 2)

        def update(i, mask):
            while i <= n + 1:
                bit[i] ^= mask
                i += i & -i

        def get(i):
            result = 0

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        def range_xor(left, right, mask):
            update(left + 1, mask)
            update(right + 2, mask)

        chars = list(s)
        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                if chars[u] != c:
                    delta = (
                        (1 << (ord(chars[u]) - ord('a')))
                        ^ (1 << (ord(c) - ord('a')))
                    )

                    range_xor(tin[u], tout[u], delta)
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                pu = prefix[u] ^ get(tin[u] + 1)
                pv = prefix[v] ^ get(tin[v] + 1)

                mask = (
                    pu ^ pv
                    ^ (1 << (ord(chars[w]) - ord('a')))
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans