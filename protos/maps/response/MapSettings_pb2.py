# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maps/response/MapSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='maps/response/MapSettings.proto',
  package='MAPAPI.Response1220737299',
  syntax='proto2',
  serialized_pb=_b('\n\x1fmaps/response/MapSettings.proto\x12\x19MAPAPI.Response1220737299\"\x1f\n\x0bMapSettings\x12\x10\n\x08settings\x18\x01 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MAPSETTINGS = _descriptor.Descriptor(
  name='MapSettings',
  full_name='MAPAPI.Response1220737299.MapSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='MAPAPI.Response1220737299.MapSettings.settings', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['MapSettings'] = _MAPSETTINGS

MapSettings = _reflection.GeneratedProtocolMessageType('MapSettings', (_message.Message,), dict(
  DESCRIPTOR = _MAPSETTINGS,
  __module__ = 'maps.response.MapSettings_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response1220737299.MapSettings)
  ))
_sym_db.RegisterMessage(MapSettings)


# @@protoc_insertion_point(module_scope)
