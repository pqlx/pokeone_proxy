# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: StatsSettings.proto

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
  name='StatsSettings.proto',
  package='PSXAPI.Request62',
  syntax='proto2',
  serialized_pb=_b('\n\x13StatsSettings.proto\x12\x10PSXAPI.Request62\"E\n\rStatsSettings\x12\x16\n\x07Private\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\rShowAsOffline\x18\x02 \x01(\x08:\x05\x66\x61lse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STATSSETTINGS = _descriptor.Descriptor(
  name='StatsSettings',
  full_name='PSXAPI.Request62.StatsSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Private', full_name='PSXAPI.Request62.StatsSettings.Private', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ShowAsOffline', full_name='PSXAPI.Request62.StatsSettings.ShowAsOffline', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=41,
  serialized_end=110,
)

DESCRIPTOR.message_types_by_name['StatsSettings'] = _STATSSETTINGS

StatsSettings = _reflection.GeneratedProtocolMessageType('StatsSettings', (_message.Message,), dict(
  DESCRIPTOR = _STATSSETTINGS,
  __module__ = 'StatsSettings_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request62.StatsSettings)
  ))
_sym_db.RegisterMessage(StatsSettings)


# @@protoc_insertion_point(module_scope)
