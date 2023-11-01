@setlocal enableextensions
@cd /d "%~dp0"
schtasks /Create /XML auto-job.xml /tn auto-job
pause