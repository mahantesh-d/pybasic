f = open('lsr.txt', 'r')
text = f.readlines()
x = ''.join(text)
print(x)
b=x.split("|")
print('SELECT')
for z in b:
    if '[' in z:
        print("array"+str(z).replace('[','(').replace(']',')'+',').strip())
    else:
        print("'" + z + "',\r\n".strip())
print("CURRENT_TIMESTAMP;")
