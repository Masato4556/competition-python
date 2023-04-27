'''
最小値と最大値のを保持するset

値の追加、削除を行いながら、最小値と最大値を取得したい場合に有効
'''


class MinMaxSet:
    def __init__(self, s=set()):
        self.s = s
        self.min = min(s) if len(s) else 10**18
        self.max = max(s) if len(s) else -1 * 10**18
        self.shouldCalcMin = False
        self.shouldCalcMax = False

    def push(self, x):
        self.s.add(x)
        if x <= self.min:
            self.min = x
            self.shouldCalcMin = False
        if x >= self.max:
            self.max = x
            self.shouldCalcMax = False

    def erase(self, x):
        self.s.remove(x)
        if x == self.min:
            self.shouldCalcMin = True
        if x == self.max:
            self.shouldCalcMax = True

    def minimum(self):
        if self.shouldCalcMin:
            self.min = min(self.s)
            self.shouldCalcMin = False
        return self.min

    def maximum(self):
        if self.shouldCalcMax:
            self.max = max(self.s)
            self.shouldCalcMax = False
        return self.max

    def __str__(self):
        return str(self.s)

    def __len__(self):
        return len(self.s)


mms = MinMaxSet({1,6,3,5,9,12,17,12})

print(mms, len(mms))
print(mms.minimum(), mms.maximum())

mms.erase(1)
mms.push(20)

print(mms.minimum(), mms.maximum())
