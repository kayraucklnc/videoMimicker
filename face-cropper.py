from PIL import Image
from autocrop import Cropper
import os

# Get a Numpy array of the cropped image
cropper = Cropper(500, 500, 70, 200, False)

directory = 'faces/'
if not os.path.exists(directory):
    os.makedirs(directory)

#THESE NUMBERS SHOULD BE ADJUSTED 
for i in range(START, END):
    cropped_array = cropper.crop(f"{i}.png")

    # Save the cropped image with PIL
    cropped_image = Image.fromarray(cropped_array)

    cropped_image.save(f"faces/{i}.png")
    print(f"{i} done!")


############################################################################################
