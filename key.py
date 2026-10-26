import random 
key=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," "]
output=[]
while key != []:
    choice = random.choice(key)
    output.append(choice)
    key.remove(choice)
print(''.join(output))