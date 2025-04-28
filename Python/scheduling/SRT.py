import heapq

class SJF:
    def __init__(self, processes):
        self.processes = sorted(processes.items(), key=lambda item: item[1][1])
        self.number_of_processes = len(processes)
        self.queue = []
        self.return_time = [0] * self.number_of_processes
        self.waiting_time = [0] * self.number_of_processes

    def execute(self):
        cp = 0
        current = None
        process_arrival = 0
        while True:
            if process_arrival < self.number_of_processes and self.processes[process_arrival][1][1] == cp:
                self.queue.append(self.processes[process_arrival])
                self.queue.sort(key=lambda item: item[1][0])
                process_arrival += 1

            if len(self.queue) != 0:
                if current and self.queue[0][1][0] < current[1][0]:
                    self.queue.append(current)
                    current = self.queue.pop(0)
                    self.queue.sort(key=lambda item: item[1][0])
                    print(f"cp {cp} current process: {current[0]} remaining time: {current[1][0]}")
                elif not current:
                    current = self.queue.pop(0)
                    print(f"cp {cp} current process: {current[0]} remaining time: {current[1][0]}")

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
sjf = SJF(processes={0: [30, 0], 1: [18, 3], 2: [9, 6]})
sjf.execute()
print(sjf.return_time)
print(sjf.waiting_time)