def log_message(message, level="INFO"):
    """Logs a message with a specified level."""
    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    if level not in levels:
        raise ValueError(f"Invalid log level: {level}")
    print(f"{level}: {message}")

def load_config(config_file):
    """Loads configuration settings from a JSON file."""
    import json
    with open(config_file, 'r') as file:
        return json.load(file)