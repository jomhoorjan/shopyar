@echo off

echo ==========================
echo Starting Shopyar...
echo ==========================

call .venv\Scripts\activate.bat

cd backend

uvicorn app.main:app --reload

pause