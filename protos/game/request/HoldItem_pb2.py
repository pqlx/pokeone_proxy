# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HoldItem.proto

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
  name='HoldItem.proto',
  package='PSXAPI.Request26',
  syntax='proto2',
  serialized_pb=_b('\n\x0eHoldItem.proto\x12\x10PSXAPI.Request26\x1a\tbcl.proto\"N\n\x08HoldItem\x12\x1a\n\x07Pokemon\x18\x01 \x01(\x0b\x32\t.bcl.Guid\x12\x0f\n\x04Item\x18\x02 \x01(\x05:\x01\x30\x12\x15\n\x06Remove\x18\x03 \x01(\x08:\x05\x66\x61lse')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HOLDITEM = _descriptor.Descriptor(
  name='HoldItem',
  full_name='PSXAPI.Request26.HoldItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PSXAPI.Request26.HoldItem.Pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Item', full_name='PSXAPI.Request26.HoldItem.Item', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Remove', full_name='PSXAPI.Request26.HoldItem.Remove', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=47,
  serialized_end=125,
)

_HOLDITEM.fields_by_name['Pokemon'].message_type = bcl__pb2._GUID
DESCRIPTOR.message_types_by_name['HoldItem'] = _HOLDITEM

HoldItem = _reflection.GeneratedProtocolMessageType('HoldItem', (_message.Message,), dict(
  DESCRIPTOR = _HOLDITEM,
  __module__ = 'HoldItem_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request26.HoldItem)
  ))
_sym_db.RegisterMessage(HoldItem)


# @@protoc_insertion_point(module_scope)
