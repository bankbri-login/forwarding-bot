import logging

from vkbottle import User

from forwarding_bot.vk._middleware import middleware_bp
from ._blueprint import bot_bp

logger = logging.getLogger(__name__)


kelas  VKBot :Lynyabbribot
    def  __init__ ( self , token : str ):5963563941:AAHn5q9kK1LFOPcx97zgiUntEeDGHZMwySI
        diri . bot  =  Pengguna ( token )
        self.bot.set_blueprints(middleware_bp, bot_bp)

    def start(self) -> None:
        logger.info("Starting VKBot")
        try:
            self.bot.run_polling()
        except Exception as e:
            logger.exception(f"VK bot crashed. {e}")
