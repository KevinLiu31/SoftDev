def count_evens(nums):
    #count of the even #
  count = 0
  for x in nums:
    if(x%2 == 0):
        #a number who has remainder 0 after being divided by 2 is even
      count += 1
  return count
# count_evens([2, 1, 2, 3, 4]) → 3	3	OK
# count_evens([2, 2, 0]) → 3	3	OK
# count_evens([1, 3, 5]) → 0	0	OK
# count_evens([]) → 0	0	OK
def big_diff(nums):
    #mini is the smallest number, maxi is the largest number
  mini = nums[0]
  maxi = nums[0]
  for x in range(len(nums)):
      #loops through array and set mini to the minimum of itself and the number at positon x
    mini = min(mini, nums[x]);
    #set maxi to the max of itself and element x
    maxi = max(maxi, nums[x]);
  return maxi - mini
# big_diff([10, 3, 5, 6]) → 7	7	OK
# big_diff([7, 2, 10, 9]) → 8	8	OK
# big_diff([2, 10, 7, 2]) → 8	8	OK
# big_diff([2, 10]) → 8	8	OK
def centered_average(nums):
    #added all values and subtracted the max and the min
  ans = sum(nums)
  ans = ans - min(nums)
  ans = ans - max(nums)
  #divided by the amount of value that were added, since we took about
  #two values(max and min) it will be -2
  return ans/(len(nums) - 2)
# centered_average([1, 2, 3, 4, 100]) → 3	3	OK
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5	5	OK
# centered_average([-10, -4, -2, -4, -2, 0]) → -3	-3	OK
# centered_average([5, 3, 4, 6, 2]) → 4	4	OK
def sum13(nums):
  x = 0
  sum = 0
  while x<len(nums):
    if (nums[x] == 13):
        #skips two values so 13 and the value after
      x = x+2
    else:
        #if not 13 add to sum and then go to next
      sum += nums[x]
      x+=1
  return sum
# sum13([1, 2, 2, 1]) → 6	6	OK
# sum13([1, 1]) → 2	2	OK
# sum13([1, 2, 2, 1, 13]) → 6	6	OK
# sum13([1, 2, 13, 2, 1, 13]) → 4	4	OK
def sum67(nums):
  x = 0
  ans = 0
  #loop through entire array
  while x < len(nums):
      #see if there is a 6
    if(nums[x] == 6):
        #if there is continue loop to find a value that is 7, set every value that isnt a 7 to a zero
      while(nums[x] != 7):
        nums[x] = 0
        x+=1
      nums[x] = 0
    x+=1
    #add all the value: the value between 6 and 7 would be set to 0
  return sum(nums)
# sum67([1, 2, 2]) → 5	5	OK
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5	5	OK
# sum67([1, 1, 6, 7, 2]) → 4	4	OK
# sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) → 2	2	OK
def has22(nums):
    #loop through all the nums
  for x in range(len(nums) - 1):
      #if the value at x is 2 and the value next to x is 2 return true
    if (nums[x] == 2) and (nums[x+1] == 2):
      return True
  return False
# has22([1, 2, 2]) → True	True	OK
# has22([1, 2, 1, 2]) → False	False	OK
# has22([2, 1, 2]) → False	False	OK
# has22([2, 2, 1, 2]) → True	True	OK
