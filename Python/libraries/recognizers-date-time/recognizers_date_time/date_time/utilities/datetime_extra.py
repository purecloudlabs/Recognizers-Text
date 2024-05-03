from typing import Dict, List, Match


class DateTimeExtra:
    def __init__(self):
        self.data_type: any = None
        self.named_entity: Dict[str, List[str]] = dict()
        self.match: Match = None
