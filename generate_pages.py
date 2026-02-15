import os

apps = {
    "itasbeeh": {
        "name": "iTasbeeh",
        "subtitle": "The Digital Zikr Counter",
        "icon": "appicon.png",
        "features": ["Recite and Tap.", "Handy and Easy to use", "Unlimited Tasbeeh.", "No Ads - 100% Free, 100% Offline."],
        "url": "https://apps.apple.com/us/app/id1534763309",
        "iap": False,
        "description": "A minimalist and beautiful digital Zikr counter (Tasbeeh) for iOS. Focus on your dhikr without ads or distractions.",
        "keywords": "itasbeeh, digital tasbeeh, zikr counter, dhikr app, islamic prayer counter, subha, tasbih",
        "category": "Utilities",
        "app_id": "1534763309"
    },
    "aqwal": {
        "name": "Aqwal",
        "subtitle": "Inspiring Islamic Quotes",
        "icon": "appicon.png",
        "features": ["Daily Wisdom.", "Beautiful Minimalist UI.", "Share with Friends.", "Works Offline."],
        "url": "#",
        "iap": False,
        "description": "Discover inspiring Islamic quotes and daily wisdom. Beautiful typography and easy sharing features.",
        "keywords": "aqwal, islamic quotes, daily wisdom, quran quotes, hadith quotes, inspiring quotes",
        "category": "Education"
    },
    "asmaulhusna": {
        "name": "Asma ul Husna",
        "subtitle": "99 Names of Allah",
        "icon": "appicon.png",
        "features": ["Full Meanings & Benefits.", "Beautiful Audio.", "Daily Reminder.", "Progress Tracking."],
        "url": "#",
        "iap": False,
        "description": "Learn and recite the 99 Names of Allah with meanings, benefits, and beautiful audio recitations.",
        "keywords": "asma ul husna, 99 names of allah, allah names app, islamic education, names of god",
        "category": "Education"
    },
    "asmaunnabi": {
        "name": "Asma un Nabi",
        "subtitle": "Names of the Prophet (PBUH)",
        "icon": "appicon.png",
        "features": ["Authentic Meanings.", "Elegant Typography.", "Lightweight & Fast.", "No Subscriptions."],
        "url": "#",
        "iap": False,
        "description": "A dedicated app for learning the names and attributes of Prophet Muhammad (PBUH) with authentic meanings.",
        "keywords": "asma un nabi, names of prophet, muhammad names, islamic apps, prophetic attributes",
        "category": "Education"
    },
    "digipin": {
        "name": "Digipin India",
        "subtitle": "Post Office Finder",
        "icon": "appicon.png",
        "features": ["Find PIN codes instantly.", "Location based search.", "Official Data.", "Offline Support."],
        "url": "#",
        "iap": False,
        "description": "The fastest way to find Indian Post Office PIN codes. Location-based search and offline support.",
        "keywords": "digipin, pin code india, post office finder, pincode search, india post app",
        "category": "Utilities"
    },
    "llm": {
        "name": "LLM Leaderboard",
        "subtitle": "AI Model Comparisons",
        "icon": "appicon.png",
        "features": ["Latest Benchmark Scores.", "Compare Performance.", "Price Tracker.", "Open Source Models."],
        "url": "#",
        "iap": False,
        "description": "Track and compare the latest AI Large Language Models (LLMs) by benchmarks, pricing, and performance.",
        "keywords": "llm leaderboard, ai benchmarks, model comparison, openai vs anthropic, ai price tracker",
        "category": "Developer Tools"
    },
    "meshly": {
        "name": "Meshly",
        "subtitle": "Private Local Network",
        "icon": "appicon.jpg",
        "features": ["Chat without Internet.", "Mesh Networking.", "End-to-End Encryption.", "Nearby Discovery."],
        "url": "#",
        "iap": True,
        "description": "Secure, internet-free communication using mesh networking. Chat with nearby users privately.",
        "keywords": "meshly, offline chat, no internet messaging, mesh network app, private nearby chat",
        "category": "Social Networking"
    },
    "quoteswipe": {
        "name": "QuoteSwipe",
        "subtitle": "Find Your Inspiration",
        "icon": "appicon.png",
        "features": ["Swipe through thousands of quotes.", "Curate your favorites.", "Custom background designs.", "Export for Social Media."],
        "url": "#",
        "iap": True,
        "description": "Swipe through thousands of curated quotes. Save your favorites and create beautiful social media posts.",
        "keywords": "quoteswipe, quote app, swiping quotes, daily inspiration, social media quote maker",
        "category": "Lifestyle"
    },
    "tt": {
        "name": "TimeTracking",
        "subtitle": "Focus & Productivity",
        "icon": "appicon.png",
        "features": ["Simple Task Timer.", "Visual Reports.", "Minimalist Interface.", "Privacy Focused."],
        "url": "#",
        "iap": False,
        "description": "A privacy-focused time tracking app for professionals and students. Simple, fast, and local-only.",
        "keywords": "time tracking, productivity app, focus timer, work log, privacy time tracker",
        "category": "Productivity"
    }
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} — {subtitle} | AppMemar</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="AppMemar">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://appmemar.in/{folder}/">
    <meta property="og:title" content="{name} — {subtitle}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://appmemar.in/{folder}/{icon}">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://appmemar.in/{folder}/">
    <meta property="twitter:title" content="{name} — {subtitle}">
    <meta property="twitter:description" content="{description}">
    <meta property="twitter:image" content="https://appmemar.in/{folder}/{icon}">

    <!-- Smart App Banner -->
    {app_banner}

    <link rel="stylesheet" href="../site.css">
    <link rel="canonical" href="https://appmemar.in/{folder}/">

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "{name}",
      "operatingSystem": "iOS",
      "applicationCategory": "{category}",
      "description": "{description}",
      "author": {{
        "@type": "Organization",
        "name": "AppMemar",
        "url": "https://appmemar.in"
      }},
      "offers": {{
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }}
    }}
    </script>
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <div class="logo"><a href="../index.html" style="text-decoration: none; color: inherit;">AppMemar</a></div>
                <div class="socials">
                    <a href="mailto:iappmemar@gmail.com">Support</a>
                    <a href="privacy.html">Privacy</a>
                </div>
            </nav>
        </div>
    </header>

    <main class="app-detail">
        <div class="container">
            <div class="detail-header">
                <img src="{icon}" alt="{name} App Icon - {subtitle}">
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
    <title>Privacy Policy - {name} | AppMemar</title>
    <meta name="description" content="Privacy Policy for {name} app by AppMemar. We value your privacy.">
    <meta name="robots" content="noindex">
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

