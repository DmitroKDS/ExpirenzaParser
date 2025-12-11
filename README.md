# ExpirenzaParser

This app is a helper tool that automatically checks the Expirenza app — a popular Ukrainian platform where people can buy secret boxes with food.

Normally, users have to constantly refresh the app to see whether new boxes appear, because the good ones sell out extremely fast.

## 🧠 What the tool does for you

This program watches the app for you. It keeps scrolling through the list of boxes and looking for new items that are available (not sold out).

If a new interesting box appears — for example, one that contains “Milk Bar” or “Namelaka” cafes — the tool immediately sends you a notification.

So instead of checking the app every 10 minutes, the script does it automatically in the background.

## 🎯 Why I created this
	•	To never miss rare boxes that appear for just a few seconds.
	•	To avoid spending time manually checking Expirenza over and over.
	•	To get instant alerts when something good is available.
	•	To help resellers, collectors, or fans who want to catch special drops.

## Use

The tool:
	1.	Opens the Expirenza app.
	2.	Reads what’s on the screen.
	3.	Scrolls through the list of boxes.
	4.	Notices when something new appears.
	5.	Sends a notification immediately.

### Setup
`pip install -r requirements.txt`

### Run
`python main.py`
