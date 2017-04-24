from django.http import JsonResponse


def companies_list_view(request):
    return JsonResponse([
        {
            "name": "Company 1",
            "id": 1,
            "birthday": "2017-04-19"
        },
        {
            "name": "Company 2",
            "id": 2,
            "birthday": "2017-04-20"
        }
    ], safe=False)
