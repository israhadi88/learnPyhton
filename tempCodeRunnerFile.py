def view_settings(settings_dict):
    # 1. Cek jika dictionary kosong
    if not settings_dict:
        return "No settings available."
    
    # 2. Inisialisasi string header
    result = "Current User Settings:"
    
    # 3. Tambahkan key-value dengan format yang diminta
    for key, value in settings_dict.items():
        # key.capitalize() mengubah 'theme' menjadi 'Theme'
        # \n memastikan setiap setting berada di baris baru
        result += f"\n{key.capitalize()}: {value}"
        
    return result

# --- Contoh Pengujian ---
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))