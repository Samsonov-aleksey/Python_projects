import roman
class Solution(object):
    def romanToInt(self, s):
        return roman.fromRoman(s)

romantic = Solution()
print(romantic.romanToInt('MCMXCIV'))        