import pytesseract
import cv2

'''SAMPLE'''
print('------------------------------------------------------------------------------')
image = cv2.imread('data/sample/input.jpg')  # Load image.
text = pytesseract.image_to_string(image)  # Use Tesseract to OCR the image.
print(text)  # Print OCR results.
print('------------------------------------------------------------------------------')

'''RECEIPT #1'''
print('------------------------------------------------------------------------------')
image = cv2.imread('data/receipts/1.jpg')  # Load image.
text = pytesseract.image_to_string(image)  # Use Tesseract to OCR the image.
print(text)  # Print OCR results.
print('------------------------------------------------------------------------------')

'''RECEIPT #2'''
print('------------------------------------------------------------------------------')
image = cv2.imread('data/receipts/2.jpg')  # Load image.
text = pytesseract.image_to_string(image)  # Use Tesseract to OCR the image.
print(text)  # Print OCR results.
print('------------------------------------------------------------------------------')

'''RECEIPT #3'''
print('------------------------------------------------------------------------------')
image = cv2.imread('data/receipts/3.jpg')  # Load image.
text = pytesseract.image_to_string(image)  # Use Tesseract to OCR the image.
print(text)  # Print OCR results.
print('------------------------------------------------------------------------------')

'''RECEIPT #4'''
print('------------------------------------------------------------------------------')
image = cv2.imread('data/receipts/4.jpg')  # Load image.
text = pytesseract.image_to_string(image)  # Use Tesseract to OCR the image.
print(text)  # Print OCR results.
print('------------------------------------------------------------------------------')

'''RECEIPT #5'''
print('------------------------------------------------------------------------------')
image = cv2.imread('data/receipts/5.jpg')  # Load image.
text = pytesseract.image_to_string(image)  # Use Tesseract to OCR the image.
print(text)  # Print OCR results.
print('------------------------------------------------------------------------------')
