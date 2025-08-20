# custom_app

A custom Frappe application for real-time messaging and event broadcasting.

## Features
- Emit messages and show popups on Desk UI
- Broadcast events with message, action type, and optional user
- Docker-ready for Frappe v15

## Structure
```
custom_app/
├── custom_app/
│   ├── __init__.py
│   ├── hooks.py
│   ├── api/
│   ├── doctype/
│   ├── public/
│   ├── modules.txt
├── setup.py
├── MANIFEST.in
├── requirements.txt
├── README.md
```

## Usage
- Add your app to `apps.json` for Docker builds
- Use the provided API and JS methods for messaging
