# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='auto_data.proto',
  package='',
  serialized_pb='\n\x0f\x61uto_data.proto\"<\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"\x1c\n\x0bItemManager\x12\r\n\x05items\x18\x01 \x03(\x05\",\n\x06\x46riend\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x11\n\tuser_name\x18\x02 \x01(\t\")\n\rFriendManager\x12\x18\n\x07\x66riends\x18\x01 \x03(\x0b\x32\x07.Friend\"o\n\x14\x43lientConnectionInfo\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x1b\n\x13gateway_server_name\x18\x02 \x01(\t\x12\x18\n\x10game_server_name\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\t')




_USER = descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user_id', full_name='User.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_name', full_name='User.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='User.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=19,
  serialized_end=79,
)


_ITEMMANAGER = descriptor.Descriptor(
  name='ItemManager',
  full_name='ItemManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='items', full_name='ItemManager.items', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=81,
  serialized_end=109,
)


_FRIEND = descriptor.Descriptor(
  name='Friend',
  full_name='Friend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user_id', full_name='Friend.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_name', full_name='Friend.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=111,
  serialized_end=155,
)


_FRIENDMANAGER = descriptor.Descriptor(
  name='FriendManager',
  full_name='FriendManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='friends', full_name='FriendManager.friends', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=157,
  serialized_end=198,
)


_CLIENTCONNECTIONINFO = descriptor.Descriptor(
  name='ClientConnectionInfo',
  full_name='ClientConnectionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='client_id', full_name='ClientConnectionInfo.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gateway_server_name', full_name='ClientConnectionInfo.gateway_server_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_server_name', full_name='ClientConnectionInfo.game_server_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='token', full_name='ClientConnectionInfo.token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=200,
  serialized_end=311,
)

_FRIENDMANAGER.fields_by_name['friends'].message_type = _FRIEND
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['ItemManager'] = _ITEMMANAGER
DESCRIPTOR.message_types_by_name['Friend'] = _FRIEND
DESCRIPTOR.message_types_by_name['FriendManager'] = _FRIENDMANAGER
DESCRIPTOR.message_types_by_name['ClientConnectionInfo'] = _CLIENTCONNECTIONINFO

class User(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USER
  
  # @@protoc_insertion_point(class_scope:User)

class ItemManager(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMMANAGER
  
  # @@protoc_insertion_point(class_scope:ItemManager)

class Friend(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIEND
  
  # @@protoc_insertion_point(class_scope:Friend)

class FriendManager(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDMANAGER
  
  # @@protoc_insertion_point(class_scope:FriendManager)

class ClientConnectionInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLIENTCONNECTIONINFO
  
  # @@protoc_insertion_point(class_scope:ClientConnectionInfo)

# @@protoc_insertion_point(module_scope)
