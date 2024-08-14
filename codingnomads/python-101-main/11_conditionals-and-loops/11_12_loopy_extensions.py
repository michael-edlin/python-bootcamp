# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
is_pdf = False
pdf_extension = ".pdf"
match_count = 0

for i in range(len(filename) - len(pdf_extension), len(filename)):
    if filename[i] == pdf_extension[match_count]:
        match_count += 1
    else:
        break

if match_count == len(pdf_extension):
    is_pdf = True

if is_pdf:
    print(f"The file '{filename}' is a PDF file.")
else:
    print(f"The file '{filename}' is NOT a PDF file.")