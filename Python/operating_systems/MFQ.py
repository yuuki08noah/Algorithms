class MFQ:

    def __init__(self, number_of_queue, burst_time, boost_time, processes):
        self.queue = [[] for _ in range(number_of_queue)]
        self.number_of_queue = number_of_queue
        self.number_of_processes = len(processes)
        self.wait_time = [0] * self.number_of_processes
        self.wait_time_accumulated = [0] * self.number_of_processes
        self.return_time = [0] * self.number_of_processes
        self.burst_time = burst_time
        self.boost_time = boost_time
        self.processes = dict(sorted(processes.items()))

    # self.processes
    # [arrival_time, burst_time]

    def execute(self):
        cp = 0
        process_number = 0
        is_running = False
        latest = 0
        process = None
        q_num = 0
        while True:
            # 더 이상 남은 프로세스가 없을 때
            flag = 0
            if process_number == self.number_of_processes:
                flag = 1
                for q in self.queue:
                    if q or is_running:
                        flag = 0
            if flag == 1:
                break

            # 프로세스가 도착했을 때 넣음
            while process_number < self.number_of_processes and self.processes[process_number][0] == cp:
                self.queue[0].append([process_number, self.processes[process_number]])
                process_number += 1

            # Running 이 없을 때
            if not is_running:
                i = 0
                latest = cp
                while i < self.number_of_queue and not self.queue[i]:
                    i += 1
                q_num = i
                if i != self.number_of_queue:
                    process = self.queue[i].pop(0)
                    self.wait_time[process[0]] = 0
                    print(f"queue {str(self.queue):<60}, clock {cp:<4}, process {(process[0] if process else None):<2}, remaining time {(process[1][1] if process else None):<3}, burst time {self.burst_time[q_num]:<3}")
                    is_running = True

            process[1][1] -= 1
            cp += 1

            # wait 타임 누적 및 wait 타임 초과 시 queue 상승
            for i in range(self.number_of_queue):
                j = 0
                popped = []
                for p in self.queue[i]:
                    if self.wait_time[p[0]] >= self.boost_time[i] and i > 0:
                        self.wait_time[p[0]] = 0
                        self.queue[i - 1].append(p)
                        popped.append(j)
                    else:
                        self.wait_time[p[0]] += 1
                    self.wait_time_accumulated[p[0]] += 1
                    j += 1
                for p in popped:
                    self.queue[i].pop(p)

            # 만약 각 큐의 버스트 시간을 모두 소진했거나 해당 프로세서의 버스트 시간이 0이 됐을 때
            if (q_num < self.number_of_queue and cp - latest == self.burst_time[q_num]) or 0 == process[1][1]:
                is_running = False
                if process[1][1] > 0:
                    if q_num + 1 >= self.number_of_queue:
                        self.queue[0].append(process)
                    else: self.queue[q_num+1].append(process)
                else:
                    self.return_time[process[0]] = cp - process[1][0]


mfq = MFQ(number_of_queue=3, burst_time=[4, 8, 16], boost_time=[0, 16, 32], processes={0:[0, 12], 1:[3, 6], 2:[4, 9], 3: [10, 16], 4: [22, 7], 5: [30, 4]})
mfq.execute()
print(mfq.wait_time_accumulated)
print(mfq.return_time)