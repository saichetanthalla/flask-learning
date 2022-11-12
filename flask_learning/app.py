# # from typing import runtime_checkable
from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route('/add_two_nums', methods=['POST','GET'])
def adding():
    if request.method == 'POST':

        data_dict=request.get_json()
        x=data_dict['x']
        y=data_dict['y']
        z=x+y
        res={
            'z':z
        }
    return jsonify(res,200)
# @app.route('/')
# def hello():
#     return 'Hello_world'
if __name__=='__main__':
    app.run(debug = True)
# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)

# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))

# if __name__ == '__main__':
#    app.run(debug = True)