from NoiseImage import NoiseImage
from PIL import Image

class ImageLoader():

    def loadFromImage(self, inputFile, imagesCount):
        im = Image.open(inputFile)

        width = im.size[0]
        height = im.size[1]

        data = []

        for y in xrange(height):
            for x in xrange(width):
                if im.getpixel((x, y))[0]:
                    data.append(1)
                else:
                    data.append(0)

        return NoiseImage(width, height, data, imagesCount)

    def saveToImage(self, outputPath, noiseImage, size):
        for index in xrange(noiseImage.imagesCount):
            self.saveSingleImage(
                outputPath,
                str(index+1),
                noiseImage.getWidth(),
                noiseImage.getHeight(),
                noiseImage.getSplitedImages()[index],
                size)
            
        self.saveSingleImage(
                outputPath,
                'original',
                noiseImage.getWidth(),
                noiseImage.getHeight(),
                noiseImage.getOriginalData(),
                size)
    
    def saveSingleImage(self, outputPath, name, width, height, data, size):
        im = Image.new("RGB", (width, height), 'black')

        for y in xrange(height):
            for x in xrange(width):
                if data[y * width + x]:
                    im.putpixel((x, y), (255, 255, 255))
                else:
                    im.putpixel((x, y), (0, 0, 0))

        im = im.resize((width * size, height * size), Image.NEAREST)

        im.save(outputPath + "/" + name + ".png")