class Password:
    def passwordTest(self, password):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        bigAlphabet = alphabet.capitalize()
        small, big = 0, 0
        if type(password) != str:
            raise TypeError("Invalid type: {}".format(type(password)))
        for char in password:
            if char in alphabet:
                small += 1
            elif char in bigAlphabet:
                big += 1
        if small + big >= 8 and big > 1:
            return True
        else:
            return False


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={'p': Password()})

# Odpalenie: python3 DocTestExample.py -v