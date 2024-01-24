print("""
              1.Email should be of length 6-30,
              2.Captial letters, first character as numerical, special characters are not allowed,
              3.Email can contain alphabets(lower case), numbers, and a period(.) followed by com/in only,
              4.Email's first and last character should be an alphabet.
""")

email = input("Enter an Email : ")



def validate_email(email):
    k,j,d,domain = 0,0,0,0

    if 6 <= len(email) <= 30:
        if (email[0].isalpha()) and (email[-1].isalpha()):
            if email.count('@')== 1 and ('gmail' in email):
                if (email.endswith('.com')) or (email.endswith('.in')):
                    for c in email:
                        if c.isspace():
                            print('Space should not exist in email')
                            return
                        elif c.isupper():
                            print('Upper case characters are not allowede in email.')
                            return
                        elif not (c.isalnum() or c in ['@','.']):
                            print('Special Characters other than @ and . are not allowed.')
                            return
                    print("Valid Email!")
                else:
                    print('email should end with .com or .in')    
            else:
                print('Email should contain atleast only one @ and followed by gmail.com/.in')
        else:
            if email[0].isalpha() == False:
                print('The first character should be an alphabet.')
            if email[-1].isalpha() == False:
                print("Email should end with .com or .in")
    else:
        print('email should be of length between 6 to 30 characters.')

validate_email(email)