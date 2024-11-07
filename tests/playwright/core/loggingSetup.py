import logging
import logging.config
import json
import os

def setup_logging():
    #Setup logging configuration
    path = os.path.join(os.path.dirname(__file__), 'logging_config.json')
    
    with open(path, 'r') as f:
        config = json.load(f) # Load the logging configuration from the JSON file
    
    # Dynamically set the absolute path for the .log file
    log_file_path = os.path.join(os.path.dirname(__file__), 'playwright_logging.log')
    
    # Clear the log file before adding new logs
    # This is optional and can be removed if you want to append logs to the existing file
    '''
    with open(log_file_path, 'w'):
        pass
    '''
    config['handlers']['file']['filename'] = log_file_path
    
    # Configure logging using the dictionary loaded from the JSON file
    logging.config.dictConfig(config) 
 