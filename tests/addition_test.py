"""Testing Addition"""
import os
import logging
import pandas as pd
from calc import log
from calc.calculations.addition import Addition

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory

#pylint: disable=unsubscriptable-object
def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename="Input Files/addition.csv"
    path = os.path.join(BASE_DIR,filename)
    data_frame = pd.read_csv(path)
    print("Read CSV file for addition!")
    # print(data_frame)
    for index, row in data_frame.iterrows():
        values = (row.value1, row.value2)
        record_num = index
        addition= Addition.create(values)
        addition_result = data_frame["result"][index]
        log.save_data(filename,row.value1,"+",row.value2,addition_result,record_num)
        logging.debug("Result....!!")
        assert addition.get_result() == addition_result
    print("End of addition operation")
