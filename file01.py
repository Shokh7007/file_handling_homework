def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=open(data,mode='r')
    return a.read()
print(main('txt_file/data01.txt'))

# Read data from file