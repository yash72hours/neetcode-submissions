class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number = 0

        for i, d in enumerate(digits):
            number += d * (10 ** (len(digits) - 1 - i))

        number += 1

        return [int(x) for x in str(number)]