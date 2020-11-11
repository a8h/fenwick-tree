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

    def prefix_sum(self, index):
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= index & ~(index - 1)
        return s

    def add(self, index, val):
        while index < len(self.tree):
            self.tree[index] += val
            index += index & ~(index - 1)

    def update(self, index, val):
        curr = self.get(index)
        self.add(index, val - curr)

    def range_sum(self, l, r):
        if l == 1:
            return self.prefix_sum(r)
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

    def get(self, index):
        return self.range_sum(index, index)


def test():
    f = fenwick([1,3,4,8,6,1,4,2])
    print(f.tree)
    assert f.range_sum(1,7) == 27
    print(f.range_sum(1,7))
    f.update(3, 10)
    assert f.range_sum(1,7) == 33
    print(f.range_sum(1,7))

def test2():
    f = fenwick([1,3,5])
    print(f.tree)
    print(f.range_sum(1,3))
    f.update(2, 2)
    print(f.tree)
    print(f.range_sum(1,3))


if __name__ == '__main__':
    test()
    test2()

