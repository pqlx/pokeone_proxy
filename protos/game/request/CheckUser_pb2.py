# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CheckUser.proto

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
  name='CheckUser.proto',
  package='PSXAPI.Request15',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x43heckUser.proto\x12\x10PSXAPI.Request15\"\x19\n\tCheckUser\x12\x0c\n\x04Name\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHECKUSER = _descriptor.Descriptor(
  name='CheckUser',
  full_name='PSXAPI.Request15.CheckUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='PSXAPI.Request15.CheckUser.Name', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=37,
  serialized_end=62,
)

DESCRIPTOR.message_types_by_name['CheckUser'] = _CHECKUSER

CheckUser = _reflection.GeneratedProtocolMessageType('CheckUser', (_message.Message,), dict(
  DESCRIPTOR = _CHECKUSER,
  __module__ = 'CheckUser_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request15.CheckUser)
  ))
_sym_db.RegisterMessage(CheckUser)


# @@protoc_insertion_point(module_scope)
