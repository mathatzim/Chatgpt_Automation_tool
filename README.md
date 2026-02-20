# ChatGPT Automation Tool (Selenium)

Python + Selenium helper that attaches to a Chrome session and lets you:
- Open ChatGPT in a real browser
- Manually log in / complete verification
- Send prompts
- Export the conversation to a text file

Compliance note: OpenAI’s Terms of Use prohibit “automatically or programmatically extract[ing] data or Output” from the Services. For programmatic use, prefer the official OpenAI API instead of automating the ChatGPT web UI. :contentReference[oaicite:2]{index=2}

## Features
- Remote debugging Chrome launch
- Manual “human verification” checkpoint
- Prompt sending + conversation export

## Requirements
- Python 3.9+
- Google Chrome installed
- ChromeDriver that matches your Chrome version
- Selenium

## Install
Create `requirements.txt` (see below) and then:
```bash
pip install -r requirements.txt
