class RR:
    def __init__(self, processes, time_quantum):
        self.processes = sorted(processes.items(), key=lambda item: item[1][1])
        self.number_of_processes = len(processes)
        self.time_quantum = time_quantum
        self.queue = []
        self.return_time = [0] * self.number_of_processes
        self.waiting_time = [0] * self.number_of_processes

    def execute(self):
        cp = 0
        current = None
        process_arrival = 0
        latest = 0
        while True:
            if process_arrival < self.number_of_processes and self.processes[process_arrival][1][1] == cp:
                self.queue.append(self.processes[process_arrival])
                process_arrival += 1

            if len(self.queue) != 0 and (cp - latest == self.time_quantum or current == None):
                if current:
                    self.queue.append(current)
                    current = self.queue.pop(0)
                else:
                    current = self.queue.pop(0)
                print(f"cp {cp} current process: {current[0]} remaining time: {current[1][0]}")
                latest = cp

            cp += 1
            if current:
                current[1][0] -= 1
            for process in self.queue:
                self.waiting_time[process[0]] += 1
            if current and current[1][0] == 0:
                self.return_time[current[0]] = cp - current[1][1]
                current = None
            if process_arrival == self.number_of_processes and not current and len(self.queue) == 0:
                break


# 넘버: [부스트시간, 도착시간]
rr = RR(processes={0: [30, 0], 1: [18, 3], 2: [9, 6]}, time_quantum=10)
rr.execute()
print(rr.return_time)
print(rr.waiting_time)