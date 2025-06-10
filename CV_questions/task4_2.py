from PIL import Image
from PIL.ExifTags import TAGS
import re

# Open the image
img = Image.open("Cat Clue 2.jpg")

# Get EXIF data
exif_data = img._getexif()

# Extract the actual code
if exif_data:
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        
        # Look for 4-digit codes
        codes = re.findall(r'\d{4}', str(value))
        
        if codes:
            for code in codes:
                print(code)  