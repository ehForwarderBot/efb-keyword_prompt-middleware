import pathlib
import shelve
import atexit
import uuid
from collections.abc import Mapping
from threading import Timer
from typing import Optional, Union, Dict
from typing_extensions import overload, Literal

from ruamel.yaml import YAML

from ehforwarderbot import Middleware, Message, Status, coordinator, utils
from ehforwarderbot.chat import Chat, SystemChat, GroupChat
from ehforwarderbot.types import ModuleID, MessageID, InstanceID, ChatID
from ehforwarderbot.message import MsgType, MessageCommands, MessageCommand, Substitutions
from ehforwarderbot.status import MessageRemoval, ReactToMessage, MessageReactionsUpdate


class KeywordPromptMiddleware(Middleware):
    """
    """
    middleware_id: ModuleID = ModuleID("blueness.KeywordPromptMiddleware")
    middleware_name: str = "Keyword Prompt Middleware"
    __version__: str = '0.0.1'

    keywords = ['收到红包，请在手机上查看',
               '收到紅包，請在手機上查看',
               '收到利是，請在手機上查看',
               'Red packet received. View on phone.']

    def __init__(self, instance_id: Optional[InstanceID] = None):
        super().__init__(instance_id)

    def process_message(self, message: Message) -> Optional[Message]:
        if message.type == MsgType.Text and \
            message.author.module_id.startswith("blueset.wechat") and \
            type(message.chat) == GroupChat and \
            self.match_list(message.text):
            
            x:int = 0
            message.text = "@ME " + message.text
            message.substitutions = Substitutions({})
            message.substitutions[(x, x+3)] = message.chat

        return message
    
    
    def match_list(self, text) -> bool:
        """
        关键字的匹配，主要匹配keywords的列表
        """
        for i in self.keywords:
            if text.find(i) != -1:
                return True
        return False
        
