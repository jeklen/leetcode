class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        flagLast = []
        flagSecond = []
        allValue = []
        flagLast.append(True)
        flagSecond.append(False)
        rank = int(ops[0])
        #valueLast = ops[0] - '0'
        allValue.append(int(ops[0]))
        for index, value in enumerate(ops):
            if not index:
                continue
            # Represents the last valid round's points you get were invalid and should be removed.
            if value == 'C':
                rank = rank - allValue[-1]
                allValue = allValue[:-1]
                flagLast = flagLast[:-1]
                flagSecond = flagSecond[:-1]
                continue
            # Represents that the points you get in this round are the doubled data of the last valid round's points.
            if value == 'D':
                value = 2 * allValue[-1]
                rank = rank + value
                allValue.append(value)
                if flagLast and flagSecond:
                    flagLast.append(True)
                    flagSecond.append(True)
                if flagLast and (not flagSecond):
                    flagLast.append(True)
                    flagSecond.append(True)
                if (not flagLast) and (not flagSecond):
                    flagLast.append(True)
                    flagSecond.append(False)
                continue
            if value == '+':
                # (one round's score): Represents that the points you get in this round are the rank of the last two valid round's point
                value = allValue[-1] + allValue[-2]
                rank = rank + value
                allValue.append(value)
                if flagLast and flagSecond:
                    flagLast.append(True)
                    flagSecond.append(True)
                if flagLast and (not flagSecond):
                    flagLast.append(True)
                    flagSecond.append(True)
                if (not flagLast) and (not flagSecond):
                    flagLast.append(True)
                    flagSecond.append(False)
                continue

            value = int(value)
            rank = rank + value
            allValue.append(value)
            if flagLast and flagSecond:
                flagLast.append(True)
                flagSecond.append(True)
            if flagLast and (not flagSecond):
                flagLast.append(True)
                flagSecond.append(True)
            if (not flagLast) and (not flagSecond):
                flagLast.append(True)
                flagSecond.append(False)
        return rank


foo = Solution()
final_rank = foo.calPoints(["5","-2","4","C","D","9","+","+"])
print(final_rank)