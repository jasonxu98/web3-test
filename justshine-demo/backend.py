from flask import Flask, request, jsonify

app = Flask(__name__)

#curl 'http://127.0.0.1:5000/view?wallet_id=1'
@app.route('/view', methods=['GET'])
def view_certificate():
	# view NFT info, based on wallet
	wallet_id = int(request.args.get('wallet_id'))
	print(wallet_id)
	return "dummy certificate"

#curl -X POST -H "Content-Type: application/json" -d '{"v1":"2"}' http://127.0.0.1:5000/trade
@app.route('/trade', methods=['POST'])
def purchase():
	# make a purchase
    data = request.json
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
