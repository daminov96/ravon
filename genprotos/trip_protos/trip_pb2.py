# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trip.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="trip.proto",
    package="trip",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\ntrip.proto\x12\x04trip\x1a\x1bgoogle/protobuf/empty.proto"\x9e\x01\n\x08Location\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63reated\x18\x02 \x01(\t\x12\x0f\n\x07updated\x18\x03 \x01(\t\x12\x15\n\rlocation_name\x18\x04 \x01(\t\x12\x17\n\x0fmodel_object_id\x18\x05 \x01(\t\x12\x19\n\x11model_object_type\x18\x06 \x01(\t\x12\x0b\n\x03lat\x18\x07 \x01(\t\x12\x0c\n\x04long\x18\x08 \x01(\t"\x15\n\x13LocationListRequest"%\n\x17LocationRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05"R\n\x12ReasonToCancelTrip\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63reated\x18\x02 \x01(\t\x12\x0f\n\x07updated\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t"\x1f\n\x1dReasonToCancelTripListRequest"/\n!ReasonToCancelTripRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05"\x9c\x02\n\x04Trip\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63reated\x18\x02 \x01(\t\x12\x0f\n\x07updated\x18\x03 \x01(\t\x12\x0e\n\x06\x64river\x18\x04 \x01(\t\x12\x10\n\x08\x63ustomer\x18\x05 \x01(\t\x12\x0c\n\x04plan\x18\x06 \x01(\t\x12\r\n\x05state\x18\x07 \x01(\t\x12\r\n\x05price\x18\x08 \x01(\x02\x12"\n\nfrom_point\x18\t \x01(\x0b\x32\x0e.trip.Location\x12 \n\x08to_point\x18\n \x01(\x0b\x32\x0e.trip.Location\x12\x18\n\x10reason_to_cancel\x18\x0b \x03(\x05\x12\x38\n\x16reason_to_cancel_infos\x18\x0c \x03(\x0b\x32\x18.trip.ReasonToCancelTrip"/\n\x10TripListResponse\x12\x1b\n\x07results\x18\x01 \x03(\x0b\x32\n.trip.Trip"B\n\x0fTripListRequest\x12\x0e\n\x06\x64river\x18\x01 \x01(\t\x12\x10\n\x08\x63ustomer\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t"!\n\x13TripRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xf7\x01\n\x0eTripController\x12\x37\n\x04List\x12\x15.trip.TripListRequest\x1a\x16.trip.TripListResponse"\x00\x12"\n\x06\x43reate\x12\n.trip.Trip\x1a\n.trip.Trip"\x00\x12\x33\n\x08Retrieve\x12\x19.trip.TripRetrieveRequest\x1a\n.trip.Trip"\x00\x12"\n\x06Update\x12\n.trip.Trip\x1a\n.trip.Trip"\x00\x12/\n\x07\x44\x65stroy\x12\n.trip.Trip\x1a\x16.google.protobuf.Empty"\x00\x32\x95\x02\n\x12LocationController\x12\x35\n\x04List\x12\x19.trip.LocationListRequest\x1a\x0e.trip.Location"\x00\x30\x01\x12*\n\x06\x43reate\x12\x0e.trip.Location\x1a\x0e.trip.Location"\x00\x12;\n\x08Retrieve\x12\x1d.trip.LocationRetrieveRequest\x1a\x0e.trip.Location"\x00\x12*\n\x06Update\x12\x0e.trip.Location\x1a\x0e.trip.Location"\x00\x12\x33\n\x07\x44\x65stroy\x12\x0e.trip.Location\x1a\x16.google.protobuf.Empty"\x00\x32\xf9\x02\n\x1cReasonToCancelTripController\x12I\n\x04List\x12#.trip.ReasonToCancelTripListRequest\x1a\x18.trip.ReasonToCancelTrip"\x00\x30\x01\x12>\n\x06\x43reate\x12\x18.trip.ReasonToCancelTrip\x1a\x18.trip.ReasonToCancelTrip"\x00\x12O\n\x08Retrieve\x12\'.trip.ReasonToCancelTripRetrieveRequest\x1a\x18.trip.ReasonToCancelTrip"\x00\x12>\n\x06Update\x12\x18.trip.ReasonToCancelTrip\x1a\x18.trip.ReasonToCancelTrip"\x00\x12=\n\x07\x44\x65stroy\x12\x18.trip.ReasonToCancelTrip\x1a\x16.google.protobuf.Empty"\x00\x62\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
    ],
)


_LOCATION = _descriptor.Descriptor(
    name="Location",
    full_name="trip.Location",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="trip.Location.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="created",
            full_name="trip.Location.created",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="updated",
            full_name="trip.Location.updated",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="location_name",
            full_name="trip.Location.location_name",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="model_object_id",
            full_name="trip.Location.model_object_id",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="model_object_type",
            full_name="trip.Location.model_object_type",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="lat",
            full_name="trip.Location.lat",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="long",
            full_name="trip.Location.long",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=50,
    serialized_end=208,
)


_LOCATIONLISTREQUEST = _descriptor.Descriptor(
    name="LocationListRequest",
    full_name="trip.LocationListRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=210,
    serialized_end=231,
)


_LOCATIONRETRIEVEREQUEST = _descriptor.Descriptor(
    name="LocationRetrieveRequest",
    full_name="trip.LocationRetrieveRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="trip.LocationRetrieveRequest.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=233,
    serialized_end=270,
)


_REASONTOCANCELTRIP = _descriptor.Descriptor(
    name="ReasonToCancelTrip",
    full_name="trip.ReasonToCancelTrip",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="trip.ReasonToCancelTrip.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="created",
            full_name="trip.ReasonToCancelTrip.created",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="updated",
            full_name="trip.ReasonToCancelTrip.updated",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reason",
            full_name="trip.ReasonToCancelTrip.reason",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=272,
    serialized_end=354,
)


_REASONTOCANCELTRIPLISTREQUEST = _descriptor.Descriptor(
    name="ReasonToCancelTripListRequest",
    full_name="trip.ReasonToCancelTripListRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=356,
    serialized_end=387,
)


_REASONTOCANCELTRIPRETRIEVEREQUEST = _descriptor.Descriptor(
    name="ReasonToCancelTripRetrieveRequest",
    full_name="trip.ReasonToCancelTripRetrieveRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="trip.ReasonToCancelTripRetrieveRequest.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=389,
    serialized_end=436,
)


_TRIP = _descriptor.Descriptor(
    name="Trip",
    full_name="trip.Trip",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="trip.Trip.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="created",
            full_name="trip.Trip.created",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="updated",
            full_name="trip.Trip.updated",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="driver",
            full_name="trip.Trip.driver",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="customer",
            full_name="trip.Trip.customer",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="plan",
            full_name="trip.Trip.plan",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="state",
            full_name="trip.Trip.state",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="price",
            full_name="trip.Trip.price",
            index=7,
            number=8,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="from_point",
            full_name="trip.Trip.from_point",
            index=8,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="to_point",
            full_name="trip.Trip.to_point",
            index=9,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reason_to_cancel",
            full_name="trip.Trip.reason_to_cancel",
            index=10,
            number=11,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reason_to_cancel_infos",
            full_name="trip.Trip.reason_to_cancel_infos",
            index=11,
            number=12,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=439,
    serialized_end=723,
)


_TRIPLISTRESPONSE = _descriptor.Descriptor(
    name="TripListResponse",
    full_name="trip.TripListResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="results",
            full_name="trip.TripListResponse.results",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=725,
    serialized_end=772,
)


_TRIPLISTREQUEST = _descriptor.Descriptor(
    name="TripListRequest",
    full_name="trip.TripListRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="driver",
            full_name="trip.TripListRequest.driver",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="customer",
            full_name="trip.TripListRequest.customer",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="state",
            full_name="trip.TripListRequest.state",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=774,
    serialized_end=840,
)


_TRIPRETRIEVEREQUEST = _descriptor.Descriptor(
    name="TripRetrieveRequest",
    full_name="trip.TripRetrieveRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="trip.TripRetrieveRequest.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=842,
    serialized_end=875,
)

_TRIP.fields_by_name["from_point"].message_type = _LOCATION
_TRIP.fields_by_name["to_point"].message_type = _LOCATION
_TRIP.fields_by_name["reason_to_cancel_infos"].message_type = _REASONTOCANCELTRIP
_TRIPLISTRESPONSE.fields_by_name["results"].message_type = _TRIP
DESCRIPTOR.message_types_by_name["Location"] = _LOCATION
DESCRIPTOR.message_types_by_name["LocationListRequest"] = _LOCATIONLISTREQUEST
DESCRIPTOR.message_types_by_name["LocationRetrieveRequest"] = _LOCATIONRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name["ReasonToCancelTrip"] = _REASONTOCANCELTRIP
DESCRIPTOR.message_types_by_name[
    "ReasonToCancelTripListRequest"
] = _REASONTOCANCELTRIPLISTREQUEST
DESCRIPTOR.message_types_by_name[
    "ReasonToCancelTripRetrieveRequest"
] = _REASONTOCANCELTRIPRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name["Trip"] = _TRIP
DESCRIPTOR.message_types_by_name["TripListResponse"] = _TRIPLISTRESPONSE
DESCRIPTOR.message_types_by_name["TripListRequest"] = _TRIPLISTREQUEST
DESCRIPTOR.message_types_by_name["TripRetrieveRequest"] = _TRIPRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType(
    "Location",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCATION,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.Location)
    },
)
_sym_db.RegisterMessage(Location)

LocationListRequest = _reflection.GeneratedProtocolMessageType(
    "LocationListRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCATIONLISTREQUEST,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.LocationListRequest)
    },
)
_sym_db.RegisterMessage(LocationListRequest)

LocationRetrieveRequest = _reflection.GeneratedProtocolMessageType(
    "LocationRetrieveRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCATIONRETRIEVEREQUEST,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.LocationRetrieveRequest)
    },
)
_sym_db.RegisterMessage(LocationRetrieveRequest)

