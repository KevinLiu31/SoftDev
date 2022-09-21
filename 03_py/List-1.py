def first_last6(nums):
    #check if last or first letter = 6
  return (nums[0] == 6) or (nums[-1] == 6)
# first_last6([1, 2, 6]) → True	True	OK
# first_last6([6, 1, 2, 3]) → True	True	OK
# first_last6([13, 6, 1, 2, 3]) → False	False	OK
# first_last6([13, 6, 1, 2, 6]) → True	True	OK
def same_first_last(nums):
  return (len(nums) >=1) and (nums[0] == nums[-1])
# same_first_last([1, 2, 3]) → False	False	OK
# same_first_last([1, 2, 3, 1]) → True	True	OK
# same_first_last([1, 2, 1]) → True	True	OK
# same_first_last([7]) → True	True	OK
def make_pi():
  return [3,1,4]
# make_pi() → [3, 1, 4]	[3, 1, 4]	OK
def common_end(a, b):
  return(a[0] == b[0]) or (a[-1] == b[-1])
# common_end([1, 2, 3], [7, 3]) → True	True	OK
# common_end([1, 2, 3], [7, 3, 2]) → False	False	OK
# common_end([1, 2, 3], [1, 3]) → True	True	OK
# common_end([1, 2, 3], [1]) → True	True	OK
def sum3(nums):
    #sum adds everything in an array
  return sum(nums)
# sum3([1, 2, 3]) → 6	6	OK
# sum3([5, 11, 2]) → 18	18	OK
# sum3([7, 0, 0]) → 7	7	OK
# sum3([1, 2, 1]) → 4	4	OK
def rotate_left3(nums):
  ans = [nums[1], nums[2], nums[0]]
  return ans
# rotate_left3([1, 2, 3]) → [2, 3, 1]	[2, 3, 1]	OK
# rotate_left3([5, 11, 9]) → [11, 9, 5]	[11, 9, 5]	OK
# rotate_left3([7, 0, 0]) → [0, 0, 7]	[0, 0, 7]	OK
# rotate_left3([1, 2, 1]) → [2, 1, 1]	[2, 1, 1]	OK
def reverse3(nums):
    #negative goes backwards
  return [nums[-1], nums[-2], nums[0]]
# reverse3([1, 2, 3]) → [3, 2, 1]	[3, 2, 1]	OK
# reverse3([5, 11, 9]) → [9, 11, 5]	[9, 11, 5]	OK
# reverse3([7, 0, 0]) → [0, 0, 7]	[0, 0, 7]	OK
# reverse3([2, 1, 2]) → [2, 1, 2]	[2, 1, 2]	OK
def max_end3(nums):
  if(nums[0] < nums[2]):
    ans = nums[2]
  else:
    ans = nums[0]
    #ans is the larger of the ends
  return [ans, ans, ans]
# max_end3([1, 2, 3]) → [3, 3, 3]	[3, 3, 3]	OK
# max_end3([11, 5, 9]) → [11, 11, 11]	[11, 11, 11]	OK
# max_end3([2, 11, 3]) → [3, 3, 3]	[3, 3, 3]	OK
# max_end3([11, 3, 3]) → [11, 11, 11]	[11, 11, 11]	OK
def sum2(nums):
  if len(nums) < 2:
    return sum(nums)
  else:
    return nums[0] + nums[1]
# sum2([1, 2, 3]) → 3	3	OK
# sum2([1, 1]) → 2	2	OK
# sum2([1, 1, 1, 1]) → 2	2	OK
# sum2([1, 2]) → 3	3	OK
def middle_way(a, b):
  return [a[1], b[1]]
# middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]	[2, 5]	OK
# middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]	[7, 8]	OK
# middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]	[2, 4]	OK
# middle_way([1, 9, 7], [4, 8, 8]) → [9, 8]	[9, 8]	OK
def make_ends(nums):
  return [nums[0],nums[-1]]
# make_ends([1, 2, 3]) → [1, 3]	[1, 3]	OK
# make_ends([1, 2, 3, 4]) → [1, 4]	[1, 4]	OK
# make_ends([7, 4, 6, 2]) → [7, 2]	[7, 2]	OK
# make_ends([1, 2, 2, 2, 2, 2, 2, 3]) → [1, 3]	[1, 3]	OK
def has23(nums):
  return ((nums[0] == 2) or (nums[0] == 3)) or ((nums[1] == 2) or (nums[1] == 3))
# has23([2, 5]) → True	True	OK
# has23([4, 3]) → True	True	OK
# has23([4, 5]) → False	False	OK
# has23([2, 2]) → True	True	OK
