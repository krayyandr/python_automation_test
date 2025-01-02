# Python Automation Project

## Overview
This project is designed to automate various tasks using Python scripts. It includes utility functions, example scripts, and a clear structure for easy navigation and execution.

## Project Structure
```
python-automation-project
├── src
│   ├── main.py          # Entry point of the automation project
│   ├── utils
│   │   └── helpers.py   # Utility functions for reuse
│   └── scripts
        ├── example_script.py  # Example automation script
│       └── sum_script.py # Test new automation script
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd python-automation-project
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the automation project, execute the main script:
```
python src/main.py
python src/main.py --run example
python src/main.py --run sum
```

## Scripts and Utilities
- **main.py**: Orchestrates the execution of various scripts and utilities.
- **helpers.py**: Contains utility functions like `log_message` and `load_config`.
- **example_script.py**: An example script that demonstrates how to perform a specific task.

Feel free to explore and modify the scripts as needed for your automation tasks!