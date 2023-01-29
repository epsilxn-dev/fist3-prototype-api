from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.conf import settings

from core.exception import ClientException, ServerException
import logging

logging.basicConfig(filename=settings.BASE_DIR / "logs.log", level=logging.WARNING, format="[%(asctime)s] [%(levelname)s]: %(message)s")


def err_handler(err, cte):
    response = exception_handler(err, cte)
    if isinstance(err, ClientException) or isinstance(err, ServerException):
        if isinstance(err, ServerException):
            logging.error(err.message)
        if response is None:
            return Response({"errors": err.message}, status=err.resp_status)
        return response
    else:
        logging.critical(str(err))
        return response
