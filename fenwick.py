class fenwick():
    def __init__(self, values):
        self.tree = self.construct(values)

    # O(n) initialization of Fenwick Tree 
    def construct(self, values):
        tree = [0] + values.copy()
        for i in range(1, len(tree)):
            index = i
            i += i & ~(i - 1)
            if i < len(tree):
                tree[i] += tree[index]
        return tree

    def sum(self, r):
        s = 0
        while r > 0:
            s += self.tree[r]
            r -= r & ~(r - 1)
        return s

    def add(self, index, val):
        while index < len(self.tree):
            self.tree[index] += val
            index += index & ~(index - 1)

    def update(self, pos, val):
        self.add(pos, val - self.tree[pos])

    def query_sum_range(self, l, r):
        if l == 1:
            return self.sum(r)
        return self.sum(r) - self.sum(l - 1)

def test():
    f = fenwick([1,3,4,8,6,1,4,2])
    print(f.tree)
    assert f.query_sum_range(1,7) == 27
    print(f.query_sum_range(1,7))
    f.update(3, 10)
    assert f.query_sum_range(1,7) == 33
    print(f.query_sum_range(1,7))

if __name__ == '__main__':
    test()

