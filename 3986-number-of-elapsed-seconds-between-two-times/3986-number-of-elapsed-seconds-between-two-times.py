class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        l1 = list(map(int , startTime.split(":")))
        l2 = list(map(int , endTime.split(":")))
        time = 3600 * (l2[0] - l1[0]) + 60 * (l2[1] - l1[1]) + (l2[2] - l1[2])
        return time

        

        