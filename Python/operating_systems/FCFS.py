class FCFS:
    def __init__(self, processes):
        self.processes = dict(sorted(processes.items()))
        self.queue = []
        self.return_time = [0] * len(processes)
        self.wait_time = [0] * len(processes)

    def execute(self):
        cp = 0
        is_running = False
        process = None
        p_n = 0
        while True:
            if p_n == len(self.processes) and not is_running and not self.queue:
                break

            while p_n < len(self.processes) and self.processes[p_n][0] == cp:
                self.queue.append([p_n, self.processes[p_n]])
                p_n += 1

            if not is_running and self.queue:
                process = self.queue.pop(0)
                print(f"process {process[0]} clock {cp} remaining {process[1][1]}")
                is_running = True

            cp += 1
            if is_running:
                process[1][1] -= 1

            for p in self.queue:
                self.wait_time[p[0]] += 1

            if process and process[1][1] <= 0:
                is_running = False
                self.return_time[process[0]] = cp - process[1][0]


fcfs = FCFS(processes={0: [0, 5], 1: [3, 7], 2:[8, 2], 3: [9, 10]})
fcfs.execute()
print(fcfs.wait_time)
print(fcfs.return_time)
