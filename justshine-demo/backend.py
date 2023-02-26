from flask import Flask, request, jsonify
from justshine.testing.setup import getAlgodClient
from justshine.testing.resources import (
    getTemporaryAccount,
    optInToAsset,
    createDummyAsset,
)

app = Flask(__name__)
CLIENT = getAlgodClient()
SELLER = None

#curl 'http://127.0.0.1:5000/view?wallet_address=1'
@app.route('/view', methods=['GET'])
def view_certificate():
	# view NFT info, based on wallet
	wallet_address = int(request.args.get('wallet_address'))

	# try to fetch the user's balances
	asset_balances = CLIENT.account_info(wallet_address)['assets']

	return str(asset_balances)

#curl -X POST -H "Content-Type: application/json" -d '{"v1":"2"}' http://127.0.0.1:5000/trade
@app.route('/trade', methods=['POST'])
def purchase():
	# Seller should initialize a NFT to sell
	nftAmount = 1
    nftID = createDummyAsset(CLIENT, nftAmount, seller)
    print("The NFT ID to sell is", nftID)

    # A new address should be signed up for this purchase
    buyer = initialize_new_buyer()
    


    # return the wallet address/nftID to the user
    data = {
    	"nftID": nftID,
    	"address": buyer.getAddress()
    }
    return jsonify(data)

def initialize_new_buyer():
	return getTemporaryAccount(CLIENT)

def initialize_seller():
	SELLER = getTemporaryAccount(CLIENT)
	print("Host seller initialized")

if __name__ == '__main__':
	initialize_seller()
	app.run(debug=True)
