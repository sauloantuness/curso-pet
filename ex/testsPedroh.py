import unittest
from pedroh import *

class TestPedroh(unittest.TestCase):
    def test_SayHi(self):
        self.assertEqual('hi', hi())

    def test_Fatorial(self):
        self.assertEqual(2, fatorial(2))
        self.assertEqual(6, fatorial(3))
        self.assertEqual(1, fatorial(0))

    def test_ehPar(self):
        self.assertEqual(True, ehPar(0))
        self.assertEqual(True, ehPar(1000))
        self.assertEqual(False, ehPar(1))

    def test_lista(self):
        self.assertEqual(['um', 'dois', 'tres'], divideString("um dois tres"))

    def test_inverso(self):
        self.assertEqual(123, inverso(321))
        self.assertEqual(123456789, inverso(987654321))

    def test_dict(self):
        d1 = {
            'nome': 'Pedroh',
            'matricula': 2014123456,
            'ehMulher': False
        }

        self.assertEqual(d1, novoDict('Pedroh', 2014123456, False))
        self.assertEqual('Pedroh', getNome(d1))

        novod1 = {
            'nome': 'Antunes',
            'matricula': 2014123456,
            'ehMulher': False
        }
        self.assertEqual(novod1, setNome(d1, 'Antunes'))

        d2 = {
            'nome': 'Pedroh',
            'matricula': 2014123456,
            'ehMulher': False
        }

        novod2 = {
            'nome': 'Pedroh',
            'matricula': 2014123456,
            'ehMulher': False,
            'aulas': ['Fisica', 'Calculo']
        }

        self.assertEqual(novod2, setAulas(d2, ['Fisica', 'Calculo']))

        d3 = {
            'nome': 'Pedroh',
            'matricula': 2014123456,
            'ehMulher': False,
            'aulas': ['Fisica', 'Calculo']
        }

        novod3 = {
            'nome': 'Pedroh',
            'matricula': 2014123456,
            'ehMulher': False,
            'aulas': ['Fisica', 'Calculo', 'GAAV']
        }
        
        self.assertEqual(novod3, insereAula(d3, 'GAAV'))

        d4 = {
            'nome': 'Pedroh',
            'matricula': 2014123456,
            'ehMulher': False
        }

        novod4 = {
            'nome': 'Pedroh',
            'matricula': 2014123456,
            'ehMulher': False,
            'aulas': ['GAAV']
        }

        self.assertEqual(novod4, insereAula(d4, 'GAAV'))
        self.assertEqual(['GAAV'], getAulas(d4))
        self.assertEqual([], getAulas(d1))

    def test_transforma(self):
        self.assertEqual([1,4,9,16], transforma([1,2,3,4]))

        def cubo(n):
            return n*n*n

        self.assertEqual([1,8,27,64], transforma([1,2,3,4], cubo))

    def test_empregado(self):
        e = Empregado('Pedroh')

        self.assertEqual(700.00, e.getSalario())
        self.assertTrue(hasattr(e, '_Empregado__salario'))

        e = Empregado('Pedroh', 1000.00)

        self.assertEqual(1000.00, e.getSalario())

        with self.assertRaises(AttributeError):
            e.salario

        e.setSalario(200)
        self.assertEqual(200.00, e.getSalario())

    def test_verificaNome(self):
        with self.assertRaises(Exception):
            e = Empregado('')

if __name__ == '__main__':
    unittest.main()
