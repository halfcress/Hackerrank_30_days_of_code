class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maxi = []
        for i in range(len(self.__elements)):
            maxi.append(abs(self.__elements[i] - max(self.__elements)))
        self.maximumDifference = max(maxi)
        return self.maximumDifference

    # tek satır;
    # def computeDifference(self):
        # self.maximumDifference = abs(min(self.__elements)-max(self.__elements))
        # return self.maximumDifference


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)