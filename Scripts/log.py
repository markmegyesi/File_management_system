import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def log_function_call(func):
    def wrapper(*args):
        logging.info(f'Calling function: {func.__name__}')
        logging.info(f'Arguments: {args}')
        result = func(*args)
        logging.info(f'{func.__name__} returned: {result}')
        file_path = f"Log.txt"
        with open(file_path, "x")as file:
            file.write(f"Calling function: {func.__name__} \nArguments: {args} \n{func.__name__} returned: {result}")
        return result
    return wrapper

