class Configuration:
    pass


setting_data = {
    "server_url": "https://api.example.com",
    "timeout_sec": 30,
    "max_retries": 5,
}

config_obj = Configuration()

for key,value in setting_data.items():
    setattr(config_obj,key,value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec)
print(config_obj.max_retries)