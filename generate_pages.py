import os

apps = {
    "itasbeeh": {
        "name": "iTasbeeh",
        "subtitle": "The Digital Zikr Counter",
        "icon": "appicon.png",
        "features": ["Recite and Tap.", "Handy and Easy to use", "Unlimited Tasbeeh.", "No Ads - 100% Free, 100% Offline."],
        "url": "https://apps.apple.com/us/app/id1534763309",
        "iap": False
    },
    "aqwal": {
        "name": "Aqwal",
        "subtitle": "Inspiring Islamic Quotes",
        "icon": "appicon.png",
        "features": ["Daily Wisdom.", "Beautiful Minimalist UI.", "Share with Friends.", "Works Offline."],
        "url": "#",
        "iap": False
    },
    "asmaulhusna": {
        "name": "Asma ul Husna",
        "subtitle": "99 Names of Allah",
        "icon": "appicon.png",
        "features": ["Full Meanings & Benefits.", "Beautiful Audio.", "Daily Reminder.", "Progress Tracking."],
        "url": "#",
        "iap": False
    },
    "asmaunnabi": {
        "name": "Asma un Nabi",
        "subtitle": "Names of the Prophet (PBUH)",
        "icon": "appicon.png",
        "features": ["Authentic Meanings.", "Elegant Typography.", "Lightweight & Fast.", "No Subscriptions."],
        "url": "#",
        "iap": False
    },
    "digipin": {
        "name": "Digipin India",
        "subtitle": "Post Office Finder",
        "icon": "appicon.png",
        "features": ["Find PIN codes instantly.", "Location based search.", "Official Data.", "Offline Support."],
        "url": "#",
        "iap": False
    },
    "llm": {
        "name": "LLM Leaderboard",
        "subtitle": "AI Model Comparisons",
        "icon": "appicon.png",
        "features": ["Latest Benchmark Scores.", "Compare Performance.", "Price Tracker.", "Open Source Models."],
        "url": "#",
        "iap": False
    },
    "meshly": {
        "name": "Meshly",
        "subtitle": "Private Local Network",
        "icon": "appicon.jpg",
        "features": ["Chat without Internet.", "Mesh Networking.", "End-to-End Encryption.", "Nearby Discovery."],
        "url": "#",
        "iap": True
    },
    "quoteswipe": {
        "name": "QuoteSwipe",
        "subtitle": "Find Your Inspiration",
        "icon": "appicon.png",
        "features": ["Swipe through thousands of quotes.", "Curate your favorites.", "Custom background designs.", "Export for Social Media."],
        "url": "#",
        "iap": True
    },
    "tt": {
        "name": "TimeTracking",
        "subtitle": "Focus & Productivity",
        "icon": "appicon.png",
        "features": ["Simple Task Timer.", "Visual Reports.", "Minimalist Interface.", "Privacy Focused."],
        "url": "#",
        "iap": False
    }
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} — AppMemar</title>
    <link rel="stylesheet" href="../site.css">
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <div class="logo"><a href="../index.html" style="text-decoration: none; color: inherit;">AppMemar</a></div>
            </nav>
        </div>
    </header>

    <main class="app-detail">
        <div class="container">
            <div class="detail-header">
                <img src="{icon}" alt="{name} Icon">
                <div class="detail-info">
                    <h1>{name}</h1>
                    <p class="subtitle">{subtitle}</p>
                </div>
            </div>

            {screenshot_html}

            <section class="features-list">
                <h2>Key Features</h2>
                <ul>
                    {features_html}
                </ul>
            </section>

            <div style="text-align: center; margin: 60px 0;">
                <a href="{url}" class="download-btn">Get it on the App Store</a>
            </div>

            <div class="secondary-links" style="justify-content: center;">
                <a href="privacy.html">Privacy Policy</a>
                <a href="mailto:iappmemar@gmail.com?subject={name} Support">Contact Support</a>
            </div>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2026 AppMemar. Built with purpose.</p>
        </div>
    </footer>
</body>
</html>
"""

privacy_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy - {name}</title>
    <link rel="stylesheet" href="../site.css">
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <div class="logo"><a href="../index.html" style="text-decoration: none; color: inherit;">AppMemar</a></div>
            </nav>
        </div>
    </header>

    <main class="container" style="padding: 40px 0;">
        <h1 style="font-size: 32px; margin-bottom: 24px;">Privacy Policy for {name}</h1>
        <p style="color: var(--text-sec); margin-bottom: 24px;">Last updated: February 15, 2026</p>

        <section style="margin-bottom: 32px;">
            <p>At AppMemar, we take your privacy seriously. This Privacy Policy describes how your personal information is collected, used, and shared when you use the {name} application.</p>
        </section>

        <section style="margin-bottom: 32px;">
            <h2 style="font-size: 20px; margin-bottom: 12px;">Information We Collect</h2>
            <p>The {name} app is designed to be privacy-first. It functions entirely offline and does not collect any personal data. We do not track your location, access your contacts, or upload your personal files to any servers.</p>
        </section>

        {iap_section}

        <section style="margin-bottom: 32px;">
            <h2 style="font-size: 20px; margin-bottom: 12px;">No Third-Party Sharing</h2>
            <p>We do not sell, trade, or otherwise transfer your personally identifiable information to outside parties.</p>
        </section>

        <section style="margin-bottom: 32px;">
            <h2 style="font-size: 20px; margin-bottom: 12px;">Changes</h2>
            <p>We may update this privacy policy from time to time in order to reflect, for example, changes to our practices or for other operational, legal or regulatory reasons.</p>
        </section>

        <section style="margin-bottom: 32px;">
            <h2 style="font-size: 20px; margin-bottom: 12px;">Contact Us</h2>
            <p>For more information about our privacy practices, if you have questions, please contact us by e‑mail at <a href="mailto:iappmemar@gmail.com">iappmemar@gmail.com</a>.</p>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2026 AppMemar. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

iap_privacy = """
        <section style="margin-bottom: 32px;">
            <h2 style="font-size: 20px; margin-bottom: 12px;">In-App Purchases</h2>
            <p>Transactions for In-App Purchases are handled entirely by Apple via the App Store. We do not collect or store any of your financial or payment information. We only receive confirmation from Apple when a purchase is successful to unlock your Pro features.</p>
        </section>
"""

def find_screenshot(folder):
    possibilities = ["app-screenshot.png", "app-screenshot.jpg", "detail.jpg", "detail.png", "leaderboard.jpg"]
    for p in possibilities:
        if os.path.exists(os.path.join(folder, p)):
            return p
    return None

for folder, data in apps.items():
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    features_html = "".join([f"<li>{f}</li>" for f in data["features"]])
    
    screenshot = find_screenshot(folder)
    if screenshot:
        screenshot_html = f'<div class="app-screenshot-container"><img src="{screenshot}" alt="{data["name"]} Screenshot"></div>'
    else:
        screenshot_html = ""
    
    # Generate index.html
    html = template.format(
        name=data["name"],
        subtitle=data["subtitle"],
        icon=data["icon"],
        screenshot_html=screenshot_html,
        features_html=features_html,
        url=data["url"]
    )
    with open(os.path.join(folder, "index.html"), "w") as f:
        f.write(html)
        
    # Generate privacy.html
    iap_section = iap_privacy if data["iap"] else ""
    privacy_html = privacy_template.format(name=data["name"], iap_section=iap_section)
    with open(os.path.join(folder, "privacy.html"), "w") as f:
        f.write(privacy_html)

print("Generated pages for all apps.")
