import pickle
import xgboost as xgb
from flask import Flask, request, jsonify

with open('lin_reg.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

bst = xgb.Booster()
bst.load_model('xgboost_model.json')

def prepare(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features[''] = ride['trip_distance']
    
    return features


def predict(features):
    X = dv.transform(features)
    preds = model.predict(X)
    return float(preds[0])

def predict_xgb(features):
    X_dict = dv.transform(features)
    X = xgb.DMatrix(X_dict)
    preds = bst.predict(X)
    return float(preds[0])

app = Flask('duration-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()
    features = prepare(ride)
    pred = predict_xgb(features)
    result = {
        'duration': pred
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
