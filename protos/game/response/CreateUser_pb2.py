# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CreateUser.proto

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
  name='CreateUser.proto',
  package='PSXAPI.Response16',
  syntax='proto2',
  serialized_pb=_b('\n\x10\x43reateUser.proto\x12\x11PSXAPI.Response16\"H\n\nCreateUser\x12:\n\x06Result\x18\x01 \x01(\x0e\x32#.PSXAPI.Response16.CreateUserResult:\x05\x45rror**\n\x10\x43reateUserResult\x12\t\n\x05\x45rror\x10\x00\x12\x0b\n\x07Success\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CREATEUSERRESULT = _descriptor.EnumDescriptor(
  name='CreateUserResult',
  full_name='PSXAPI.Response16.CreateUserResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Error', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Success', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=113,
  serialized_end=155,
)
_sym_db.RegisterEnumDescriptor(_CREATEUSERRESULT)

CreateUserResult = enum_type_wrapper.EnumTypeWrapper(_CREATEUSERRESULT)
Error = 0
Success = 1



_CREATEUSER = _descriptor.Descriptor(
  name='CreateUser',
  full_name='PSXAPI.Response16.CreateUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='PSXAPI.Response16.CreateUser.Result', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=39,
  serialized_end=111,
)

_CREATEUSER.fields_by_name['Result'].enum_type = _CREATEUSERRESULT
DESCRIPTOR.message_types_by_name['CreateUser'] = _CREATEUSER
DESCRIPTOR.enum_types_by_name['CreateUserResult'] = _CREATEUSERRESULT

CreateUser = _reflection.GeneratedProtocolMessageType('CreateUser', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUSER,
  __module__ = 'CreateUser_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response16.CreateUser)
  ))
_sym_db.RegisterMessage(CreateUser)


# @@protoc_insertion_point(module_scope)
