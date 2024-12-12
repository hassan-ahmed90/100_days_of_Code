def format_name(f_name, l_name):
    """This fucntion return the name with formated title"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))


def is_leap_year(year):
    if year % 400 == 0:
        # print("Yes its a leap year")
        return True
    elif year % 100 == 0:
        # print("Its not a leap year"
        return False
    elif year % 4 == 0:
        # print("Yes leap year")
        return True
    else:
        return False

    # Write your code here.
    # Don't change the function name.


print(is_leap_year(1989))