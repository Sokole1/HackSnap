

def process(*args):
    s = ""
    for elem in args:
        s += f"<option value='{elem}'>{elem}</option>"
    print(s)
        
process("May 2019", "November 2018", "May 2018", "November 2017", "May 2017", "November 2016", "May 2016", "November 2015", "May 2015")













