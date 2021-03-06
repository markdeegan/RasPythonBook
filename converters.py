# converters module

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to   = units_to
        self.factor     = factor

    def description(self):
        return 'Convert ' + self.units_from + ' to ' + self.units_to

    def convert(self, value):
        return value * self.factor

class ScaleAndOffsetConverter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        ScaleConverter.__init__(self, units_from, units_to, factor)
        self.offset=offset

    def convert(self, value):
        return (value * self.factor) + self.offset

c1 = ScaleConverter('inches', 'mm', 25.0)
# print(c1.description())
# print('Converting 2 inches')
# print(str(c1.convert(2)) + c1.units_to)

c2 = ScaleAndOffsetConverter('Celsius', 'Fahrenheit', 1.8, 32.0)
print(c2.description())
print('Converting 100 degrees C')
print(str(c2.convert(100)) + ' ' + c2.units_to)

c4 = ScaleAndOffsetConverter('Fahrenheit', 'Celsius', 0.5555, -32.0)
print(c4.description())
print('Converting 0 degrees F')
print(str(c4.convert(0)) + ' ' + c4.units_to)

c5 = ScaleAndOffsetConverter('Fahrenheit', 'Celsius', 0.5555, -32.0)
print(c5.description())
print('Converting 0 degrees F')
print(str(c5.convert(100)) + ' ' + c5.units_to)
