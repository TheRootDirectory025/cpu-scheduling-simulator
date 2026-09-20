def main():
    processes = get_processes()
    print(processes)

def get_processes():
    num_of_proceese = int(input("Number of processes:"))
    processes = []

    for i in range(num_of_proceese):
        process = []
        print(f"Enter data for proceese {i+1}")
        process.append(input("Enter Process ID:"))
        process.append(int(input("Arrival time: ")))
        process.append(int(input("Brust time: ")))
        processes.append(process)

    return processes


if __name__ == "__main__":
    main()
