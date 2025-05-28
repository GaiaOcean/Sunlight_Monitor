from flask import Flask, render_template
import json

app = Flask(__name__)

def read_sensor_data():
    try:
        with open('sensor_data.json', 'r') as file:
            data = json.load(file)
        return data.get("solar", 0), data.get("humidity", 0)
    except FileNotFoundError:
        return 0, 0

@app.route('/')
def index():
    solar, humidity = read_sensor_data()
    return render_template('index.html', solar=solar, humidity=humidity)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
