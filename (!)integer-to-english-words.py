class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        dic = {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", \
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", \
                  70: "Seventy", 80: "Eighty", 90: "Ninety"}
        unit = ["", "Thousand", "Million", "Billion"]

        result, i = [], 0
        while num:
            cur = num % 1000
            if num % 1000:
                result.append(self.threeDigits(cur, dic, unit[i]))
            num //= 1000
            i += 1
        return ' '.join(result[::-1])

    def threeDigits(self, num, dic, unit):
        result = []
        if num / 100:
            result = [dic[num / 100] + " " + "Hundred"]
        if num % 100:
            result.append(self.twoDigits(num % 100, dic))
        if unit != '':
            result.append(unit)
        return ' '.join(result)

    def twoDigits(self, num, dic):
        if num in dic:
            return dic[num]
        return dic[(num / 10) * 10] + " " + dic[num % 10]
