"""
This code will fail at runtime...
Could you help `mypy` catching the problem at compile time?
"""
def sum_numbers(*n) -> float:
    return sum(n)

if __name__ == '__main__':
    sum_numbers(1, 2.0)       # this is not a bug
    sum_numbers('bad value')  # this is a bug - can `mypy` catch it?!

