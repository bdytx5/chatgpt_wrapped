# ChatGPT Statistics Visualizer

![Example Visualization](https://github.com/bdytx5/chatgpt_wrapped/blob/main/conversation-stats.png?raw=true)

`python stats_visual.py "I apologize" "please forgive me" "thank you" "sorry" "kindly" "excuse me" "pardon me" "my apologies" "I regret" "with respect" "I deeply regret" "sincerely sorry"`


This Python script processes nested `conversations.json` files, analyzes word and phrase frequencies, calculates the total word count, and generates a Spotify Wrapped-style visualization of the results.

## Features

- Automatically discovers all `conversations.json` files in the current directory and its subdirectories.
- Calculates:
  - Total word count across all conversations.
  - Frequencies of specified words or phrases (e.g., "hello world").
- Exports results as a visually appealing image (`conversation_stats.png`).
- Simple command-line interface for ease of use.

## Installation

Clone the repository:

Install the required Python packages:

pip install matplotlib


place the script in the in the same directory as your unzipped chatgpt export folders 
