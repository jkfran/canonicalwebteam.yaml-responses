# Core
import os

# Packages
from django.conf.urls import url
from django.http import HttpResponse
from canonicalwebteam.yaml_responses.django_helpers import (
    create_redirect_views,
)


parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Add redirects
urlpatterns = create_redirect_views(path=f"{parent_dir}/redirects.yaml")

# Standard patterns
urlpatterns += [url("homepage", lambda request: HttpResponse("hello world"))]
