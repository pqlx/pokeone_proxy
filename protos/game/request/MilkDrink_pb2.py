# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MilkDrink.proto

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
  name='MilkDrink.proto',
  package='PSXAPI.Request44',
  syntax='proto2',
  serialized_pb=_b('\n\x0fMilkDrink.proto\x12\x10PSXAPI.Request44\x1a\tbcl.proto\"A\n\tMilkDrink\x12\x19\n\x06Source\x18\x01 \x01(\x0b\x32\t.bcl.Guid\x12\x19\n\x06Target\x18\x02 \x01(\x0b\x32\t.bcl.Guid')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MILKDRINK = _descriptor.Descriptor(
  name='MilkDrink',
  full_name='PSXAPI.Request44.MilkDrink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Source', full_name='PSXAPI.Request44.MilkDrink.Source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Target', full_name='PSXAPI.Request44.MilkDrink.Target', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=48,
  serialized_end=113,
)

_MILKDRINK.fields_by_name['Source'].message_type = bcl__pb2._GUID
_MILKDRINK.fields_by_name['Target'].message_type = bcl__pb2._GUID
DESCRIPTOR.message_types_by_name['MilkDrink'] = _MILKDRINK

MilkDrink = _reflection.GeneratedProtocolMessageType('MilkDrink', (_message.Message,), dict(
  DESCRIPTOR = _MILKDRINK,
  __module__ = 'MilkDrink_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request44.MilkDrink)
  ))
_sym_db.RegisterMessage(MilkDrink)


# @@protoc_insertion_point(module_scope)
