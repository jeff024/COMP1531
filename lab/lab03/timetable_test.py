from datetime import date, time, datetime
from timetable import timetable
import pytest

def test_document():
    result = timetable([date(2019,9,27), date(2019,9,30)], [time(14,10), time(10,30)])
    assert result == [datetime(2019,9,27,10,30), datetime(2019,9,27,14,10), datetime(2019,9,30,10,30), datetime(2019,9,30,14,10)]

def test_emptydate():
    result = timetable([], [time(14,10), time(10,30)])
    assert result == []

def test_emptytime():
    result = timetable([date(2019,9,27), date(2019,9,30)], [])
    assert result == []

def test_allempty():
    result = timetable([], [])
    assert result == []

def test_invalid_date():
    with pytest.raises(ValueError, match = r".*"):
        result = timetable([date(2019,15,27), date(2019,9,30)], [time(14,10), time(10,30)])

def test_invalid_time():
    with pytest.raises(ValueError, match = r".*"):
        result = timetable([date(2019,9,27), date(2019,9,30)], [time(25,10), time(10,30)])
