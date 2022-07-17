from abc import ABC, abstractmethod


class Kpi(ABC):
    value = None
    required_schema = None

    def get_value(self):
        return self.value

    def get_required_schema(self):
        return self.required_schema

    @abstractmethod
    def preprocess_data(self, data):
        pass

class GoodKpi(Kpi):
    def preprocess_data(self):
        pass

class BadKpi(Kpi):
    pass

if __name__ == '__main__':
    # this can be instantiated
    good_kpi = GoodKpi()

    # this can't be instantiated, because it hasn't implemented preprocess_data() 
    bad_kpi = BadKpi()