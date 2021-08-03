class config:
    BOT_TOKEN = "1837774262:AAEDDICI3Dviim2FT6nHLHVxfvdXW0GW0iI"
    APP_ID = "6277451"
    API_HASH = "401f66ed51a03e2eeabb7f14d9d04b0d"
    DATABASE_URL = "postgres://hjpxmlqpqvjydw:f6334a3802eb2698589db10d8906e123967233e330865de10616cdb99adbc9f7@ec2-34-197-105-186.compute-1.amazonaws.com:5432/db4s7rhpchfntq"
    SUDO_USERS = "1821879869" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = "829735817774-nkqmlusgpimmt9fbn0q8388m3607c6d7.apps.googleusercontent.com"
    G_DRIVE_CLIENT_SECRET = "eVlLZnW9Mbs0DzgxPwOgSBEc"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**Hi  {}!**\n__I'm Google Drive Uploader Bot.I have been created by @adarshgoelo5 .You can use me to upload any file / video to Google Drive from direct link or Telegram Files.__\n__You can know more from /help. use /auth   to start the authorisation process__  "

    HELP_MSG = [
        ".",
        "**GOOGLE DRIVE ADARSH**\n__I can upload files from direct link or Telegram Files to your Google Drive. All you need is to authenticate me to use  your Google Drive Account and then send a direct download link or Telegram File.__\n\nI have more features... ! Wanna know about it ? Just walkthrough this tutorial and read the information carefully.",
        
        f"**Authenticating Google Drive**\n__Send the /{BotCommands.Authorize[0]} commmand and you will receive a URL, visit URL and follow the steps and send the received code here. Use /{BotCommands.Revoke[0]} to revoke your currently logged Google Drive Account.__\n\n**Note: I will not listen to any command or message (except /{BotCommands.Authorize[0]} command) until you authorize me.\nSo, Authorization is mandatory !**",
        
        f"**Direct Links**\n__Send me a direct download link for a file and i will download it on my server and Upload it to your Google Drive Account. You can rename files before uploading to GDrive Account. Just send me the URL and new filename separated by ' | '.__\n\n**__Examples:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n__To Upload telegram files in your Google drive Account just send me the file and i will download and upload it to your Google Drive Account. Note: Telegram Files Downloading are slow. it may take longer for big files.__\n\n**YouTube-DOWNLOADL Support**\n__Download files via youtube-downloader.\nUse /{BotCommands.YtDl[0]} (then read the instructions)__",
        
        f"**Custom Folder for Upload**\n__Want to upload in custom folder or in__ **TeamDrive** __ ?\nUse /{BotCommands.SetFolder[0]} (Folder URL) to set custom upload folder.\nAll the files are uploaded in the custom folder you provide.__",
        
        f"**Delete Google Drive Files**\n__Delete google drive files. Use /{BotCommands.Delete[0]} (File/Folder URL) to delete file or reply /{BotCommands.Delete[0]} to bot message.\nYou can also empty trash files use /{BotCommands.EmptyTrash[0]}\nNote: Files are deleted permanently. This process cannot be undone.\n\n**Copy Google Drive Files**\n__Yes, Clone or Copy Google Drive Files.\n__Use /{BotCommands.Clone[0]} (File id / Folder id or URL) to copy Google Drive Files in your Google Drive Account.__",
        
        "**Rules & Precautions**\n__1. Don't copy BIG Google Drive Files/Folders. It may hang the bot and your files maybe damaged.\n2. Send One request at a time unless bot will stop all processes.\n3. Don't send slow links .\n4. Don't misuse, overload or abuse this free service.NOTHING AHEAD NOW USE /auth TO AUTHORIZE ME __",
        
        # Dont remove this ↓ if you respect developer.
        "**Developed by @adarshgoelo5**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__User rate limit exceeded try after 24 hours.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder not found.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"
    
    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in valid format."
    
    COPIED_SUCCESSFULLY = "✅ **Copied successfully.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **You have not authenticated GDRIVE ADARSH to upload to your account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Uploading File...THANK YOU FOR USING GOOGLE DRIVE ADARSH BOT :)**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Uploaded Successfully.THANK YOU FOR USING GOOGLE DRIVE ADARSH BOT :)**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Downloader Failed**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Downloading File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__   **YOU MAY GET A MESSAGE THAT IT IS IS NOT SAFE GET BACK TO SAFETY SIMPLY CLICK ADVANCED  AND  THEN CLICK ON 'GO TO ADARSH G DRIVE(unsafe)'**"
    
    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder link set successfully.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Cleared Successfuly.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__The link you send its not belong to a folder.__"
    
    CLONING = "🗂️ **Cloning into Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**Trash Emptied Successfully !**"
    
    PROVIDE_YTDL_LINK = "❗**inorder to download a video follow these steps  first get the link to the video you want to download     and then open https://yt1s.com and paste the link  ,there you will get various options to download video choose the quality preffered and start   download         enjoy :).   **"
