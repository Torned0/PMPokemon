import unittest
import pokemon as Pokemon


class MyTestCase(unittest.TestCase):
    def testPaths(self):
        self.assertEqual(Pokemon.move('N'), 2)
        self.assertEqual(Pokemon.move('NESSOONNEESSOONNEE'), 9)
        self.assertEqual(Pokemon.move('NSNSNSNSNSNSNSNSNSNSN'), 2)
        self.assertEqual(Pokemon.move('EEEEEEEEEEEEEEEEEEEEEEEE'), 25)
        self.assertEqual(Pokemon.move('NESSOONNEESSOONNEE'), 9)

    def testValidation(self):
        self.assertEqual(Pokemon.checkinput(''), 0)
        self.assertEqual(Pokemon.checkinput('nN e'), 1)
        self.assertEqual(Pokemon.checkinput('nnnnnao'), 1)
        self.assertEqual(Pokemon.checkinput('Q'), 1)
        self.assertEqual(Pokemon.checkinput('quit'), -1)
        self.assertEqual(Pokemon.checkinput('n'), 0)


if __name__ == '__main__':
    unittest.main()
