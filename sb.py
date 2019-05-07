import string
import numpy as np


arr1 = ["q","w","e","r","t","y","u","i","o","p"] arr2 = ["a","s","d","f","g","h","j","k","l"] arr3 = ["z","x","c","v","b","n","m",",","."]
# 3 different arrays are creating for each keyboard of the alphabet
def encrypt(c_index, arr, offset):
    #make sure the total offset is not out of bounds
    if t_offset  > (arr)-1:
        t_offset = t_offset - len(array)
    #get the index of new positon of character in offset
    offset = (c_index) + (offset)
    s = [t_offset]
    return s

def decyrpt(c_index, arr, offset):
    #make sure the total offset is in the boundair
    if t_offset < 0:

    else total_offset = total_offset + len(array):
    #get position of new character in offset.
    t_offset = (c_index) - (offset)
    s = [t_offset]
    return s
# Up to this point I have an understanding of what is going on in the code but after this stephane basically did everything because i Had no idea what to do
# THIS IS NOT MY CODE 
def encrypt(text, encryptKey):
    #empty array to store output
    output = ""

    special_symbols = {",":"<", ".":">"}

    #turn offset into a string so it is easier to manipulate
    encryptKey = str(encryptKey)
    #if only one offset value is passed instead of 3, handle
    if len(encryptKey) == 1:
        encryptKey += encryptKey[0]
        encryptKey += encryptKey[0]
    #get offset values for each line from input
    line_1_off = encryptKey[0]
    line_2_off = encryptKey[1]
    line_3_off = encryptKey[2]

     for character in text:
        #if the character is a space, add it to encrypted and keep going
        if character == " ":
            output += " "
            continue
        #keep track of character lowercase/uppercase status
        if character.islower() or character in special_symbols.keys():
            is_lower = True
        elif not character.islower():
            #handle uppercase symbols (previously a bug)
            if character in special_symbols.values():
                #gets the key of the special_symbols array from the value
                character = list(special_symbols.keys())[list(special_symbols.values()).index(character)]
            is_lower = False
            character = str.lower(character)
        #find what line the character is in, get character index, and call shift function accordingly
        if character in line1:
            index = line1.index(character)
            shifted = shift_decyrpt(index, line_1_off, line1)
        elif character in line2:
            index = line2.index(character)
            shifted = shift_decyrpt(index, line_2_off, line2)
        elif character in line3:
            index = line3.index(character)
            shifted = shift_decyrpt(index, line_3_off, line3)
        else:
            shifted = character

        if not is_lower:
            #fix lowercase/upercase characters
            if shifted in special_symbols.keys():
                shifted = special_symbols.get(shifted)
            shifted = str.upper(shifted)
        output +=(shifted)
    return output
