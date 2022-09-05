"""
An abstract base class with a required *abstract attribute*
"""

from abc import ABC, abstractmethod
from typing import Optional

class Kpi(ABC):
    @property
    @abstractmethod
    def required_attribute(self):
        pass


class GoodKpi(Kpi):
    required_attribute: Optional[int] = None


class BadKpi(Kpi):
    pass

if __name__ == '__main__':
    # this can be instantiated
    good_kpi = GoodKpi()

    # this can't be instantiated, because it's missing the required attribute
    bad_kpi = BadKpi()