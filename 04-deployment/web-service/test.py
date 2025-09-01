import requests
import predict

ride = {
    "PULocationID": 2500,
    "DOLocationID": 3500,
    "trip_distance": 5100
}
target = "duration"

url = 'http://localhost:9696/predict'
response = requests.post(url, json=ride)
print(response.json())



# features = predict.prepare(ride)
# pred = predict.predict(features)
# print(f"Linear Regression: {pred}")
# pred2 = predict.predict_xgb(features)
# print(f"Xgboost: {pred2}")