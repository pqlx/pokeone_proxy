# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/request/Trade.proto

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
  name='game/request/Trade.proto',
  package='PSXAPI.Request230124799',
  syntax='proto2',
  serialized_pb=_b('\n\x18game/request/Trade.proto\x12\x17PSXAPI.Request230124799\x1a\tbcl.proto\"\xce\x01\n\x05Trade\x12V\n\x06\x41\x63tion\x18\x01 \x01(\x0e\x32>.PSXAPI.Request230124799.PREFIX_AGDFASBV1446123149.TradeAction:\x06\x43\x61ncel\x12\x1a\n\x07Pokemon\x18\x02 \x01(\x0b\x32\t.bcl.Guid\x12\x11\n\x06ItemID\x18\x03 \x01(\x05:\x01\x30\x12\x15\n\nItemAmount\x18\x04 \x01(\x05:\x01\x30\x12\x10\n\x05Money\x18\x05 \x01(\r:\x01\x30\x12\x15\n\x06\x41\x63\x63\x65pt\x18\x06 \x01(\x08:\x05\x66\x61lse\"\x90\x01\n\x19PREFIX_AGDFASBV1446123149\"s\n\x0bTradeAction\x12\n\n\x06\x43\x61ncel\x10\x00\x12\x0e\n\nAddPokemon\x10\x01\x12\x11\n\rRemovePokemon\x10\x02\x12\x0b\n\x07SetItem\x10\x03\x12\x0c\n\x08SetMoney\x10\x04\x12\r\n\tSetAccept\x10\x05\x12\x0b\n\x07\x43onfirm\x10\x06')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV1446123149_TRADEACTION = _descriptor.EnumDescriptor(
  name='TradeAction',
  full_name='PSXAPI.Request230124799.PREFIX_AGDFASBV1446123149.TradeAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Cancel', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AddPokemon', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RemovePokemon', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetItem', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetMoney', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetAccept', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Confirm', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=303,
  serialized_end=418,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1446123149_TRADEACTION)


_TRADE = _descriptor.Descriptor(
  name='Trade',
  full_name='PSXAPI.Request230124799.Trade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Request230124799.Trade.Action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PSXAPI.Request230124799.Trade.Pokemon', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ItemID', full_name='PSXAPI.Request230124799.Trade.ItemID', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ItemAmount', full_name='PSXAPI.Request230124799.Trade.ItemAmount', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Money', full_name='PSXAPI.Request230124799.Trade.Money', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Accept', full_name='PSXAPI.Request230124799.Trade.Accept', index=5,
      number=6, type=8, cpp_type=7, label=1,
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
  serialized_start=65,
  serialized_end=271,
)


_PREFIX_AGDFASBV1446123149 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1446123149',
  full_name='PSXAPI.Request230124799.PREFIX_AGDFASBV1446123149',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1446123149_TRADEACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=418,
)

_TRADE.fields_by_name['Action'].enum_type = _PREFIX_AGDFASBV1446123149_TRADEACTION
_TRADE.fields_by_name['Pokemon'].message_type = bcl__pb2._GUID
_PREFIX_AGDFASBV1446123149_TRADEACTION.containing_type = _PREFIX_AGDFASBV1446123149
DESCRIPTOR.message_types_by_name['Trade'] = _TRADE
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1446123149'] = _PREFIX_AGDFASBV1446123149

Trade = _reflection.GeneratedProtocolMessageType('Trade', (_message.Message,), dict(
  DESCRIPTOR = _TRADE,
  __module__ = 'game.request.Trade_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request230124799.Trade)
  ))
_sym_db.RegisterMessage(Trade)

PREFIX_AGDFASBV1446123149 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1446123149', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1446123149,
  __module__ = 'game.request.Trade_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request230124799.PREFIX_AGDFASBV1446123149)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1446123149)


# @@protoc_insertion_point(module_scope)
