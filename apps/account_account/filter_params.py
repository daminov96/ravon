from drf_yasg import openapi


def get_user_params():
    query = openapi.Parameter(
        "query",
        openapi.IN_QUERY,
        description="Query for search",
        type=openapi.TYPE_STRING,
    )
    group_id = openapi.Parameter(
        "group_id", openapi.IN_QUERY, description="group_id ", type=openapi.TYPE_INTEGER
    )
    not_in_group_id = openapi.Parameter(
        "not_in_group_id",
        openapi.IN_QUERY,
        description="not_in_group_id ",
        type=openapi.TYPE_INTEGER,
    )
    center_id = openapi.Parameter(
        "center_id",
        openapi.IN_QUERY,
        description="center_id ",
        type=openapi.TYPE_INTEGER,
    )
    parent_id = openapi.Parameter(
        "parent_id",
        openapi.IN_QUERY,
        description="Parent ning farzandlari royxatini olish uchun",
        type=openapi.TYPE_INTEGER,
    )
    is_verified = openapi.Parameter(
        "is_verified",
        openapi.IN_QUERY,
        description="is_verified ",
        type=openapi.TYPE_BOOLEAN,
    )
    not_verified = openapi.Parameter(
        "not_verified",
        openapi.IN_QUERY,
        description="not_verified ",
        type=openapi.TYPE_BOOLEAN,
    )
    return [
        parent_id,
        query,
        group_id,
        center_id,
        not_in_group_id,
        is_verified,
        not_verified,
    ]


def get_cashelok_params():
    owner_id = openapi.Parameter(
        "owner_id", openapi.IN_QUERY, description="owner_id ", type=openapi.TYPE_INTEGER
    )
    return [owner_id]


def get_cashelokfill_params():
    owner_id = openapi.Parameter(
        "owner_id", openapi.IN_QUERY, description="owner_id ", type=openapi.TYPE_INTEGER
    )
    return [owner_id]


def get_followers_params():
    user_id = openapi.Parameter(
        "user_id", openapi.IN_QUERY, description="user_id ", type=openapi.TYPE_INTEGER
    )
    query = openapi.Parameter(
        "query",
        openapi.IN_QUERY,
        description="Query for search",
        type=openapi.TYPE_STRING,
    )
    return [user_id, query]


def get_follow_connection_params():
    owner_id = openapi.Parameter(
        "owner_id", openapi.IN_QUERY, description="owner_id ", type=openapi.TYPE_INTEGER
    )
    return [owner_id]


def get_post_params():
    owner_id = openapi.Parameter(
        "owner_id",
        openapi.IN_QUERY,
        description="enter the id to get the user data",
        type=openapi.TYPE_INTEGER,
    )

    return [owner_id]


def get_post_file_comments():
    post_id = openapi.Parameter(
        "post_id",
        openapi.IN_QUERY,
        description="enter the post id to get the user data",
        type=openapi.TYPE_INTEGER,
    )

    return [post_id]


def get_video_params():
    owner_id = openapi.Parameter(
        "owner_id",
        openapi.IN_QUERY,
        description="enter the owner_id",
        type=openapi.TYPE_INTEGER,
    )

    return [owner_id]


def get_video_params():
    owner_id = openapi.Parameter(
        "owner_id",
        openapi.IN_QUERY,
        description="enter the owner_id",
        type=openapi.TYPE_INTEGER,
    )

    return [owner_id]


def get_comment_of_video_params():
    video_id = openapi.Parameter(
        "video_id",
        openapi.IN_QUERY,
        description="enter the video_id",
        type=openapi.TYPE_INTEGER,
    )

    return [video_id]
