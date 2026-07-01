@echo off

start "" code .

timeout /t 2 > nul

start "" cmd /k "call .venv\Scripts\activate.bat && cd backend && uvicorn app.main:app --reload"