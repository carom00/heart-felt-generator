import image_generator
from image_transformer import transformImage
from poet import getResponse

text = 'I was such an asshole to her, I\'ll never forgive myself'
fileName = 'testimg'

image_generator.execute(text, fileName)
transformImage(fileName)
poem = getResponse(text)
print('done')
