# myapp/views.py

from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from User_auth.models import Document
from api.serializer.Task_serializers import DocumentSerializer
from django.http import HttpResponse, Http404

class DocumentUploadView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admins can upload files.")
        serializer.save(uploaded_by=self.request.user)
        
        
class DocumentDownloadView(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        document = self.get_object()
        if not document:
            raise Http404("File does not exist")

        file_path = document.file.path
        file_name = document.file.name.split('/')[-1]
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = f'attachment; filename={file_name}'
            return response
