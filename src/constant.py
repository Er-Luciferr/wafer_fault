import os

# Artifact folder path
artifact_folder: str = os.path.join(os.getcwd(), "artifacts")

# Source data file path (CSV file in artifacts folder)
SOURCE_DATA_FILE: str = os.path.join(artifact_folder, "wafer_fault.csv")

# Target column name
TARGET_COLUMN: str = "Good/Bad"

