from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page open')
    return render(request, 'index.html')


def about(request):
    logger.info('About page open')
    return render(request, 'about.html')
