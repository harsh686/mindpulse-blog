@echo off
echo.
echo ========================================================================
echo    AUTONOMOUS BLOG SYSTEM - Quick Launch Menu
echo ========================================================================
echo.
echo Choose what you want to do:
echo.
echo   [1] Generate ONE blog post now (autonomous - discovers topic + writes)
echo   [2] Start the beautiful web showcase (view all posts)
echo   [3] Set up daily/weekly automation (scheduler)
echo   [4] Just discover trending topics (no writing)
echo   [5] Manual blog generation (you choose topic)
echo   [6] Exit
echo.
set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" (
    echo.
    echo 🚀 Starting autonomous blog generation...
    echo.
    python auto_scheduler.py
    goto end
)

if "%choice%"=="2" (
    echo.
    echo 🌐 Starting web showcase...
    echo 📍 Open your browser to: http://localhost:5000
    echo.
    python web_showcase.py
    goto end
)

if "%choice%"=="3" (
    echo.
    echo ⏰ Starting scheduler...
    echo.
    python auto_scheduler.py
    goto end
)

if "%choice%"=="4" (
    echo.
    echo 🔍 Discovering trending topics...
    echo.
    python trend_monitor.py
    pause
    goto start
)

if "%choice%"=="5" (
    echo.
    echo ✍️  Starting manual blog generator...
    echo.
    python blog_generator.py
    goto end
)

if "%choice%"=="6" (
    echo.
    echo 👋 Goodbye!
    goto end
)

echo Invalid choice. Please try again.
pause
goto start

:end
