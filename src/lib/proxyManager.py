import logging

logger = logging.getLogger(__name__)
class ProxyManager:
    PROXY_HTTP = 0
    PROXY_SOCK4 = 1
    PROXY_SOCK5 = 2
    def __init__(self, ProxyType: int):
        self.ProxyType = ProxyType
    def FetchList(self):
        pass