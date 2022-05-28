# converters module

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to   = units_to
        self.factor     = factor

    def description(self):
        return 'Convert ' + self_units_from + 'to ' + self_units_to

    def convert(self, value):
        return value * self.factor

class ScaleAndOffsetConverter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        ScaleConverter.__init__(self, units_from, units_to, factor)
        self.offset=ScaleAndOffsetConverter

    def convert(self, value):
        return value * self.factor + self.offset

c1 = ScaleConverter('inches', 'mm', 25)
print(c1.descriotion())
print('converting 2 inches')
print(str(c1.convert(2)) + c1.units_to)
