#!/usr/bin/env python3
"""
Content Validator for Euphoric Wreckage Website
Checks content.json for errors before publishing
"""

import json
import sys
from datetime import datetime

def validate_content(filepath='content.json'):
    """Validate the content.json file"""
    
    print("🔍 Validating content.json...")
    errors = []
    warnings = []
    
    # Try to load JSON
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ JSON Syntax Error: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return False
    
    # Check required fields
    required_fields = ['lastUpdated', 'heroVideo', 'featuredTrack', 'dailyQuote', 'news', 'gallery']
    for field in required_fields:
        if field not in content:
            errors.append(f"Missing required field: {field}")
    
    # Validate lastUpdated
    if 'lastUpdated' in content:
        try:
            datetime.strptime(content['lastUpdated'], '%Y-%m-%d')
        except ValueError:
            errors.append("lastUpdated must be in YYYY-MM-DD format")
    
    # Validate heroVideo
    if 'heroVideo' in content:
        valid_videos = [
            'scorpion_spotify_canvas.mp4',
            'finnian_spotify_canvas.mp4',
            'queen_wreckage_spotify_canvas.mp4',
            'e1b5cf17d6fe2efc8988550c11c17024.mp4'
        ]
        if content['heroVideo'] not in valid_videos:
            warnings.append(f"heroVideo '{content['heroVideo']}' may not exist")
    
    # Validate featuredTrack
    if 'featuredTrack' in content:
        track = content['featuredTrack']
        if 'number' not in track:
            errors.append("featuredTrack missing 'number'")
        if 'title' not in track:
            errors.append("featuredTrack missing 'title'")
        if 'description' not in track:
            errors.append("featuredTrack missing 'description'")
        
        if 'description' in track and len(track['description']) < 10:
            warnings.append("featuredTrack description seems very short")
    
    # Validate dailyQuote
    if 'dailyQuote' in content:
        quote = content['dailyQuote']
        if 'text' not in quote:
            errors.append("dailyQuote missing 'text'")
        if 'author' not in quote:
            errors.append("dailyQuote missing 'author'")
        
        valid_authors = ['Vesper Sinclair', 'Justin Sakurai', 'Finnian Frost']
        if 'author' in quote and quote['author'] not in valid_authors:
            warnings.append(f"dailyQuote author '{quote['author']}' is not a band member")
    
    # Validate news
    if 'news' in content:
        if not isinstance(content['news'], list):
            errors.append("news must be an array")
        else:
            for i, item in enumerate(content['news']):
                if 'date' not in item:
                    errors.append(f"news item {i} missing 'date'")
                if 'title' not in item:
                    errors.append(f"news item {i} missing 'title'")
                if 'content' not in item:
                    errors.append(f"news item {i} missing 'content'")
                if 'image' not in item:
                    errors.append(f"news item {i} missing 'image'")
                
                # Validate date format
                if 'date' in item:
                    try:
                        datetime.strptime(item['date'], '%Y-%m-%d')
                    except ValueError:
                        errors.append(f"news item {i} date must be in YYYY-MM-DD format")
            
            if len(content['news']) > 10:
                warnings.append(f"You have {len(content['news'])} news items. Consider keeping only the most recent 6-8.")
    
    # Validate gallery
    if 'gallery' in content:
        if 'rotatingImages' not in content['gallery']:
            errors.append("gallery missing 'rotatingImages'")
        elif not isinstance(content['gallery']['rotatingImages'], list):
            errors.append("gallery.rotatingImages must be an array")
    
    # Report results
    print()
    if errors:
        print("❌ ERRORS FOUND:")
        for error in errors:
            print(f"   • {error}")
        print()
    
    if warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(f"   • {warning}")
        print()
    
    if not errors and not warnings:
        print("✅ All checks passed! Your content.json is valid.")
        print()
        return True
    elif not errors:
        print("✅ No errors found. Warnings are just suggestions.")
        print()
        return True
    else:
        print("❌ Please fix the errors before publishing.")
        print()
        return False

if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'content.json'
    success = validate_content(filepath)
    sys.exit(0 if success else 1)
