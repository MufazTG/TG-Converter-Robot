class Translation(object):


#This will be appeared when anyone use start command

      START = """Hello {0}

`I am a TG Converter bot with permanent thumbnail support.`

Press /settings to change my settings โ.

For More Details check Help ๐

Maintained By: [**สx สแดแดแดข ๐จโ๐ป**](https://t.me/BX_Botz)
"""


#This will be appeared when anyone use help command

      HELP = """**Hey you need help ๐ค ?**

1. Send me the telegram file or video which you wanted to convert.

2. Send me the thumbnail(photo) optional.

3. Reply to video /converttofile for converting into file.

4. Reply to file /converttovideo for converting into video.

**SUPPORT GROUP:** [BX Support](https://telegram.dog/BxSupport)
"""


#Please don't change this about command ๐

      ABOUT = """
**๐ Language:** Python 3

**๐งฐ Framework:** Pyrogram

**๐จโ๐ป Developer:** [แดสแด แดแด๊ฐแดแดข](https://t.me/Mufaz123)

**๐ฎ Channel:** [BX Bot Updates](https://t.me/Bx_Botz)

**๐ฅ Group:** [BX Bot Support](https://t.me/BxSupport)

**๐ป Source Code:**[Press Me](https://github.com/MufazTG/TG-Converter-Robot)

"""

####################################################################################################################################################
####################################################################################################################################################



#If you set the password for the bot if anyone use the bot without logging in this text will appear

      NOT_LOGGED_TEXT = """ This bot was a private bot you need to login using the password.
For logging in use command <code>/login BotPassword</code>. And then use me ๐ฅฐ"""


#This will be sent to the user when the user logged successfully

      SUCESS_LOGIN = """You are successfully logged in. So you can use me for today.
You access will be revoke by tomorrow"""


# This will be show when an user send wrong password

      WRONG_PWD = """This is a wrong password ๐ please try with correct password"""


# This will appear if the user is already logged

      EXISTING_USER = "You are already logged in you can use me"

####################################################################################################################################################
####################################################################################################################################################


#DON'T CHANGE THE NUMBERS IN THE FLOWER BRACKETS AND THE ORDER OF PERCENTAGE, DONE, TOTAL, SPEED, ETA ONLY CHANGE THE THEME 

      PROGRESS = """
Percentage : {0}%
Done โ: {1}
Total ๐: {2}
Speed ๐: {3}/s
ETA ๐ฐ: {4}
"""
       
      DOWNLOAD_PROGRESS = "โช๏ธ"
      UPLOAD_PROGRESS = "โซ๏ธ"

####################################################################################################################################################
####################################################################################################################################################



      DOWNLOAD_START = "Trying to Download ๐ฅ"
      DOWNLOAD_COMPLETE = "โ Media Downloaded successfully\nPreparing for upload"
      UPLOAD_START = "Trying to Upload ๐ค"
      UPLOAD_COMPLETE = "THANKS FOR USING ME"
      SAVED_CUSTOM_THUMB_NAIL = "โ Saved Thumbnail Successfully. This will be deleted in 24hrs"
      BANNED_TEXT = "YOU ARE BANNED. SO YOUR ARE NOT ABLE TO USE ME ๐"
      REPLY_TEXT = "๐ฉโโ๏ธ Reply to the media which you need to convert"
      DEL_ETED_CUSTOM_THUMB_NAIL = "Thumbnail Deleted Successfully โ"
