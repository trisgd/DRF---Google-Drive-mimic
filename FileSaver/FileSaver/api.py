from rest_framework import routers
from file_saver_app import views as app_view

router=routers.DefaultRouter()
router.register(r'files',app_view.FileUploadViewset)
