from flask import json
from pathlib import Path

def load_json():
    json_data_file = Path("data/data.json")
    if json_data_file.exists():
        return json.load(open(json_data_file))
    else:
        return


def returnBuildLabel(key):
    _data = load_json()
    if _data:
        if key in _data:
            msg = {key : _data[key]}
        else:
            msg = {'result':"no result found in data.json for key " + key}

        return json.dumps(msg , indent=2)
    else:
        return "Input JSON data file not found or error in loading input JSON data file ....."


		
	
