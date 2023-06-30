def get_int(ask="", min_number=-1000000, max_number=1000000):
    while True:
        try: 
            while True:
                user_input = input(ask)
                number = int(user_input)
                if number < max_number and number > min_number:
                    return number
                else:
                    print("You should have number between " + str(min_number) + " and " + str(max_number))
        except KeyboardInterrupt:
            exit()
        except:
            print("Try Again")
def get_str(ask=""):
    while True:
        try: 
            while True:
                user_input = input(ask)
                string = str(user_input)
                if string != '':
                    return string
        except KeyboardInterrupt:
            exit()
        except:
            print("Try Again")
def get_float(ask="", min_number=-1000000, max_number=1000000):
    while True:
        try: 
            user_input = input(ask)
            float_number = float(user_input)
            if float_number < max_number and float_number > min_number:
                return float_number
            else:
                print("You should have number between " + str(min_number) + " and " + str(max_number))
        except KeyboardInterrupt:
            exit()
        except:
            print("Try Again")
def get_bool(ask=""):
    while True:
        try: 
            user_input = input(ask)
            if user_input == "True" or user_input == "true" or user_input == "1" or user_input == "Yes" or user_input == "yes" or user_input == "Y" or user_input == "y":
                return True
            if user_input == "False" or user_input == "false" or user_input == "0" or user_input == "No" or user_input == "no" or user_input == "N" or user_input == "n":
                return False
        except KeyboardInterrupt:
            exit()
        except:
            print("Try Again")
def get_char(ask=""):
    while True:
        try: 
            user_input = input(ask)
            char = list(user_input)
            if len(char) == 1:
                char = char[0]
                return char
            else:
                print("Write only one symbol!")
        except KeyboardInterrupt:
            exit()
        except:
            print("Try Again")