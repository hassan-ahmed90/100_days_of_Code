def format_name(f_name,l_name):
    """This function make the name in formated title"""
    if f_name=="" and l_name=="":
        return "No value given"
    formated_f=f_name.title()
    formated_l=l_name.title()
    return f" hello jee {formated_f} {formated_l}"

print(format_name(input("Enter the first name? "),input("Enter the lasta name ?")))

def func01(text):
    return text+text
def func02(text):
    return text.title()

# print(func02(func01("shani")))
