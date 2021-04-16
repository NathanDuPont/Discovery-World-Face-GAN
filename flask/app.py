import os
from flask import Flask, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

# python -m flask run
# based on - https://gist.github.com/greyli/81d7e5ae6c9baf7f6cdfbf64e8a7c037

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    submit = SubmitField('Upload')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
        # Pass file into Kiels/Nathans stuff
        fname = filename.split(".")
        out_fname = fname[0] + "_updated" + "." + fname[1]
        out_url = str(file_url).replace(filename, out_fname)
        print(out_url)
    else:
        file_url = None
        out_url = None
    return render_template('index.html', form=form, file_url=file_url, out_url=out_url)


if __name__ == "__main__":
    app.run(debug=True)