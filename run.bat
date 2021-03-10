@echo off
cd python3-windows
Python-Launcher.exe -c 'import sys; sys.path.insert(0, ".."); import autotyper.py'