from flask import
app Flask ( _name
@ app.route ( ' / ' )
def setcookie( ) :
if
    res make response ( " cookie is inserted " )
res.set_cookie( ' Flask " , " Framework ' )
    return res
     name main
app.run( debug - True )
