import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='loggerinfo.log',
    filemode='w'
)

def divide(a, b):
    logging.info(f"Divide {a} by {b}")
    try:
        result = a / b
        logging.debug(f"RESULT: {result}")
        return result
    except ZeroDivisionError:
        logging.error("CANNOT DIVIDE BY 0")

divide(10, 2)
divide(10, 0)