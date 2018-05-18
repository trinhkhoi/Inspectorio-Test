import sys

from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from com.inspectorio.test.services import HandlingExcelFileService as hExcelService


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def excecute_exel_file(request):
    try:
        print('Start handling .... ')
        hExcelService.read_excel_file('/data/Sample 2.xlsx')
        return Response(status=status.HTTP_201_CREATED)
    except Exception as ex:
        sys.stderr(ex)
        return Response(ex.__cause__, status=status.HTTP_400_BAD_REQUEST)