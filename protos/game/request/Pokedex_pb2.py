# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/request/Pokedex.proto

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
  name='game/request/Pokedex.proto',
  package='PSXAPI.Request961485215',
  syntax='proto2',
  serialized_pb=_b('\n\x1agame/request/Pokedex.proto\x12\x17PSXAPI.Request961485215\"\t\n\x07Pokedex')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POKEDEX = _descriptor.Descriptor(
  name='Pokedex',
  full_name='PSXAPI.Request961485215.Pokedex',
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
  serialized_start=55,
  serialized_end=64,
)

DESCRIPTOR.message_types_by_name['Pokedex'] = _POKEDEX

Pokedex = _reflection.GeneratedProtocolMessageType('Pokedex', (_message.Message,), dict(
  DESCRIPTOR = _POKEDEX,
  __module__ = 'game.request.Pokedex_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request961485215.Pokedex)
  ))
_sym_db.RegisterMessage(Pokedex)


# @@protoc_insertion_point(module_scope)
