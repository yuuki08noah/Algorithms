import heapq

class SJF:
    def __init__(self, processes):
        self.processes = dict(sorted(processes.items(), key=lambda item: item[1]))
        self.number_of_processes = len(processes)
        self.queue = []
        self.return_time = [0] * self.number_of_processes
        self.waiting_time = [0] * self.number_of_processes

    def execute(self):
        cp = 0
        current = None
        process_arrival = 0
        while True:
            if process_arrival < self.number_of_processes and self.processes[process_arrival][1] == cp:
                heapq.heappush(self.queue, [self.processes[process_arrival], process_arrival])
                process_arrival += 1

            if len(self.queue) != 0 and not current:
                current = heapq.heappop(self.queue)
                print(f"current process: {current[1]} remaining time: {current[0][0]}")
            cp += 1
            if current:
                current[0][0] -= 1
            for process in self.queue:
                self.waiting_time[process[1]] += 1
            if current and current[0][0] == 0:
                self.return_time[current[1]] = cp - current[0][1]
                current = None
            if process_arrival == self.number_of_processes and not current and len(self.queue) == 0:
                break


# 넘버: [부스트시간, 도착시간]
sjf = SJF(processes={0: [30, 0], 1: [18, 3], 2: [9, 6]})
sjf.execute()
print(sjf.return_time)
print(sjf.waiting_time)