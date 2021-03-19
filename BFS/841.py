class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = rooms[0]
        visited_rooms = [False] * len(rooms)
        visited_rooms[0] = True
        for key in rooms[0]:
            visited_rooms[key] = True
        
        def bfs(rooms, queue, visited_rooms):
            if len(queue) == 0:
                return visited_rooms
            new_keys = rooms[queue.pop(0)]
            for key in new_keys:
                if not visited_rooms[key]:
                    visited_rooms[key] = True
                    queue.append(key)
            return bfs(rooms, queue, visited_rooms)
        visited_rooms = bfs(rooms, queue, visited_rooms)
        
        for room in visited_rooms:
            if room == False:
                return False
        return True