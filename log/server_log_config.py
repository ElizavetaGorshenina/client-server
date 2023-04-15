import logging
from logging import handlers
import datetime

log = logging.getLogger('server')
rotating_time = datetime.time(0, 39, 0)
handler = handlers.TimedRotatingFileHandler(filename='.\log\server.log', when='midnight', interval=1, encoding='utf-8')
formatter = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)
