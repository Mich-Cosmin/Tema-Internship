
# ******************* Inregistrarea pasilor executiei ************************
import logging

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,  # Set the minimum log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='Result_Analysis.log',  # Log to a file
    filemode='w'  # Clear the log file if it exists
)


# Create a logger instance
logger = logging.getLogger('my_debug_logger')
# ***************************************************************************