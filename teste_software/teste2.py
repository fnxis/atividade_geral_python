def validaSenha(senha):
    return len(senha) >=8 and any(char.isdigit() for char in senha)

import unittest
class testSenha(unittest.TestCase):
    def test_senha_valida(self):
        self.assertTrue(validaSenha("senha123"))
    def test_senha_curta(self):
        self.assertFalse(validaSenha("curta"))
    def test_senha_sem_numero(self):
        self.assertFalse(validaSenha("semnumero"))

if __name__=='__main__':
    unittest.main()