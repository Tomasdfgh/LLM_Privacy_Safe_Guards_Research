@echo off
:loop
cls
nvidia-smi
timeout /t 1 >nul
goto loop
