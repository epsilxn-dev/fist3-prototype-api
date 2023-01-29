from collections import OrderedDict
import math
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Paginator(PageNumberPagination):
    page_query_param = "page"  # http://127.0.0.1:8000/.../?page=1 - по такому пути вернёт первую страницу
    max_page_size = 20  # максимум на странице может быть 20 элементов
    page_size = 15  # обычный размер страницы 15 элементов

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('pages', math.ceil(self.page.paginator.count / self.page_size)),
            ('items_per_page', self.page_size),
            ('current', self.page.number),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
