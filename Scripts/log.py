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
        with open(file_path, "a")as file:
            file.write(f"\n-Calling function: {func.__name__} \n-Arguments: {args} \n-{func.__name__} returned: {result}")
        return result
    return wrapper

