import base64
import mimetypes
import os

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
 
from flask import Flask, render_template, request 
from flask_wtf import CSRFProtect 

@csrf_exempt
def csrf_image(request):
    env = {'qs': request.GET.get('qs', '')}
    return render(request, 'vulnerable/csrf/image.html', env)

## 

app = Flask(__name__) 
app.secret_key = b'_53oi3uriq9pifpff;apl'
csrf = CSRFProtect(app) 

@app.route("/protected_form", methods=['GET', 'POST']) 
def protected_form(): 
    if request.method == 'POST': 
        name = request.form['Name'] 
        return (' Hello ' + name + '!!!') 
    return render_template('index.html') 
  
@app.route("/unprotected_form", methods=['GET', 'POST']) 
def unprotected_form(): 
    if request.method == 'POST': 
        name = request.form['Name'] 
        return (' Hello ' + name + '!!!') 
    return render_template('index.html') 
  
if __name__ == '__main__': 
    app.run(debug=True)