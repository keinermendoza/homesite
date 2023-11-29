from PIL import Image
from os import listdir

size = (750, 410)
folder = listdir()

for file in folder:
	if '.py' in file:
		continue
	
	name,_ = str(file).split('.')
	
	with Image.open(file) as img:
		img.thumbnail(size)
		new_name = img.save(f'{name}.webp')

		print(name, 'is ready')
