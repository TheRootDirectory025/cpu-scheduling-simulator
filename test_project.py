from project import calculate_averages, fcfs , sjf

def test_calculate_averages():
    processes = [
        ["p1", 0, 8, 0, 8, 0, 8],
        ["p2", 1, 4, 8, 12, 7, 11],
        ["p3", 2, 2, 12, 14, 10, 12]
    ]

    avg_waiting, avg_turnaround = calculate_averages(processes)

    assert avg_waiting == 17 / 3
    assert avg_turnaround == 31 / 3

def test_fcfs():
    processes = [
        ["p1", 0, 8],
        ["p2", 1, 4],
        ["p3", 2, 2],
    ]

    scheduled_processes, gantt = fcfs(processes)

    assert scheduled_processes == [
        ["p1", 0, 8, 0, 8, 0, 8],
        ["p2", 1, 4, 8, 12, 7, 11],
        ["p3", 2, 2, 12, 14, 10, 12],
    ]

def test_sjf():
    processes = [
        ["p1", 0, 8],
        ["p2", 1, 4],
        ["p3", 2, 2],
    ]

    scheduled_processes, gantt = sjf(processes)

    assert scheduled_processes == [
        ["p1", 0, 8, 0, 8, 0, 8],
        ["p3", 2, 2, 8, 10, 6, 8],
        ["p2", 1, 4, 10, 14, 9, 13],
    ]

def test_sjf_with_cpu_idle():
    processes = [
        ["p1", 5, 3],
        ["p2", 6, 2],
        ["p3", 7, 4],
    ]

    scheduled_processes, gantt = sjf(processes)

    assert scheduled_processes == [
        ["p1", 5, 3, 5, 8, 0, 3],
        ["p2", 6, 2, 8, 10, 2, 4],
        ["p3", 7, 4, 10, 14, 3, 7],
    ]

    assert gantt == [
        ["IDLE", 0, 5],
        ["p1", 5, 8],
        ["p2", 8, 10],
        ["p3", 10, 14],
    ]

def test_fcfs_with_cpu_idle():
    processes = [
        ["p1", 5, 3],
        ["p2", 6, 2],
        ["p3", 7, 4],
    ]

    scheduled_processes, gantt = fcfs(processes)

    assert scheduled_processes == [
        ["p1", 5, 3, 5, 8, 0, 3],
        ["p2", 6, 2, 8, 10, 2, 4],
        ["p3", 7, 4, 10, 14, 3, 7],
    ]

    assert gantt == [
        ["IDLE", 0, 5],
        ["p1", 5, 8],
        ["p2", 8, 10],
        ["p3", 10, 14],
    ]

def test_fcfs_same_arrival_time():
    processes = [
        ["p1", 0, 5],
        ["p2", 0, 2],
        ["p3", 0, 3],
    ]

    scheduled_processes, gantt = fcfs(processes)

    assert scheduled_processes == [
        ["p1", 0, 5, 0, 5, 0, 5],
        ["p2", 0, 2, 5, 7, 5, 7],
        ["p3", 0, 3, 7, 10, 7, 10],
    ]

def test_sjf_same_arrival_time():
    processes = [
        ["p1", 0, 5],
        ["p2", 0, 2],
        ["p3", 0, 3],
    ]

    scheduled_processes, gantt = sjf(processes)

    assert scheduled_processes == [
        ["p2", 0, 2, 0, 2, 0, 2],
        ["p3", 0, 3, 2, 5, 2, 5],
        ["p1", 0, 5, 5, 10, 5, 10],
    ]

def test_sjf_same_burst_time():
    processes = [
        ["p1", 0, 4],
        ["p2", 0, 4],
        ["p3", 0, 2],
    ]

    scheduled_processes, gantt = sjf(processes)

    assert scheduled_processes == [
        ["p3", 0, 2, 0, 2, 0, 2],
        ["p1", 0, 4, 2, 6, 2, 6],
        ["p2", 0, 4, 6, 10, 6, 10],
    ]

def test_algorithms_do_not_modify_input():
    processes = [
        ["p1", 0, 8],
        ["p2", 1, 4],
        ["p3", 2, 2],
    ]

    original_processes = [process.copy() for process in processes]

    fcfs(processes)
    sjf(processes)

    assert processes == original_processes

def test_sjf_with_large_burst_time():
    processes = [
        ["p1", 0, 15000],
        ["p2", 1, 2],
    ]

    scheduled_processes, gantt = sjf(processes)

    assert scheduled_processes == [
        ["p1", 0, 15000, 0, 15000, 0, 15000],
        ["p2", 1, 2, 15000, 15002, 14999, 15001],
    ]

    assert gantt == [
        ["p1", 0, 15000],
        ["p2", 15000, 15002],
    ]