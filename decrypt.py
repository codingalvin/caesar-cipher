#defining vars and collecting input
key,loop,secondloop,output,keyinput=[],0,0,[],""
text = input("ciphertext:  ")
shift = int(input("shift integer:  ")) #between 0 - 126
keyinput = input("key:  ")
input = text.split()

#insert key using for loop
if keyinput == "":
    key=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
for keyletter in keyinput:
    key.append(keyletter)
print(key)

#key generation
loop = 0
while loop < 100:
    key.append(key[loop])
    loop = loop + 1

#analyzing the text
for currentinput in input:
    secondloop = 0
    for _ in key:
        if str(secondloop) == currentinput:
            a=int(currentinput)
            output.append(key[a-shift])
            a=0
        secondloop = secondloop + 1

#displaying output
print(''.join(output))