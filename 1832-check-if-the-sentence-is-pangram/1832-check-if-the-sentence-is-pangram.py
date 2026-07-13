class Solution(object):
    def checkIfPangram(self, sentence):
        hash_table = [0]*26
        for ch in sentence:
            index = ord(ch)-97
            hash_table[index] += 1
        for i in hash_table:
            if i == 0:
                return False
            else:
                pass
        return True
        
        