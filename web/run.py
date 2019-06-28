from flask import Flask, request, json, jsonify

import sys
sys.path.append("..")

from atm import ATM

app = Flask(__name__)


@app.route('/run', methods=["POST"])
def run():
    if request.method == 'POST':
        atm = ATM()
        data = json.loads(request.get_data('data'))
        results = atm.run(train_path=data['train_path'])
        return jsonify(status='ok', result=results.get_best_classifier().__repr__())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)