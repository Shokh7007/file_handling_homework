def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=open(data,mode='r')
    b=a.read()
    z=0
    x=0
    c=0
    while x<len(b):
        if b[x].isdigit():
            z+=1
        else:
            c+=1
        x+=1
    d=[c,z]
    return d
print(main('txt_file/data05.txt'))    
# Read data from file