ReasonToCancelTrip = _reflection.GeneratedProtocolMessageType(
    "ReasonToCancelTrip",
    (_message.Message,),
    {
        "DESCRIPTOR": _REASONTOCANCELTRIP,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.ReasonToCancelTrip)
    },
)
_sym_db.RegisterMessage(ReasonToCancelTrip)

ReasonToCancelTripListRequest = _reflection.GeneratedProtocolMessageType(
    "ReasonToCancelTripListRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REASONTOCANCELTRIPLISTREQUEST,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.ReasonToCancelTripListRequest)
    },
)
_sym_db.RegisterMessage(ReasonToCancelTripListRequest)

ReasonToCancelTripRetrieveRequest = _reflection.GeneratedProtocolMessageType(
    "ReasonToCancelTripRetrieveRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REASONTOCANCELTRIPRETRIEVEREQUEST,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.ReasonToCancelTripRetrieveRequest)
    },
)
_sym_db.RegisterMessage(ReasonToCancelTripRetrieveRequest)

Trip = _reflection.GeneratedProtocolMessageType(
    "Trip",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRIP,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.Trip)
    },
)
_sym_db.RegisterMessage(Trip)

TripListResponse = _reflection.GeneratedProtocolMessageType(
    "TripListResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRIPLISTRESPONSE,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.TripListResponse)
    },
)
_sym_db.RegisterMessage(TripListResponse)

