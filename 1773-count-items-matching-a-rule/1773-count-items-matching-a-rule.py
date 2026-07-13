class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        target = {"type":0,"color":1,"name":2}
        index = target[ruleKey]
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
        return count


        
        