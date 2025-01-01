import unittest

from src.provider.BenchmarkMeasure.BenchmarkMeasure import BenchmarkMeasure
from src.model.TimeFormat.TimeFormat import TimeFormat

class BenchmarkMeasureTest(unittest.TestCase):

    def testNewInstance(self):
        instance = BenchmarkMeasure()
        self.assertIsInstance(instance, BenchmarkMeasure, "1. Devera ser instanciavel corretamente")

    def testStartState(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.startState("a")
        except:
            value = bool(1)

        self.assertFalse(value, "2. 'startState()' devera retornar valor valido caso possua parametros validos")

    def testStartStateInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.startState(0)
        except:
            value = bool(1)

        self.assertTrue(value, "3. 'startState()' devera retornar excessao caso possua parametros invalidos")

    def testEndState(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.endState("a")
        except:
            value = bool(1)

        self.assertFalse(value, "4. 'endState()' devera retornar valor valido caso possua parametros validos")

    def testEndStateInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.endState(0)
        except:
            value = bool(1)

        self.assertTrue(value, "5. 'endState()' devera retornar excessao caso possua parametros invalidos")

    def testResultByTag(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.startState("a")
            instance.endState("a")
            instance.resultByTag("a", TimeFormat.MILLISEGUNDOS)
        except:
            value = bool(1)

        self.assertFalse(value, "6. 'resultByTag()' devera retornar valor valido caso possua parametros validos")

    def testResultByTagTagInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.resultByTag(0, TimeFormat.MILLISEGUNDOS)
        except:
            value = bool(1)

        self.assertTrue(value, "7. 'resultByTag()' devera retornar excessao caso 'tag' seja invalido")

    def testResultByTagFormatInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.resultByTag("a", 0)
        except:
            value = bool(1)

        self.assertTrue(value, "8. 'resultByTag()' devera retornar excessao caso 'format' seja invalido")

    def testResultByTagNoMatchInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.resultByTag("a", TimeFormat.MILLISEGUNDOS)
        except:
            value = bool(1)

        self.assertTrue(value, "9. 'resultByTag()' devera retornar excessao caso 'tag' nao exista")

    def testResultByTagNoStartInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.startState("a")
            instance.resultByTag("a", TimeFormat.MILLISEGUNDOS)
        except:
            value = bool(1)

        self.assertTrue(value, "10. 'resultByTag()' devera retornar excessao caso 'tag' nao possua start")

    def testResultByTagNoEndInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.endState("a")
            instance.resultByTag("a", TimeFormat.MILLISEGUNDOS)
        except:
            value = bool(1)

        self.assertTrue(value, "11. 'resultByTag()' devera retornar excessao caso 'tag' nao possua end")

    def testResult(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.result(TimeFormat.MILLISEGUNDOS)
        except:
            value = bool(1)

        self.assertFalse(value, "12. 'result()' devera ser valido caso possua parametros validos")

    def testResultFormatInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.result(0)
        except:
            value = bool(1)

        self.assertTrue(value, "13. 'result()' devera retornar uma excessao caso 'format' seja invalido")

    def testExport(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.export("benchmark.json", TimeFormat.MILLISEGUNDOS)
        except:
            value = bool(1)

        self.assertFalse(value, "14. 'export()' devera ser valido caso possua parametros validos")

    def testExportFileNameInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.export(0, TimeFormat.MILLISEGUNDOS)
        except:
            value = bool(1)

        self.assertTrue(value, "15. 'export()' devera retornar uma excessao caso 'fileName' seja invalido")

    def testExportFormatInvalid(self):
        instance = BenchmarkMeasure()
        value = bool(0)
        try:
            instance.export("benchmar.json", 0)
        except:
            value = bool(1)

        self.assertTrue(value, "16. 'export()' devera retornar uma excessao caso 'format' seja invalido")

if __name__ == '__main__':
    unittest.main()
