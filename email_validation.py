# Simple Email Validation Program Using Python

# Take Input From The User
email = input("Enter your Email : ")

# These flags help detect invalid conditions
k = 0   # k → becomes 1 if there is a space in the email
j = 0   # j → becomes 1 if there is an uppercase letter
d = 0   # d → becomes 1 if there is an invalid/special character

# 1 Email must have at least 6 characters
if len(email) >= 6:  # print Wrong email 1.

    # 2 The email must begin with a letter, not a number or special char.
    if email[0].isalpha():  # If it fails → Wrong email 2

        # 3 Valid emails contain exactly one @.
        if ("@" in email) and (email.count("@") == 1):  # If invalid → Wrong email 3

            # 4 XOR (only one must be True)
            # email[-4] == "." → checks .com
            # email[-3] == "." → checks .in / .uk endings
            if (email[-4] == ".") ^ (email[-3] == "."):

                # 5 Check every character
                for i in email:
                    if i.isspace():        # Spaces NOT allowed
                        k = 1
                    elif i.isalpha():      # Check uppercase letters
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():      # Digits allowed
                        continue
                    elif i == "_" or i == "." or i == "@":  # Allowed special chars
                        continue
                    else:                  # All other chars invalid
                        d = 1

                # Final decision
                if k == 1 or j == 1 or d == 1:
                    print("wrong email 5")
                else:
                    print("Right Email")

            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("Wrong email 1")
