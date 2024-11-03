# events/views.py
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event, RSVP
from .serializers import EventSerializer, RSVPSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description','date_time','location']
    
    def perform_create(self, serializer):
        serializer.save(host=self.request.user)
    
    @action(detail=True, methods=['post'])
    def rsvp(self, request, pk=None):
        event = self.get_object()
        status = request.data.get('status')
        
        if not status:
            return Response(
                {'error': 'Status is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        rsvp, created = RSVP.objects.update_or_create(
            event=event,
            user=request.user,
            defaults={'status': status}
        )
        
        serializer = RSVPSerializer(rsvp)
        return Response(serializer.data)