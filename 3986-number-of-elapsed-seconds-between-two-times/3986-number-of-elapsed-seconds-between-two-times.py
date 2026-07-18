class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        l1 = startTime.split(":")
        l2 = endTime.split(":")
        time = 3600 * (int(l2[0]) - int(l1[0])) + 60 * (int(l2[1]) - int(l1[1])) + (int(l2[2]) - int(l1[2]))
        return time

        

        