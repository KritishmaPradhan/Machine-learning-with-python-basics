from loguru import logger

from time import perf_counter, sleep


def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        logger.debug(f"The function {func.__name__} took {duration} seconds")
        return result

    return wrapper


def a_database_connection():
    sleep(4)


a = timeit(a_database_connection)

a()


@timeit
def a_database_connection():
    sleep(4)
    return "successful authentication"


print(a_database_connection())
@timeit
def generate_100_billion_numbers():
    return (
        x
        for x in range(
            10000000000000000000000000000000000000000000000000000000000000000000000000
        )
    )


x = generate_100_billion_numbers()

@timeit
def generate_100_billion_numbers():
    return [x for x in range(100000)]
x = generate_100_billion_numbers()
