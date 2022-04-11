import math
import string


class Polynomial:
    def __init__(self, highestPower: float, coefficients: list):
        self.highestPower = highestPower
        self.coefficients = coefficients

    def findFactors(self):
        factors = []
        j = 0
        for input in range(-20, 20):
            j += 1
            result = 0
            i = 0
            for coefficient in self.coefficients:
                powerAns = math.pow(input, self.highestPower - i)
                result += (powerAns * coefficient)
                i += 1
            if result == 0:
                if input <= 0:
                    input = math.fabs(input)
                    factors.append(f"x + {input}")
                else:
                    input = math.fabs(input)
                    factors.append(f"x - {input}")
        return factors

highestPower = int(input("What's the highest power of x? "))
currentPower = highestPower
coefficients = list()

alphabet = string.ascii_lowercase

model = "Your equation should be in the form: "

for i in range(highestPower):
    model += f"{alphabet[i]}x^{highestPower - i} + "

model += f"{alphabet[highestPower]}"

print(model)

for i in range(highestPower + 1):
    coefficient = int(input(f"{alphabet[i]}: "))
    coefficients.append(coefficient)

poly = Polynomial(highestPower, coefficients)
factors = poly.findFactors()

for i in factors:
    print(i)

input("Press any key to exit: ")