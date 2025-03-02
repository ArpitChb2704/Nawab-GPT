# NAWAB GPT - The Soul of Lucknow

Welcome to **NAWAB GPT**, your AI-powered guide to the heart of Lucknow! This web application provides insights into the city's culture, attractions, and food while also featuring an interactive chatbot to answer queries about Lucknow.

## Features

- 🌆 **Discover Lucknow**: Learn about the city's history, culture, and famous landmarks.
- 🍽️ **Explore Food Delights**: Know about iconic dishes like Tunday Kebab and Makhan Malai.
- 🤖 **Ask Nawab GPT**: An AI chatbot to answer your queries about Lucknow.
- 🎨 **Beautiful UI**: Frontend designed by Vaibhav Patel @vaibha-v7.
- 🚀 **Backend with Flask**: Implemented and deployed by Arpit Chhabra.

---

## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Deployment**: Render / Other hosting service

## Installation & Setup

To run this project locally, follow these steps:

### Prerequisites

- Python 3.x installed
- `pip` package manager

### Steps to Install

```bash
# Clone the repository
git clone https://github.com/your-username/nawab-gpt.git
cd nawab-gpt

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

---

## Deployment Instructions

### Using Render (or any cloud hosting)

1. Push your code to GitHub.
2. Connect the repository to **Render**.
3. Set the **Start Command** to:
   ```bash
   gunicorn app:app
   ```
4. Deploy and get your public URL!

---

## API Key Management

To keep your API keys safe:

- Store them in an `.env` file (DO NOT PUSH `.env` TO GIT!)
- Use environment variables in your Flask app:
  ```python
  import os
  api_key = os.getenv("API_KEY")
  ```

---

## Contributors

- **Arpit Chhabra** - Backend & Deployment
- **Vaibhav Patel** - Frontend Design

---


**Enjoy your virtual tour of Lucknow!** ✨

