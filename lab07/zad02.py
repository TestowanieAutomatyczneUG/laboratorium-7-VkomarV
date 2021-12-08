import unittest
import doctest


class Password:
    def passwordTest(self, password):
        """
        >>> p = Password()
        >>> p.passwordTest("P@ssword123")
        True
        >>> p.passwordTest("Passworld")
        False
        >>> p.passwordTest("@awokado17")
        False
        >>> p.passwordTest("1!qQ")
        False
        >>> p.passwordTest([])
        Traceback (most recent call last):
            File "C:/Aplikacje/Python/lib/doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.Password.passwordTest[4]>", line 1, in <module>
                p.passwordTest([])
            File "c:/Users/patry/github-classroom/TestowanieAutomatyczneUG/laboratorium-7-VkomarV/lab07/zad02.py", line 25, in passwordTest
                raise TypeError("Invalid type: {}".format(type(password)))
        TypeError: Invalid type: <class 'list'>
        >>> p.passwordTest(11)
        Traceback (most recent call last):
            File "C:/Aplikacje/Python/lib/doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.Password.passwordTest[5]>", line 1, in <module>
                p.passwordTest(11)
            File "c:/Users/patry/github-classroom/TestowanieAutomatyczneUG/laboratorium-7-VkomarV/lab07/zad02.py", line 33, in passwordTest
                raise TypeError("Invalid type: {}".format(type(password)))
        TypeError: Invalid type: <class 'int'>
        """

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        bigAlphabet = alphabet.upper()
        numbers = "0123456789"
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if type(password) != str:
            raise TypeError("Invalid type: {}".format(type(password)))

        if len(password) >= 8 and any(l in bigAlphabet for l in password) and any(
                n in numbers for n in password) and any(s in special_characters for s in password):
            return True
        else:
            return False


class PasswordTest(unittest.TestCase):
    def setUp(self):
        self.temp = Password()

    def testTrue(self):
        self.assertEqual(self.temp.passwordTest("P@ssword123"), True)

    def testFalse(self):
        self.assertEqual(self.temp.passwordTest("p@ssword123"), False)

    def tearDown(self):
        self.tem = None


if __name__ == "__main__":

    doctest.testmod()
    unittest.main()
