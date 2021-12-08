class Pangram:
    def is_pangram(self, word):
        """
        # >>> p = Pangram()
        >>> p.is_pangram("abcdefghijklmnopqrstuvwxyz")
        True
        >>> p.is_pangram("abc")
        False
        >>> p.is_pangram(11)
        Traceback (most recent call last):
          File "C:\Python310\lib\doctest.py", line 1336, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.Pangram.is_pangram[2]>", line 1, in <module>
            p.is_pangram(11)
          File "C:/Users/pwawrzyniak/github-classroom/TestowanieAutomatyczneUG/laboratorium-7-VkomarV/lab07/zad01.py", line 14, in is_pangram
            raise TypeError("Invalid type: {}".format(type(word)))
        TypeError: Invalid type: <class 'int'>
        >>> p.is_pangram("s p a c j a")
        False
        """


        alphabet = "abcdefghijklmnopqrstuvwxyz"
        if type(word) != type("word"):
            raise TypeError("Invalid type: {}".format(type(word)))

        else:
            for char in alphabet:
                if char not in word.lower():
                    return False

            return True


if __name__ == "__main__":
    # g = Gwiazda()
    # print(g.gwiazda(3, 3)
    # print(g.gwiazdaTest(3, 3))
    # print(Gwiazda.gwiazdaTest.__doc__)
    import doctest

    # doctest.testmod()
    doctest.testmod(extraglobs={'p': Pangram()})

# Odpalenie: python3 DocTestExample.py -v
