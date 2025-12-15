[app]
# (str) Title of your application
title = MLProjectFitness
# (str) Package name
package.name = mlprojectfitness
# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (list) Application requirements
requirements = python3,kivy==2.1.0,kivymd==1.1.1,kivy_garden.graph

# (str) Source dir (where the main.py is located)
source.dir = .
source.include_exts = py,png,jpg,kv

# (str) Application entry point
entrypoint = mobile/main.py

# (int) Target API for android
android.api = 31

# (str) Presplash / icon settings can be added here

[buildozer]
# Buildozer config - run buildozer from a Linux environment (WSL recommended on Windows)
