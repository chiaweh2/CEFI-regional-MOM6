#!/bin/bash

# Directory where your JSON files are
CONFIG_DIR="/home/Chia-wei.Hsu/CEFI-regional-MOM6/xmls/postprocessing/json_list"

# Loop over all JSON files in the directory
for json_file in "$CONFIG_DIR"/*.json; do
    echo "Running: python extract_var_from_ens_forecast.py $json_file"
    python extract_var_from_ens_forecast.py "$json_file" &
done
