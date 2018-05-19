import sys
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from com.inspectorio.extracting_excel.services import HandlingExcelFileService as hExcelService


@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def excecute_excel_file(request):
    if "GET" == request.method:
        return render(request, 'index.html', context=None)
    else:
        print('starting handling .....')
        excel_file = request.FILES["excel_file"]

        hExcelService.read_excel_file(excel_file)
        return render(request, 'index.html', context=None)