# ============================================
# AI Blog Generator - Quick Start Script
# ============================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  AI Blog Post Generator - Setup Wizard" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Step 1: Check Python
Write-Host "Step 1: Checking Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ $pythonVersion found`n" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found! Please install Python 3.10+ from python.org" -ForegroundColor Red
    exit 1
}

# Step 2: Install Dependencies
Write-Host "Step 2: Installing dependencies..." -ForegroundColor Yellow
Write-Host "(This may take a minute...)`n" -ForegroundColor Gray

pip install marvin python-dotenv google-generativeai groq -q

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencies installed successfully!`n" -ForegroundColor Green
} else {
    Write-Host "❌ Installation failed. Please check your internet connection." -ForegroundColor Red
    exit 1
}

# Step 3: Check for API Key
Write-Host "Step 3: Checking for API keys..." -ForegroundColor Yellow

if (Test-Path .env) {
    Write-Host "✅ .env file found`n" -ForegroundColor Green
    $envContent = Get-Content .env -Raw
    
    if ($envContent -match "GOOGLE_API_KEY=.+") {
        Write-Host "✅ Google Gemini API key detected" -ForegroundColor Green
        $apiConfigured = $true
    } elseif ($envContent -match "GROQ_API_KEY=.+") {
        Write-Host "✅ Groq API key detected" -ForegroundColor Green
        $apiConfigured = $true
    } else {
        $apiConfigured = $false
    }
} else {
    $apiConfigured = $false
}

if (-not $apiConfigured) {
    Write-Host "`n⚠️  No API key found!`n" -ForegroundColor Yellow
    Write-Host "You need a FREE API key to use this generator.`n" -ForegroundColor White
    
    Write-Host "Choose a FREE option:" -ForegroundColor Cyan
    Write-Host "  1. Google Gemini (Recommended - Most generous free tier)" -ForegroundColor White
    Write-Host "     Get key: https://makersuite.google.com/app/apikey`n" -ForegroundColor Gray
    Write-Host "  2. Groq (Fast & Free)" -ForegroundColor White
    Write-Host "     Get key: https://console.groq.com/keys`n" -ForegroundColor Gray
    
    $choice = Read-Host "Select option (1 or 2)"
    
    if ($choice -eq "1") {
        Write-Host "`n🌐 Opening Google AI Studio..." -ForegroundColor Cyan
        Start-Process "https://makersuite.google.com/app/apikey"
        $apiKey = Read-Host "`nPaste your Google Gemini API key here"
        "GOOGLE_API_KEY=$apiKey" | Out-File -FilePath .env -Encoding UTF8
        Write-Host "✅ API key saved to .env file`n" -ForegroundColor Green
    } elseif ($choice -eq "2") {
        Write-Host "`n🌐 Opening Groq Console..." -ForegroundColor Cyan
        Start-Process "https://console.groq.com/keys"
        $apiKey = Read-Host "`nPaste your Groq API key here"
        "GROQ_API_KEY=$apiKey" | Out-File -FilePath .env -Encoding UTF8
        Write-Host "✅ API key saved to .env file`n" -ForegroundColor Green
    } else {
        Write-Host "❌ Invalid choice. Please run the script again." -ForegroundColor Red
        exit 1
    }
}

# Step 4: Ready to Run
Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  ✨ Setup Complete!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Green

Write-Host "You're ready to generate blog posts!`n" -ForegroundColor White

$run = Read-Host "Would you like to run the blog generator now? (y/n)"

if ($run -eq "y" -or $run -eq "Y") {
    Write-Host "`n🚀 Starting blog generator...`n" -ForegroundColor Cyan
    python blog_generator.py
} else {
    Write-Host "`nTo generate a blog post later, run:" -ForegroundColor White
    Write-Host "  python blog_generator.py`n" -ForegroundColor Cyan
}

Write-Host "Thank you for using AI Blog Generator! 🎉`n" -ForegroundColor Magenta
