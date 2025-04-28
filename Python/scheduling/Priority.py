class Priority:

    def __init__(self, number_of_queue, processes):
        self.queue = [[] for _ in range(number_of_queue)]
        self.number_of_queue = number_of_queue
        self.number_of_processes = len(processes)
        self.waiting_time = [0] * self.number_of_processes
        self.return_time = [0] * self.number_of_processes
        self.processes = sorted(processes.items(), key=lambda item: item[1][1])
        print(self.processes)

    # self.processes
    # [arrival_time, burst_time]

    def execute(self):
        cp = 0
        process_arrival = 0
        current = None
        while True:
            if process_arrival < self.number_of_processes and self.processes[process_arrival][1][1] == cp:
                self.queue[self.processes[process_arrival][1][2]].append(self.processes[process_arrival])
                process_arrival += 1

            if not current:
                for q in self.queue:
                    if q:
                        current = q.pop(0)
                        print(f"cp {cp} current process: {current[0]} remaining time: {current[1][0]}")
                        break

            cp += 1
            if current:
                current[1][0] -= 1
            for q in self.queue:
                for process in q:
                    self.waiting_time[process[0]] += 1
            if current and current[1][0] == 0:
                self.return_time[current[0]] = cp - current[1][1]
                current = None
            if process_arrival == self.number_of_processes and not current and sum(int(len(q) != 0) for q in self.queue) == 0:
                break

rr = Priority(processes={0: [30, 0, 2], 1: [18, 3, 1], 2: [9, 6, 0]}, number_of_queue=3)
rr.execute()
print(rr.return_time)
print(rr.waiting_time)