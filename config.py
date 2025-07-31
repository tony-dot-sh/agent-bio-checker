# config.py
PLATFORM_RULES = {
    "zillow.com": {"tag": "div", "class": "Text-c11n-8-65-2__sc-aiai24-0"},  # Update if needed
    "realtor.com": {"tag": "div", "class": "agent-about-section"},
    "homes.com": {"tag": "div", "class": "agent-profile__bio"},
    "yelp.com": {"tag": "p", "class": "css-1x8b1c0"},
    # Add more platforms here as needed
}
#TODO Update config.py with new CSS selectors for other platforms like:
#FastExpert
#UpNest
#Redfin