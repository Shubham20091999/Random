def binary_search(lst: list, v):
    l = 0
    r = len(lst)-1
    while l <= r:
        m = (l+r)//2
        if(lst[m] == v):
            return m
        if(v > lst[m]):
            l = m+1
        else:
            r = m-1
    return -1


# point of inflection
# time Complexity
# Avg O(log(m))
# worst O(m)
# Space Complexity O(1)
def bin_inf(lst: list):
    l = 0
    r = len(lst)-1
    while l < r:
        m = (l+r)//2
        if(lst[m] > lst[m+1]):
            return m+1
        if(lst[l] == lst[r]):
            l += 1
        elif(lst[l] > lst[m]):
            r = m
        elif(lst[r] < lst[m]):
            l = m
        else:
            return 0
    return 0


def bin_rot(lst: list, v):
    m = bin_inf(lst)
    if(lst[-1] >= v):
        l = m
        r = len(lst)-1
    else:
        r = m-1
        l = 0

    while(l <= r):
        m = (l+r)//2
        if(lst[m] == v):
            return m
        if(lst[m] > v):
            r = m-1
        else:
            l = r-1
    return -1

# class Solution:
#     def search(self, nums: list[int], target: int) -> bool:
#         start = 0
#         end = len(nums)-1
#         while start <= end:
#             while start < end and nums[start] == nums[end]:
#                 start += 1

#             mid = (start+end)//2

#             if nums[mid] == target:
#                 return True

#             if nums[start] <= nums[mid]:
#                 if nums[start] <= target <= nums[mid]:
#                     end = mid-1
#                 else:
#                     start = mid+1
#             else:
#                 if nums[mid] <= target <= nums[end]:
#                     start = mid+1
#                 else:
#                     end = mid-1
#         return False


def leftMostOccurance(lst, v, r=None):
    l = 0

    # if len(lst)-1 than end will happen
    # even if we dont have the item in the lst
    if(r==None):
        r = len(lst)

    while l < r:
        m = (l+r)//2
        if(lst[m] < v):
            l = m+1
        else:
            r = m
    if(l < len(lst) and lst[l]==v):
        return l
    else:
        return -1


def rightMostOccurence(lst, v, l=0):
    r = len(lst)

    while l < r:
        m = (l+r)//2
        if(lst[m] > v):
            r = m
        else:
            l = m+1
    if(lst[r-1] == v):
        return r-1
    else:
        return -1




print(leftMostOccurance([5,7,7,8,8,10], 6))
