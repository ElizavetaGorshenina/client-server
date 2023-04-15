import logging

log = logging.getLogger('client')
handler = logging.FileHandler(filename='.\log\client.log', encoding='utf-8')
formatter = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)
