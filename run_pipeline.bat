@echo off

echo ===============================
echo NHS AE Monthly Data Pipeline
echo ===============================

cd C:\Users\Suruthi\Portfolio_projects\nhs

echo.
echo Running Full Pipeline...
python src/pipeline.py

echo.
echo Pipeline execution completed successfully.

pause