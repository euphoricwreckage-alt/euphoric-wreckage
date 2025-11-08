#!/usr/bin/env python3
"""
Automated Daily Content Generator for Euphoric Wreckage
This script randomly selects content for daily updates
"""

import json
import random
from datetime import datetime

# Track data
TRACKS = [
    {"number": "01", "title": "Static Goddess", "description": "Where noise becomes signal. The opening statement of controlled chaos and hidden beauty."},
    {"number": "02", "title": "Silver Wreckage", "description": "Tarnished beauty shines brightest. Heavy breakbeats meet melodic devastation."},
    {"number": "03", "title": "Analog Vertigo (The Lullaby)", "description": "A 175 BPM lullaby for the sleepless. Chaos becomes comfort."},
    {"number": "04", "title": "Victorious Failure", "description": "Finding triumph in defeat. Our lead single that captures the essence of beautiful contradiction."},
    {"number": "05", "title": "No Rhyme or Reason", "description": "Logic is overrated. Pure feeling translated into breakbeat fury."},
    {"number": "06", "title": "Pretty Damaged", "description": "Imperfection perfected. The cracks are where the light gets in."},
    {"number": "07", "title": "Paranoid Bliss", "description": "Where anxiety meets ecstasy. Two emotions closer than you think."},
    {"number": "08", "title": "Glitch Choir", "description": "Digital angels singing through corrupted files. Sacred meets synthetic."},
    {"number": "09", "title": "No Geography", "description": "Music that transcends borders. Frequency knows no boundaries."},
    {"number": "10", "title": "Gut Feeling", "description": "Trust your instincts. They know the beat before your brain does."},
    {"number": "11", "title": "After the Wreckage (we dance)", "description": "When everything falls apart, the real party starts. Our anthem of resilience."},
    {"number": "12", "title": "Found Sounds", "description": "The world is a sample library. We just know how to listen."}
]

# Quotes
QUOTES = [
    {"text": "Dance in the ruins. Build beauty from wreckage.", "author": "Vesper Sinclair"},
    {"text": "Static holds secrets. The white noise between stations is where we find our signal.", "author": "Justin Sakurai"},
    {"text": "Sometimes chaos is the only lullaby that makes sense.", "author": "Finnian Frost"},
    {"text": "Every defeat is just a victory we haven't understood yet.", "author": "Vesper Sinclair"},
    {"text": "Logic is overrated. Feel first, think later.", "author": "Finnian Frost"},
    {"text": "The cracks are where the light gets in. We just made ours glow neon.", "author": "Justin Sakurai"},
    {"text": "Anxiety and ecstasy are closer than you think.", "author": "Vesper Sinclair"},
    {"text": "Digital angels singing through corrupted files.", "author": "Justin Sakurai"},
    {"text": "Music transcends borders. Bass transcends everything.", "author": "Finnian Frost"},
    {"text": "Trust your gut. It knows the beat before your brain does.", "author": "Vesper Sinclair"},
    {"text": "When everything falls apart, that's when the real party starts.", "author": "Finnian Frost"},
    {"text": "The world is a sample library if you know how to listen.", "author": "Justin Sakurai"},
    {"text": "160-180 BPM isn't just a tempo. It's a lifestyle.", "author": "Vesper Sinclair"},
    {"text": "Every kick drum is a heartbeat. Every snare is a battle cry.", "author": "Finnian Frost"},
    {"text": "Synths don't just make sounds. They tell stories.", "author": "Justin Sakurai"},
    {"text": "The mix is where the magic happens. Or the disaster. Usually both.", "author": "Justin Sakurai"},
    {"text": "Bass is not just heard. It's felt. It's survival.", "author": "Finnian Frost"},
    {"text": "Mistakes are just happy accidents waiting to be loops.", "author": "Justin Sakurai"},
    {"text": "Geography is imaginary. Frequency is forever.", "author": "Vesper Sinclair"},
    {"text": "Your gut has a BPM. Find it.", "author": "Finnian Frost"},
    {"text": "After destruction comes creation. After silence comes the beat.", "author": "Vesper Sinclair"},
    {"text": "Listen to everything. Use anything.", "author": "Justin Sakurai"},
    {"text": "Dance like the floor is lava. Because it is.", "author": "Finnian Frost"},
    {"text": "Silver doesn't tarnish. It evolves.", "author": "Justin Sakurai"},
    {"text": "Vertigo is just perspective asking for a new angle.", "author": "Vesper Sinclair"},
    {"text": "Failure is just success practicing its entrance.", "author": "Finnian Frost"},
    {"text": "Reason is overrated. Rhythm is eternal.", "author": "Vesper Sinclair"},
    {"text": "We're not a band. We're a collision.", "author": "Vesper Sinclair"},
    {"text": "Opposites don't attract. They create.", "author": "Justin Sakurai"}
]

# Videos
VIDEOS = [
    'scorpion_spotify_canvas.mp4',
    'finnian_spotify_canvas.mp4',
    'queen_wreckage_spotify_canvas.mp4',
    'e1b5cf17d6fe2efc8988550c11c17024.mp4'
]

def generate_daily_content(output_file='content.json'):
    """Generate new daily content"""
    
    print("🎵 Generating daily content for Euphoric Wreckage...")
    
    # Load existing content to preserve news
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            existing = json.load(f)
            news = existing.get('news', [])
            gallery = existing.get('gallery', {})
    except (FileNotFoundError, json.JSONDecodeError):
        news = []
        gallery = {"rotatingImages": [
            "Euphoric_Wreckage18.png",
            "Vesper13.png",
            "Justin10.png",
            "FinnianVesper2.png",
            "Gen4_complete_band_standing_on_the_stage_IMG_1___IMG_2_and_IMG_3___singer_in_the_front__Dut_35651001.png",
            "Gen4_the_model_IMG_2_standing_on_this_stage_behind_this_ribbon_microphone_IMG_1_in_a_this_ex_1015420.png"
        ]}
    
    # Select random content
    track = random.choice(TRACKS)
    quote = random.choice(QUOTES)
    video = random.choice(VIDEOS)
    
    # Build new content
    content = {
        "lastUpdated": datetime.now().strftime('%Y-%m-%d'),
        "heroVideo": video,
        "featuredTrack": track,
        "dailyQuote": quote,
        "news": news,
        "gallery": gallery
    }
    
    # Save
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Content updated!")
    print(f"   Featured Track: {track['number']}. {track['title']}")
    print(f"   Quote by: {quote['author']}")
    print(f"   Hero Video: {video}")
    print(f"   Date: {content['lastUpdated']}")
    print()

if __name__ == '__main__':
    generate_daily_content()
