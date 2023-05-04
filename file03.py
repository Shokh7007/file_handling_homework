def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=open(data,mode='r')
    b=a.read()
    z= ''
    x=0
    while x<len(b):
        if b[x].isdigit():
            z=z+b[x]
        x+=1
        
    return list(z)
print(main('txt_file/data03.txt'))

# Read data from file
