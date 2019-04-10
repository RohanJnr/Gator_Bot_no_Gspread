import os


class Channels:
    announcements = 252596802497282048
    gator_swamp = 256653238286286848
    global_chomp = 251099476243120128
    elders = 254664901102927873
    elder_meeting_notes = 383452517499011072
    elder_war_notes = 414234128158818305
    bot_logs = 565408904092319775
    applications = 259392741627133952
    trials = 372524143876374530
    bot_setup = 256273702121897984


class Client:
    guild = 251099476243120128
    prefixes = ['.']
    token = os.environ.get('token')
    owner_id = 263560579770220554


class Roles:
    leader = 255419757895876608
    co_leader = 255403079669645312
    elder = 255409211385708546
    member = 255404616420687873
    trial = 256272488772665344