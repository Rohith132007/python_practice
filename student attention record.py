'''

================================== Leet Code problem =================================

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") >= 2:
            return False

        if "LLL" in s:
            return False

        return True

================================ Test Case ================================

'''


def checkRecord(s):
    if s.count("A") >= 2:
        return False

    if "LLL" in s:
        return False

    return True


s = input("Enter attendance record: ")

print(checkRecord(s))
