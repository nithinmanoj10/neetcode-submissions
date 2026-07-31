class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_string = ""

        for char in s:
            if char.isalnum():
                valid_string += char

        valid_string = valid_string.lower()

        i = 0 
        j = len(valid_string) - 1

        while i < j:

            if valid_string[i] != valid_string[j]:
                return False

            i += 1
            j -= 1

        return True