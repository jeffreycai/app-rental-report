import os
import datetime
import math
from dotenv import load_dotenv
from dateutil.relativedelta import relativedelta

# Load environment variables from .env file
load_dotenv()

# Read environment variables
rental = float(os.getenv('RENTAL', '0'))
start_date_str = os.getenv('START', '2023-01-01')
pay_cycle_weeks = int(os.getenv('PAY_CYCLE', '2'))
bank_details = os.getenv('BANK_DETAILS', '')

# Parse the start date
start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()

# Calculate the current payment cycle dates and total payment cycles
today = datetime.date.today()
days_since_start = (today - start_date).days
total_payment_cycles = math.ceil(days_since_start / 7 / pay_cycle_weeks)

# Calculate first and last day of the current payment cycle
first_day = start_date + relativedelta(weeks=(total_payment_cycles-1)*pay_cycle_weeks)
last_day = first_day + relativedelta(weeks=pay_cycle_weeks, days=-1)

# Calculate payment amount for the current cycle
payment_amount = rental * pay_cycle_weeks

# Read and process the template
with open('rental_report.template', 'r') as file:
    template = file.read()

report = template.format(
    START=start_date_str,
    RENTAL=rental,
    first_day=first_day.strftime('%Y-%m-%d'),
    last_day=last_day.strftime('%Y-%m-%d'),
    payment_amount=payment_amount,
    total_payment_cycles=total_payment_cycles,
    bank_details=bank_details
)

# Write the report to a file
with open('message.txt', 'w') as file:
    file.write(report)
