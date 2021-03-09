
class BMI:
    def __init__(self, sex, age, height, weight):
        self.sex = sex
        self.age = float(age)
        self.height = float(height)
        self.weight = float(weight)

    def calculateMiffin(self):
        if self.sex == 'men':
            S = 5
            PPM = 9.99 * self.weight + 6.25 * self.height + 4.92 * self.age + S
            return round(PPM,2)
        elif self.sex == 'women':
            S = -161
            PPM = 9.99 * self.weight + 6.25 * self.height + 4.92 * self.age + S
            return round(PPM,2)

    def calculateHarris(self):
        if self.sex == 'men':
            S = 66
            PPM = S + (13.7 * self.weight) + (5 * self.height) - (6.76 * self.age)
            return round(PPM,2)
        elif self.sex == 'women':
            S = 655
            PPM = S + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age)
            return round(PPM,2)
    def bmi(self):
        return round(self.weight / (self.height/100)**2, 2)

    def category(self):
        n = self.bmi()
        if n<18.49:
            return 'Underweight'
        elif n<24.99:
            return 'Normal'
        elif n<29.99:
            return 'Overweight'
        elif n<34.99:
            return 'Obese level 1'
        elif n<39.99:
            return 'Obese level 2'
        else:
            return 'Obese level 3'

