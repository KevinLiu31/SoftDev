def string_times(str, n):
    #return str n times
  return str *n
# string_times('Hi', 2) → 'HiHi'	'HiHi'	OK
# string_times('Hi', 3) → 'HiHiHi'	'HiHiHi'	OK
# string_times('Hi', 1) → 'Hi'	'Hi'	OK
# string_times('Hi', 0) → ''	''	OK
def front_times(str, n):
  ans = ""
  #check if str length is less than 3
  #if true, set the part we are returning to it
  if len(str) < 3:
    ans = str;
  else:
      #if not set the part we are returning to the first three letter
    ans = str[:3]
  return ans *n
# front_times('Chocolate', 2) → 'ChoCho'	'ChoCho'	OK
# front_times('Chocolate', 3) → 'ChoChoCho'	'ChoChoCho'	OK
# front_times('Abc', 3) → 'AbcAbcAbc'	'AbcAbcAbc'	OK
# front_times('Ab', 4) → 'AbAbAbAb'	'AbAbAbAb'	OK
def string_bits(str):
  x = 0
  ans = ""
  while (x<len(str)):
    ans += str[x]
    #loop through every other
    x+=2
  return ans
# string_bits('Hello') → 'Hlo'	'Hlo'	OK
# string_bits('Hi') → 'H'	'H'	OK
# string_bits('Heeololeo') → 'Hello'	'Hello'	OK
# string_bits('HiHiHi') → 'HHH'	'HHH'	OK
def string_splosion(str):
  ans = ""
  #loop trough the first letter to the last letter
  for x in range(len(str) + 1):
    #adds everything up to the letter at x to ans
    ans += str[0:x]
  return ans
# string_splosion('Code') → 'CCoCodCode'	'CCoCodCode'	OK
# string_splosion('abc') → 'aababc'	'aababc'	OK
# string_splosion('ab') → 'aab'	'aab'	OK
# string_splosion('x') → 'x'	'x'	OK
def last2(str):
    #holds the last 2 letters
  holding = str[-2:]
  ans = 0
  #check all the letters up to the length -2 to see if they are equal to holding
  for x in range(len(str) - 2):
    if str[x:x+2] == holding:
      ans += 1
  return ans
# last2('hixxhi') → 1	1	OK
# last2('xaxxaxaxx') → 1	1	OK
# last2('axxxaaxx') → 2	2	OK
# last2('xxaxxaxxaxx') → 3	3	OK
def array_count9(nums):
  ans = 0
  #look through all elements in nums, if the element = nums, add one to counter
  for x in nums:
    if x == 9:
      ans +=1
  return ans
# array_count9([1, 2, 9]) → 1	1	OK
# array_count9([1, 9, 9]) → 2	2	OK
# array_count9([1, 9, 9, 3, 9]) → 3	3	OK
# array_count9([1, 2, 3]) → 0	0	OK
def array_front9(nums):
    #set the max of what we check to 4
  max = 4;
  #see if the length of the array is less than 4
  #if not set the upper limit to the length
  if len(nums) < 4:
    max = len(nums)
 #take the part of the array we care about
  num = nums[0:max]
  #loo[ through the part and see if it equals 9]
  for x in num:
    if x == 9:
      return True
  return False
# array_front9([1, 2, 9, 3, 4]) → True	True	OK
# array_front9([1, 2, 3, 4, 9]) → False	False	OK
# array_front9([1, 2, 3, 4, 5]) → False	False	OK
# array_front9([9, 2, 3]) → True	True	OK
def array123(nums):
    #loop through array, checking all pairs of 3.
    #stops two before end to stop out of bound.
  for x in range(len(nums) - 2):
    if nums[x:x+3] == [1,2,3]:
      return True
  return False
#  array123([1, 1, 2, 3, 1]) → True	True	OK
# array123([1, 1, 2, 4, 1]) → False	False	OK
# array123([1, 1, 2, 1, 2, 3]) → True	True	OK
# array123([1, 1, 2, 1, 2, 1]) → False	False	OK
def string_match(a, b):
  ans = 0
  if(len(a) < len(b)):
    mini = len(a)
  else:
    mini = len(b)
    #mini takes the length of the smaller string as we only need to check that
  for x in range(mini - 1):
    if a[x: x+2] == b[x: x+2]:
        #see two letters are the same in the same position
      ans += 1
  return ans

# string_match('xxcaazz', 'xxbaaz') → 3	3	OK
# string_match('abc', 'abc') → 2	2	OK
# string_match('abc', 'axc') → 0	0	OK
# string_match('hello', 'he') → 1	1	OK
