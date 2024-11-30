# ChatGPT Statistics Visualizer

![Example Visualization](https://github.com/bdytx5/chatgpt_wrapped/blob/main/conversation-stats.png?raw=true)


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


Install the required Python packages:

pip install matplotlib

Usage
Here's the corrected Markdown format for your directory structure:

Your directory should look like this:

project/ ├── stats_visual.py ├── conversation_stats.png # Generated output ├── byyoung3_export_aug_24/ │ ├── conversations.json │ └── ...
