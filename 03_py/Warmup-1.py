def sleep_in(weekday, vacation):
    #fullfill boolean
  return not weekday or vacation
# sleep_in(False, False) → True	True	OK
# sleep_in(True, False) → False	False	OK
# sleep_in(False, True) → True	True	OK
# sleep_in(True, True) → True	True	OK
def monkey_trouble(a_smile, b_smile):
    #check if a == b
  return a_smile == b_smile
# monkey_trouble(True, True) → True	True	OK
# monkey_trouble(False, False) → True	True	OK
# monkey_trouble(True, False) → False	False	OK
# monkey_trouble(False, True) → False	False	OK
def sum_double(a, b):
  ans = a+b
  if a==b:
      #check if a == b, if true, double the sum
    return ans *2;
  return ans
# sum_double(1, 2) → 3	3	OK
# sum_double(3, 2) → 5	5	OK
# sum_double(2, 2) → 8	8	OK
# sum_double(-1, 0) → -1	-1	OK
def diff21(n):
    #if n > 21 double the difference
  multiplier = 1
  if n>21:
    multiplier = 2
  return (abs(n - 21))*multiplier
# diff21(19) → 2	2	OK
# diff21(10) → 11	11	OK
# diff21(21) → 0	0	OK
# diff21(22) → 2	2	OK
def parrot_trouble(talking, hour):
  return(talking and(hour > 20 or hour < 7))
# parrot_trouble(True, 6) → True	True	OK
# parrot_trouble(True, 7) → False	False	OK
# parrot_trouble(False, 6) → False	False	OK
# parrot_trouble(True, 21) → True	True	OK
def makes10(a, b):
  return a == 10 or b == 10 or a+b == 10
# makes10(9, 10) → True	True	OK
# makes10(9, 9) → False	False	OK
# makes10(1, 9) → True	True	OK
# makes10(10, 1) → True	True	OK
def near_hundred(n):
  return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
# near_hundred(93) → True	True	OK
# near_hundred(90) → True	True	OK
# near_hundred(89) → False	False	OK
# near_hundred(110) → True	True	OK
def pos_neg(a, b, negative):
  if not negative:
      #^ means if one is true while the other is not
    return (a < 0) ^ (b < 0)
  else:
    return (a < 0) and (b < 0)
# pos_neg(1, -1, False) → True	True	OK
# pos_neg(-1, 1, False) → True	True	OK
# pos_neg(-4, -5, True) → True	True	OK
# pos_neg(-4, -5, False) → False	False	OK
def not_string(str):
  toadd = "not "
  #check if there is already a not
  if(str[:3] == "not"):
    toadd = ""
  return toadd + str
# not_string('candy') → 'not candy'	'not candy'	OK
# not_string('x') → 'not x'	'not x'	OK
# not_string('not bad') → 'not bad'	'not bad'	OK
# not_string('bad') → 'not bad'	'not bad'	OK
def missing_char(str, n):
  return str[:n] + str[n +1:]
# missing_char('kitten', 1) → 'ktten'	'ktten'	OK
# missing_char('kitten', 0) → 'itten'	'itten'	OK
# missing_char('kitten', 4) → 'kittn'	'kittn'	OK
# missing_char('Hi', 0) → 'i'	'i'     'i'     OK
def front_back(str):
  if len(str) > 1:
      #just flip first and last letter
    ans = str[-1] + str[1:len(str) - 1] + str[0]
    return ans
  else:
      #if length is 1 or less there is nothing to flip
    return str
# front_back('code') → 'eodc'	'eodc'	OK
# front_back('a') → 'a'	'a'	OK
# front_back('ab') → 'ba'	'ba'	OK
# front_back('abc') → 'cba'	'cba'	OK
def front3(str):
  if(len(str) < 3):
    ans = str;
    #again if str is less than len 3, then set what we return t0 str
  else:
    ans = str[:3]
  return ans *3
# front3('Java') → 'JavJavJav'	'JavJavJav'	OK
# front3('Chocolate') → 'ChoChoCho'	'ChoChoCho'	OK
# front3('abc') → 'abcabcabc'	'abcabcabc'	OK
# front3('abcXYZ') → 'abcabcabc'	'abcabcabc'	OK
