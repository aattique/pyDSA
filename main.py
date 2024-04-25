from stack import Stack

def convert_int_to_bin(dec_num):
  s = Stack()
  num2 = dec_num
  rem2 = 1
  bin_num = ""
  while rem2 > 0 :
    rem2 = num2 // 2
    rem = num2 % 2
    s.push(rem)
    num2 = rem2
  while not s.is_empty():
    bin_num += str(s.pop())
  return bin_num

print(convert_int_to_bin(10))
print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))

print(int(convert_int_to_bin(56),2)==56)
    

