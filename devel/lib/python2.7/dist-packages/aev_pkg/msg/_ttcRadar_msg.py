# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from aev_pkg/ttcRadar_msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ttcRadar_msg(genpy.Message):
  _md5sum = "68796b4398ded33c3293e6153473810f"
  _type = "aev_pkg/ttcRadar_msg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 numObj
uint8[] IdObj
bool[] isApproach
float32[] alpha
float32[] posX
float32[] posY
float32[] dis
float32[] vel
float32[] ttc
string[] safetyZone

uint32 msg_counter
bool isObject
float32 distance
"""
  __slots__ = ['numObj','IdObj','isApproach','alpha','posX','posY','dis','vel','ttc','safetyZone','msg_counter','isObject','distance']
  _slot_types = ['uint8','uint8[]','bool[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','string[]','uint32','bool','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       numObj,IdObj,isApproach,alpha,posX,posY,dis,vel,ttc,safetyZone,msg_counter,isObject,distance

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ttcRadar_msg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.numObj is None:
        self.numObj = 0
      if self.IdObj is None:
        self.IdObj = b''
      if self.isApproach is None:
        self.isApproach = []
      if self.alpha is None:
        self.alpha = []
      if self.posX is None:
        self.posX = []
      if self.posY is None:
        self.posY = []
      if self.dis is None:
        self.dis = []
      if self.vel is None:
        self.vel = []
      if self.ttc is None:
        self.ttc = []
      if self.safetyZone is None:
        self.safetyZone = []
      if self.msg_counter is None:
        self.msg_counter = 0
      if self.isObject is None:
        self.isObject = False
      if self.distance is None:
        self.distance = 0.
    else:
      self.numObj = 0
      self.IdObj = b''
      self.isApproach = []
      self.alpha = []
      self.posX = []
      self.posY = []
      self.dis = []
      self.vel = []
      self.ttc = []
      self.safetyZone = []
      self.msg_counter = 0
      self.isObject = False
      self.distance = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.numObj
      buff.write(_get_struct_B().pack(_x))
      _x = self.IdObj
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.isApproach)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(struct.Struct(pattern).pack(*self.isApproach))
      length = len(self.alpha)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.alpha))
      length = len(self.posX)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.posX))
      length = len(self.posY)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.posY))
      length = len(self.dis)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.dis))
      length = len(self.vel)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.vel))
      length = len(self.ttc)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.ttc))
      length = len(self.safetyZone)
      buff.write(_struct_I.pack(length))
      for val1 in self.safetyZone:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      _x = self
      buff.write(_get_struct_IBf().pack(_x.msg_counter, _x.isObject, _x.distance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.numObj,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.IdObj = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.isApproach = s.unpack(str[start:end])
      self.isApproach = list(map(bool, self.isApproach))
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.alpha = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.posX = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.posY = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.dis = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.vel = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ttc = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.safetyZone = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.safetyZone.append(val1)
      _x = self
      start = end
      end += 9
      (_x.msg_counter, _x.isObject, _x.distance,) = _get_struct_IBf().unpack(str[start:end])
      self.isObject = bool(self.isObject)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.numObj
      buff.write(_get_struct_B().pack(_x))
      _x = self.IdObj
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.isApproach)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(self.isApproach.tostring())
      length = len(self.alpha)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.alpha.tostring())
      length = len(self.posX)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.posX.tostring())
      length = len(self.posY)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.posY.tostring())
      length = len(self.dis)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.dis.tostring())
      length = len(self.vel)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.vel.tostring())
      length = len(self.ttc)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.ttc.tostring())
      length = len(self.safetyZone)
      buff.write(_struct_I.pack(length))
      for val1 in self.safetyZone:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      _x = self
      buff.write(_get_struct_IBf().pack(_x.msg_counter, _x.isObject, _x.distance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.numObj,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.IdObj = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.isApproach = numpy.frombuffer(str[start:end], dtype=numpy.bool, count=length)
      self.isApproach = list(map(bool, self.isApproach))
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.alpha = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.posX = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.posY = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.dis = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.vel = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ttc = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.safetyZone = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.safetyZone.append(val1)
      _x = self
      start = end
      end += 9
      (_x.msg_counter, _x.isObject, _x.distance,) = _get_struct_IBf().unpack(str[start:end])
      self.isObject = bool(self.isObject)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_IBf = None
def _get_struct_IBf():
    global _struct_IBf
    if _struct_IBf is None:
        _struct_IBf = struct.Struct("<IBf")
    return _struct_IBf
