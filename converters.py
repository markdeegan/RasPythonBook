# converters module

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to   = units_to
        self.factor     = factor

    def description(self)
        return 'Convert ' + self_units_from + 'to ' + self_units_to

    def convert(self, value)
        return value * self.factor
