from flask import Flask,render_template,request,redirect,jsonify
from model import Model
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('/Users/vineeth/PycharmProjects/Assesment','UPLOAD_FOLDER')
ALLOWED_EXTENSIONS = {"csv"}
@app.route('/')
def upload():
    return render_template('upload.html')

def allowed_file(filename):
    """Check if the uploaded file has a .csv extension"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

#CSV uploaded
@app.route('/upload',methods =['POST'])
def upload_data():
    if request.method == 'POST':
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            file.save(filepath)
            model=Model()
        if model.upload(data=filepath):
            return jsonify({'Message':'uploaded successfully!'}),200
        return jsonify({'message': 'Something went wrong'}), 400



