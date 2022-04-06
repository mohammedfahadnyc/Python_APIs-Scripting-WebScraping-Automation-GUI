
PLACEHOLDER = "[name]"

with open(file="/Users/fahadsmacbook/Downloads/Python 100 Days/Code/Day 24  - Working with files, directory and path/Mail Merge/Input/Names/invited_names.txt",mode="r+") as names_file:
    names_list = names_file.readlines()



with open(file="/Users/fahadsmacbook/Downloads/Python 100 Days/Code/Day 24  - Working with files, directory and path/Mail Merge/Input/Letters/starting_letter.txt",mode="r+") as letter_file :
    template = letter_file.read()
    for name in names_list :
        new_letter = template.replace(PLACEHOLDER,name.strip())
        with open(file=f"/Users/fahadsmacbook/Downloads/Python 100 Days/Code/Day 24  - Working with files, directory and path/Mail Merge/Output/ReadyToSend/Letter_For_{name.strip()}.txt",mode="w") as send_file :
            send_file.write(new_letter)










# PLACEHOLDER  = "[name]"
#
# with open(file="/Users/fahadsmacbook/Downloads/Python 100 Days/Code/Mail Merge Project Start/Input/Names/invited_names.txt",mode="r") as names_file :
#     names = names_file.readlines()
#
# with open(file="/Users/fahadsmacbook/Downloads/Python 100 Days/Code/Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r") as letter_file :
#     letter_content = letter_file.read()
#     for name in names :
#         new_letter = letter_content.replace(PLACEHOLDER,name.strip())
#         with open(file=f"/Users/fahadsmacbook/Downloads/Python 100 Days/Code/Mail Merge Project Start/Output/ReadyToSend/letter_for{name.strip()}" ,mode="w") as letter_send :
#             letter_send.write(new_letter)
#
#

