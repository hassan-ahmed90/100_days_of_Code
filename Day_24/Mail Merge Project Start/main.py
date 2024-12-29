#
# with open("Input\\Names\invited_names.txt","r") as input_names:
#     b = input_names.readlines()
#
# for name in b:
#     clean_name=name.strip()
#     invitation=f"""Dear {clean_name}
#
#                             You are invited to my birthday this Saturday.
#
#                             Hope you can make it!
#
#                             Angela
#                                 """
#     with open(f"Output\ReadyToSend\\attendee{clean_name}.txt",mode='w') as input_letter:
#         input_letter.write(invitation)
#
#
#
PLACEHOLDER="[name]"

with open("Input\\Names\invited_names.txt") as guest_names:
    a=guest_names.readlines()
with open('Input\Letters\starting_letter.txt') as my_letter:
    b=my_letter.read()
    for name in a:
        striped_name=name.strip()
        completed_letter=b.replace(PLACEHOLDER,striped_name)
        print(completed_letter)
        with open(f"Output\ReadyToSend\letter_for_{striped_name}",mode='w') as final_letter:
            final_letter.write(completed_letter)
