translated=''
message=input("Enter plain text or cipher text")
i=len(message)-1
while i>=0:
    translated = translated + message[i]
    i = i - 1

print("The traslated text is \t " + translated)
