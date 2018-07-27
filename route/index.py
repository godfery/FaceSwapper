from flask import render_template,redirect,url_for,request,Response,session,flash
from config.manager import app
from route.forms import LoginForm,ImageForm
# from flask.ext.upload import UploadSet,configure_uploads,IMAGES
from flask_uploads import UploadSet,configure_uploads,IMAGES
from util.FaceWapper import FaceWapper

@app.errorhandler(404)
def not_found(error):
    # return Response.
    # pass
    return render_template('404.html'), 200
@app.route('/')
def index():
    return redirect(url_for('upload'))
    # form = ImageForm()
    # return render_template("login.html",form=form)

@app.route('/register')
def register():

    form = ImageForm()
    return render_template("login.html",form=form)


photos = UploadSet('photos', IMAGES)  
app.config['UPLOADED_PHOTOS_DEST'] = 'static/upload'  
configure_uploads(app, photos)
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print(request.files)
    imageName = ""
    if request.method == 'POST' and 'photo' in request.files:
        # print(request.files)
        filename = photos.save(request.files['photo'])
        filenameNew = photos.save(request.files['photo1'])
        # print(filename)
        session['file1'] = filename
        session['fileNew'] = filenameNew
        print(session.get('file1'))
        print((app.root_path)+"static/upload/"+filename)
        print((app.root_path)+"static/upload/"+filenameNew)
        
        fw = FaceWapper((app.root_path)+"static/upload/"+filename,(app.root_path)+"static/upload/"+filenameNew)
        imageName = fw.uuid_image_name()
        fw.save_image_special((app.root_path)+"static/upload/" + imageName)

        # rec = Photo(filename=filename, user=g.user.id)
        # rec.store()
        flash("Photo saved.")
        # return redirect(url_for('show', id=rec.id))
    form = ImageForm()
    # redirect(url_for('/'))
    return render_template('login.html',form=form,imageName=imageName)

@app.route('/photo/<id>')
def show(id):
    # photo = Photo.load(id)
    # if photo is None:
    #     abort(404)
    # url = photos.url(photo.filename)
    return render_template('show.html', url=url, photo=photo)