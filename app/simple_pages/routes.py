from flask import Blueprint, redirect, render_template, url_for

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def root():
    # Log:
    print('WELCOME HOME, SIR')

    return render_template("simple_pages/root.html")

@blueprint.route('/home')
def home():
    # Log:
    print('REDIRECT /home TO /')
    
    return redirect(url_for('simple_pages.root'))

@blueprint.route('/login')
def login():
    # Log:
    print('YOU ARE NOW ABLE TO LOG IN')

    return render_template("simple_pages/login.html")