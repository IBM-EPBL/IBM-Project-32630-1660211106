from flask import Flask ,render_template , request
from werkzeug.utils import secure_filename
app Flask ( _name__ )
Bapp.route( ' / ' )
def upload_file( ) :
    return render_template( ' upload1.html " )
Bapp.route( ' / uploader ' ,
def flask_upload( ) :
                          methods = [ ' GET ' , ' POST ' ] )
    if request.method == ' POST ' :
        f = request.files [ ' file ' ]
f.save ( secure_filename ( f.filename ) )
        return file uploaded successfully '
     name === __ main_ ' :
app.run( debug - True )
