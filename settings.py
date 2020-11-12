import os
def setsettings(ROMPATH, OUTPATH, custom=None):
    open("settings/settings.sav", "w").write("")
    numberlines = 0
    if custom == "import":
        settingfile = open("settings/settings.sav.import", "r")
    else:
        settingfile = open("settings/settings.sav.default", "r")
    settingswrite = open("settings/settings.sav", "r+")
    for i in settingfile.readlines():
        if numberlines == 1:
            settingswrite.write(f'    "rom": "{ROMPATH}",\n')
        elif numberlines == 2:
            settingswrite.write(f'    "output_dir": "{OUTPATH}",\n')
        elif numberlines == 3:
            if custom == "random":
                settingswrite.write(f'    "enable_distribution_file": true,\n')
            else:
                settingswrite.write(f'    "enable_distribution_file": false,\n')
        elif numberlines == 4:
            if custom == "random":
                plandorandompath = os.path.abspath("OoT-Randomizer/plando-random-settings/blind_random_settings.json")
                settingswrite.write(f'    "distribution_file": "{plandorandompath}",\n')
            else:
                settingswrite.write(i)
        else:
            settingswrite.write(i)
        numberlines = numberlines+1
    os.replace("settings/settings.sav", "OoT-Randomizer/settings.sav")
