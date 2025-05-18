import sys
def sum(value1, value2):
    """
    This function takes two values and returns their sum.
    """
    value1 = float(value1)
    value2 = float(value2)
    return value1 + value2

if __name__ == "__main__":
    print("Sum : ", sum(sys.argv[1], sys.argv[2]))
    print(__name__)