# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Items.proto

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
  name='Items.proto',
  package='PSXAPI.Request29',
  syntax='proto2',
  serialized_pb=_b('\n\x0bItems.proto\x12\x10PSXAPI.Request29\"\x07\n\x05Items')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ITEMS = _descriptor.Descriptor(
  name='Items',
  full_name='PSXAPI.Request29.Items',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=33,
  serialized_end=40,
)

DESCRIPTOR.message_types_by_name['Items'] = _ITEMS

Items = _reflection.GeneratedProtocolMessageType('Items', (_message.Message,), dict(
  DESCRIPTOR = _ITEMS,
  __module__ = 'Items_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request29.Items)
  ))
_sym_db.RegisterMessage(Items)


# @@protoc_insertion_point(module_scope)
