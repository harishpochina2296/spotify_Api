from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, TrackViewSet, PlaylistViewSet

router= DefaultRouter()
router.register('artist', ArtistViewSet, basename= 'artist')
router.register('track', TrackViewSet, basename= 'track')
router.register('playlists', PlaylistViewSet, basename= 'playlist')

urlpatterns = router.urls
