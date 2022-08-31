'''
Alinkar Lu
643040818-5
'''

class Numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def add(self):
        return self.x + self.y

    @classmethod
    def display_factors(cls,number):
        if number % 2 == 0:
            num_a = str(number/2)
            num_b = str(number/2)


        else:
            num_a = int(number/2)
            num_b = int(number/2+1) 
        return f"Factors of the {number} is {num_a} and {num_b}"


    @staticmethod
    def is_valid_divisor(number):
        if number // 2 == 0:
            return f"{number} is not a valid divisor"
        else:
            return f"{number} is a valid divisor"

        
        
if __name__ == '__main__':
    print(f'2 + 3 is {Numbers(2,3).add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))