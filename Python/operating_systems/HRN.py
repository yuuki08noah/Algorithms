class HRN:
    def __init__(self, processes):
        self.processes = sorted(processes.items(), key=lambda item: item[1][1])
        self.number_of_processes = len(processes)
        self.queue = []
        self.return_time = [0] * self.number_of_processes
        self.waiting_time = [0] * self.number_of_processes
        self.waiting_time_refresh = [0] * self.number_of_processes

    def execute(self):
        cp = 0
        current = None
        process_arrival = 0
        while True:
            if process_arrival < self.number_of_processes and self.processes[process_arrival][1][1] == cp:
                self.queue.append(self.processes[process_arrival])
                process_arrival += 1

            if len(self.queue) != 0 and not current:
                max_value = -1
                max_process = 0
                i = 0
                for process in self.queue:
                    if (process[1][0] + self.waiting_time_refresh[process[0]])/process[1][0] > max_value:
                        max_value = (process[1][0] + self.waiting_time_refresh[process[0]])/process[1][0]
                        max_process = i
                    i += 1
                current = self.queue.pop(max_process)
                self.waiting_time_refresh[current[0]] = 0
                print(f"cp {cp} current process: {current[0]} remaining time: {current[1][0]}")

            cp += 1
            if current:
                current[1][0] -= 1
            for process in self.queue:
                self.waiting_time[process[0]] += 1
                self.waiting_time_refresh[process[0]] += 1
            if current and current[1][0] == 0:
                self.return_time[current[0]] = cp - current[1][1]
                current = None
            if process_arrival == self.number_of_processes and not current and len(self.queue) == 0:
                break


# 넘버: [부스트시간, 도착시간]
hrn = HRN(processes={0: [3, 0], 1: [7, 1], 2: [2, 3], 3: [5, 5], 4: [3, 6]})
hrn.execute()
print(sum(hrn.return_time)/hrn.number_of_processes)
print(sum(hrn.waiting_time)/hrn.number_of_processes)