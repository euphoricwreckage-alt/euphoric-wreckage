# 🚀 QUICK START GUIDE

## Upload to GitHub Pages in 5 Minutes

### Step 1: Create GitHub Account
If you don't have one: https://github.com/signup

### Step 2: Create New Repository
1. Go to https://github.com/new
2. Name: `euphoric-wreckage`
3. Public repository
4. Click "Create repository"

### Step 3: Upload Files
1. Click "uploading an existing file"
2. Drag ALL files from the `euphoric-wreckage-github` folder
3. Click "Commit changes"

### Step 4: Enable GitHub Pages
1. Click "Settings" tab
2. Click "Pages" in left sidebar
3. Under "Source" → select "main" branch
4. Click "Save"
5. Wait 2 minutes

### Step 5: Visit Your Site!
Your site will be at:
```
https://YOUR-USERNAME.github.io/euphoric-wreckage/
```

---

## Daily Updates (2 minutes)

### On GitHub.com:
1. Go to your repository
2. Click `content.json`
3. Click pencil icon (✏️ Edit)
4. Make your changes
5. Click "Commit changes"
6. Site updates automatically!

### What to change daily:
```json
"featuredTrack": {
    "number": "05",
    "title": "No Rhyme or Reason",
    "description": "New description here"
}
```

```json
"dailyQuote": {
    "text": "Your new quote",
    "author": "Vesper Sinclair"
}
```

Add news at TOP of news array:
```json
"news": [
    {
        "date": "2025-11-08",
        "title": "Your Title",
        "content": "Your content",
        "image": "Euphoric_Wreckage18.png"
    },
    // ... rest of news
]
```

---

## Need Help?

**JSON Validation:** Use https://jsonlint.com/ to check for errors

**File Names:**
- `index.html` - Your website
- `content.json` - Content you update daily
- `README.md` - Full documentation
- `CONTENT_IDEAS.md` - 30 days of ideas
- `validate_content.py` - Check for errors
- `auto_update.py` - Random daily content

**Common Issues:**
- Site not updating? Clear cache (Ctrl+Shift+R)
- JSON error? Check commas and quotes
- Image not showing? Check exact filename

---

## Optional: Automation

Run locally to generate random daily content:
```bash
python3 auto_update.py
```

Then commit the updated `content.json` to GitHub!

---

## Tips

✅ Update at the same time daily
✅ Keep news to 5-8 most recent items
✅ Rotate through all 12 tracks
✅ Mix quotes between all three characters
✅ Use `validate_content.py` before committing

---

**You're ready! Dance in the ruins. 🦀🌻⚡**
