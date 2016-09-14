import os
import transform
from flask import Flask, request, make_response
from jinja2 import Environment, PackageLoader, Template

ALLOWED_EXTENSIONS = set(['txt', 'csv'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Setup web app and templates
env = Environment(loader=PackageLoader('app', 'templates'))
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        props = {"init_sequence": int(request.form["init_sequence"]),
                 "branch_code": request.form["branch_code"],
                 "pos_code": request.form["pos_code"],
                 "fixed_address": "",
                 "fixed_phone": "",
                 "issue_date": request.form["issue_date"],
                 "product_codes": [request.form["product_code_01"],
                                   request.form["product_code_02"],
                                   request.form["product_code_03"],
                                   request.form["product_code_04"]],
                 "product_aux_code": "",
                 "id_type": request.form["id_type"]}
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = "datil_" + file.filename
            content = file.stream.read()
            response = make_response(transform.datilize(content, props))
            response.headers["Content-Disposition"] = "attachment; filename=" + filename
            return response
    template = env.get_template('index.html')
    return template.render()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
