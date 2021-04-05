import os
from flask import Flask, flash, request, redirect, url_for,send_from_directory,render_template,jsonify
from werkzeug.utils import secure_filename
import gdb_interface
import time

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','c'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
a = ''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET', 'POST'])
def upload_file():
    global a
    if request.method == 'POST':
        # check if the post request has the file part
        print(request.files)
        if 'files' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist("files")
        print(files)
        # if user does not select file, browser also
        # submit an empty part without filename
        if len(files)==0:
            flash('No selected file')
            return redirect(request.url)
        result=''
        if len(files) :
            for file in files:
                filename = secure_filename(file.filename)
                result+=filename+' '
                file.save(os.path.join(filename))
            # time.sleep(10)
            a=gdb_interface.hello_world(result)
            # return a
            return ('',204)

    return render_template('index.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)
# @app.route('/result/<filename>')
# def processing(filename):
    
#     a=gdb_interface.hello_world(filename)
#     return a

@app.route('/json_data_func')
def json_data_func():
    return jsonify({'a':a})

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)
    	


    	            # return redirect(url_for('processing',
            #                             filename=result))