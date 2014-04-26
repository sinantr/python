import base64

MESSAGE = "life of brian"


base64.encode(open("a.xlsx"), open("out.b64", "w"))
base64.decode(open("out.b64"), open("out.txt", "w"))

print "original:", repr(MESSAGE)
print "encoded message:", open("out.b64").read()
print "decoded message:", repr(open("out.txt").read())