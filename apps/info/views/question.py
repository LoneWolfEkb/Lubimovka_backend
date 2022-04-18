from django.conf import settings
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Setting
from apps.core.utils import send_email
from apps.info.models import Question
from apps.info.schema.schema_extension import ERROR_MESSAGES_FOR_QUESTION_FOR_400


class QuestionCreateAPIView(APIView):
    """Create Question."""

    class QuestionSerializer(serializers.ModelSerializer):
        sent = serializers.CharField(read_only=True)

        class Meta:
            model = Question
            fields = "__all__"

    @extend_schema(
        request=QuestionSerializer,
        responses={
            201: None,
            400: ERROR_MESSAGES_FOR_QUESTION_FOR_400,
        },
    )
    def post(self, request):
        serializer = self.QuestionSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            from_email = Setting.get_setting("email_send_from")
            to_emails = (Setting.get_setting("email_to_send_questions"),)
            template_id = settings.MAILJET_TEMPLATE_ID_QUESTION
            context = {
                "question": instance.question,
                "author_name": instance.author_name,
                "author_email": instance.author_email,
            }

            response_success = send_email(from_email, to_emails, template_id, context)

            if response_success:
                instance.sent = True
                instance.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
