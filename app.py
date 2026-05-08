from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

# Create Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get frontend JSON data
        data = request.get_json()

        review = data["review"]

        # Predict
        prediction = model.predict([review])[0]

        print("Prediction:", prediction)

        # LABEL MAPPING
        # OR = Fake
        # CG = Genuine

        if prediction == "OR":
            result = "Fake Review ❌"
        else:
            result = "Genuine Review ✅"

        return jsonify({
            "prediction": result
        })

    except Exception as e:

        return jsonify({
            "prediction": "Server Error",
            "error": str(e)
        })

# Run server
if __name__ == "__main__":
    app.run(debug=True)