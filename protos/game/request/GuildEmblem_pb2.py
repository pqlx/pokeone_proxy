# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GuildEmblem.proto

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
  name='GuildEmblem.proto',
  package='PSXAPI.Request25',
  syntax='proto2',
  serialized_pb=_b('\n\x11GuildEmblem.proto\x12\x10PSXAPI.Request25\"\x1b\n\x0bGuildEmblem\x12\x0c\n\x04Name\x18\x01 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GUILDEMBLEM = _descriptor.Descriptor(
  name='GuildEmblem',
  full_name='PSXAPI.Request25.GuildEmblem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='PSXAPI.Request25.GuildEmblem.Name', index=0,
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
  serialized_start=39,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['GuildEmblem'] = _GUILDEMBLEM

GuildEmblem = _reflection.GeneratedProtocolMessageType('GuildEmblem', (_message.Message,), dict(
  DESCRIPTOR = _GUILDEMBLEM,
  __module__ = 'GuildEmblem_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request25.GuildEmblem)
  ))
_sym_db.RegisterMessage(GuildEmblem)


# @@protoc_insertion_point(module_scope)
