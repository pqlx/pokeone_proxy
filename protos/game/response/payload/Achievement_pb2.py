# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/response/payload/Achievement.proto

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
  name='game/response/payload/Achievement.proto',
  package='PSXAPI.Response.Payload1009261781',
  syntax='proto2',
  serialized_pb=_b('\n\'game/response/payload/Achievement.proto\x12!PSXAPI.Response.Payload1009261781\"X\n\x0b\x41\x63hievement\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x13\n\x0b\x44iscription\x18\x02 \x01(\t\x12\x11\n\x06Points\x18\x03 \x01(\r:\x01\x30\x12\x13\n\x08Required\x18\x04 \x01(\r:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACHIEVEMENT = _descriptor.Descriptor(
  name='Achievement',
  full_name='PSXAPI.Response.Payload1009261781.Achievement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='PSXAPI.Response.Payload1009261781.Achievement.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Discription', full_name='PSXAPI.Response.Payload1009261781.Achievement.Discription', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Points', full_name='PSXAPI.Response.Payload1009261781.Achievement.Points', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Required', full_name='PSXAPI.Response.Payload1009261781.Achievement.Required', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=78,
  serialized_end=166,
)

DESCRIPTOR.message_types_by_name['Achievement'] = _ACHIEVEMENT

Achievement = _reflection.GeneratedProtocolMessageType('Achievement', (_message.Message,), dict(
  DESCRIPTOR = _ACHIEVEMENT,
  __module__ = 'game.response.payload.Achievement_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response.Payload1009261781.Achievement)
  ))
_sym_db.RegisterMessage(Achievement)


# @@protoc_insertion_point(module_scope)
