# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Friend.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bcl_pb2 as bcl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Friend.proto',
  package='PSXAPI.Response.Payload16',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x46riend.proto\x12\x19PSXAPI.Response.Payload16\x1a\tbcl.proto\"\xba\x01\n\x06\x46riend\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x15\n\x06Online\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\"\n\x0bOnlineSince\x18\x03 \x01(\x0b\x32\r.bcl.TimeSpan\x12\"\n\x0b\x46riendSince\x18\x04 \x01(\x0b\x32\r.bcl.TimeSpan\x12\x0b\n\x03Map\x18\x05 \x01(\t\x12\x13\n\x04\x41way\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x0f\n\x07Message\x18\x07 \x01(\t\x12\x10\n\x05Level\x18\x08 \x01(\r:\x01\x30')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FRIEND = _descriptor.Descriptor(
  name='Friend',
  full_name='PSXAPI.Response.Payload16.Friend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='PSXAPI.Response.Payload16.Friend.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Online', full_name='PSXAPI.Response.Payload16.Friend.Online', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OnlineSince', full_name='PSXAPI.Response.Payload16.Friend.OnlineSince', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FriendSince', full_name='PSXAPI.Response.Payload16.Friend.FriendSince', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Map', full_name='PSXAPI.Response.Payload16.Friend.Map', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Away', full_name='PSXAPI.Response.Payload16.Friend.Away', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Message', full_name='PSXAPI.Response.Payload16.Friend.Message', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Level', full_name='PSXAPI.Response.Payload16.Friend.Level', index=7,
      number=8, type=13, cpp_type=3, label=1,
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
  serialized_start=55,
  serialized_end=241,
)

_FRIEND.fields_by_name['OnlineSince'].message_type = bcl__pb2._TIMESPAN
_FRIEND.fields_by_name['FriendSince'].message_type = bcl__pb2._TIMESPAN
DESCRIPTOR.message_types_by_name['Friend'] = _FRIEND

Friend = _reflection.GeneratedProtocolMessageType('Friend', (_message.Message,), dict(
  DESCRIPTOR = _FRIEND,
  __module__ = 'Friend_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response.Payload16.Friend)
  ))
_sym_db.RegisterMessage(Friend)


# @@protoc_insertion_point(module_scope)
