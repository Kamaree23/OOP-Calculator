# Notes while watching the video


# Four different functions needed
# First will be income

# Second is expenses

#  Third is CashFlow (income -  expenses)

# CashOnCash ROI
# how much are you making from what you put in
# Annual CashFlow /
from gc import garbage
import os
import math


class ROI():
    def __init__(self):
        self.inc = 0
        self.laundry = 0
        self.tax = 0
        self.tot_income = 0
        self.tot_expenses = 0
        self.electric = 0
        self.water = 0
        self.sewer = 0
        self.garbage = 0
        self.gas = 0
        self.lawn = 0
        self.HOA = 0 
        self.lawn = 0
        self.vacancy = 0
        self.repair = 0
        self.copEX = 0 
        self.propertyManage = 0
        self.mortgage = 0
        self.insurance = 0
        self.Cashhflow = 0
        self.downpayment = 0
        self.closingcosts = 0
        self.rehabbudget = 0
        self.other = 0
        self.totalInvestment = 0 
        self.annualcashflow = 0
        self.returnrate = 0
        self.all = 0
         

    def income(self):
        self.inc = float(input('How much is the rental Property Income? \n'))
        self.laundry = float(
            input('How much is the estimated MONTHLY laundry? \n'))
        self.storage = float(
            input('How much is the estimated MONTHLY storage?\n'))
        self.tot_income = self.inc + self.laundry + self.storage
        print(f"your total income is {'{:.2f}'.format(float(self.tot_income))}")

    def expense(self):
        os.system('cls')
        self.tax = float(
            input(f'How much is the MONTHLY tax on the property?:\n'))
        self.insurance = float(
            input(f'How much is the MONTHLY insurance on the property?:\n'))
        self.utilities = input(
            'Will your tenants be paying for utilities? [y] or [n]\n')
        if self.utilities == 'y':
            print(f'Okay! Lets continue!\n')
        else:
            self.electric = float(
                input(f'What is the estimated MONTHLY price for electricity?\n'))
            self.water = float(
                input(f'whatis the estimated MONTHLY price for water?\n'))
            self.sewer = float(
                input(f'What is the estimated MONTHLY price for sewer?\n'))
            self.garbage = float(
                input(f'What is the estimated MONTHLY price for garbage?\n'))
            self.gas = float(
                input(f'What is the estimated MONTHLY price for gas?\n'))
        got_any = input(
            f'is this property loacted in a place where there is HOA fees? [y] or [n]\n')
        if got_any == 'y':
            self.HOA = float(
                input(f'please enter the cost of the Monthly HOA fee:\n'))
        else:
            print(f'Okay! Lets continue!\n')
        self.care =input(f'Will the tenant be covering the Lawn Care? [y] or [n]\n')
        if self.care == 'y':
            print(f'Okay! Lets continue!\n')
        elif self.care == 'n':
            self.lawn = float(
                input(f'How much is the expected MONTHLY lawn care?\n'))
        self.vacancy = float(input(
            f'How much do you want to set aside MONTHLY just incase the property goes without a tenant?\n'))
        self.repair = float(input(
            f'How much do you want to put aside for the small repairs that could pop up during a tenant\'s stay?\n'))
        self.CopEX = float(input(
            f'How much do you want to put aside MONTHLY for the big jobs of the property?\n EX: Roofing, Water Heater, Air Conditioning etc\n'))
        self.propertyManage = float(input(
            f'How much for a property manager? (Normally 10% of the rent if you are paying for one)\n IN this case {self.inc*.10}\n'))
        self.mortgage = float(input(f'How much is the MONTHLY mortgage?\n'))
        self.tot_expenses = self.tax + self.insurance + self.electric + self.water + self.sewer + self.garbage + self.gas + self.HOA + self.lawn + self.vacancy + self.repair +  self.CopEX + self.propertyManage + self.mortgage
        print(f'Your total MONTLY expenses would be {self.tot_expenses}!')
        self.tobesure = input('Everything looks good so far right?\n')
        if self.tobesure == 'y':
            print('Alrighty!')
        else:
            print('Okay! Let\'s start over and see if we can figure it out!')

    def cashFlow(self):
        os.system('cls')
        self.Cashhflow = self.tot_income - self.tot_expenses
        print(f"After calculating everything above, your total Cash flow (Income - Expenses) would be {'{:.2f}'.format(float(self.Cashhflow))}")
   
    def cashOnCashROI(self):
        self.downpayment = float(input(f'What did you put down as a downpayment?\n'))
        self.closingcosts = float(input(f'How much is the expected closing cost?\n'))
        self.rehabbudget = float(input(f'How much is the estimated cost to bring the property up to standard?\n'))
        self.misc = input(f'Any Other expenses? [y] or [n]')
        self.annualcashflow = ('{:.2f}'.format(float(self.Cashhflow * 12)))
        if self.misc == 'y':
            self.other = float(input(f'How much extra have you put into the property?'))
        else:
            print("Alright! Now lets tally all this up!")
        self.totalInvestment = self.downpayment + self.closingcosts + self.rehabbudget + self.other
        print(f'After calulating everything your total investment into the property is\n{self.totalInvestment}\n')
        self.all = (float(self.annualcashflow) / self.totalInvestment) * 100
        elfin = input(f'Alright! It\'s time for the reason we are all here!\ntype (GIVE ME MY MONEY) for results\n')
        if elfin == 'give me my money'.upper():
            print(f"After entering everything that you have given me your total Cash On Cash ROI is....\n\n{'{:.2f}'.format(float(self.all))}%")
        else: 
            print(f'Please enter the appropriate input.')
            ROI.cashOnCashROI(self)

    def quit(self):
        print(f'Thank you for taking the time out today to use our COCROI calculator')
        

#--------Main Body---------#

# def calculations():

#     welcome = input(f'Hello! Welcome to our Rental Property ROI Calculator! Would you like to start?\n Type"y" for yes and "n" for no')
#     if welcome == 'y':
#         ROI.income()


# calculations()
calculator = ROI()
calculator.income()
calculator.expense()
calculator.cashFlow()
calculator.cashOnCashROI()
calculator.quit()
