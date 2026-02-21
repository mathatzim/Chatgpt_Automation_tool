# ChatGPT Automation Tool (Selenium)

A small Python + Selenium project that drives a real Chrome browser session to:
- open ChatGPT in the browser
- let you log in manually (and pass any verification)
- send a prompt
- save the conversation to a local file

## Important note (use responsibly)
Automating the ChatGPT *website UI* can be unreliable (UI changes break selectors) and may be restricted by platform terms.
For stable, compliant programmatic usage, consider using the **OpenAI API** instead:
- https://openai.com/policies/terms-of-use
- https://platform.openai.com/docs

## Features
- Chrome remote debugging profile support (optional)
- Manual login checkpoint (no bypassing verification)
- Prompt send + export conversation text

## Requirements
- Python 3.9+
- Google Chrome
- ChromeDriver that matches your Chrome version
- Selenium

## Install
```bash
pip install -r requirements.txt

## Run
python app.py --prompt "Write a short summary of what PCA does."
