# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: detective.proto

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
  name='detective.proto',
  package='detective',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x64\x65tective.proto\x12\tdetective\"\x1d\n\rWitnessEvents\x12\x0c\n\x04name\x18\x01 \x03(\t\"J\n\x16GetWitnessMergeRequest\x12\x30\n\x0ewitness_events\x18\x01 \x03(\x0b\x32\x18.detective.WitnessEvents\"{\n\x14GetWitnessMergeReply\x12\x31\n\x08\x64\x65\x63ision\x18\x01 \x01(\x0e\x32\x1f.detective.WitnessEventDecision\x12\x30\n\x0ewitness_events\x18\x02 \x03(\x0b\x32\x18.detective.WitnessEvents*\xb6\x01\n\x14WitnessEventDecision\x12 \n\x1cWITNESS_DECISION_CANT_DECIDE\x10\x00\x12\'\n#WITNESS_DECISION_MERGE_ALL_POSSIBLE\x10\x01\x12+\n\'WITNESS_DECISION_PARTIAL_MERGE_POSSIBLE\x10\x02\x12&\n\"WITNESS_DECISION_NO_MERGE_POSSIBLE\x10\x03\x32q\n\x10\x44\x65tectiveService\x12]\n\x17GetWitnessMergeDecision\x12!.detective.GetWitnessMergeRequest\x1a\x1f.detective.GetWitnessMergeReplyb\x06proto3')
)

_WITNESSEVENTDECISION = _descriptor.EnumDescriptor(
  name='WitnessEventDecision',
  full_name='detective.WitnessEventDecision',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WITNESS_DECISION_CANT_DECIDE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITNESS_DECISION_MERGE_ALL_POSSIBLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITNESS_DECISION_PARTIAL_MERGE_POSSIBLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITNESS_DECISION_NO_MERGE_POSSIBLE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=263,
  serialized_end=445,
)
_sym_db.RegisterEnumDescriptor(_WITNESSEVENTDECISION)

WitnessEventDecision = enum_type_wrapper.EnumTypeWrapper(_WITNESSEVENTDECISION)
WITNESS_DECISION_CANT_DECIDE = 0
WITNESS_DECISION_MERGE_ALL_POSSIBLE = 1
WITNESS_DECISION_PARTIAL_MERGE_POSSIBLE = 2
WITNESS_DECISION_NO_MERGE_POSSIBLE = 3



_WITNESSEVENTS = _descriptor.Descriptor(
  name='WitnessEvents',
  full_name='detective.WitnessEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='detective.WitnessEvents.name', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=59,
)


_GETWITNESSMERGEREQUEST = _descriptor.Descriptor(
  name='GetWitnessMergeRequest',
  full_name='detective.GetWitnessMergeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='witness_events', full_name='detective.GetWitnessMergeRequest.witness_events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=135,
)


_GETWITNESSMERGEREPLY = _descriptor.Descriptor(
  name='GetWitnessMergeReply',
  full_name='detective.GetWitnessMergeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='decision', full_name='detective.GetWitnessMergeReply.decision', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='witness_events', full_name='detective.GetWitnessMergeReply.witness_events', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=260,
)

_GETWITNESSMERGEREQUEST.fields_by_name['witness_events'].message_type = _WITNESSEVENTS
_GETWITNESSMERGEREPLY.fields_by_name['decision'].enum_type = _WITNESSEVENTDECISION
_GETWITNESSMERGEREPLY.fields_by_name['witness_events'].message_type = _WITNESSEVENTS
DESCRIPTOR.message_types_by_name['WitnessEvents'] = _WITNESSEVENTS
DESCRIPTOR.message_types_by_name['GetWitnessMergeRequest'] = _GETWITNESSMERGEREQUEST
DESCRIPTOR.message_types_by_name['GetWitnessMergeReply'] = _GETWITNESSMERGEREPLY
DESCRIPTOR.enum_types_by_name['WitnessEventDecision'] = _WITNESSEVENTDECISION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WitnessEvents = _reflection.GeneratedProtocolMessageType('WitnessEvents', (_message.Message,), dict(
  DESCRIPTOR = _WITNESSEVENTS,
  __module__ = 'detective_pb2'
  # @@protoc_insertion_point(class_scope:detective.WitnessEvents)
  ))
_sym_db.RegisterMessage(WitnessEvents)

GetWitnessMergeRequest = _reflection.GeneratedProtocolMessageType('GetWitnessMergeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETWITNESSMERGEREQUEST,
  __module__ = 'detective_pb2'
  # @@protoc_insertion_point(class_scope:detective.GetWitnessMergeRequest)
  ))
_sym_db.RegisterMessage(GetWitnessMergeRequest)

GetWitnessMergeReply = _reflection.GeneratedProtocolMessageType('GetWitnessMergeReply', (_message.Message,), dict(
  DESCRIPTOR = _GETWITNESSMERGEREPLY,
  __module__ = 'detective_pb2'
  # @@protoc_insertion_point(class_scope:detective.GetWitnessMergeReply)
  ))
_sym_db.RegisterMessage(GetWitnessMergeReply)



_DETECTIVESERVICE = _descriptor.ServiceDescriptor(
  name='DetectiveService',
  full_name='detective.DetectiveService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=447,
  serialized_end=560,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetWitnessMergeDecision',
    full_name='detective.DetectiveService.GetWitnessMergeDecision',
    index=0,
    containing_service=None,
    input_type=_GETWITNESSMERGEREQUEST,
    output_type=_GETWITNESSMERGEREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DETECTIVESERVICE)

DESCRIPTOR.services_by_name['DetectiveService'] = _DETECTIVESERVICE

# @@protoc_insertion_point(module_scope)