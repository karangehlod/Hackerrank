class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maximumDifference = 0
        m = list()
        for i in range(0, len(a)):
            for j in range(0, len(a)):
                m = abs(a[i]-a[j])
                if m > maximumDifference:
                    maximumDifference = m
                else:
                    self.maximumDifference = maximumDifference
        return maximumDifference

        # Add your code here

# End of Difference class


_ = input()  # enter number of elements in array
a = [int(e) for e in input().split(' ')]  # array input

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
