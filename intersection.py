class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        inter = []
        i = j = 0
        while i < len(nums1) and j < len(nums2) :
            if nums1[i] == nums2[j] :
                if len(inter) > 0 and inter[len(inter)-1] == nums1[i] :
                    i += 1
                    j+= 1
                    continue
                inter.append(nums1[i])
                i += 1
                j+= 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j+=1
        return inter
        
        