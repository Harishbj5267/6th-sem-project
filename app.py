from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__,template_folder='templetes')

# Load the model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
data = pickle.load(open('data.pkl', 'rb'))

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST',])
def predict():
    if request.method == 'POST':
        # Retrieve input values from the form
        company = request.form['company']
        laptop_type = request.form['laptop_type']
        RAM = (request.form['RAM'])
        weight = (request.form['weight'])
        touchscreen = int (request.form['touchscreen'])
        ips = int(request.form['ips']) 
        resolution = request.form['resolution']
        cpu = request.form['cpu']
        hdd = int(request.form['hdd'])
        ssd = int(request.form['ssd'])
        gpu = request.form['gpu']
        os = request.form['os']

        # Create query array
        query = np.array([company, laptop_type, RAM, weight, touchscreen, ips, resolution, cpu, hdd, ssd, gpu, os], dtype=object)
        query = query.reshape(1, 12)

        # Make prediction
        try:
            predicted_price = int(np.exp(pipe.predict(query)[0]))
        except Exception as e:
            print("Error occurred during prediction:", e)
    
            predicted_price = 10000

        return render_template('result.html',predicted_price=predicted_price)


if __name__ == '__main__':
    app.run(debug=True)
