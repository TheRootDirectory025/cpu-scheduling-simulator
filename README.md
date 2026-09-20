# CPU Scheduling Simulator

A Python-based CPU scheduling simulator for exploring process scheduling algorithms.

## Description

This project simulates CPU scheduling using a queue of processes.

Each process has:
- Process ID
- Arrival Time
- Burst Time

The simulator supports two scheduling algorithms:

- First-Come, First-Served (FCFS)
- Shortest Job First (SJF)

For each process, the simulator calculates:
- Start Time
- Completion Time
- Waiting Time
- Turnaround Time

It also displays a Gantt chart and calculates the average waiting time and average turnaround time.

## How to Run

Clone the repository:

```bash
git clone https://github.com/TheRootDirectory025/cpu-scheduling-simulator.git
cd cpu-scheduling-simulator

Run the program:
python project.py
Run the tests:
pytest test_project.py -v