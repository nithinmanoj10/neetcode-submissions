class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(word1: str, word2: str) -> bool:

            if len(word1) != len(word2):
                return False

            char_count = dict()

            for char in word1:
                if char not in char_count:
                    char_count[char] = 1
                else:
                    char_count[char] += 1

            for char in word2:
                if char not in char_count:
                    return False
                else:
                    char_count[char] -= 1

            for char, count in char_count.items():
                if count != 0:
                    return False

            return True
                    
                

        result = []

        for word in strs:
            found_group = False
            for idx, group in enumerate(result):
                reference = group[0]

                if isAnagram(reference, word):
                    result[idx].append(word)
                    found_group = True
                    break

            if not found_group:
                result.append([word])

        return result