from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify

app = Flask(__name__)
 
@app.route('/upload_image', methods=['POST'])
@cross_origin()
def upload_image():
    print(request.files)
    if 'image' not in request.files:
        return jsonify({'error': 'no image provided'})
    image_file = request.files['image']
    image_bytes = image_file.read()
    # process the image here
    return jsonify({'message': 'image received'})
 
if __name__ == '__main__':
    app.run()
