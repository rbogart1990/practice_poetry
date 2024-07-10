from datetime import datetime
import logging
import os

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
LOG.info(f'current_date: {current_date}')