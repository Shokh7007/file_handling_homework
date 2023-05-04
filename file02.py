def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=open(data,mode='r')
    b=a.read()
    return len(b)
print(main('txt_file/data02.txt'))

# Read data from file