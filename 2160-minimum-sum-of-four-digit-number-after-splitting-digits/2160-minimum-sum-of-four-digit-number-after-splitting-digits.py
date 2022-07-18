class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = sorted(list(map(int, str(num))))
        new1 = str(num_list[0]) + str(num_list[2])
        new2 = str(num_list[1]) + str(num_list[3])
        return int(new1) + int(new2)
        