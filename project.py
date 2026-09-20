def main():
    processes = get_processes()
    fcfs_scheduled = fcfs(processes)
    avg_waiting_time, avg_turnaround_time = calculate_averages(fcfs_scheduled)
    display_results(fcfs_scheduled, avg_waiting_time, avg_turnaround_time)

def get_processes():
    num_of_proceese = int(input("Number of processes:"))
    processes = []

    for i in range(num_of_proceese):
        process = []
        print(f"Enter data for process {i + 1}")
        process.append(input("Enter Process ID:"))
        process.append(int(input("Arrival time: ")))
        process.append(int(input("Burst time: ")))
        processes.append(process)

    return processes


def fcfs(processes):
    processes_sorted = processes.copy()
    processes_sorted.sort(key=lambda process: process[1])
    current_time = 0

    for process in processes_sorted:
        arrival_time = process[1]
        burst_time = process[2]
        if current_time < arrival_time:
            start_time = arrival_time

        else:
            start_time = current_time

        current_time = start_time + burst_time
        process.append(start_time)
        process.append(current_time)
        waiting_time = start_time - arrival_time
        process.append(waiting_time)
        turnaround_time = current_time - arrival_time
        process.append(turnaround_time)

    return processes_sorted


def calculate_averages(processes):
    sum_of_waiting_time = 0
    sum_of_turnaround_time = 0
    for process in processes:
        sum_of_waiting_time += process[5]
        sum_of_turnaround_time += process[6]

    avg_waiting_time = sum_of_waiting_time / len(processes)
    avg_turnaround_time = sum_of_turnaround_time / len(processes)

    return avg_waiting_time, avg_turnaround_time

def display_results(processes, avg_waiting_time, avg_turnaround_time):
    print(f"|{'ID':^10}|{'Arrival':^12}|{'Burst':^10}|{'Start':^10}|{'Completion':^12}|{'Waiting':^10}|{'Turnaround':^12}")
    print("-" * 83)
    for process in processes:
        print(f"|{process[0]:^10}|{process[1]:^12}|{process[2]:^10}|{process[3]:^10}|{process[4]:^12}|{process[5]:^10}|{process[6]:^12}")


    print()
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

if __name__ == "__main__":
    main()
