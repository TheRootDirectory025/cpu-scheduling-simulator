
def main():
    choice = choose_algorithm()
    if choice == "1":
        processes = get_processes()
        processes_sorted, gantt = fcfs(processes)
        avg_waiting_time, avg_turnaround_time = calculate_averages(processes_sorted)
        display_results(processes_sorted, avg_waiting_time, avg_turnaround_time)
        display_gantt_chart(gantt)

    elif choice == "2":
        processes = get_processes()
        processes_sorted, gantt = sjf(processes)
        avg_waiting_time, avg_turnaround_time = calculate_averages(processes_sorted)
        display_results(processes_sorted, avg_waiting_time, avg_turnaround_time)
        display_gantt_chart(gantt)

    elif choice == "3":
        return 0

def get_processes():
    while True :
        try :
            num_of_proceese = int(input("Number of processes:"))
            if num_of_proceese > 0:
                break
            print("Number of processes must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    processes = []

    for i in range(num_of_proceese):
        process = []
        print(f"Enter data for process {i + 1}")
        process.append(input("Enter Process ID:"))

        # Arrival time control
        while True:
            try:
                arrival_time = int(input("Arrival time: "))

                if arrival_time >= 0:
                    break

                print("Arrival time cannot be negative.")

            except ValueError:
                print("Please enter a valid integer.")

        process.append(arrival_time)

        # Burst time
        while True:
            try:
                burst_time = int(input("Burst time: "))

                if burst_time > 0:
                    break

                print("Burst time must be greater than 0.")

            except ValueError:
                print("Please enter a valid integer.")

        process.append(burst_time)
        processes.append(process)

    return processes

def choose_algorithm():
    while True:
        print("\n===== CPU Scheduling Simulator =====")
        print("1. FCFS")
        print("2. SJF")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice in ["1", "2", "3"]:
            return choice

        print("Invalid option. Please choose 1, 2, or 3.")

def fcfs(processes):
    gantt = []
    processes_sorted = [process.copy() for process in processes]
    processes_sorted.sort(key=lambda process: process[1])
    current_time = 0

    for process in processes_sorted:
        arrival_time = process[1]
        burst_time = process[2]
        if current_time < arrival_time:
            idle_time = arrival_time - current_time
            gantt.append(["IDLE", current_time, arrival_time])
            start_time = arrival_time

        else:
            start_time = current_time

        current_time = start_time + burst_time
        gantt.append([process[0], start_time, current_time])
        process.append(start_time)
        process.append(current_time)
        waiting_time = start_time - arrival_time
        process.append(waiting_time)
        turnaround_time = current_time - arrival_time
        process.append(turnaround_time)

    return processes_sorted, gantt

def sjf(processes):
    gantt = []
    scheduled_processes = []
    current_time = 0
    remaining_processes = [process.copy() for process in processes]
    while remaining_processes :
        ready_processes = []
        for process in remaining_processes:
            if current_time >= process[1]:
                ready_processes.append(process)
        min_burst_time = 10000

        selected_process = None
        for process in ready_processes:
            if process[2] < min_burst_time:
                min_burst_time = process[2]
                selected_process = process



        if selected_process is None:
            next_arrival_time = 10000

            for process in remaining_processes:
                if process[1] < next_arrival_time:
                    next_arrival_time = process[1]
            gantt.append(["IDLE", current_time, next_arrival_time])
            current_time = next_arrival_time
            continue

        arrival_time = selected_process[1]
        burst_time = selected_process[2]


        if current_time < arrival_time:
            start_time = arrival_time
        else:
            start_time = current_time
        completion_time = start_time + burst_time
        gantt.append([selected_process[0], start_time, completion_time])
        current_time = completion_time
        waiting_time = start_time - arrival_time
        turnaround_time = completion_time - arrival_time


        selected_process.append(start_time)
        selected_process.append(completion_time)
        selected_process.append(waiting_time)
        selected_process.append(turnaround_time)


        scheduled_processes.append(selected_process)
        remaining_processes.remove(selected_process)


    return scheduled_processes  , gantt

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
    print(
        f"|{'ID':^10}|{'Arrival':^12}|{'Burst':^10}|{'Start':^10}|{'Completion':^12}|{'Waiting':^10}|{'Turnaround':^12}")
    print("-" * 83)
    for process in processes:
        print(
            f"|{process[0]:^10}|{process[1]:^12}|{process[2]:^10}|{process[3]:^10}|{process[4]:^12}|{process[5]:^10}|{process[6]:^12}")

    print()
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

def display_gantt_chart(gantt):
    print("Gantt Chart:")

    gantt_line = "|"
    positions = []

    for item in gantt:
        process_id = item[0]
        start_time = item[1]
        end_time = item[2]

        width = end_time - start_time

        gantt_line += f"{process_id:^{width}}|"
        positions.append(len(gantt_line) - 1)

    print(gantt_line)

    time_line = [" "] * len(gantt_line)

    for i, item in enumerate(gantt):
        start_time = str(item[1])
        end_time = str(item[2])

        if i == 0:
            start_position = 0
            for j, character in enumerate(start_time):
                time_line[start_position + j] = character

        position = positions[i]
        end_position = position - len(end_time) + 1

        for j, character in enumerate(end_time):
            time_line[end_position + j] = character

    print("".join(time_line))

if __name__ == "__main__":
    main()
