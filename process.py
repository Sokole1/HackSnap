def process(*args):
    s = ""
    for elem in args:
        s += f"<option value='{elem}'>{elem}</option>"
    print(s)
        
process("May 2013", "November 2013", "May 2014", "November 2014", "May 2015")