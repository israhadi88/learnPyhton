test_settings = {
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high'
}
def add_setting(settings_dict,kv_pair):
    key = str(kv_pair[0]).lower()
    value = str(kv_pair[1]).lower()
    #kalo udah ada
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    #kalo gaada di tambahin
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict,kv_pair):
    key = str(kv_pair[0]).lower()
    value = str(kv_pair[1]).lower()
    #kalo udah ada
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    #kalo gaada
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict,key_to_delete):
    key = str(key_to_delete).lower()
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    return f"Setting not found!"
    
def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
    
    result = "Current User Settings:\n"
    
    for key, value in settings_dict.items():
        result += f"{key.capitalize()}: {value}\n"
        
    return result

# --- Contoh Pengujian ---
print(test_settings(add_setting({'theme': 'light'}, 'theme')))
print(update_setting({'theme': 'light'}, 'theme'))
print(view_settings({'theme': 'light'}))
print(delete_setting({'theme': 'light'}, 'theme'))