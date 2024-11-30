"""
This script processes all `conversations.json` files nested in the current directory,
counts the total word count across all conversations, and calculates the frequency
of specific words or phrases passed as command-line arguments. It exports the results
as an image similar to Spotify Wrapped.

Usage:
    python stats_visual.py "fuck you" "hello world"
"""

import os
import json
import argparse
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt


def find_conversations_json():
    """
    Find all `conversations.json` files in the current directory and subdirectories.

    Returns:
        list: List of paths to `conversations.json` files.
    """
    json_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file == "conversations.json":
                json_files.append(os.path.join(root, file))
    return json_files


def extract_message_parts(message):
    """
    Extract the text parts from a message content.

    Args:
        message (dict): A message object.

    Returns:
        list: List of text parts.
    """
    content = message.get("content")
    if content and content.get("content_type") == "text":
        return content.get("parts", [])
    return []


def get_author_name(message):
    """
    Get the author name from a message.

    Args:
        message (dict): A message object.

    Returns:
        str: The author's role or a custom label.
    """
    author = message.get("author", {}).get("role", "")
    if author == "assistant":
        return "ChatGPT"
    elif author == "system":
        return "System"
    return author


def get_conversation_messages(conversation):
    """
    Extract messages from a conversation.

    Args:
        conversation (dict): A conversation object.

    Returns:
        list: List of messages with author and text.
    """
    messages = []
    current_node = conversation.get("current_node")
    mapping = conversation.get("mapping", {})
    while current_node:
        node = mapping.get(current_node, {})
        message = node.get("message") if node else None
        if message:
            parts = extract_message_parts(message)
            author = get_author_name(message)
            if parts:
                messages.append({"author": author, "text": parts[0]})
        current_node = node.get("parent") if node else None
    return messages[::-1]


def process_conversations(json_files, target_phrases):
    """
    Process all conversations from the list of JSON files and count word/phrase frequencies.

    Args:
        json_files (list): List of paths to `conversations.json` files.
        target_phrases (list): List of words/phrases to count frequencies for.

    Returns:
        tuple: Total word count and frequencies of target phrases.
    """
    total_word_count = 0
    phrase_counter = Counter()

    for file in json_files:
        print(f"Processing file: {file}")
        with open(file, "r", encoding="utf-8") as f:
            conversations = json.load(f)
            for conversation in conversations:
                messages = get_conversation_messages(conversation)
                for message in messages:
                    text = message["text"].lower()
                    words = text.split()
                    total_word_count += len(words)

                    # Count occurrences of each phrase
                    for phrase in target_phrases:
                        phrase_counter[phrase] += text.count(phrase.lower())

    return total_word_count, phrase_counter


def create_visual(total_word_count, phrase_counter):
    """
    Create a visual representation of the results.

    Args:
        total_word_count (int): Total word count.
        phrase_counter (Counter): Frequency of phrases.
    """
    phrases = list(phrase_counter.keys())
    counts = list(phrase_counter.values())

    # Create a bar chart
    plt.figure(figsize=(12, 8))
    plt.barh(phrases, counts, color="purple")
    plt.xlabel("Frequency", fontsize=14)
    plt.ylabel("Phrases", fontsize=14)
    plt.title(f"Conversation Statistics\nTotal Word Count: {total_word_count}", fontsize=16)
    plt.tight_layout()

    # Annotate bars
    for index, value in enumerate(counts):
        plt.text(value, index, str(value), va="center", ha="left", fontsize=12)

    # Save the visualization as an image
    output_path = "conversation_stats.png"
    plt.savefig(output_path)
    plt.close()
    print(f"Visualization saved as {output_path}")


def main():
    """
    Main function to parse arguments and process conversations.
    """
    parser = argparse.ArgumentParser(
        description="Process all conversations.json files and create a visual representation of statistics."
    )
    parser.add_argument(
        "phrases",
        nargs="+",
        help='List of words/phrases to calculate frequencies for. Example:  "hello world"',
    )
    args = parser.parse_args()

    # Find all `conversations.json` files
    json_files = find_conversations_json()

    if not json_files:
        print("No `conversations.json` files found.")
        return

    # Process conversations and calculate word/phrase frequencies
    total_word_count, phrase_counter = process_conversations(json_files, args.phrases)

    # Create a visual representation
    create_visual(total_word_count, phrase_counter)


if __name__ == "__main__":
    main()

