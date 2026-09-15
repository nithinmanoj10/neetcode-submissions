class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def is_unwanted_triplet(triplet: List[int]) -> bool:
            return (triplet[0] > target[0]) or (triplet[1] > target[1]) or (triplet[2] > target[2])

        has_x = False
        has_y = False
        has_z = False

        for triplet in triplets:
            if is_unwanted_triplet(triplet):
                continue
            
            if triplet[0] == target[0]:
                has_x = True
            if triplet[1] == target[1]:
                has_y = True
            if triplet[2] == target[2]:
                has_z = True

        return has_x and has_y and has_z