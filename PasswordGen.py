import random                                                                                               # Random Module
print('Simple Password Generator \nIdea by Johan Godinho \nWritten by MattCatt27.')
def main():
    string='abcdefghijklmnopqrstuvwxyz!?@#$%^&*(),.?0123456789'                                             # String of chars to read from
    pw_len=int(input('Enter Length of Password' ))                                                          # Length of Passwords
    pw_amo=int(input('Enter Amount of Passwords to Generate' ))                                             # Amount of Passwords to Generate
    for i in range(pw_amo):                                                                                 # State that in the # of times we want to generate passwords to do the following
        password = ''
        for i in range (pw_len):                                                                            # State that in the length of the passwords we want the following     
            password+=random.choice(string)                                                                  # Password is a random choice of chars from string
        print('Password:', password)                                                                        # Print the password
main()
