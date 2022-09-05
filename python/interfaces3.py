"""
Example: Abstract class attributes
"""

from abc import ABC, abstractproperty, abstractmethod

class Kpi(ABC):
    # @abstractproperty
    # def some_attribute(self):
    #     pass

    def some_method(self):
        pass

    @abstractmethod
    def another_method(self):
        pass


class GoodKpi(Kpi):
    some_attribute: int = None

    def some_method(self):
        return "some method"

    def another_method(self):
        return "another method"


class BadKpi(Kpi):
    pass

if __name__ == '__main__':
    # this can be instantiated
    good_kpi = GoodKpi()

    # this can't be instantiated, because it hasn't implemented preprocess_data() 
    bad_kpi = BadKpi()