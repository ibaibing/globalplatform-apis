@echo off
REM Build script for gpapis package
REM This script builds the wheel distribution for the gpapis package

echo Building gpapis package...

REM Navigate to the script directory
cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo Error: pip is not installed or not in PATH
    pause
    exit /b 1
)

REM Install required build tools if not present
echo Installing build tools...
pip install --upgrade setuptools wheel twine

REM Clean previous build artifacts
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.egg-info rmdir /s /q *.egg-info
if exist gpapis.egg-info rmdir /s /q gpapis.egg-info

REM Build the wheel package
echo Building wheel package...
echo This will copy the API directories into the gpapis package structure...
python setup.py bdist_wheel

REM Check if build was successful
if errorlevel 0 (
    echo Build completed successfully!
    echo Wheel file created in the 'dist' directory.
    
    REM List the created wheel files
    if exist dist (
        echo Available distribution files:
        dir /b dist\*.whl
    )
) else (
    echo Build failed!
    pause
    exit /b 1
)

echo Build process finished.
pause