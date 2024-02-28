from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = 25
    max_limit = 25
    limit_query_param = "limit"
