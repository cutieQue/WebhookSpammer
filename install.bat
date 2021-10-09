@echo OFF

ECHO Installing Required Packages for Webhook Spammer
TIMEOUT 3

py -3 -m pip install -U -r requirements.txt

echo python main.py >> "runSpammer.bat"
echo pause >> "runSpammer.bat"

echo ---------------------------------------------------------------------------------------------

echo Now Run "runSpammer.bat"!
echo Report any Errors on the github! https://github.com/cutieQue/Discord-Server-Lookup

pause
