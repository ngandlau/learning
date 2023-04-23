from collections import namedtuple
from datetime import datetime
from typing import NamedTuple
from dataclasses import dataclass

# a named tuple without typing hints
DateRange = namedtuple('DateRange', 'from_date to_date')

# a named tuple with typing hints
class DateRangeTyped(NamedTuple):
    from_date: datetime
    to_date: datetime

# an alternative, but has caveats
@dataclass
class DateRangeDataclass:
    from_date: datetime
    to_date: datetime
    
if __name__ == '__main__':
    dr = DateRange(
        from_date=datetime(2022, 5, 1),
        to_date=datetime(2022, 5, 2)
    )
    print(dr)
    print(dr.from_date == datetime(2022, 5, 1))
    print(dr[0] == dr.from_date)
    print(dr.to_date == datetime(2022, 5, 2))
    for date in dr:
        print(f'{date=}')

    print('----------------')

    dr_typed = DateRangeTyped(
        from_date=datetime(2022, 5, 1),
        to_date=datetime(2022, 5, 2)
    )
    print(dr_typed)
    print(dr_typed.from_date == datetime(2022, 5, 1))
    print(dr_typed[0] == dr_typed.from_date)
    print(dr_typed.to_date == datetime(2022, 5, 2))
    for date in dr_typed:
        print(f'{date=}')

    print('----------------')

    dr_dataclass = DateRangeDataclass(
        from_date=datetime(2022, 5, 1),
        to_date=datetime(2022, 5, 2)
    )
    print(dr_dataclass)
    print(dr_dataclass.from_date == datetime(2022, 5, 1))
    print(dr_dataclass.to_date == datetime(2022, 5, 2))

    # doesn't work because dataclasses are not unpackable
    print(dr_dataclass[0] == dr_dataclass.from_date)

    # doesn't work because dataclasses are not iterable
    for date in dr_dataclass:
        print(f'{date=}')


