import os
import json

if os.environ.get("DEBUG"):
    _CFGPATH="config.json"
else:
    _CFGPATH="/app/config/config.json"

config = None
if os.path.exists(_CFGPATH):
    with open(_CFGPATH, "r") as f:
        config = json.load(f)
else:
    config = {
        "broadcastAddr": "255.255.255.255",
        "port": 9,
        "servers": [
            {
                "name": "Test Server",
                "mac": "FF:FF:FF:FF:FF:FF"
            }
        ]
    }
    with open(_CFGPATH, "w") as f:
        f.write(json.dumps(config))
    