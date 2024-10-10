import unittest

def soma(a,b):
    return a+b

class testSoma(unittest.TestCase):
    def test_Soma_Positivo(self):
        self.assertEqual(soma(1,2),3)

    def test_Soma_Negativo(self):
        self.assertEqual(soma(-1,-2),-3)

    def test_Soma_Zero(self):
        self.assertEqual(soma(0,0),0)

if __name__=='__main__':
    unittest.main()