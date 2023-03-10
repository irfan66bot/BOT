import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """<i><b>π Helo {}, I'm <a href=https://telegram.me/{}>{}</a></i></b> \n\n<i><b>πI Can Provide You Any Movies, Web-Series, Anime, K-Dramas, Animation, etc.,</i></b>"""
    HELP_TXT = """<b>π₯ </b><b><u>How To Download Any Movie, Series, Anime etc., For Free???</u></b> \n\n<b>πGroup [01]: </b><b>https://t.me/+WzsvFY3qXa9kZGVl</b> \n\n<b>πGroup</b> <b>[02]: </b><b>https://t.me/+EdJU1Hqk1N80ZWQ1</b> \n\n<b>π</b> <b>Join Any Of The Above Groups</b>π"""
    ABOUT_TXT = """<i><u>π§Ά </u></i><i><u><b>Follow These Steps To Connect Me To Your Group</b>π</u>

1. Click on This [</i><a href="http://telegram.me/heroriderbot?startgroup=true"><i>Blue Text</i></a><i>]
2. Select Your Group
3. Make Me Admin in Your Group</i>"""    
    SOURCE_TXT = """<i><b><u>AutoFilter + UrlShortner Bot</u></b>

π Want An </i><i><b>'AutoFilter + UrlShortner Bot'</b> Like Me For Your Group &amp; Earn Money Using It?

π² </i><i><b>Contact Β»</b> </i><i>@DR_STARNGE</i>"""    
    MANUELFILTER_TXT = """Help: <b>FILTERS Β»</b>

Β» <b>Filter is A Feature Where Users can Set Automated Reply to a Specific Word</b>

<b>Important Notes:</b>
1.<i> I Have To Be Admin </i>
2.<i> Only admins can add Filters in Chat</i>
3.<i> Buttons have a limit of 64 Characters</i>

<b>Commands and Usage:</b>
β’ <i> /filter - Add a Filter</i>
β’ <i> /filters - List of All Filters</i>
β’ <i> /del - Delete a Filter</i>
β’ <i> /delall - Delete All Filters</i> """
    BUTTON_TXT = """Help: <b>BUTTONS Β»</b>

Β» Supports both url and alert inline buttons.

<b>NOTE:</b>
1. <i>Telegram will not allows you to send buttons without any content, so content is mandatory.</i>
2. <i>Supports buttons with any telegram media type</i>
3. <i>Buttons should be properly parsed as markdown format</i>

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/HeroRiderbot)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>AUTO FILTER Β»</b>

Add Me In Your Group as Admin & I Will Provide Any Movie, Series, Animation etc.,"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. <i>Only Admins Can Add Connection</i>
2. <i>Send <code>/connect</code> To Connect Me to Your PM</i>

<b>Commands and Usage:</b>
β’<i> /connect  - Connect a Chat to your PM</i>
β’<i> /disconnect  - Disconnect from a Chat</i>
β’<i> /connections - List Of All Connections</i>"""
    EXTRAMOD_TXT = """Help: <b>Extra Features of Me Β»</b>

<b>Commands and Usage:</b>
β’<i> /id - Get ID Of A User</i>
β’<i> /imdb  - Get Movie/Series Info from IMDb</i>"""
    ADMIN_TXT = """Help: <b>ADMIN MODS Β»</b>

<b>NOTE:</b>
This Works Only For Admins!

<b>Commands and Usage:</b>
β’<i> /stats - Get Status of DataBase</i>
β’<i> /delete - Delete A File</i>
β’<i> /users - List of My Users </i>
β’<i> /chats - Get List Of My Chats </i>
β’<i> /leave  - Leave from a chat</i>
β’<i> /disable  - Disable a Chat</i>
β’<i> /ban  - Ban a User</i>
β’<i> /unban  - Unban a User</i>
β’<i> /channel - List of All Connected Channels</i>
β’<i> /broadcast - Broadcast a Message to All Users</i>"""
    STATUS_TXT = """<b>ποΈ My Statistics π²</b>

β <b>Total Files :</b> {}
β <b>Total Users :</b> {}
β <b>Total Chats :</b> {}
β <b>Used Storage :</b> {} 
β <b>Free Storage :</b> {}"""

    LOG_TEXT_G = """<b>#NewGroup</b>
<b>Group Β»</b> {} (<code>{}</code>)
<b>Total Members Β»</b> <code>{}</code>
<b>Added By Β»</b> {}
"""
    LOG_TEXT_P = """<b>#NewUser</b>
β ID - <code>{}</code>
β Name - {}
"""
