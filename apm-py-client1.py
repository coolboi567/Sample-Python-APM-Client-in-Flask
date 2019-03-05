from flask import Flask, redirect, request, jsonify, abort
from flask_cors import CORS
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
apm = ElasticAPM(app,
	server_url='http://localhost:8200',
	service_name='app-02',
	secret_token='',
	capture_body='transactions',
	#transaction_sample_rate = 0.2
	)
CORS(app)

@app.route('/')
def index():
	return jsonify({"message": "response ok"})

@app.route('/test', methods=["GET","POST"])
def bar():
	abort(500)
	return "/test exception"

@app.errorhandler(500)
def internal_error(error):
	return "500 error", 500

@app.errorhandler(404)
def not_found(error):
	return "404 error",404

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)