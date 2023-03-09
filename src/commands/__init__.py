# ********************************************************************* #
#          .-.                                                          #
#    __   /   \   __                                                    #
#   (  `'.\   /.'`  )   DisMaid - __init__.py                           #
#    '-._.(;;;)._.-'                                                    #
#    .-'  ,`"`,  '-.                                                    #
#   (__.-'/   \'-.__)   BY: Rosie (https://github.com/BlankRose)        #
#       //\   /         Last Updated: Thu Mar  9 14:42:35 CET 2023      #
#      ||  '-'                                                          #
# ********************************************************************* #

from src.utils.construct import import_entries
from src.commands import help

import src.commands.messages as msg

__all__ = ["random", "mute", "unmute", "debug"]
__all__.append("help")

categories: list = ["messages"]
sub_entries = import_entries(categories, "src.commands")

entries = import_entries(__all__, "src.commands")

a = {k: v for d in (entries, msg.entries) for k, v in d.items()}
entries = {**entries, **msg.entries}