class Solution:
    def countSeniors(self, details: List[str]) -> int:

        x = 0 

        for d in details:
            if int(d[11:13]) > 60:
                x += 1

        return x
        