from django.http import JsonResponse


def companies_list_view(request):
    return JsonResponse([
        {
            "name": "Company 1",
            "id": 1,
            "nameOfFounder": "Marcos Cardoso",
            "birthday": "2017-04-19",
        },
        {
            "name": "Company 2",
            "id": 2,
            "nameOfFounder": "Samuel Medeiros",
            "birthday": "2017-04-24",
        }
    ], safe=False)
