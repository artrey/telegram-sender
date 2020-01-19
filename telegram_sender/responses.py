from django.http import JsonResponse


def base_response(data: dict, *args, **kwargs):
    return JsonResponse(data, *args, **kwargs)


def valid_response(data: dict, *args, **kwargs):
    data['result'] = True
    return base_response(data, *args, **kwargs)


def invalid_response(data: dict, *args, **kwargs):
    data['result'] = False
    return base_response(data, *args, **kwargs)
