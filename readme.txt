# Conversation Statistics Visualizer

This Python script processes nested `conversations.json` files, analyzes word and phrase frequencies, calculates the total word count, and generates a Spotify Wrapped-style visualization of the results.

## Features

- Automatically discovers all `conversations.json` files in the current directory and its subdirectories.
- Calculates:
  - Total word count across all conversations.
  - Frequencies of specified words or phrases (e.g., "hello world", "fuck you").
- Exports results as a visually appealing image (`conversation_stats.png`).
- Simple command-line interface for ease of use.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/conversation-stats-visualizer.git
cd conversation-stats-visualizer

Install the required Python packages:

pip install matplotlib

Usage

Run the script with the words or phrases you want to analyze as arguments:

python stats_visual.py "word1" "phrase1" "phrase2"




Your directory should look like this:

project/
├── stats_visual.py
├── conversation_stats.png  # Generated output
├── byyoung3_export_aug_24/
│   ├── conversations.json
│   └── ...
