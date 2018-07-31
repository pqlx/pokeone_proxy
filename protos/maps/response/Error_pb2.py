# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Error.proto',
  package='MAPAPI.Response9',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x45rror.proto\x12\x10MAPAPI.Response9\"P\n\x05\x45rror\x12\x36\n\tErrorType\x18\x01 \x01(\x0e\x32\x1b.MAPAPI.Response9.ErrorType:\x06__None\x12\x0f\n\x07Message\x18\x02 \x01(\t*M\n\tErrorType\x12\n\n\x06__None\x10\x00\x12\x10\n\x0cInvalidLogin\x10\x01\x12\x0e\n\nInvalidMap\x10\x02\x12\x12\n\x0eInvalidSession\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ERRORTYPE = _descriptor.EnumDescriptor(
  name='ErrorType',
  full_name='MAPAPI.Response9.ErrorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidLogin', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidMap', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidSession', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=115,
  serialized_end=192,
)
_sym_db.RegisterEnumDescriptor(_ERRORTYPE)

ErrorType = enum_type_wrapper.EnumTypeWrapper(_ERRORTYPE)
__None = 0
InvalidLogin = 1
InvalidMap = 2
InvalidSession = 3



_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='MAPAPI.Response9.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ErrorType', full_name='MAPAPI.Response9.Error.ErrorType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Message', full_name='MAPAPI.Response9.Error.Message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=113,
)

_ERROR.fields_by_name['ErrorType'].enum_type = _ERRORTYPE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.enum_types_by_name['ErrorType'] = _ERRORTYPE

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'Error_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response9.Error)
  ))
_sym_db.RegisterMessage(Error)


# @@protoc_insertion_point(module_scope)
