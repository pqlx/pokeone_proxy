# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Reorder.proto

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
  name='Reorder.proto',
  package='PSXAPI.Response70',
  syntax='proto2',
  serialized_pb=_b('\n\rReorder.proto\x12\x11PSXAPI.Response70\x1a\tbcl.proto\"5\n\x07Reorder\x12\x1a\n\x07Pokemon\x18\x01 \x03(\x0b\x32\t.bcl.Guid\x12\x0e\n\x03\x42ox\x18\x02 \x01(\x05:\x01\x30')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REORDER = _descriptor.Descriptor(
  name='Reorder',
  full_name='PSXAPI.Response70.Reorder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PSXAPI.Response70.Reorder.Pokemon', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Box', full_name='PSXAPI.Response70.Reorder.Box', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=47,
  serialized_end=100,
)

_REORDER.fields_by_name['Pokemon'].message_type = bcl__pb2._GUID
DESCRIPTOR.message_types_by_name['Reorder'] = _REORDER

Reorder = _reflection.GeneratedProtocolMessageType('Reorder', (_message.Message,), dict(
  DESCRIPTOR = _REORDER,
  __module__ = 'Reorder_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response70.Reorder)
  ))
_sym_db.RegisterMessage(Reorder)


# @@protoc_insertion_point(module_scope)
