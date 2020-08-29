import queue
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
readline = sys.stdin.readline


class UnionFind():
    def __init__(self, n=0):
        # 負なら根、非負なら親IDの情報を持たせる。負の値の絶対値で連結成分のサイズを表す（-2なら連結成分サイズ2の根）
        self.d = [-1]*n

    def find(self, x):
        """
        根のIDを返す
        """
        if self.d[x] < 0:
            return x  # 今の頂点が根なら頂点番号を返す
        # 今の頂点が根でないなら親についてfindクエリを投げる. d[x] = find(d[x])で経路縮約できる
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        """
        根同士をくっつける
        """
        x = self.find(x)
        y = self.find(y)  # 根同士をくっつける
        if x == y:
            return False  # 根が同じなら何もする必要はない。Falseを返しているのは、くっつけられたかどうかを返した方が便利なときがあるから（MSTなど）
        if self.d[x] > self.d[y]:
            x, y = y, x  # 小さい方の部分木を大きい方の部分木にくっつけるためにswap。dがマイナスなので不等号が逆になる点に注意
        self.d[x] += self.d[y]  # 連結成分サイズを更新
        self.d[y] = x  # 根をyからxに張り替える
        return True

    def same(self, x, y):
        """
        同じ集合に所属しているかどうか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        連結成分サイズを返す
        """
        return -self.d[self.find(x)]


uf = UnionFind(n)

for _ in range(m):
    a, b = [int(i) for i in readline().split()]
    a -= 1
    b -= 1
    uf.unite(a, b)

ans = 0
for i in range(n):
    ans = max(ans, uf.size(i))

print(ans)
