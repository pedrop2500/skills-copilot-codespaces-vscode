from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
     if file is None:
         return 'No file uploaded'
    # Process the uploaded file here
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()





