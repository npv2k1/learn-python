import os
import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import curses

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "


def scale_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    return image.convert("L")


def map_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value * len(ASCII_CHARS) // 256]
    return ascii_str


def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image, new_width)
    image = convert_to_grayscale(image)
    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    return ascii_img


def print_ascii_with_color(image, ascii_img, new_width=100):
    image = scale_image(image, new_width)
    pixels = image.convert("RGB").getdata()
    colored_ascii_img = ""

    pixel_index = 0
    for char in ascii_img:
        if char in ASCII_CHARS:
            r, g, b = pixels[pixel_index]
            # Setting background color and resetting foreground color
            colored_ascii_img += f"\033[48;2;{r};{g};{b}m\033[38;2;255;255;255m \033[0m"
            pixel_index += 1
        else:
            colored_ascii_img += char

    # print(colored_ascii_img)
    return colored_ascii_img


def main(image_path, new_width=100):
    image = Image.open(image_path)
    ascii_img = convert_image_to_ascii(image, new_width)
    s = print_ascii_with_color(image, ascii_img, new_width)
    animate_draw(s)
    # print(s)


def clear(): return os.system('cls')

# Example usage:
# main("path_to_image.jpg", 100)


def plot_sin(t, new_width=100):
    # Generate x values
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    # Compute sin(x) values
    y = np.sin(t)

    # Create the plot with a green line
    plt.plot(x, y, 'g')

    # Remove the x and y axis
    plt.axis('off')

    # Set the background color to none
    plt.gca().set_facecolor('none')

    # Save the plot as an image with a transparent background
    image_path = "sinx_plot.png"
    plt.savefig(image_path, bbox_inches='tight',
                pad_inches=0, transparent=True)

    # Open the image
    image = Image.open(image_path)

    # Convert the image to ASCII and print it
    ascii_img = convert_image_to_ascii(image, new_width)
    print_ascii_with_color(image, ascii_img, new_width)

    # Remove the image file
    os.remove(image_path)


def animate_draw(string: str):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.move(100, 100)
    print(string)
    # source = list(string.split('\n'))
    # k = 0
    # while k < len(source[1]):
    #     for i in source:
    #         if (len(i) == 0):
    #             break
    #         print(i[:k+1] + '\x1b[0m')
    #     # time.sleep(0.05)
    #     k += 1
    #     if (k != len(source[1])):
    #         # clear()
          


if __name__ == "__main__":
    clear()
    main("image.jpg", 50)
    # plot_sin(1, 100)
    # while True:
    #     for i in range(100):
    #         plot_sin(i, 100)
    #         clear()
