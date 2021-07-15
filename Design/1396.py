class UndergroundSystem:

    def __init__(self):
        self.id_table = {}
        self.time_table = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_table[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.id_table[id][0]
        time_passed = t - self.id_table[id][1]
        if start_station not in self.time_table:
            self.time_table[start_station] = {}
        if stationName not in self.time_table[start_station]:
            self.time_table[start_station][stationName] = (0, 0)
        total_time, count = self.time_table[start_station][stationName]
        self.time_table[start_station][stationName] = (total_time + time_passed, count + 1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.time_table[startStation][endStation]
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)