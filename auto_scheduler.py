"""
Autonomous Blog Generation Scheduler
Discovers trending topics and automatically generates blog posts
"""
import schedule
import time
from datetime import datetime
import subprocess
import sys
from pathlib import Path
import json

def generate_blog_post_automatically():
    """
    Main automation function:
    1. Discover trending topic
    2. Generate blog post with that topic
    3. Log the process
    """
    print("\n" + "=" * 80)
    print(f"🚀 AUTONOMOUS BLOG GENERATION - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print()
    
    try:
        # Step 1: Discover trending topic
        print("🔍 Step 1: Discovering trending topic...")
        result = subprocess.run(
            [sys.executable, "trend_monitor.py"],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode != 0:
            print(f"❌ Error discovering trend: {result.stderr}")
            return
        
        print(result.stdout)
        
        # Load the latest trend
        log_dir = Path("trend_logs")
        log_file = log_dir / f"trend_log_{datetime.now().strftime('%Y%m')}.json"
        
        with open(log_file, 'r', encoding='utf-8') as f:
            trends = json.load(f)
            latest_trend = trends[-1]
        
        topic = latest_trend['topic']
        tone = latest_trend['tone']
        
        print(f"\n✅ Topic discovered: {topic}")
        print(f"🎨 Tone: {tone}\n")
        
        # Step 2: Generate blog post
        print("✍️  Step 2: Generating blog post...")
        print("-" * 80)
        
        # Create input for blog generator (topic + tone selection)
        # Tone mapping: "casual and friendly" = option 2
        tone_map = {
            "professional and informative": "1",
            "casual and friendly": "2",
            "enthusiastic and inspiring": "3",
            "authoritative and expert-level": "4"
        }
        
        tone_input = tone_map.get(tone.lower(), "2")
        input_text = f"{topic}\n{tone_input}\n"
        
        # Run blog generator with automated input
        result = subprocess.run(
            [sys.executable, "blog_generator.py"],
            input=input_text,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        print(result.stdout)
        
        if result.returncode == 0:
            print("\n" + "=" * 80)
            print("✅ AUTONOMOUS GENERATION COMPLETE!")
            print("=" * 80)
            print(f"📌 Topic: {topic}")
            print(f"🎨 Tone: {tone}")
            print(f"📁 Check the generated_posts/ folder for your new blog post")
            print("=" * 80 + "\n")
        else:
            print(f"\n❌ Error generating blog: {result.stderr}\n")
    
    except Exception as e:
        print(f"\n❌ Automation error: {str(e)}\n")

def run_scheduler_interactive():
    """Run the scheduler with interactive menu"""
    print("=" * 80)
    print("🤖 AUTONOMOUS BLOG SCHEDULER")
    print("=" * 80)
    print()
    print("Choose your scheduling preference:")
    print()
    print("  1. Generate ONE blog post NOW")
    print("  2. Schedule DAILY generation (every day at 9:00 AM)")
    print("  3. Schedule WEEKLY generation (every Monday at 9:00 AM)")
    print("  4. Custom interval (every N hours)")
    print("  5. Exit")
    print()
    
    choice = input("Select (1-5): ").strip()
    
    if choice == "1":
        print("\n🚀 Generating blog post now...\n")
        generate_blog_post_automatically()
    
    elif choice == "2":
        schedule.every().day.at("09:00").do(generate_blog_post_automatically)
        print("\n✅ Scheduled! Will generate a new blog post every day at 9:00 AM")
        print("⏰ Scheduler is now running... Press Ctrl+C to stop\n")
        run_schedule_loop()
    
    elif choice == "3":
        schedule.every().monday.at("09:00").do(generate_blog_post_automatically)
        print("\n✅ Scheduled! Will generate a new blog post every Monday at 9:00 AM")
        print("⏰ Scheduler is now running... Press Ctrl+C to stop\n")
        run_schedule_loop()
    
    elif choice == "4":
        hours = input("Generate every N hours (enter number): ").strip()
        try:
            hours = int(hours)
            schedule.every(hours).hours.do(generate_blog_post_automatically)
            print(f"\n✅ Scheduled! Will generate a new blog post every {hours} hours")
            print("⏰ Scheduler is now running... Press Ctrl+C to stop\n")
            run_schedule_loop()
        except ValueError:
            print("❌ Invalid number")
    
    elif choice == "5":
        print("👋 Goodbye!")
        sys.exit(0)
    
    else:
        print("❌ Invalid choice")

def run_schedule_loop():
    """Run the schedule loop"""
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\n\n⏹️  Scheduler stopped by user")
        print("👋 Goodbye!\n")

if __name__ == "__main__":
    run_scheduler_interactive()
