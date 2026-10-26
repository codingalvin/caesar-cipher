#defining vars and collecting input
key,loop,secondloop,output,keyinput=[],0,0,[],""
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
for currenti in text:
    secondloop = 0
    while secondloop<length_key:
        if key[secondloop] == currenti:
            a= key.index(currenti)
            output.append(str(a+shift))
            output.append(" ")
            a=0
        secondloop = secondloop +1

#displaying output
print(''.join(output))