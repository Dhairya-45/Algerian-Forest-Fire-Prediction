import pickle
import os
import numpy as np
from flask import Flask, request, render_template

application = Flask(__name__)
app = application

# Load trained model & scaler
ridge_model = pickle.load(open("pkl/ridge.pkl", "rb"))
standard_scaler = pickle.load(open("pkl/scaler.pkl", "rb"))


@app.route("/")
def index():
    # Directly open the prediction page
    return render_template("home.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():

    if request.method == "POST":
        # Fetch values from form
        Temperature = float(request.form["Temperature"])
        RH = float(request.form["RH"])
        Ws = float(request.form["Ws"])
        Rain = float(request.form["Rain"])
        FFMC = float(request.form["FFMC"])
        DMC = float(request.form["DMC"])
        ISI = float(request.form["ISI"])
        Classes = int(request.form["Classes"])
        Region = int(request.form["Region"])

        # Order MUST match training data
        input_data = np.array([[ 
            Temperature, RH, Ws, Rain,
            FFMC, DMC, ISI, Classes, Region
        ]])

        # Scale input
        scaled_data = standard_scaler.transform(input_data)

        # Predict FWI
        fwi = ridge_model.predict(scaled_data)[0]

        # Fire risk interpretation
        if fwi < 5:
            risk = "🟢 Low Fire Risk"
        elif fwi < 10:
            risk = "🟡 Moderate Fire Risk"
        elif fwi < 20:
            risk = "🟠 High Fire Risk"
        else:
            risk = "🔴 Extreme Fire Risk"

        return render_template(
            "home.html",
            result=round(fwi, 2),
            risk=risk
        )

    return render_template("home.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
