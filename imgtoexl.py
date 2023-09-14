from pandas import DataFrame
from PIL import Image

# grad = ['▓','▒','░','']
while not 'img' in locals():
    try: img = Image.open(input('Enter file here:'))
    except: print("File doesn't exist")

ys = 400

# grada = 1

k = ys/img.size[0]

data = {}

img = img.resize((int(img.size[0]//3*k), ys), Image.LANCZOS)

for x in range(img.size[0]):

    mass = []
    
    for y in range(ys):
        p = img.getpixel((x,y))
        # if grada:
        mass.append((6-(p[0]+p[1]+p[2])//120)*'O')
        # else:
        #     g = (p[0]+p[1]+p[2])//(255*4//len(grad))
        #     # print(g)
        #     mass.append(grad[g]*3)

    data.update({x:mass})

print('Image loaded. Creating table..')
try:
    DataFrame(data).to_excel('./image.xlsx') 
    print('Success!')    
except:
    print('Error')
input()
