from collections import deque

class MemoryObject:
    MEM_TRACKER = {}
    def __init__(self, name):
        MemoryObject.MEM_TRACKER[id(self)] = {"count":1, "children":[], "name":name, "marked":False, "id": id(self)}

    def add_ref(self):
        MemoryObject.MEM_TRACKER[id(self)]["count"] += 1

    def release_ref(self):
        MemoryObject.MEM_TRACKER[id(self)]["count"] -= 1
        if MemoryObject.MEM_TRACKER[id(self)]["count"] <= 0:
            print(f"{id(self)} : 객체 소멸")
            del MemoryObject.MEM_TRACKER[id(self)]

    def add_child(self, child):
        MemoryObject.MEM_TRACKER[id(self)]["children"].append(id(child))
        self.add_ref()

    def force_collect(**kwargs):
        queue = deque(kwargs["root_ids"])
        for id in kwargs["root_ids"]:
            MemoryObject.MEM_TRACKER[id]["marked"] = True

        while queue:
            id = queue.popleft()
            for child in MemoryObject.MEM_TRACKER[id]['children']:
                if not MemoryObject.MEM_TRACKER[child]['marked']:
                    queue.append(child)
                    MemoryObject.MEM_TRACKER[child]['marked'] = True

        cnt = 0
        c = []
        for obj_id, info in MemoryObject.MEM_TRACKER.items():
            if not info['marked']:
                print(f"Collecting '{info['name']}' (id: {info['id']})")
                c.append(obj_id)
                cnt += 1
        for k in c:
            del MemoryObject.MEM_TRACKER[k]
        return cnt

obj1 = MemoryObject("A")
obj2 = MemoryObject("B")
obj3 = MemoryObject("C")
obj4 = MemoryObject("D")
obj5 = MemoryObject("E")

obj1.add_child(obj2)
obj2.add_child(obj3)
obj4.add_child(obj5)
obj5.add_child(obj4)

print("\n순환 참조 형성 후 MEM_TRACKER 상태")
for obj_id, info in MemoryObject.MEM_TRACKER.items():
    print(f"id: {obj_id}, name: {info['name']}, count: {info['count']}")

obj1.release_ref()
obj2.release_ref()

print("\n외부 참조 제거 후 MEM_TRACKER 상태")
for obj_id, info in MemoryObject.MEM_TRACKER.items():
    print(f"id: {obj_id}, name: {info['name']}, count: {info['count']}")

print()

collected = MemoryObject.force_collect(root_ids=[id(obj1)])
print(f"collected {collected}")

print("\n최종 후 MEM_TRACKER 상태")
for obj_id, info in MemoryObject.MEM_TRACKER.items():
    print(f"id: {obj_id}, name: {info['name']}, count: {info['count']}")
