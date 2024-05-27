#!/bin/bash --login
# The --login ensures the bash configuration is loaded,
# enabling Conda.

# Enable strict mode.
set -euo pipefail

echo "Inside the entrypoint script"

# Check if team_name is provided
if [ "$#" -ne 1 ]; then
    echo "Error: Please provide a team name as an argument."
    exit 1
fi

team_name="$1"

# Run the participant's solution with the provided test input file
python /app/src/solution.py /app/test_cases/input/test_input.csv /app/test_cases/output/${team_name}_output.csv


