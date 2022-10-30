import string

# put your code here
first_line = input()
second_line = input()
first_line = string.capwords(first_line, ",")
second_line = string.capwords(second_line)
print(first_line)
print(second_line)
