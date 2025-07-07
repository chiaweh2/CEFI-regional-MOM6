import json
from pathlib import Path

# base_config_name = "extract_var_from_ens_forecast_decadal_andrew"
# output_json_dir = 'json_list'
base_config_name = "extract_var_from_ens_forecast_deacadal_vimal"
output_json_dir = 'v_json_list'


# Load the base config
with open(f"{base_config_name}.json") as f:
    base_config = json.load(f)

# Output directory (optional)
output_dir = Path(f"/home/Chia-wei.Hsu/CEFI-regional-MOM6/xmls/postprocessing/{output_json_dir}/")
output_dir.mkdir(exist_ok=True)

# Loop through years
for year in range(1965, 2023):
    config = base_config.copy()
    config["initialization_year_range"] = [year]
    
    output_path = output_dir / f"{base_config_name}_{year}.json"
    with open(output_path, "w") as f:
        json.dump(config, f, indent=4)
    
    print(f"Created {output_path}")