import unittest

class Money:
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount*multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amout/divisor, self.currency)


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        fiver = Money(5, "USD")
        tenner = Money(10, "USD")
        self.assertEqual(10, tenner.amount)

    def testMultiplicationInEuros(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = tenEuros.times(2)
        self.assertEqual(20, twentyEuros.amount)
        self.assertEqual("EUR", twentyEuros.currency)

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision.amount, 
                         actualMoneyAfterDivison.amount)
        self.assertEqual(expectedMoneyAfterDivision.currency, 
                         actualMoneyAfterDivison.currency)


if __name__ == '__main__':
    unittest.main()
