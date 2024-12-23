import json
import urllib.request

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'python_module'))
from ffxiv_aku import *
with urllib.request.urlopen("https://raw.githubusercontent.com/Bodmass/ffxiv-sss/master/public/bossdata/data.json") as url:
    data = json.loads(url.read().decode())

translationsJobs = {
    "pld": "Paladin",
    "war": "Warrior",
    "drk": "DarkKnight",
    "gnb": "Gunbreaker",
    "whm": "Whitemage",
    "sch": "Scholar",
    "ast": "Astrologian",
    "sge": "Sage",
    "mnk": "Monk",
    "drg": "Dragoon",
    "nin": "Ninja",
    "sam": "Samurai",
    "rpr": "Reaper",
    "vpr": "Viper",
    "brd": "Bard",
    "mch": "Machinist",
    "dnc": "Dancer",
    "blm": "Blackmage",
    "smn": "Summoner",
    "rdm": "Redmage",
    "blu": "Bluemage",
    "pct": "Pictomancer",
}

translationsBoss = {
    "Basic": "Basic",
    # Heavensward
    "Gordias (Normal)": "Gordias",
    "Alex 1 (Savage)": "A1S",
    "Alex 2 (Savage)": "A2S",
    "Alex 3 (Savage)": "A3S",
    "Alex 4 (Savage)": "A4S",
    "Midas (Normal)": "Midas",
    "Alex 5 (Savage)": "A5S",
    "Alex 6 (Savage)": "A6S",
    "Alex 7 (Savage)": "A7S",
    "Alex 8 (Savage)": "A8S",
    "Creator (Normal)": "Creator",
    "Alex 9 (Savage)": "A9S",
    "Alex 10 (Savage)": "A10S",
    "Alex 11 (Savage)": "A11S",
    "Alex 12 (Savage)": "A12S",

    "Bismark (Extreme)": "Bismark EX",
    "Thordan (Extreme)": "Thordan EX",
    "Sephirot (Extreme)": "Sephirot EX",
    "Nidhogg (Extreme)": "Nidhogg EX",
    "Sophia (Extreme)": "Sophia EX",
    "Zurvan (Extreme)": "Zurvan EX",

    # Stormblood
    "Deltascape (Normal)": "Delta",
    "Deltascape V1.0 (Savage)": "O1S",
    "Deltascape V2.0 (Savage)": "O2S",
    "Deltascape V3.0 (Savage)": "O3S",
    "Deltascape V4.0 (Savage)": "O4S",
    "Sigmascape (Normal)": "Sigma",
    "Sigmascape V1.0 (Savage)": "O5S",
    "Sigmascape V2.0 (Savage)": "O6S",
    "Sigmascape V3.0 (Savage)": "O7S",
    "Sigmascape V4.0 (Savage)": "O8S",
    "Alphascape (Normal)": "Alpha",
    "Alphascape V1.0 (Savage)": "O9S",
    "Alphascape V2.0 (Savage)": "O10S",
    "Alphascape V3.0 (Savage)": "O11S",
    "Alphascape V4.0 (Savage)": "O12S",

    "Susano (Extreme)": "Susano EX",
    "Lakshmi (Extreme)": "Lakshmi EX",
    "Shinryu (Extreme)": "Shinryu EX",
    "Shinryu (Normal)": "Shinryu",
    "Byakko (Extreme)": "Byakko EX",
    "Tsukyomi (Extreme)": "Tsukyomi EX",
    "Suzaku (Extreme)": "Suzaku EX",
    "Seiryu (Extreme)": "Seiryu EX",

    # Shadowbringers
    "Eden's Gate (Normal)": "EdenErwachen",
    "Eden's Gate 1 (Savage)": "E1S",
    "Eden's Gate 2 (Savage)": "E2S",
    "Eden's Gate 3 (Savage)": "E3S",
    "Eden's Gate 4 (Savage)": "E4S",
    "Eden's Verse (Normal)": "EdenResonanz",
    "Eden's Verse 1 (Savage)": "E5S",
    "Eden's Verse 2 (Savage)": "E6S",
    "Eden's Verse 3 (Savage)": "E7S",
    "Eden's Verse 4 (Savage)": "E8S",
    "Eden's Promise": "EdenVerheißung",
    "Eden's Promise 1 (Savage)": "E9S",
    "Eden's Promise 2 (Savage)": "E10S",
    "Eden's Promise 3 (Savage)": "E11S",
    "Eden's Promise 4 (Savage)": "E12S",

    "Titania (Extreme)": "Titania EX",
    "Innocence (Extreme)": "Innozenz EX",
    "Hades (Normal)": "Hades EX",
    "Hades (Extreme)": "Hades EX",
    "The Ruby Weapon (Extreme)": "Ruby EX",
    "Warrior of Light (Extreme)": "WoL EX",
    "The Emerald Weapon (Extreme)": "Smaragd EX",
    "The Diamond Weapon (Extreme)": "Diamant EX",

    # Endwalker
    "Level 90 (i560 Synced)": "Level 90 (i560 Synced)",
    "Asphodelos (Normal)": "Asphodelos",
    "The First Circle (Savage)": "P1S",
    "The Second Circle (Savage)": "P2S",
    "The Third Circle (Savage)": "P3S",
    "The Fourth Circle (Savage)": "P4S",
    "Abyssos (Normal)": "Abyssos",
    "The Fifth Circle (Savage)": "P5S",
    "The Sixth Circle (Savage)": "P6S",
    "The Seventh Circle (Savage)": "P7S",
    "The Eigth Circle (Savage)": "P8S",
    "Anabaseios (Normal)": "Anabaseios",
    "The Ninth Circle (Savage)": "P9S",
    "The Tenth Circle (Savage)": "P10S",
    "The Eleventh Circle (Savage)": "P11S",
    "The Twelfth Circle (Savage)": "P12S",

    "Zodiark (Extreme)": "Zodiark EX",
    "Hydaelyn (Extreme)": "Hydaelyn EX",
    "The Final Day (Normal)": "Endsängerin",
    "Endsinger (Extreme)": "Endsängerin EX",
    "Barbariccia (Extreme)": "Barbarizia EX",
    "Rubicante (Extreme)": "Rubicante EX",
    "Golbez (Extreme)": "Golbez EX",
    "Zeromus (Extreme)": "Zeromus EX",

    # Dawntrail
    "Level 100 (i690 Synced)": "Level 100 (i690 Synced)",
    "AAC Light-heavyweight ": "Arkadion - Halbschwergewicht",
    "AAC Light-heavyweight M1 (Savage)": "M1S",
    "AAC Light-heavyweight M2 (Savage)": "M2S",
    "AAC Light-heavyweight M3 (Savage)": "M3S",
    "AAC Light-heavyweight M4 (Savage)": "M4S",

    "The Interphos": "Ewige Königin",
    "Worqor Lar Dor (Extreme) ": "Valigarmanda EX",
    "Everkeep (Extreme) ": "Zoraal Ja EX",

    "The Interphos (Extreme)": "Ewige Königin EX"
}

final = {}

for value in data["boss"]:
    try:
        translationsBoss[value['bossName']]
    except:
        print_color_red(f"ERROR add '{value['bossName']}' to the json")
        continue
    #print(value)
    for job in value['jobs']:
        bigJob = translationsJobs[job['job']]
        if not final.get(bigJob, None):
            final[bigJob] = {}
        final[bigJob][translationsBoss[value['bossName']]] = job['bossHp']

writeJsonFile("jobs_dps.json", final)
#print_pretty_json(final)
