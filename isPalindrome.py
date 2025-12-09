class Solution:
    # CHALLENGE VERSION (NO STRING CONVERSION)
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        quotient = x // 10
        base_ten_power = 0
        while quotient >= 1:
            quotient = quotient // 10
            base_ten_power += 1

        for digit in range(base_ten_power):
            front = x // 10 ** (base_ten_power - digit) % 10
            back = x // 10 ** digit % 10
            print(front, back)
            if (front != back):
                return False
        return True
    
    # STRING CONVERSION SOLUTION
    # def isPalindrome(self, x: int) -> bool:
        # answer = True
        # x_copy = x
        # i = 0
        # while x_copy > 0 :
        #     x_copy = x_copy // 10
        # print(i)
        # if x < 0:
        #     answer = False
        # else:
        #     x = str(x)

        #     for i, char in enumerate(x):
        #         print("x[i]:", x[i], "char:", char)
        #         print("x[-i]:", x[-i])
        #         if char != x[-i - 1]:
        #             answer = False
        #             break
            
        # return answer
        