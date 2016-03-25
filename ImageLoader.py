from NoiseImage import NoiseImage
from PIL import Image, ImageDraw

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

    def saveToImage(self, outputPath, noiseImage, size, lines):
        for index in xrange(noiseImage.imagesCount):
            self.saveSingleImage(
                outputPath,
                str(index+1),
                noiseImage.getWidth(),
                noiseImage.getHeight(),
                noiseImage.getSplitedImages()[index],
                size, lines)
            
        self.saveSingleImage(
                outputPath,
                'original',
                noiseImage.getWidth(),
                noiseImage.getHeight(),
                noiseImage.getOriginalData(),
                size, lines)
    
    def saveSingleImage(self, outputPath, name, width, height, data, size, lines):
        
        linesWidth = 1
        linesColor = (127, 127, 127)
        im = Image.new("RGB", (width, height), 'black')

        for y in xrange(height):
            for x in xrange(width):
                if data[y * width + x]:
                    im.putpixel((x, y), (255, 255, 255))
                else:
                    im.putpixel((x, y), (0, 0, 0))

        if lines:
            im = im.resize(((width * size)+linesWidth, (height * size)+linesWidth), Image.NEAREST)
            draw = ImageDraw.Draw(im)
            for x in xrange(width):
                draw.line((size * x, 0, size * x, height * size), fill=linesColor)
            for y in xrange(height):
                draw.line((0, size * y, width * size, size * y), fill=linesColor)
            draw.line((width * size, 0, width * size, width * size), fill=linesColor)
            draw.line((0, width * size, width * size, width * size), fill=linesColor)
        else:
            im = im.resize((width * size, height * size), Image.NEAREST)

        im.save(outputPath + name + ".png")