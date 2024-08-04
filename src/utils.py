import uuid
from django.core.paginator import Paginator

from src.settings import paginator_num

def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code

def get_page_obj(obj, request):
    paginator = Paginator(obj, paginator_num)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)