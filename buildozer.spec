[app]

# (str) Title of your application
title = Envoice

# (str) Package name
package.name = invoice_front

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = .env,.env.*

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,python-dotenv

# (list) Supported orientations
orientation = portrait

# Android specific
android.api = 34
android.minapi = 24
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a, x86_64

# Разрешения для Android
android.permissions = INTERNET, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_SCAN, BLUETOOTH_CONNECT, BLUETOOTH_ADVERTISE, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, ACCESS_NETWORK_STATE

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# Build settings
android.private_storage = True

# Поддержка современных функций
android.gradle_dependencies = androidx.core:core:1.12.0
android.enable_androidx = True

# Оптимизации для новых устройств
android.allow_backup = True
android.backup_rules = @xml/backup_rules
android.data_extraction_rules = @xml/data_extraction_rules

# Настройки эмулятора (рекомендуемые устройства 2024)
# Pixel 7 Pro (API 34)
# Samsung Galaxy S23 Ultra (API 34)
# Pixel Fold (API 34)