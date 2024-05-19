import os



class Config(object):
      BOT_TOKEN = os.environ.get("6733043530:AAHlbh-sA7AxyUxPguR5d92cYhURxUOFkWk", "")
      API_ID = int(os.environ.get("26112881", 12345))
      API_HASH = os.environ.get("8898fa823ffa1810ca10cc5c77417e85")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "AnurajRajsa")
