# EUPHORIC WRECKAGE - Dynamic Website Guide

## 🎯 Quick Start for Daily Updates

Your website now updates automatically by editing just ONE file: `content.json`

### Daily Update Workflow (Takes 2 minutes!)

1. Go to your GitHub repository
2. Click on `content.json`
3. Click the pencil icon (Edit)
4. Make your changes
5. Click "Commit changes"
6. Your website updates automatically!

---

## 📝 How to Update Content

### Change the Featured Track
```json
"featuredTrack": {
    "number": "05",
    "title": "No Rhyme or Reason",
    "description": "A chaotic journey through unpredictable rhythms and haunting melodies."
}
```

### Change the Daily Quote
```json
"dailyQuote": {
    "text": "Build cathedrals from ashes.",
    "author": "Justin Sakurai"
}
```

### Change the Hero Video
```json
"heroVideo": "finnian_spotify_canvas.mp4"
```

Available videos:
- `scorpion_spotify_canvas.mp4`
- `finnian_spotify_canvas.mp4`
- `queen_wreckage_spotify_canvas.mp4`
- `e1b5cf17d6fe2efc8988550c11c17024.mp4`

### Add a New Blog Post/News Item

Add a new entry at the TOP of the news array:

```json
"news": [
    {
        "date": "2025-11-08",
        "title": "Your New Post Title",
        "content": "Your post content goes here. Keep it concise and engaging!",
        "image": "YourImageFile.png"
    },
    // ... existing news items follow
]
```

---

## 🚀 Setting Up GitHub Pages

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the **+** icon → **New repository**
3. Name it: `euphoric-wreckage-website` (or any name you want)
4. Keep it **Public**
5. Click **Create repository**

### Step 2: Upload Your Files

**Method A: Using GitHub Web Interface (Easiest)**

1. In your new repository, click **uploading an existing file**
2. Drag and drop ALL these files:
   - `index.html` (rename from `index-dynamic.html`)
   - `content.json`
   - All images (.png, .jpeg files)
   - All videos (.mp4 files)
3. Click **Commit changes**

**Method B: Using Git Command Line**

```bash
git clone https://github.com/YOUR-USERNAME/euphoric-wreckage-website.git
cd euphoric-wreckage-website
# Copy all your files here
git add .
git commit -m "Initial website upload"
git push
```

### Step 3: Enable GitHub Pages

1. Go to your repository **Settings**
2. Scroll down to **Pages** (in the left sidebar)
3. Under **Source**, select **main** branch
4. Click **Save**
5. Wait 1-2 minutes
6. Your site will be live at: `https://YOUR-USERNAME.github.io/euphoric-wreckage-website/`

### Step 4: (Optional) Add Custom Domain

1. Buy a domain (like `euphoricwreckage.com`)
2. In repository Settings → Pages → Custom domain
3. Enter your domain
4. Follow the DNS instructions provided

---

## 🎨 Content Ideas for Daily Updates

### Featured Track Rotation (12-day cycle)
Rotate through all your tracks, highlighting a different one each day with unique descriptions.

### Daily Quotes
Mix quotes from all three band members:
- Vesper: Fire and intensity
- Justin: Cool precision and wisdom
- Finnian: Warmth and connection

### News Post Ideas
- Behind-the-scenes content
- Track breakdowns
- Production insights
- Tour announcements (even fictional ones!)
- Fan interactions
- Merchandise updates
- Collaboration announcements
- Music video teasers
- Studio sessions
- Inspiration sources

---

## 🔧 Advanced: Automated Daily Updates

Want the site to update itself? Create a GitHub Action:

### Create `.github/workflows/daily-update.yml`:

```yaml
name: Daily Content Update
on:
  schedule:
    - cron: '0 0 * * *'  # Runs at midnight UTC daily
  workflow_dispatch:  # Allows manual trigger

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Update content
        run: |
          # Add your update script here
          # For example: rotate featured track, change quote, etc.
          
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add content.json
          git commit -m "Daily content update" || exit 0
          git push
```

---

## 📱 Tips for Mobile Editing

You can edit `content.json` from your phone!

1. Install **GitHub Mobile App**
2. Navigate to your repository
3. Open `content.json`
4. Tap the three dots → **Edit file**
5. Make changes
6. Commit!

---

## 🎯 Content Templates

### Template: New Music Announcement
```json
{
    "date": "2025-11-XX",
    "title": "New Track: [Track Name]",
    "content": "We're excited to share our latest creation. [Brief description]. Available now on all platforms.",
    "image": "EuphoricWreckageFrontStream.png"
}
```

### Template: Behind the Scenes
```json
{
    "date": "2025-11-XX",
    "title": "Studio Insights: Creating [Track Name]",
    "content": "A look into our creative process. [What inspired it, techniques used, interesting facts].",
    "image": "Euphoric_Wreckage18.png"
}
```

### Template: Band Member Spotlight
```json
{
    "date": "2025-11-XX",
    "title": "[Member Name] Spotlight",
    "content": "[Member's philosophy, approach to music, interesting fact]. The [fire/ice/earth] that drives our sound.",
    "image": "[MemberName].png"
}
```

---

## 🐛 Troubleshooting

**Website not updating after editing content.json?**
- Clear your browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Wait 1-2 minutes for GitHub Pages to rebuild
- Check for JSON syntax errors (missing commas, quotes)

**Images not showing?**
- Make sure filename in content.json exactly matches uploaded file
- Check that images are in the root directory
- Filenames are case-sensitive!

**JSON syntax errors?**
- Use [JSONLint](https://jsonlint.com/) to validate your JSON
- Make sure all strings are in quotes
- Don't forget commas between items (but not after the last item!)

---

## 📞 Need Help?

If something's not working, check:
1. Is the file name spelled correctly?
2. Did you save and commit your changes?
3. Are there any syntax errors in the JSON?

---

## 🎉 You're All Set!

Your dynamic Euphoric Wreckage website is ready to go. Update daily, keep it fresh, and let the world see your creative journey!

**Dance in the ruins. Build beauty from wreckage.** 🦀🌻⚡
