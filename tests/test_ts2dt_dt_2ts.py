# -*- coding: utf-8 -*-
import time
from datetime import datetime
import plazy

DATETIME_FORMAT = "%Y/%m/%d %H:%M:%S.%f"


def test_dt2ts():
    dt = datetime(2018, 1, 1, 12, 0, 0)
    assert plazy.dt2ts(dt) == dt.timestamp()


def test_dt2ts_str():
    dt = "2021/08/28 13:27:53.3245"
    assert plazy.dt2ts(dt) == datetime.strptime(dt, DATETIME_FORMAT).timestamp()


def test_ts2dt():
    ts = time.time()
    assert plazy.ts2dt(ts) == datetime.fromtimestamp(ts).strftime(DATETIME_FORMAT)
