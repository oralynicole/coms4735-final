import pytesseract
import re
from PIL import Image


def process():
    flip()
    # Load the image
    image = Image.open('book.png')

    # Perform OCR on the image
    text = pytesseract.image_to_string(image)

    # Extract the book title and author name from the OCR output
    title = ''
    author = ''
    for line in text.splitlines():
        line = line.strip()
        if not title and re.search(r'([A-Za-z]+[ -])*[A-Za-z]+', line):
            title = line
        elif not author and re.search(r'[Bb][Yy] ([A-Za-z]+[ -])*[A-Za-z]+', line):
            author = line.split('by', 1)[1].strip()

    # Print the book title and author name
    print('Book Title:', title)
    print('Author Name:', author)


def flip(): 
    # Open the image using PIL
    img = Image.open('book.png')

    # Rotate the image by 180 degrees
    img = img.rotate(180)

    # Flip the image horizontally
    img = img.transpose(method=Image.FLIP_LEFT_RIGHT)

    # Save the flipped and rotated image
    img.save('book.png')