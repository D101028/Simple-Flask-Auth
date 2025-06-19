import argparse
import configparser

# Initialize the parser
parser = argparse.ArgumentParser(description="A script that uses command-line arguments.")

# Add arguments
parser.add_argument("-c", "--config", type=str, help="Path to the configuration file")

# Parse the arguments
args = parser.parse_args()

# Access the argument
if args.config:
    config_path = args.config
else:
    config_path = "config.conf"

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read(config_path)

# Accessing the data
default_section = config["DEFAULT"]
auth_section = config["AUTH"]

class Config:
    # Flask configuration
    HOST = default_section.get("HOST")
    PORT = default_section.get("PORT")

    # Authentication
    USERNAME = auth_section.get("USERNAME")
    PASSWORD = auth_section.get("PASSWORD")

    # Check if any of the configuration parameters are missing
    if HOST is None or PORT is None or USERNAME is None or PASSWORD is None:
        raise ValueError("One or more configuration parameters are missing.")

    # Set default values
    if HOST == "":
        HOST = "localhost"
    if PORT == "":
        PORT = "5000"
