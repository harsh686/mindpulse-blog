"""
Trend Monitor Agent - Discovers trending topics by analyzing internet trends
"""
import marvin
from datetime import datetime
import json
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Get model config (same as blog_generator)
def get_model_config():
    from dotenv import dotenv_values
    raw_env = dotenv_values(".env") if Path(".env").exists() else {}
    env_values = {(k.lstrip('\ufeff') if isinstance(k, str) else k): v for k, v in raw_env.items()}
    
    if env_values.get("GOOGLE_API_KEY"):
        google_key = env_values.get("GOOGLE_API_KEY")
        if google_key:
            os.environ["GOOGLE_API_KEY"] = google_key
        return "gemini-2.5-flash"
    
    if env_values.get("GROQ_API_KEY"):
        groq_key = env_values.get("GROQ_API_KEY")
        if groq_key:
            os.environ["GROQ_API_KEY"] = groq_key
        return "groq:llama-3.3-70b-versatile"
    
    raise ValueError("No API key found")

MODEL = get_model_config()

# Create trend monitoring agent
trend_agent = marvin.Agent(
    name="Trend Monitor",
    model=MODEL,
    instructions="""You are an expert trend analyst who monitors internet culture and social conversations.
    
    Your mission:
    - Identify what people are genuinely talking about and struggling with RIGHT NOW
    - Focus on universal human experiences: relationships, mental health, personal growth, work-life balance
    - Look for topics that resonate emotionally and spark thoughtful reflection
    - Choose topics that would make someone stop scrolling and say "wow, I needed this"
    - Think about what Kelly.today or thoughtful Medium writers would explore
    
    Topics should feel:
    - Deeply personal yet universally relatable
    - Reflective and thought-provoking
    - About real struggles people face daily
    - Modern but timeless
    
    Examples of GOOD topics:
    - "why saying no feels impossible when you're a people pleaser"
    - "the quiet grief of outgrowing friendships"
    - "learning to be okay with being misunderstood"
    - "when productivity culture makes you forget how to rest"
    - "the discomfort of choosing yourself first"
    
    Avoid:
    - Generic self-help ("10 ways to be happy")
    - Business/tech trends unless deeply human
    - Celebrity gossip or news events
    - Superficial topics
    """
)

def discover_trending_topic():
    """
    Use AI to identify a trending topic based on current human struggles and conversations.
    Returns: dict with topic, reasoning, and suggested tone
    """
    print("🔍 Monitoring internet trends and human conversations...")
    print("📊 Analyzing what people are struggling with and talking about...\n")
    
    current_date = datetime.now().strftime("%B %d, %Y")
    
    result = marvin.run(
        f"""Today is {current_date}. 
        
        Based on current social conversations, seasonal timing, and universal human experiences:
        
        1. Identify ONE specific, emotionally resonant topic people are dealing with right now
        2. Make it deeply personal yet relatable
        3. Choose something that would make readers feel seen and understood
        4. Think about what's keeping people up at night or making them scroll social media for answers
        
        Consider:
        - What emotional struggles are trending in wellness/mental health spaces?
        - What relationship dynamics are people questioning?
        - What cultural pressures are causing stress?
        - What personal growth challenges feel particularly relevant right now?
        
        Return ONLY the topic as a concise, compelling phrase (5-12 words).
        Example format: "the art of setting boundaries without guilt"
        """,
        agents=[trend_agent],
        result_type=str
    )
    
    topic = result.strip().strip('"').strip("'")
    
    print(f"✨ Discovered topic: {topic}\n")
    
    # Get reasoning and tone suggestion
    reasoning = marvin.run(
        f"""Why is this topic '{topic}' resonant and important right now? 
        In 1-2 sentences, explain the human struggle behind it.""",
        agents=[trend_agent],
        result_type=str
    )
    
    print(f"💡 Why this matters: {reasoning}\n")
    
    return {
        "topic": topic,
        "reasoning": reasoning,
        "tone": "casual and friendly",  # Match the inspirational images
        "discovered_at": datetime.now().isoformat(),
        "source": "AI trend analysis"
    }

def save_trend_log(trend_data):
    """Save discovered trends to a log file"""
    log_dir = Path("trend_logs")
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f"trend_log_{datetime.now().strftime('%Y%m')}.json"
    
    # Load existing logs
    logs = []
    if log_file.exists():
        with open(log_file, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    
    # Add new trend
    logs.append(trend_data)
    
    # Save updated logs
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)
    
    print(f"📝 Trend logged to {log_file}\n")

if __name__ == "__main__":
    print("=" * 70)
    print("🌐 TREND MONITOR - Discovering What People Need Right Now")
    print("=" * 70)
    print()
    
    trend = discover_trending_topic()
    save_trend_log(trend)
    
    print("=" * 70)
    print("✅ Trend discovery complete!")
    print(f"📌 Topic: {trend['topic']}")
    print(f"🎨 Tone: {trend['tone']}")
    print("=" * 70)
