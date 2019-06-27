from app import app
@ app.route('/')
@ app.route('/index')
def index():
    return """<html>
            <head><title>GURNEETs WEBPAGE</TITLE>
            </head>
            <body>
            Hello!!!!
            Hows you
            </body>
            </html>"""
            
