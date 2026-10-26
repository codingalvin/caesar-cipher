#defining vars and collecting input
text = input("plain text:  ")
shift = int(input("shift integer:  ")) #beween 0 - 126
keyinput = input("key here:  ")
key,loop,secondloop,output=[],0,0,[]

#insert key using for loop
for keyletter in keyinput:
    key.append(keyletter)
print(key)
length_key = 26#len(key)
key=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

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