from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets

from apps.library.schema.schema_extension import ERROR_MESSAGES_FOR_PARTICIPATION_FOR_400
from apps.library.serializers.participation import ParticipationSerializer
from apps.library.utilities.export_to_google import export


@extend_schema(
    responses={
        201: ParticipationSerializer,
        400: ERROR_MESSAGES_FOR_PARTICIPATION_FOR_400,
    }
)
class ParticipationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ParticipationSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        export_success = export(instance)
        if export_success:
            instance.exported_to_google = True
            instance.save()
