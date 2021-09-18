from drf_yasg import openapi


def get_city_params():
    name = openapi.Parameter(
        "name", openapi.IN_QUERY, description="send city name", type=openapi.TYPE_STRING
    )

    return [name]


def get_routine_params():
    name = openapi.Parameter(
        "name", openapi.IN_QUERY, description="send city name", type=openapi.TYPE_STRING
    )

    return [name]


def get_min_price_params():
    price = openapi.Parameter(
        "price", openapi.IN_QUERY, description="price", type=openapi.TYPE_STRING
    )

    return [price]


def get_brand_params():
    name = openapi.Parameter(
        "name",
        openapi.IN_QUERY,
        description="send brand name",
        type=openapi.TYPE_STRING,
    )

    return [name]


def get_model_params():
    name = openapi.Parameter(
        "name",
        openapi.IN_QUERY,
        description="send model name",
        type=openapi.TYPE_STRING,
    )

    return [name]


def get_car_params():
    number = openapi.Parameter(
        "number",
        openapi.IN_QUERY,
        description="send car number ",
        type=openapi.TYPE_STRING,
    )

    return [number]
