from rest_framework import viewsets, permissions, routers
from .models import Artist, Track, Playlist
from .serializers import ArtistSerializer, TrackSerializer, PlaylistSerializer
from rest_framework import filters

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fileds = ['name']


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'artist__name']
    

    def get_queryset(self):
        return Track.objects.select_related('artist').only('title', 'artist__name')

class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields= ['name', 'tracks__title', 'tracks__artist__name']
    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)\
                               .prefetch_related('tracks__artist')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


        