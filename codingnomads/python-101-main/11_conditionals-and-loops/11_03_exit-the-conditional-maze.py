# You wake up in a maze of `if` statements and you need
# to find the path to get out:
#
# .--.--.--.  .--.--.
# |     |        |  |
# :  :--:  :  :  :  :
# |  |     |  |     |
# :  :  :  :--:--:--:
# |  |  |           |
# :  :  :--:--:--:  :
# |  |   You  |  |  |
# :  :--:--:  :  :  :
# |     |     |  |  |
# :--:  :  :--:  :  :
# |        |        |
# :--:--:--:--:--:--:
#
# However, this maze has a BIG limitation!
# There are only two actions you can take, you can only ADD
# either one of the following lines of code:
#
#     flag = True
#     flag = False
#
# You can add as many of them as you want to, but you can't change
# any of the code that is already there.
#
# Add the code so when you run it, it will print out all steps
# that you need to take in order to get out of the maze!
# You are always facing North and you can take sideways steps
# without changing the direction that you're looking.

flag = True

if flag == True:  # Step 1
    print("left")

flag = False      # Step 2
if flag == False:
    print("straight ahead")

flag = True       # Step 3
if flag == True:
    print("left")

flag = False      # Step 4
if flag == False:
    print("straight ahead")

flag = True       # Step 5
if flag == True:
    print("straight ahead")

flag = True       # Step 6
if flag == True:
    print("straight ahead")

flag = False      # Step 7
if flag == False:
    print("right")

flag = True       # Step 8
if flag == True:
    print("straight ahead")

flag = False      # Step 9
if flag == False:
    print("straight ahead")

flag = False      # Step 10

flag = False      # Step 11
if flag == False:
    print("EXIT!!")
