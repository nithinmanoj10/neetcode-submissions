class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        total_stations = len(gas)

        if total_cost > total_gas:
            return -1

        curr_station = 0
        start_station = 0
        gas_tank = 0

        while curr_station < total_stations:
            total_gas += gas[curr_station]
            total_cost += cost[curr_station]

            gas_tank += (gas[curr_station] - cost[curr_station])

            if gas_tank < 0:
                start_station = curr_station + 1
                gas_tank = 0
            
            curr_station += 1

        return -1 if total_cost > total_gas else start_station