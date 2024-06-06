from enum import Enum

class Status(Enum):
    LIVE = 1       # 配信中
    COMPLETED = 2  # 配信済み
    UPCOMING = 3   # 配信予定

    def get_name(self) -> str:
        if self == Status.LIVE:
            return '配信中'
        elif self == Status.COMPLETED:
            return '配信済み'
        elif self == Status.UPCOMING:
            return '配信予定'
            
        