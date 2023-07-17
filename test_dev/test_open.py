import base64

PATH_TO_IMAGE = r'C:\Users\btema\PycharmProjects\TestAppTrix\test_set\media\pupsen.jpg'

# def binary_file():
with open(PATH_TO_IMAGE, 'rb') as image_file:
    encoded_image = image_file.read()
    print(encoded_image)
    # return encoded_image
