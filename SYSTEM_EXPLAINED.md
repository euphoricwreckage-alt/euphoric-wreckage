# HOW THE DYNAMIC SYSTEM WORKS

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR GITHUB REPOSITORY                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ All files stored here
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
   index.html           content.json          images/videos
   (The website)        (Daily updates)       (Media files)
        │                     │                     │
        └─────────────────────┴─────────────────────┘
                              │
                              │ GitHub Pages publishes
                              │
                              ▼
                    ┌──────────────────┐
                    │   LIVE WEBSITE   │
                    │  yoursite.com    │
                    └──────────────────┘
```

## The Magic: How Daily Updates Work

```
┌──────────────┐
│   YOU EDIT   │
│ content.json │  ← Change track, quote, news
└──────┬───────┘
       │
       │ Save changes on GitHub
       │
       ▼
┌──────────────────┐
│ GitHub rebuilds  │
│   your site      │  ← Takes 1-2 minutes
└──────┬───────────┘
       │
       │
       ▼
┌──────────────────┐
│  Website shows   │
│   new content!   │  ← Automatically!
└──────────────────┘
```

## What Gets Updated

```
content.json contains:
├── lastUpdated ────────► Date stamp (bottom right)
├── heroVideo ──────────► Background video on hero
├── featuredTrack ──────► Daily featured track section
│   ├── number
│   ├── title
│   └── description
├── dailyQuote ─────────► Quote section
│   ├── text
│   └── author
├── news ───────────────► News/blog posts (array)
│   └── Each item has:
│       ├── date
│       ├── title
│       ├── content
│       └── image
└── gallery ────────────► Gallery images (future use)
```

## Update Workflow

```
MANUAL UPDATES (Recommended)
1. Open GitHub in browser
2. Navigate to content.json
3. Click edit (✏️)
4. Make changes
5. Commit
6. Wait 1-2 minutes
7. Site is updated! ✅

AUTOMATED UPDATES (Optional)
1. Run: python3 auto_update.py
2. Commit the updated content.json
3. Push to GitHub
4. Site is updated! ✅
```

## File Structure on GitHub

```
your-repository/
├── index.html ───────────► Main website file
├── content.json ─────────► Your daily updates (EDIT THIS!)
├── README.md ────────────► Full documentation
├── QUICKSTART.md ────────► Quick setup guide
├── CONTENT_IDEAS.md ─────► 30 days of content ideas
├── WEEKLY_TEMPLATE.md ───► Template for planning
├── validate_content.py ──► Check for errors
├── auto_update.py ───────► Auto-generate content
│
├── Images:
│   ├── EuphoricWreckageFrontStream.png
│   ├── EuphoricWreckageLogoBreed.png
│   ├── Euphoric_Wreckage18.png
│   ├── Vesper13.png
│   ├── Justin10.png
│   ├── FinnianVesper2.png
│   └── [other images...]
│
└── Videos:
    ├── scorpion_spotify_canvas.mp4
    ├── finnian_spotify_canvas.mp4
    ├── queen_wreckage_spotify_canvas.mp4
    └── e1b5cf17d6fe2efc8988550c11c17024.mp4
```

## The Power of This System

✅ Update anywhere (computer, phone, tablet)
✅ No coding required for daily updates
✅ Free hosting with GitHub Pages
✅ Automatic HTTPS
✅ Fast global CDN
✅ Version history (undo mistakes!)
✅ Can add custom domain
✅ No databases needed
✅ Works offline (after first load)

## Why It's Better Than Traditional CMS

Traditional CMS (WordPress, etc.):
❌ Monthly hosting fees
❌ Security updates needed
❌ Database management
❌ Slower loading
❌ More complex

This System:
✅ Free forever
✅ No maintenance
✅ Super fast
✅ Edit one simple file
✅ Can't be hacked (static files)

---

Dance in the ruins. 🦀🌻⚡