TripListRequest = _reflection.GeneratedProtocolMessageType(
    "TripListRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRIPLISTREQUEST,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.TripListRequest)
    },
)
_sym_db.RegisterMessage(TripListRequest)

TripRetrieveRequest = _reflection.GeneratedProtocolMessageType(
    "TripRetrieveRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRIPRETRIEVEREQUEST,
        "__module__": "trip_pb2"
        # @@protoc_insertion_point(class_scope:trip.TripRetrieveRequest)
    },
)
_sym_db.RegisterMessage(TripRetrieveRequest)


_TRIPCONTROLLER = _descriptor.ServiceDescriptor(
    name="TripController",
    full_name="trip.TripController",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=878,
    serialized_end=1125,
    methods=[
        _descriptor.MethodDescriptor(
            name="List",
            full_name="trip.TripController.List",
            index=0,
            containing_service=None,
            input_type=_TRIPLISTREQUEST,
            output_type=_TRIPLISTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Create",
            full_name="trip.TripController.Create",
            index=1,
            containing_service=None,
            input_type=_TRIP,
            output_type=_TRIP,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Retrieve",
            full_name="trip.TripController.Retrieve",
            index=2,
            containing_service=None,
            input_type=_TRIPRETRIEVEREQUEST,
            output_type=_TRIP,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Update",
            full_name="trip.TripController.Update",
            index=3,
            containing_service=None,
            input_type=_TRIP,
            output_type=_TRIP,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Destroy",
            full_name="trip.TripController.Destroy",
            index=4,
            containing_service=None,
            input_type=_TRIP,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_TRIPCONTROLLER)

DESCRIPTOR.services_by_name["TripController"] = _TRIPCONTROLLER


_LOCATIONCONTROLLER = _descriptor.ServiceDescriptor(
    name="LocationController",
    full_name="trip.LocationController",
    file=DESCRIPTOR,
    index=1,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1128,
    serialized_end=1405,
    methods=[
        _descriptor.MethodDescriptor(
            name="List",
            full_name="trip.LocationController.List",
            index=0,
            containing_service=None,
            input_type=_LOCATIONLISTREQUEST,
            output_type=_LOCATION,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Create",
            full_name="trip.LocationController.Create",
            index=1,
            containing_service=None,
            input_type=_LOCATION,
            output_type=_LOCATION,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Retrieve",
            full_name="trip.LocationController.Retrieve",
            index=2,
            containing_service=None,
            input_type=_LOCATIONRETRIEVEREQUEST,
            output_type=_LOCATION,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Update",
            full_name="trip.LocationController.Update",
            index=3,
            containing_service=None,
            input_type=_LOCATION,
            output_type=_LOCATION,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Destroy",
            full_name="trip.LocationController.Destroy",
            index=4,
            containing_service=None,
            input_type=_LOCATION,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_LOCATIONCONTROLLER)

DESCRIPTOR.services_by_name["LocationController"] = _LOCATIONCONTROLLER


_REASONTOCANCELTRIPCONTROLLER = _descriptor.ServiceDescriptor(
    name="ReasonToCancelTripController",
    full_name="trip.ReasonToCancelTripController",
    file=DESCRIPTOR,
    index=2,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1408,
    serialized_end=1785,
    methods=[
        _descriptor.MethodDescriptor(
            name="List",
            full_name="trip.ReasonToCancelTripController.List",
            index=0,
            containing_service=None,
            input_type=_REASONTOCANCELTRIPLISTREQUEST,
            output_type=_REASONTOCANCELTRIP,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Create",
            full_name="trip.ReasonToCancelTripController.Create",
            index=1,
            containing_service=None,
            input_type=_REASONTOCANCELTRIP,
            output_type=_REASONTOCANCELTRIP,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Retrieve",
            full_name="trip.ReasonToCancelTripController.Retrieve",
            index=2,
            containing_service=None,
            input_type=_REASONTOCANCELTRIPRETRIEVEREQUEST,
            output_type=_REASONTOCANCELTRIP,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Update",
            full_name="trip.ReasonToCancelTripController.Update",
            index=3,
            containing_service=None,
            input_type=_REASONTOCANCELTRIP,
            output_type=_REASONTOCANCELTRIP,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Destroy",
            full_name="trip.ReasonToCancelTripController.Destroy",
            index=4,
            containing_service=None,
            input_type=_REASONTOCANCELTRIP,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_REASONTOCANCELTRIPCONTROLLER)

DESCRIPTOR.services_by_name[
    "ReasonToCancelTripController"
] = _REASONTOCANCELTRIPCONTROLLER

# @@protoc_insertion_point(module_scope)
