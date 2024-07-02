from materials.models import Category


def get_footer_menu(request):
    return {'chapters': Category.objects.all()}
