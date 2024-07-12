# Channel Exemption Clear Bot

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Running the Bot](#running-the-bot)
7. [Credits](#credits)

## Introduction
Channel Exemption Clear Bot is an IRC bot designed to clear all exemptions in the channel it is in. To use this feature, the bot must have 'op' permissions, and you simply need to send the bot a message with the word 'clear'.

## Features
- Joins specified IRC channel and listens for the 'clear' command.
- Removes all channel exemption and invite exemption modes.
- Sends confirmation message to the user who issued the command.

## Requirements
- Python 3.x
- `irc` library for Python
- `jaraco.stream` library for Python

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/chanclear-bot.git
    cd chanclear-bot
    ```

2. **Install required packages using pip:**
    ```sh
    pip3 install irc jaraco.stream
    ```

## Usage
- **Join the bot to the IRC channel:**
  Configure the server, port, channel, and bot nickname in the `main()` function.

- **Issue the 'clear' command:**
  Send a private message with the word `clear` to the bot to trigger the clearing of exemptions.

## Running the Bot
To run the bot using `screen`:

1. **Start a new screen session:**
    ```sh
    screen -S chanclear-bot
    ```

2. **Run the bot:**
    ```sh
    python3 chanclear.py
    ```

3. **Detach from the screen session:**
    Press `Ctrl-A` then `D`

4. **To reattach to the screen session:**
    ```sh
    screen -r chanclear-bot
    ```

## Credits
Made by gh0st

Visit us at IRC.TWISTEDNET.ORG channels #TWISTED & #DEV
