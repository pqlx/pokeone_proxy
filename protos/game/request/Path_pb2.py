# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Path.proto

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
  name='Path.proto',
  package='PSXAPI.Request48',
  syntax='proto2',
  serialized_pb=_b('\n\nPath.proto\x12\x10PSXAPI.Request48\x1a\tbcl.proto\"\"\n\x04Path\x12\x1a\n\x07Request\x18\x01 \x01(\x0b\x32\t.bcl.Guid')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='PSXAPI.Request48.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Request', full_name='PSXAPI.Request48.Path.Request', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=43,
  serialized_end=77,
)

_PATH.fields_by_name['Request'].message_type = bcl__pb2._GUID
DESCRIPTOR.message_types_by_name['Path'] = _PATH

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), dict(
  DESCRIPTOR = _PATH,
  __module__ = 'Path_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request48.Path)
  ))
_sym_db.RegisterMessage(Path)


# @@protoc_insertion_point(module_scope)
