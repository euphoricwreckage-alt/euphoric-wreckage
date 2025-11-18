#!/usr/bin/env python3
"""
Euphoric Wreckage - Smart Content Rotation Agent
Intelligently rotates featured tracks, quotes, videos, and news posts
Avoids recent repetitions and maintains engagement
"""

import json
import random
import os
from datetime import datetime
from pathlib import Path

class SmartRotationAgent:
    def __init__(self, content_file='content.json', history_file='update_history.json'):
        # Get the directory where the script is located
        script_dir = Path(__file__).parent if '__file__' in globals() else Path.cwd()
        
        self.content_file = script_dir / content_file
        self.history_file = script_dir / history_file
        
        print(f"Looking for content.json at: {self.content_file}")
        print(f"Looking for update_history.json at: {self.history_file}")
        
        self.content = self.load_content()
        self.history = self.load_history()
        
    def load_content(self):
        """Load current content.json"""
        try:
            with open(self.content_file, 'r', encoding='utf-8') as f:
                content = json.load(f)
                print(f"✓ Successfully loaded content.json")
                return content
        except FileNotFoundError:
            print(f"✗ ERROR: content.json not found at {self.content_file}")
            raise
        except json.JSONDecodeError as e:
            print(f"✗ ERROR: content.json is not valid JSON: {e}")
            raise
    
    def save_content(self):
        """Save updated content.json"""
        with open(self.content_file, 'w', encoding='utf-8') as f:
            json.dump(self.content, f, indent=2, ensure_ascii=False)
    
    def load_history(self):
        """Load update history or create new one"""
        try:
            with open(self.history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
                print(f"✓ Successfully loaded update_history.json")
                return history
        except FileNotFoundError:
            print(f"! update_history.json not found, creating new one")
            return {
                'recent_tracks': [],
                'recent_quotes': [],
                'recent_videos': [],
                'last_update': None,
                'total_updates': 0
            }
    
    def save_history(self):
        """Save update history"""
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2)
    
    def get_tracks_data(self):
        """Return all 12 tracks with metadata"""
        return [
            {
                "number": "01",
                "title": "Static Goddess",
                "description": "Where digital worship meets analog decay. The divine in the machine noise.",
                "vibe": "ethereal, glitchy, worship"
            },
            {
                "number": "02",
                "title": "Silver Wreckage",
                "description": "Chrome and chaos. Beauty forged from destruction, shining in the ruins.",
                "vibe": "metallic, aggressive, beautiful"
            },
            {
                "number": "03",
                "title": "Analog Vertigo (The Lullaby)",
                "description": "Spinning backwards while moving forward. A dizzy embrace of warmth and distortion.",
                "vibe": "warm, disorienting, nostalgic"
            },
            {
                "number": "04",
                "title": "Victorious Failure",
                "description": "Our lead single. Celebrating the beauty of falling apart and getting back up.",
                "vibe": "triumphant, dark, resilient"
            },
            {
                "number": "05",
                "title": "No Rhyme or Reason",
                "description": "Pure chaos energy. When the pattern breaks and something better emerges.",
                "vibe": "chaotic, liberating, wild"
            },
            {
                "number": "06",
                "title": "Pretty Damaged",
                "description": "Scars are just stories written on skin. Damage can be beautiful.",
                "vibe": "emotional, raw, gorgeous"
            },
            {
                "number": "07",
                "title": "Paranoid Bliss",
                "description": "Where anxiety meets ecstasy. Two emotions closer than you think.",
                "vibe": "tense, euphoric, contradictory"
            },
            {
                "number": "08",
                "title": "Glitch Choir",
                "description": "Voices from broken circuits singing in perfect disharmony.",
                "vibe": "vocal, fragmented, sacred"
            },
            {
                "number": "09",
                "title": "No Geography",
                "description": "Borderless sound. Music that exists everywhere and nowhere.",
                "vibe": "spacious, boundless, flowing"
            },
            {
                "number": "10",
                "title": "Gut Feeling",
                "description": "Trust the instinct. When your body knows before your mind does.",
                "vibe": "primal, instinctive, powerful"
            },
            {
                "number": "11",
                "title": "After the Wreckage (we dance)",
                "description": "The title track spirit. Finding joy in the aftermath. Movement through destruction.",
                "vibe": "celebratory, resilient, joyful"
            },
            {
                "number": "12",
                "title": "Found Sounds",
                "description": "The closer. Discovering music in unexpected places. Every ending is a beginning.",
                "vibe": "exploratory, found, conclusive"
            }
        ]
    
    def get_quotes_data(self):
        """Return all quotes from band members"""
        return [
            # Vesper Sinclair (Fire/Intensity) - 10 quotes
            {
                "text": "We don't make music for the algorithm. We make it for the people who feel too much.",
                "author": "Vesper Sinclair"
            },
            {
                "text": "Every breakdown in the music mirrors a breakthrough in the soul.",
                "author": "Vesper Sinclair"
            },
            {
                "text": "Dance like the world is ending. Because it is, and it's beautiful.",
                "author": "Vesper Sinclair"
            },
            {
                "text": "The wreckage isn't the end. It's where we begin.",
                "author": "Vesper Sinclair"
            },
            {
                "text": "Euphoria and pain are neighbors. We live on that border.",
                "author": "Vesper Sinclair"
            },
            {
                "text": "After destruction comes creation. After silence comes the beat.",
                "author": "Vesper Sinclair"
            },
            {
                "text": "Your damage is your superpower. Wear your scars like armor.",
                "author": "Vesper Sinclair"
            },
            {
                "text": "We're not here to be perfect. We're here to be honest.",
                "author": "Vesper Sinclair"
            },
            {
                "text": "The most beautiful sounds come from broken things learning to sing again.",
                "author": "Vesper Sinclair"
            },
            {
                "text": "Feel everything. Fear nothing. Dance through it all.",
                "author": "Vesper Sinclair"
            },
            
            # Justin Sakurai (Ice/Precision) - 10 quotes
            {
                "text": "Perfection is sterile. We're interested in the beautiful mistakes.",
                "author": "Justin Sakurai"
            },
            {
                "text": "Every glitch is a decision waiting to be made.",
                "author": "Justin Sakurai"
            },
            {
                "text": "The space between beats is where the magic lives.",
                "author": "Justin Sakurai"
            },
            {
                "text": "Precision without soul is just mathematics. We need both.",
                "author": "Justin Sakurai"
            },
            {
                "text": "Control the chaos, then let the chaos control you.",
                "author": "Justin Sakurai"
            },
            {
                "text": "The best producers know when to step back and let the song breathe.",
                "author": "Justin Sakurai"
            },
            {
                "text": "Every track is a conversation between order and entropy.",
                "author": "Justin Sakurai"
            },
            {
                "text": "We shape the sound, then the sound shapes us.",
                "author": "Justin Sakurai"
            },
            {
                "text": "Technical mastery means nothing if you have nothing to say.",
                "author": "Justin Sakurai"
            },
            {
                "text": "The coldest sounds can carry the warmest emotions.",
                "author": "Justin Sakurai"
            },
            
            # Finnian Frost (Earth/Warmth) - 10 quotes
            {
                "text": "Bass isn't just sound. It's a feeling in your chest, a connection to the earth.",
                "author": "Finnian Frost"
            },
            {
                "text": "We sample the world because the world is already music.",
                "author": "Finnian Frost"
            },
            {
                "text": "Low frequencies heal what words can't reach.",
                "author": "Finnian Frost"
            },
            {
                "text": "The foundation holds everything. Be someone's foundation.",
                "author": "Finnian Frost"
            },
            {
                "text": "Found sounds are love letters from the universe.",
                "author": "Finnian Frost"
            },
            {
                "text": "Warmth in music isn't about temperature. It's about presence.",
                "author": "Finnian Frost"
            },
            {
                "text": "Every sound carries the memory of where it came from.",
                "author": "Finnian Frost"
            },
            {
                "text": "The bassline is the heartbeat. Everything else dances around it.",
                "author": "Finnian Frost"
            },
            {
                "text": "We don't just make beats. We make spaces where people can feel safe.",
                "author": "Finnian Frost"
            },
            {
                "text": "Grounding isn't about staying still. It's about knowing where home is.",
                "author": "Finnian Frost"
            }
        ]
    
    def get_videos_data(self):
        """Return available hero videos"""
        return [
            "scorpion_spotify_canvas.mp4",
            "finnian_spotify_canvas.mp4",
            "queen_wreckage_spotify_canvas.mp4",
            "e1b5cf17d6fe2efc8988550c11c17024.mp4"
        ]
    
    def select_smart_track(self):
        """Select a track that hasn't been featured recently"""
        tracks = self.get_tracks_data()
        recent_tracks = self.history.get('recent_tracks', [])
        
        # Filter out recently used tracks (last 4 updates)
        available_tracks = [t for t in tracks if t['number'] not in recent_tracks[-4:]]
        
        # If all tracks have been used recently, allow any track
        if not available_tracks:
            available_tracks = tracks
        
        selected = random.choice(available_tracks)
        
        # Update history
        recent_tracks.append(selected['number'])
        if len(recent_tracks) > 6:  # Keep last 6 tracks in history
            recent_tracks.pop(0)
        self.history['recent_tracks'] = recent_tracks
        
        return selected
    
    def select_smart_quote(self):
        """Select a quote that hasn't been shown recently"""
        quotes = self.get_quotes_data()
        recent_quotes = self.history.get('recent_quotes', [])
        
        # Filter out recently used quotes (last 5 updates)
        available_quotes = [q for q in quotes if q['text'] not in recent_quotes[-5:]]
        
        # If all quotes have been used recently, allow any quote
        if not available_quotes:
            available_quotes = quotes
        
        selected = random.choice(available_quotes)
        
        # Update history
        recent_quotes.append(selected['text'])
        if len(recent_quotes) > 10:  # Keep last 10 quotes in history
            recent_quotes.pop(0)
        self.history['recent_quotes'] = recent_quotes
        
        return selected
    
    def select_smart_video(self):
        """Select a video that hasn't been used recently"""
        videos = self.get_videos_data()
        recent_videos = self.history.get('recent_videos', [])
        
        # Filter out recently used videos (last 2 updates)
        available_videos = [v for v in videos if v not in recent_videos[-2:]]
        
        # If all videos have been used recently, allow any video
        if not available_videos:
            available_videos = videos
        
        selected = random.choice(available_videos)
        
        # Update history
        recent_videos.append(selected)
        if len(recent_videos) > 3:  # Keep last 3 videos in history
            recent_videos.pop(0)
        self.history['recent_videos'] = recent_videos
        
        return selected
    
    def generate_news_post(self, track):
        """Generate a news post about the featured track"""
        templates = [
            f"Today we're highlighting '{track['title']}' - track {track['number']} from our album. {track['description']}",
            f"Diving deep into '{track['title']}' today. This track embodies {track['vibe']}.",
            f"'{track['title']}' is taking center stage. {track['description']}",
            f"Track {track['number']}: '{track['title']}' - {track['description']}",
            f"Exploring the sonic landscape of '{track['title']}' today. {track['vibe'].title()} energy throughout."
        ]
        
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "title": f"Featured Track: {track['title']}",
            "content": random.choice(templates),
            "image": "EuphoricWreckageFrontStream.png"
        }
    
    def update_content(self):
        """Main update function - performs smart rotation"""
        print("\n🎵 Euphoric Wreckage Smart Update Agent")
        print("=" * 50)
        
        # Select new content
        new_track = self.select_smart_track()
        new_quote = self.select_smart_quote()
        new_video = self.select_smart_video()
        
        print(f"\n✓ Selected Track: {new_track['title']} ({new_track['number']})")
        print(f"✓ Selected Quote: \"{new_quote['text'][:60]}...\"")
        print(f"  - By: {new_quote['author']}")
        print(f"✓ Selected Video: {new_video}")
        
        # Update content.json
        self.content['featuredTrack'] = {
            "number": new_track['number'],
            "title": new_track['title'],
            "description": new_track['description']
        }
        
        self.content['dailyQuote'] = new_quote
        self.content['heroVideo'] = new_video
        
        # Generate and add news post (keep max 8 posts)
        news_post = self.generate_news_post(new_track)
        news_posts = self.content.get('news', [])
        news_posts.insert(0, news_post)  # Add to beginning
        if len(news_posts) > 8:
            news_posts = news_posts[:8]  # Keep only 8 most recent
        self.content['news'] = news_posts
        
        # Update timestamp
        self.content['lastUpdated'] = datetime.now().strftime("%Y-%m-%d")
        
        # Update history
        self.history['last_update'] = datetime.now().isoformat()
        self.history['total_updates'] = self.history.get('total_updates', 0) + 1
        
        # Save everything
        self.save_content()
        self.save_history()
        
        print(f"\n✅ Content updated successfully!")
        print(f"📊 Total updates: {self.history['total_updates']}")
        print(f"🕐 Last update: {self.content['lastUpdated']}")
        print("\n" + "=" * 50)
        print("🦀🌻⚡ Dance in the ruins. Build beauty from wreckage. 🦀🌻⚡")

def main():
    agent = SmartRotationAgent()
    agent.update_content()

if __name__ == "__main__":
    main()
