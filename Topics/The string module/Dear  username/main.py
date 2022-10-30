import string

# put your code here
username = input()
message = string.Template("Dear $username! It was really nice to meet you. Hopefully, you have a nice day! See you "
                          "soon, $username!")
message = message.substitute(username=username)
print(message)
