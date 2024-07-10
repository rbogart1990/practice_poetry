from datetime import datetime
import logging
import os
import pendulum

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create logger object:
LOG = logging.getLogger(os.path.basename(__file__))

# Get current date
current_datetime = datetime.now()
current_date = current_datetime.date()
current_date_str = current_date.strftime('%Y-%m-%d')
LOG.info(f'current_date: {current_date_str}')

# Get first day of current quarter
p = pendulum.from_format(current_date_str, 'YYYY-MM-DD')
first_of_quarter = p.first_of('quarter').strftime('%Y-%m-%d')
# Convert to datetime.date object:
first_of_quarter = datetime.strptime(first_of_quarter, '%Y-%m-%d').date()
LOG.info(f'first_of_quarter: {first_of_quarter}')