import logging

from django.conf import settings
from datetime import datetime

logging.basicConfig(filename="/logs.log",
                    level=logging.WARNING,
                    format="[%(asctime)s] [%(levelname)s]: %(message)s")


def add_error_log(error_filename: str, error: Exception, additional_info: dict = None):
    with open(settings.BASE_DIR / "logs.log", "a") as file:
        file.write(f"[ERR] [{error_filename}] [{datetime.now()}]: {error}\nINFO: "
                   f"{additional_info if additional_info is not None else '-'}\n{str(error.__traceback__)}\n")


def add_log(filename: str, message: str, *args, **kwargs):
    with open(settings / "logs.log", "a") as file:
        file.write(f"[INF] [{filename}] [{datetime.now()}]: {message}\nARGS: {args}\nKWARGS: {kwargs}\n")
