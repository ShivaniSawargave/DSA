
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

        def getDays(date):
            month = int(date[:2])
            day = int(date[3:])

            total = day

            for i in range(month - 1):
                total += months[i]

            return total

        start = max(getDays(arriveAlice), getDays(arriveBob))
        end = min(getDays(leaveAlice), getDays(leaveBob))

        if start > end:
            return 0

        return end - start + 1
