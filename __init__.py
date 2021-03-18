from flask import Flask, render_template,request,abort,Response
from werkzeug.utils import secure_filename
import requests
import cv2
import numpy as np

app = Flask(__name__)
api = 'http://10.127.240.120:5000/'
headers = {'content-type': 'image/png'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            app.logger.info('POST request received.')
            image_decoded = cv2.imdecode(np.fromstring(request.files['file'].read(), np.uint8), cv2.cv2.IMREAD_UNCHANGED)
            app.logger.info('Image has been received and decoded.')
            image_decoded = cv2.resize(image_decoded, (128, 128))
            result = requests.post(api, data=image_decoded.tostring(),headers=headers)
            result = result.json()
            app.logger.info(result)
            prediction = int(result['message'])
            if prediction == 0:
                return render_template('prediction.html',message='healthy patient')
            if prediction == 1:
                return render_template('prediction.html',message='patient with Viral Pneumonia')
            if prediction == 2:
                return render_template('prediction.html',message='patient with COVID-19')
            else:
                return abort(404)

            data = request
        except Exception as e:
            print('Exception: '+str(e))
            return abort(404)
    else:
        return render_template('predictor.html')
	

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)