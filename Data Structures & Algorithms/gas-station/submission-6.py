class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        total_stations = len(gas)

        if total_cost > total_gas:
            return -1

        curr_station = 0
        start_station = 0
        gas_tank = 0

        while curr_station < total_stations:
            gas_tank += (gas[curr_station] - cost[curr_station])

            if gas_tank < 0:
                start_station = curr_station + 1
                gas_tank = 0
            
            curr_station += 1

        return start_station