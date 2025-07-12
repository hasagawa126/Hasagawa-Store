from telethon import Button
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/d70af44b1ce6daaeda9c8-38d69240bf4233c55a.jpg",
                caption="𝗛𝗮𝘀𝗮𝗴𝗮𝘄𝗮-𝗦𝘁𝗼𝗿𝗲.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Store", "https://t.me/HasagawaStoree")),
                         (Button.url("Owner", "https://t.me/heycaa25"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None
