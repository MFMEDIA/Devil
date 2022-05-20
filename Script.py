class script(object):
    START_TXT = """ Hᴇʟʟᴏ {},
<b>I ᴀᴍ <a href=https://t.me/{}>{}</a>, or you can call me as EvaMaria Bot.Its easy to use me; just add me to your group as admin, thats all, i will provide movies there.</b>"""

    HELP_TXT = """𝙷𝙴𝚈 {}
Hᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs."""
    ABOUT_TXT = """✯ Mʏ ɴᴀᴍᴇ: {}
✯ Cʀᴇᴀᴛᴏʀ: <a href=https://t.me/HRIDESH_TG>Hʀɪᴅᴇsʜ ᴛɢ</a>
✯ ʟɪʙʀᴀʀʏ: Pʏʀᴏɢʀᴀᴍ
✯ Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3
✯ Dᴀᴛᴀ ʙᴀsᴇ: Mᴀɴɢᴏ ᴅʙ
✯ Bᴏᴛ sᴇʀᴠᴇʀ: Rᴀɪʟᴡᴀʏ
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v1.0.1 [ ʙᴇᴛᴀ]"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>നിങ്ങളുടെ മാത്രമായി ഒരു സിനിമ ഗ്രൂപ്പ് തുടങ്ങാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നുണ്ടോ? നിങ്ങളുടെ അടുത്ത കൂട്ടുകാർക്ക് മാത്രം, അല്ലെങ്കിൽ നിങ്ങളുടെ Family and Relatives മാത്രമായി, അതുമല്ലെങ്കിൽ മറ്റുള്ളവർക്ക് വേണ്ടി, സിനിമ നിങ്ങൾക്ക് ഒരു ബുദ്ധിമുട്ടും കൂടാതെ മറ്റുള്ളവർക്ക് ഗ്രൂപ്പ് വഴി നൽകാം,നമ്മുടെ " Lɪsᴀ ◢ ◤ ബോട്ട് @Lisa_FZ_Bot " ഇപ്പോൾ പൂർണമായും മറ്റുള്ളവർക്കും ഉപയോഗിക്കാവുന്ന രീതിയിലേക്ക് മാറ്റിയിരിക്കുക ആണ് നിങ്ങളുടെ ഗ്രൂപ്പിൽ admin ആയി @Lisa_FZ_Bot നെ add ചെയ്താൽ മതി, നിങ്ങൾ സിനിമയുടെ spelling തെറ്റുകൂടാതെ അയച്ചാൽ മാത്രം മതി, സിനിമ ബോട്ട് തരും.</b> 

<b>Dᴇᴠs</b>
- <a href=https://t.me/HRIDESH_TG>Hʀɪᴅᴇsʜ Tɢ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝐓𝐨𝐥𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: <code>{}</code>
★ 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: <code>{}</code>
★ 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐚𝐭𝐬: <code>{}</code>
★ 𝐔𝐬𝐞𝐝 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: <code>{}</code> 𝕄𝔹
★ 𝐅𝐫𝐞𝐞 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: <code>{}</code> 𝕄𝔹"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
