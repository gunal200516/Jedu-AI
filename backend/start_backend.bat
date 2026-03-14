@echo off
echo ========================================
echo JeduAI Media Translation Backend
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
echo.

REM Start server
echo ========================================
echo Starting backend server...
echo Backend will run on: http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo Health Check: http://localhost:8000/health
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

python main.py
