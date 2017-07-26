from structlog import get_logger
log = get_logger()
log = log.bind(user='anonymous', some_key=23)
log = log.bind(user='hynek', another_key=42)
log.info('user.logged_in', happy=True)