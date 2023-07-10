from flask import Flask, request, make_response
from werkzeug.utils import secure_filename
from formatter_ import convert

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/home/prod/mfg/files'

site = '''
<html>
    <style>
    .outer { outline: 1px solid #eee; }
    .outer > p { display: table-cell; height: 200px; vertical-align: middle; }
    </style>
   <body>
      <form class="outer" action = "/uploader" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>   
   </body>
</html>
'''

@app.route('/')
def index():
    return site

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        f = request.files['file']
        output = make_response(convert(f))
        output.headers["Content-Disposition"] = "attachment; filename=export.csv"
        output.headers["Content-type"] = "text/csv"
        return output

if __name__ == '__main__':
    app.run(debug=True)