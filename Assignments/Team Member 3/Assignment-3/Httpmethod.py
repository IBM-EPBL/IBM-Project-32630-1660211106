from flask import Flask , redirect , url_for , request , render_template , json
import os
app Flask ( _name__ )
food items = { " 1 " : " Apple " , " 2 " : " Banana " , " 3 " : " watermelon " , " " grapes " , " 5 " : " pineapple " , " 6 " : " Ch
@ app.route ( ' / data , methods = [ ' POST ' , ' GET ' ] )
def api( ) :
    if request.method == ' GET ' :
        return food items
    if request.method == ' POST ' :
        data request.json
        food items.update ( data )
        return " Data is inserted "
    @ app.route ( " / data / < td > " , methods - [ " PUT " ] )
    def update ( id ) :
        data request.form [ ' item ' ]
        food items [ str ( id ) ) = data
        return Data updated "
Sopp.route( " / route ( / data / < id > " , nethods- [ " DELETE " ] )
    def delete ( id ) :
    food items.pop( str ( id ) )
    return " data deleted "
         name -- ' main ' : if
portos.evniron.get( ' FLASK_PORT ' )
        port - int ( port )
app.run( post - post , host = 0.0.0.0 ' )
app.run( debug True )
