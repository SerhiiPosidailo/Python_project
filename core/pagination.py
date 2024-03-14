import math

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_pages = math.ceil(count / self.get_page_size(self.request))
        return Response({
            'total_items': count,
            'total_pages': total_pages,
            'next': bool(self.get_next_link()),
            'prev': bool(self.get_previous_link()),
            'deta': data
        }, status.HTTP_200_OK)