import random
from datetime import datetime, timedelta

def generate_employee_time(overtime_minutes,userinput):
    userinput+=" AM"


    duty_start = datetime.strptime(userinput, "%I:%M %p")

    # Calculate total duty time in minutes
    duty_duration = 465

    # Add overtime to duty duration
    total_minutes = duty_duration + overtime_minutes

    # Generate random in-time between 10:00 AM and 11:00 AM
    in_time = duty_start

    # Calculate out-time by adding total_minutes to in-time
    out_time = in_time + timedelta(minutes=total_minutes)

    return in_time.strftime("%I:%M %p"), out_time.strftime("%I:%M %p")

def handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello, world!"
    }

def main():
    print("Enter the overtime in minutes:")
    try:
        overtime_minutes = int(input("Overtime (in minutes): "))
        userinput=input("IN TIME :")
        if overtime_minutes < 0:
            print("Overtime cannot be negative. Please enter a valid number.")
            return

        in_time, out_time = generate_employee_time(overtime_minutes,userinput)
        print(f"Employee In-Time: {in_time}")
        print(f"Employee Out-Time: {out_time}")

    except ValueError:
        print("Invalid input. Please enter a valid number for overtime.")


if __name__ == "__main__":
    main()