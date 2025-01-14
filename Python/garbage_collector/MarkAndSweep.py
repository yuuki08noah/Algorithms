from collections import deque

class MarkAndSweep:
    MEM_TRACKER = {}

    def __init__(self, name):
        MarkAndSweep.MEM_TRACKER[id(self)] = {"count":1, "children":[], "name":name, "marked":False, "id": id(self)}

    def add_ref(self):
        MarkAndSweep.MEM_TRACKER[id(self)]["count"] += 1

    def release_ref(self):
        MarkAndSweep.MEM_TRACKER[id(self)]["count"] -= 1
        if MarkAndSweep.MEM_TRACKER[id(self)]["count"] <= 0:
            print(f"{id(self)} : 객체 소멸")
            del MarkAndSweep.MEM_TRACKER[id(self)]

    def add_child(self, child):
        MarkAndSweep.MEM_TRACKER[id(self)]["children"].append(id(child))
        self.add_ref()

    def collect(**kwargs):
        queue = deque(kwargs["root_ids"])
        for id in kwargs["root_ids"]:
            MarkAndSweep.MEM_TRACKER[id]["marked"] = True

        while queue:
            id = queue.popleft()
            for child in MarkAndSweep.MEM_TRACKER[id]['children']:
                if not MarkAndSweep.MEM_TRACKER[child]['marked']:
                    queue.append(child)
                    MarkAndSweep.MEM_TRACKER[child]['marked'] = True

        cnt = 0
        c = []
        for obj_id, info in MarkAndSweep.MEM_TRACKER.items():
            if not info['marked']:
                print(f"Collecting '{info['name']}' (id: {info['id']})")
                c.append(obj_id)
                cnt += 1
        for k in c:
            del MarkAndSweep.MEM_TRACKER[k]
        return cnt