# CONVERTS ROMAN NUMERALS WITHIN SCOPE TO INTEGER
class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = {'M': 1000, 'D': 500, 'C': 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I': 1}
        prev_val = romanValues[s[0]]
        total = prev_val
        for item in range(1, len(s)):
            current_val = romanValues[s[item]]
            if prev_val < current_val: total += current_val - prev_val * 2
            else: total += current_val
            prev_val = current_val
        return total