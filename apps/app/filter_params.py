from drf_yasg import openapi



def get_city_params():
    name = openapi.Parameter("name", openapi.IN_QUERY, description='send city name', type=openapi.TYPE_STRING)


    return [name]