sitemap_urls = ["https://appmemar.in/"]

for folder, data in apps.items():
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    features_html = "".join([f"<li>{f}</li>" for f in data["features"]])
    screenshot = find_screenshot(folder)
    screenshot_html = f'<div class="app-screenshot-container"><img src="{screenshot}" alt="{data["name"]} App Screenshot"></div>' if screenshot else ""
    app_banner = f'<meta name="apple-itunes-app" content="app-id={data["app_id"]}">' if "app_id" in data else ""
    
    # Generate index.html
    html = template.format(
        name=data["name"],
        subtitle=data["subtitle"],
        icon=data["icon"],
        screenshot_html=screenshot_html,
        features_html=features_html,
        url=data["url"],
        description=data["description"],
        keywords=data["keywords"],
        folder=folder,
        category=data.get("category", "Utilities"),
        app_banner=app_banner
    )
    with open(os.path.join(folder, "index.html"), "w") as f:
        f.write(html)
    
    sitemap_urls.append(f"https://appmemar.in/{folder}/")
        
    # Generate privacy.html
    iap_section = iap_privacy if data["iap"] else ""
    privacy_html = privacy_template.format(name=data["name"], iap_section=iap_section)
    with open(os.path.join(folder, "privacy.html"), "w") as f:
        f.write(privacy_html)

# Generate sitemap.xml
with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url in sitemap_urls:
        f.write(f'  <url><loc>{url}</loc></url>\n')
    f.write('</urlset>')

# Generate robots.txt
with open("robots.txt", "w") as f:
    f.write("User-agent: *\nAllow: /\nSitemap: https://appmemar.in/sitemap.xml")

print("Generated SEO-optimized pages, sitemap, and robots.txt.")
