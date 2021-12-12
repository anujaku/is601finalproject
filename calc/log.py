"""Log file generation"""
import logging

# pylint: disable=line-too-long
# pylint: disable=too-many-arguments)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(recored_number)s %(asctime)s - %(levelname)s - %(message)s','%Y-%m-%d %H:%M:%S')
fh = logging.FileHandler('demo.log')
fh.setFormatter(f)
logger.addHandler(fh)
logging.info("Start to save")
#pylint: disable=logging-fstring-interpolation
#pylint: disable=unspecified-encoding
#pylint: disable=f-string-without-interpolation
#pylint: disable=pointless-string-statement

def save_data(filename, value1, operation, value2, result,log_1_counter):
    """Save data function"""
    log_1_counter=log_1_counter+1
    """Save data function"""
    logger.debug(f'saving details of {filename}..')
    with open('demo.log','a') as append_file:
        append_file.write(f'Filename:{filename} -Record Number:{log_1_counter} - Value1:{value1}, Operation:{operation}, '
                         f'Value2:{value2} - Result:{result}\n')

    return append_file
logger.info(f"Details saved successfully")
