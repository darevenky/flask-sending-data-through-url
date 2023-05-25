from flask import Flask

FI=Flask(__name__)


@FI.route('/venky/<name>')
def venky(name):
    return f'sending data through url {name}'

if __name__=='__main__':
    FI.run(debug=True,port=5001,host='192.168.111.130')