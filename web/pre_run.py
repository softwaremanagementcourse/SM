from flask import Flask, request, json, jsonify

import sys
sys.path.append("..")

from atm import ATM

app = Flask(__name__)


@app.route('/pre_run', methods=["POST"])
def pre_run():
    if request.method == 'POST':
        atm = ATM()
        data = json.loads(request.get_data('data'))
        results = atm.run(train_path=data['train_path'])
        return jsonify(status='ok', result=results.describe())


if __name__ == '__main__':
    print "hello!"
    app.run(debug=True, host='0.0.0.0', port=8888)