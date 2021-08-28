# -*- coding: utf-8 -*-
import time
import plazy

DELTA_THRESHOLD = 0.005  # 5ms
TIME_SLEEP = 0.05  # 50ms


def test_tictoc_no_param():
    tstart = time.time()
    tic_ts = plazy.tic()

    time.sleep(TIME_SLEEP)

    tend = time.time()
    delta_0 = tend - tstart
    delta_1 = plazy.toc()
    assert abs(tic_ts - tstart) <= DELTA_THRESHOLD
    assert abs(delta_0 - delta_1) <= DELTA_THRESHOLD


def test_tictoc_one_name():
    plazy.tic("query")
    time.sleep(TIME_SLEEP)
    delta = plazy.toc("query")
    assert abs(delta - TIME_SLEEP) <= DELTA_THRESHOLD


def test_tictoc_multi_names():
    plazy.tic("db", "orm")
    time.sleep(TIME_SLEEP)
    time_db = plazy.toc("db")
    time.sleep(TIME_SLEEP)
    time_orm = plazy.toc("orm")
    assert abs(time_db - TIME_SLEEP) <= DELTA_THRESHOLD
    assert abs(time_orm - 2 * TIME_SLEEP) <= DELTA_THRESHOLD


def test_toc_multi_names():
    plazy.tic("a", "b", "c")
    time.sleep(TIME_SLEEP)
    times = plazy.toc("b", "a", "c", "d", default=-1)
    print("times", times)
    assert len(times) == 4
    for i in range(3):
        assert abs(times[i] - TIME_SLEEP) <= DELTA_THRESHOLD
    assert times[-1] == -1
