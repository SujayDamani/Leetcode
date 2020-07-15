class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        str_x = "{0:b}".format(x)
        str_y = "{0:b}".format(y)

        print(str_x, str_y)
        str_x = str_x[::-1]
        str_y = str_y[::-1]

        print(str_x, str_y)

        if len(str_x) > len(str_y):
            while len(str_x) != len(str_y):
                str_y = str_y+'0'

        if len(str_x) < len(str_y):
            while len(str_x) != len(str_y):
                str_x = str_x+'0'
        print(str_x, str_y)

        count = 0
        for i in range(0, len(str_x)):
            if str_x[i] != str_y[i]:
                count = count+1

        return count
