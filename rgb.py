def validate(n):
    if n>255:
        n=255
    elif n<0:
        n=0
    return n
def hex_convert(n_int):
    n_hex = hex(n_int)[2:].upper()
    if len(n_hex) != 2:
        return "0"+n_hex
    else:
        return n_hex
def rgb(r, g, b):
    r = validate(r)
    g = validate(g)
    b = validate(b)
    return hex_convert(r) + hex_convert(g) + hex_convert(b)
