#defining vars and collecting input
key,loop,output=[],0,[]
text = input("plain text:  ")
shift = int(input("shift integer:  ")) #beween 0 - 126
keyinput = input("key here:  ")

#insert key using for loop
if keyinput == "":
    key=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
length_key = len(key)
for keyletter in keyinput:
    key.append(keyletter)
print(key)

#key generation
while loop < 100:
    key.append(key[loop])
    loop = loop + 1

#analyzing the text
for currentinput in text:
    for currentkey in key:
        if currentkey == currentinput:
            output.append(str(key.index(currentinput)+shift))
            output.append(" ")
            break

#displaying output
print(''.join(output))