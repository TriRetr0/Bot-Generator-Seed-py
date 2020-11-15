# Bot-Generator-Seed

This is a repository to the discord bot ho generate standard and random settings seed.
It's used on my discord channel : [Join](https://discord.gg/psSGn45)

## Installation

After cloning :
- Run `initialize.sh` script to initialize submodules and copy random settings generator inside rando and settings
- Create .env from .env.example and insert your Token, ~~channelid where the bot can answer~~ (REPLACED), rom path and output path (need to be empty or it will send and delete your files).

## To use

Run `pip3 install -r requirements.txt` to install dependencies
Run `python3 main.py` to start bot

## On discord

First you need to link a channel:
```
!set_channel (#your channel)
```
Then, the bot can answer to `!help` command

## NEW!

### ChannelID in .env is replace by !set_channel

Can be used in multiple servers in the same time

Import a settings file with attachements or url `!generate import url` or `!generate` if you upload a settings file
Fixing some bugs

Generation logs now given after generation and can tell you if the generation contain errors

Color status :
```
Red = Fatal error during generation
Yellow = May be unbeatable
Blue = Still Ok
Green = No errors
Grey = No spoil/No logs
```

Of course, it can spoil... So I add a new opt:
```
!generate [Settings] [N/A, SString or a url] [Something different than "True" will activate "no logs spoils" opt]
Example: !generate random N/A f
Another: !generate custom aSString false
Another one: !generate import https://some.url/to/a/file true
```
