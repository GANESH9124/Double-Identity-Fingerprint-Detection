from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import cv2
app = Flask(__name__)
from PIL import Image
import joblib
import io
from models.matching import get_score
from models.model1 import *
import numpy as np
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    fingerprint_image = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        username = request.form['username']
        fingerprint_image = request.files['fingerprint_image']
        user = User.query.filter_by(username=username).first()
        if user:
            db_image_filename = user.fingerprint_image
            db_image = np.array(Image.open(f'uploads/{db_image_filename}'))
            print(username)
            print(db_image.shape)

            img = Image.open(io.BytesIO(fingerprint_image.read()))
            img_array = np.array(img.convert('L'))
            print(img_array.shape)
            score=get_score(db_image,[img_array])
            print(score)
            if score>25:
                import joblib
                model1=joblib.load('models/logistic_regression_model.pkl')
                pred=predict_lr(img_array,model1)
                return render_template('feedback2.html')
            else:
                return render_template('feedback3.html')
        else:
            return render_template('feedback4.html')
    else:
        return render_template('index.html')
@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method=='POST':
        username = request.form['username']
        fingerprint_image = request.files['fingerprint_image']
        fingerprint_image.save(f'uploads/{fingerprint_image.filename}')  # Save image to uploads folder
        print(username)
        image = Image.open(fingerprint_image.stream)
        # Convert the image to a NumPy array
        image= np.array(image)
        print(image.shape)
        model=joblib.load('models/random_forest_model.joblib')
        output=predict(image,model)
        if output==1:
            new_user = User(username=username, fingerprint_image=fingerprint_image.filename)
            db.session.add(new_user)
            db.session.commit()
            return render_template('index.html')
        else:
            return render_template('feedback1.html')
    else:
        return render_template('reg.html')
@app.route('/back', methods=['GET','POST'])
def back():
    return render_template('index.html')
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
