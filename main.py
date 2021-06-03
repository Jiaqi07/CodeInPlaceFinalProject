import cv2
from simpleimage import SimpleImage
from matplotlib import pyplot as plt

DEFAULT_FILE = 'images/ocean.jpg'


def show(filename):
    image = SimpleImage(filename)
    image.show()


def grayscale(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height
    grayimg = SimpleImage.blank(width, height)

    for pixel in image:
        intensity = .2989 * pixel.red + .587 * pixel.green + .114 * pixel.blue
        pixel.red = intensity
        pixel.blue = intensity
        pixel.green = intensity
        grayimg.set_pixel(pixel.x, pixel.y, pixel)
    grayimg.show()


def hist(filename):
    img = cv2.imread(filename, 0)
    histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(histr)
    plt.xlabel("Intensity")
    plt.ylabel("Pixel Count")
    plt.title("Intesity to Pixel Count Diagram")

    plt.show()


def flip(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    direction = input('Horizontal or Vertical? (H or V): ')

    if direction.lower() == 'v':
        flippedimg = SimpleImage.blank(width, height)
        for y in range(height):
            for x in range(width):
                pixel = image.get_pixel(x, y)
                flippedimg.set_pixel(width - (x + 1), y, pixel)
        flippedimg.show()
    elif direction.lower() == 'h':
        flippedimg = SimpleImage.blank(width, height)
        for y in range(height):
            for x in range(width):
                pixel = image.get_pixel(x, y)
                flippedimg.set_pixel(x, height - (y + 1), pixel)
        flippedimg.show()
    else:
        print("Ain't an answer bud")


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    print("")
    print("")
    return filename


if __name__ == '__main__':
    filename = get_file()
    go = True
    while (go):
        ans = input('What would you like to do? (or press enter to exit): ')
        if ans == "":
            go = False
        elif ans.lower() == 'show':
            show(filename)
        elif ans.lower() == 'flip':
            flip(filename)
        elif ans.lower() == 'hist':
            hist(filename)
        elif ans.lower() == 'grayscale':
            grayscale(filename)
        elif ans.lower() == 'help':
            print("Grayscale, Show, Flip, Hist, Help")
        else:
            print("That isn't a command, help for a list of commands.")
        print()
        print()
