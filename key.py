import random 
key=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
output=[]
while key != []:
    choice = random.choice(key)
    output.append(choice)
    key.remove(choice)
print(''.join(output))