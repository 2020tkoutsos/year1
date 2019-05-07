import re
def string_incrementer(string):
    num = re.findall(r'\d+$',string)
     ## Here re.findall() returns a list of all the found strings
    if len(num)==0:
        number.append(0)
    num = str(num[0])

    str = str.replace(num,'')

    if len(num) == 0:
        number.append('0')

    len_num = len(number)
    num = int(num)+1
    num = str(num).zfill(len_num)
    #(str.zfill) This is final width of the string. This is the width which we would get after filling zeros.
    str = str + num
    return str

#sources
#https://www.tutorialspoint.com/python/python_reg_expressions.htm
#https://developers.google.com/edu/python/regular-expressions
