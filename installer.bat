@echo off
echo [+] Setting up python virtual environment

python -m venv .env && (
./.env/Scripts/Activate

echo [+] installing required packages
pip install -r requirements.txt

echo [+] Starting the keylogger
python app.py
) || (
    echo [-] failed to create a virtual environment
    echo [!] looking for local environment

    .\.env\Scripts\activate.bat && (
        echo [+] Found environment, activating
        echo [!] Installing packages 
        pip install -r requirements.txt && (
            echo [+] packages installed
            echo [!] Starting application
            python ./app.py 
        ) || (
            echo [-] Operation failed exiting....
        )
    )
)