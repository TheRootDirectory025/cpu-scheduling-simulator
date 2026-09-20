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

## Scheduling Algorithms

### First-Come, First-Served (FCFS)

FCFS schedules processes according to their arrival time.

The process that arrives first is executed first.

FCFS is a non-preemptive scheduling algorithm, meaning that once a process starts running, it continues until it finishes.

### Shortest Job First (SJF)

SJF selects the available process with the shortest burst time.

This implementation uses non-preemptive SJF.

If no process has arrived yet, the CPU remains idle until the next process arrives.

## Input

For each process, the program asks for:

- Process ID
- Arrival Time
- Burst Time

The program validates the input to make sure:

- The number of processes is greater than zero.
- Process IDs are not empty.
- Process IDs are unique.
- Arrival Time is not negative.
- Burst Time is greater than zero.

## Output

The simulator displays:

- Process information
- Start Time
- Completion Time
- Waiting Time
- Turnaround Time
- Average Waiting Time
- Average Turnaround Time
- Gantt Chart

## How to Run

Clone the repository:

```bash
git clone https://github.com/TheRootDirectory025/cpu-scheduling-simulator.git
cd cpu-scheduling-simulator
Run the program:
python project.py
Run the tests:
pytest test_project.py -v
Example
A sample input can contain processes such as:
Process ID: p1
Arrival Time: 0
Burst Time: 8

Process ID: p2
Arrival Time: 1
Burst Time: 4

Process ID: p3
Arrival Time: 2
Burst Time: 2
For FCFS, the processes are executed according to their arrival time.
For SJF, the CPU selects the shortest available process after the current process finishes.
The program then displays the scheduling results and a Gantt chart.
Project Structure
cpu-scheduling-simulator/
├── project.py
├── test_project.py
├── README.md
└── requirements.txt
project.py
Contains the main program, scheduling algorithms, input validation, calculations, and output functions.
test_project.py
Contains automated tests for the scheduling algorithms and calculations.
README.md
Contains documentation and instructions for using the project.
requirements.txt
Contains the Python packages required for running the tests.
Testing
The project uses pytest for automated testing.
The tests cover:
- Average waiting time and turnaround time
- FCFS scheduling
- SJF scheduling
- CPU idle time
- Processes with the same arrival time
- Processes with the same burst time
- Large burst times
- Input data protection from modification
Run all tests with:
pytest test_project.py -v
Technologies
- Python
- pytest
- Git
- GitHub
Author
Mohsen Bagheri