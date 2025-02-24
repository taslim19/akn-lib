# original pyrogram
# base AkenoX API & ErAPI # Itzpire API
from enum import Enum


class AutoName(Enum):
    def _generate_next_value_(self, *args):
        return self.lower()

    def __repr__(self):
        return f"akenoai.enums.{self}"
