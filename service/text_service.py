from pytesseract import image_to_data, pytesseract

pytesseract.tesseract_cmd = r'../TesseractOCR/tesseract.exe'


def extract_text(image):
    return image_to_data(image, output_type='dict')


if __name__ == '__main__':
    data = image_to_data('D:/Pictures/Screenshots/屏幕截图 2024-05-04 002108.png', output_type='dict')
    parsed_data = []
    num_boxes = len(data['text'])
    for i in range(num_boxes):
        if int(data['conf'][i]) > 60:
            d = {'text': data['text'][i],
                 'x': data['left'][i],
                 'y': data['top'][i],
                 'w': data['width'][i],
                 'h': data['height'][i]}
            parsed_data.append(d)
    for parsed_datum in parsed_data:
        print(parsed_datum)
