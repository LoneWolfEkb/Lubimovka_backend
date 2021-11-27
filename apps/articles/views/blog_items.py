from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.articles.filters import PubDateFilter
from apps.articles.mixins import PubDateSchema
from apps.articles.models import BlogItem
from apps.articles.serializers import (
    BlogItemDetailedSerializer,
    BlogItemListSerializer,
)


class BlogItemsViewSet(PubDateSchema, ReadOnlyModelViewSet):
    queryset = BlogItem.objects.all()
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_filters.OrderingFilter,
    )
    filterset_class = PubDateFilter
    ordering_fields = (
        "pub_date__year",
        "pub_date__month",
    )

    def get_serializer_class(self):
        if self.action == "list":
            return BlogItemListSerializer
        return BlogItemDetailedSerializer

    class Meta:
        model = BlogItem
