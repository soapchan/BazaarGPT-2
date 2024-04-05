
# BazaarGPT

## Introduction

BazaarGPT is a tool that uses AI to help people understand complex bazaar information more easily. It takes all the complicated numbers and makes them simple to understand, especially for beginners.
## Table of Contents

1. Usage
2. Introduction
3. Getting Started
4. Installation
5. Configuration
6. Features
7. Dependencies
8. Troubleshooting
9. License

## Features

- AI generated descriptions of the item's economy.
- Real-time data fetching from Hypixel Skyblock Bazaar.
- Detailed Markdown reports on item trends and statistics.
- Available API function for further 3rd party expansion.

## Getting Started

Obtain a Hypixel API key at https://developer.hypixel.net and an OpenAI API key at https://platform.openai.com/api-keys

## Installation

1. Ensure you have Python 3 installed on your system.
2. Download or clone this repository to your local machine.

## Configuration

1. Retrieve your 2 API keys.
2. Create a `.env` file in the `python` directory.
3. Add your Hypixel API and OpenAI API keys to the `.env` file in this format:
   ```
   HYPIXEL_KEY=your_api_key_here
    OPENAI_API_KEY=your_openAI_key_here
   ```
   Do not share your .env file with ANYONE.

## Usage

To start using BazaarGPT:

1. Run `run.bat` or execute the command:
   ```bash
   python main.py
   ```
2. Follow the on-screen prompts to select a model and item.
- the current available models are either `3.5` or `4`. Model `4` is overkill with the current setup.
3. The tool will fetch data and present a Markdown-formatted analysis of the selected item, aswell as the JSON output.

## Dependencies

- Python 3
- Requests: For making API calls.
- python-dotenv: For managing environment variables.

## Troubleshooting

- Ensure both the Hypixel API and the OpenAI API keys are correctly set in the `.env` file.
- If you encounter any issues with API connectivity, check your internet connection and API key validity.
- If issues continue, please contact me on my discord  `@soapchan`

## License

MIT License

Copyright (c) 2024 soapchan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

