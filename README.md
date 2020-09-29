# Bot-Generator-Seed

This is a repository to the discord bot ho generate standard and random settings seed.
It's used on my discord channel : https://discord.gg/psSGn45

## Installation

After cloning :
- Run `initialize.sh` script to initialize submodules and copy random settings generator inside rando and settings
- Go to settings and write inside `settings.sav.ran` and `settings.sav.std` the path for
    - rom : The aboslute path for your n64 rom
    - output_dir : The absolute path to ./files
    - distribution_file : Only for `settings.sav.ran`, the absolute path to ./ootrando/OoT-Randomizer/mystery-plando.json
- Create .env from .env.example and insert your Token and channel where the bot can answer, if there are multiple channel, you can seperate with comma
like `channel1,channel2,channel3`

## To use

Run `pip3 install -r requirements.txt` to install dependencies
Run `python3 main.py` to start bot

## On discord

The bot can answer to `!help` command