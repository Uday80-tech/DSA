class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        target = {"type":0,"color":1,"name":2}
        count = 0
        for item in items:
            if item[target[ruleKey]] == ruleValue:
                count += 1
        return count


        
        