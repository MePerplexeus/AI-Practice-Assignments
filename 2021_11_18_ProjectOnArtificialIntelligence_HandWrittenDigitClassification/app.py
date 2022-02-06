# Import Libraries
from crypt import methods
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from sklearn import datasets
import pickle
import random
import base64
from io import BytesIO
from PIL import Image, ImageFilter
import numpy as np
import json


# Initiate Flask
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


# Home Directory
@app.route('/')
def index():
    # The digits dataset
    digits = datasets.load_digits()
    n_samples = len(digits.images)
    data = digits.images.reshape(n_samples, 64)
    ind = random.randint(0, n_samples)

    figfile = BytesIO()
    plt.axis('off')
    plt.imshow(digits.images[ind], cmap=plt.cm.gray_r, interpolation='nearest')
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    
    figdata_png = base64.b64encode(figfile.getvalue())
    res = 'Predicted Digit: ' + str(model.predict(data[ind].reshape(1, 64))[0])
    target ='Target Digit: ' +  str(digits.target[ind])
    return render_template('index.html', trg=target, res=res, img=figdata_png.decode('utf8'))


# Draw Directory
@app.route('/draw')
def draw():
    return render_template('draw.html')

# DrawAPI Directory
@app.route('/draw_api', methods=['POST', 'GET'])
def draw_api():
    if request.method == 'POST':
        w = imageprepare(b64toimg(request.form['img64']))
        x = w[0]
        y = model.predict(x.reshape(1, 64))
        conv_b64 = w[1]
        print('Prediction Number is', str(y[0]))
        result = {
            "output": str(x),
            "pred": str(y),
            "b64": str(conv_b64)
        }
        resultJSON = json.dumps(result)
        return resultJSON
    else:
        return render_template('draw.html')


def b64toimg(b64):
    im_bytes = base64.b64decode(b64)   # im_bytes is a binary image
    im_file = BytesIO(im_bytes)  # convert image to file-like object
    img = Image.open(im_file)   # img is now PIL Image object
    return img

def imgtob64(img):
    output_buffer = BytesIO()
    img.save(output_buffer, format='PNG')
    binary_data = output_buffer.getvalue()
    base64_data = base64.b64encode(binary_data).decode('utf8')
    return base64_data

def imageprepare(img):
    """
    This function returns the pixel values.
    The imput is a png file location.
    """
    im = img.convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    print(width, height)
    newImage = Image.new('L', (8, 8), (255))  # creates white canvas of 28x28 pixels

    # resize and sharpen
    img = im.resize((8, 8), Image.ANTIALIAS).filter(ImageFilter.DETAIL).filter(ImageFilter.DETAIL)

    width = float(img.size[0])
    height = float(img.size[1])
    print(width, height)

    wleft = 0
    newImage.paste(img, (wleft, 0))  # paste resized image on white canvas

    im_b64 = imgtob64(img)

    tv = list(newImage.getdata())  # get pixel values

    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    print('====================================================')
    print('====================================================')
    print(tv)
    print('====================================================')
    print(tva)
    print('====================================================')
    print('====================================================')
    return np.array(tva), im_b64

if __name__ == "__main__":
    app.run(debug=True)