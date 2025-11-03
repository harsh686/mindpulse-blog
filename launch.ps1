# Set UTF-8 encoding for emojis
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONIOENCODING = "utf-8"

Write-Host ""
Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host "   AUTONOMOUS BLOG SYSTEM - Quick Launch" -ForegroundColor Cyan
Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Choose what you want to do:" -ForegroundColor White
Write-Host ""
Write-Host "  [1] Generate ONE blog post now (autonomous)" -ForegroundColor Green
Write-Host "  [2] Start the beautiful web showcase" -ForegroundColor Green
Write-Host "  [3] Set up automation (daily/weekly/custom)" -ForegroundColor Green
Write-Host "  [4] Just discover trending topics" -ForegroundColor Green
Write-Host "  [5] Manual blog generation (you choose topic)" -ForegroundColor Green
Write-Host "  [6] Exit" -ForegroundColor Green
Write-Host ""

$choice = Read-Host "Enter your choice (1-6)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "🚀 Starting autonomous blog generation..." -ForegroundColor Yellow
        Write-Host ""
        echo "1" | python auto_scheduler.py
    }
    "2" {
        Write-Host ""
        Write-Host "🌐 Starting web showcase..." -ForegroundColor Yellow
        Write-Host "📍 Open your browser to: http://localhost:5000" -ForegroundColor Cyan
        Write-Host ""
        python web_showcase.py
    }
    "3" {
        Write-Host ""
        Write-Host "⏰ Starting scheduler..." -ForegroundColor Yellow
        Write-Host ""
        python auto_scheduler.py
    }
    "4" {
        Write-Host ""
        Write-Host "🔍 Discovering trending topics..." -ForegroundColor Yellow
        Write-Host ""
        python trend_monitor.py
        Write-Host ""
        Read-Host "Press Enter to continue"
    }
    "5" {
        Write-Host ""
        Write-Host "✍️ Starting manual blog generator..." -ForegroundColor Yellow
        Write-Host ""
        python blog_generator.py
    }
    "6" {
        Write-Host ""
        Write-Host "👋 Goodbye!" -ForegroundColor Green
        exit
    }
    default {
        Write-Host "Invalid choice. Please try again." -ForegroundColor Red
        Read-Host "Press Enter to continue"
    }
}
