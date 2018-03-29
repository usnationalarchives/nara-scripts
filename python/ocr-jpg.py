try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract, os

for item in os.listdir(os.getcwd()):
	if item.endswith(".jpg"):
		img = Image.open(item)
		img.load()
		i = pytesseract.image_to_string(img)
		print i.encode('utf8')