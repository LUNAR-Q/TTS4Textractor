# TTS4Textractor
A Text-to-Speech plugin &amp; script for Textractor with multiple voices.

## Introduction

The project uses Textractor to read texts from games (e.g. visual novels), then speak them out with TTS services while identifying the speaker, achieving various goals.

E.g. While reading Japanese VNs, supplement the unvoiced text for a better experience.

TTS4Textractor.xdll - Tags text with speakers' name and outputs to clipboard.

TTS4Textractor.py - Reads the clipboard and handles TTS service.



## Functions

- Tagging texts as "P", "N", and "O"
  - P for protagonist (who is often unvoiced)
  - N for narration (which is also unvoiced)
  - O for others (not spoken, used to stop playback, avoiding overlapped voices)

- Allocating each tag with different voices
- Stop playback when another text is send
- Shortcuts for stopping and replaying

## Usage

Tested with [VOICEVOX](https://voicevox.hiroshiba.jp/) & [SAPI for VOICEVOX](https://github.com/shigobu/SAPIForVOICEVOX/releases).

1. Edit & compile the .dll and rename the extension to .xdll.

2. Install it to Textractor.
3. `pip install -r requirements.txt`
4. Edit & Run TTS4Textractor.py.

PS: The parameters and settings are in source files. More user-friendly configurations will be implemented (i guess).

## TO DO

- [ ] Further documentation
- [ ] GUI for the plugin
- [ ] Implement TTS into C++ to make a standalone plugin

