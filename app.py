from flask import Flask, request, jsonify
from datetime import datetime, timedelta



app = Flask(__name__)

def generate_employee_time(overtime_minutes, userinput):
    userinput += " AM"
    duty_start = datetime.strptime(userinput, "%I:%M %p")
    duty_duration = 465
    total_minutes = duty_duration + overtime_minutes
    in_time = duty_start
    out_time = in_time + timedelta(minutes=total_minutes)
    return in_time.strftime("%I:%M %p"), out_time.strftime("%I:%M %p")

@app.route('/calculate_time', methods=['POST'])
def calculate_time():
    data = request.json
    overtime_minutes = int(data.get("overtime_minutes", 0))
    userinput = data.get("in_time", "")

    if overtime_minutes < 0:
        return jsonify({"error": "Overtime cannot be negative."}), 400

    in_time, out_time = generate_employee_time(overtime_minutes, userinput)
    return jsonify({"in_time": in_time, "out_time": out_time})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
