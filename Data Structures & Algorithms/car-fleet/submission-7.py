class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stack = []
        pos_speed_map = {pos: speed[idx] for idx, pos in enumerate(position)}

        position.sort()

        for pos in reversed(position):
            req_time = (target - pos) / pos_speed_map[pos]

            if len(car_stack) == 0:
                car_stack.append((pos, req_time))
            else:
                front_car_req_time = car_stack[-1][1]
                if req_time > front_car_req_time:
                    car_stack.append((pos, req_time))

        return len(car_stack)