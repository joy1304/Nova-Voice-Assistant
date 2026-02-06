# Nova Voice Assistant

**Nova** is a lightweight, Python-based voice assistant designed to handle hands-free tasks through speech recognition and text-to-speech synthesis. It operates in a passive "listening" mode until it hears its wake word, at which point it becomes active to help you search the web, check the time, or look up information.



---

## Features

* **Wake Word Activation**: Stays idle until you say "Nova," saving processing power and ensuring privacy.
* **Web Searching**: Specialized commands to search for tutorials on **Edureka** or videos on **YouTube**.
* **Knowledge Base**: Pulls concise summaries directly from **Wikipedia**.
* **Time Reporting**: Get the current local time instantly.
* **Natural Feedback**: Uses `pyttsx3` for offline text-to-speech interaction.

---

## Prerequisites

Before running the script, you’ll need to install the following dependencies:

> **Note:** You must have **PyAudio** installed for the microphone to work. If you are on Windows, `pip install pyaudio` usually works. On Linux, you may need `sudo apt-get install python3-pyaudio`.

### Required Libraries
```bash
pip install speechrecognition pyttsx3 wikipedia
