"""Multiplication Class"""

from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """multiplication calculation object"""
    def get_result(self):
        """get the multiplication results"""
        for index, value  in enumerate(self.values):
            if index == 0:
                multiplication_values = value
            else:
                multiplication_values = multiplication_values * value
        return multiplication_values
