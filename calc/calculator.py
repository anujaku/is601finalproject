""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction

from calc.history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def addition(values: tuple):
        """ adds list of numbers"""
        Calculations.add_calculation_to_history(Addition.create(values))
        return True

    @staticmethod
    def subtraction(values: tuple):
        """ adds list of numbers"""
        Calculations.add_calculation_to_history(Subtraction.create(values))
        return True

    @staticmethod
    def multiplication(values: tuple):
        """ adds list of numbers"""
        Calculations.add_calculation_to_history(Multiplication.create(values))
        return True

    @staticmethod
    def division(values: tuple):
        """ adds list of numbers"""
        Calculations.add_calculation_to_history(Division.create(values))
        return True
