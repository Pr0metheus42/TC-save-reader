# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Tc(KaitaiStruct):

    class CircuitKind(Enum):
        ck_bit = 0
        ck_byte = 1
        ck_qword = 2

    class ComponentKind(Enum):
        error = 0
        false = 1
        true = 2
        buffer = 3
        not = 4
        and = 5
        and3 = 6
        nand = 7
        or = 8
        or3 = 9
        nor = 10
        xor = 11
        xnor = 12
        bytecounter = 13
        virtualbytecounter = 14
        qwordcounter = 15
        virtualqwordcounter = 16
        ram = 17
        virtualram = 18
        qwordram = 19
        virtualqwordram = 20
        stack = 21
        virtualstack = 22
        register = 23
        virtualregister = 24
        registerred = 25
        virtualregisterred = 26
        registerredplus = 27
        virtualregisterredplus = 28
        qwordregister = 29
        virtualqwordregister = 30
        byteswitch = 31
        bytemux = 32
        decoder1 = 33
        decoder3 = 34
        byteconstant = 35
        bytenot = 36
        byteor = 37
        byteand = 38
        bytexor = 39
        byteequal = 40
        bytelessu = 41
        bytelessi = 42
        byteneg = 43
        byteadd = 44
        bytemul = 45
        bytesplitter = 46
        bytemaker = 47
        qwordsplitter = 48
        qwordmaker = 49
        fulladder = 50
        bitmemory = 51
        virtualbitmemory = 52
        srlatch = 53
        random = 54
        clock = 55
        waveformgenerator = 56
        httpclient = 57
        asciiscreen = 58
        keypad = 59
        filerom = 60
        halt = 61
        circuitcluster = 62
        screen = 63
        program1 = 64
        program1red = 65
        program2 = 66
        program3 = 67
        program4 = 68
        levelgate = 69
        input1 = 70
        input2 = 71
        input3 = 72
        input4 = 73
        input1bconditions = 74
        input1b = 75
        inputqword = 76
        input1bcode = 77
        input1_1b = 78
        output1 = 79
        output1sum = 80
        output1car = 81
        output1aval = 82
        output1bval = 83
        output2 = 84
        output3 = 85
        output4 = 86
        output1b = 87
        outputqword = 88
        output1_1b = 89
        outputcounter = 90
        inputoutput = 91
        custom = 92
        virtualcustom = 93
        qwordprogram = 94
        delaybuffer = 95
        virtualdelaybuffer = 96
        console = 97
        byteshl = 98
        byteshr = 99
        qwordconstant = 100
        qwordnot = 101
        qwordor = 102
        qwordand = 103
        qwordxor = 104
        qwordneg = 105
        qwordadd = 106
        qwordmul = 107
        qwordequal = 108
        qwordlessu = 109
        qwordlessi = 110
        qwordshl = 111
        qwordshr = 112
        qwordmux = 113
        qwordswitch = 114
        statebit = 115
        statebyte = 116
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(1)
        if not self.magic == b"\x01":
            raise kaitaistruct.ValidationNotEqualError(b"\x01", self.magic, self._io, u"/seq/0")
        self.save_version = self._io.read_s8le()
        self.nand = self._io.read_u4le()
        self.delay = self._io.read_u4le()
        self.custom_visible = self._io.read_u1()
        self.clock_speed = self._io.read_u4le()
        self.nesting_level = self._io.read_u1()
        self.dependcy_count = self._io.read_u8le()
        self.dependecies = [None] * (self.dependcy_count)
        for i in range(self.dependcy_count):
            self.dependecies[i] = self._io.read_u8le()

        self.description = Tc.String(self._io, self, self._root)
        self.unpacked = self._io.read_u1()
        self.camera_position = Tc.Point(self._io, self, self._root)
        self.cached_design = self._io.read_u1()
        self.component_count = self._io.read_u8le()
        self.components = [None] * (self.component_count)
        for i in range(self.component_count):
            self.components[i] = Tc.Component(self._io, self, self._root)

        self.circuit_count = self._io.read_u8le()
        self.circuits = [None] * (self.circuit_count)
        for i in range(self.circuit_count):
            self.circuits[i] = Tc.Circuit(self._io, self, self._root)


    class Point(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s2le()
            self.y = self._io.read_s2le()


    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_u8le()
            self.content = (self._io.read_bytes(self.len)).decode(u"utf8")


    class CircuitPath(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.start = Tc.Point(self._io, self, self._root)
            self.body = []
            i = 0
            while True:
                _ = Tc.CircuitSegment(self._io, self, self._root)
                self.body.append(_)
                if _.length == 0:
                    break
                i += 1
            if  ((self.body[-1].direction == 1) and (self.body[-1].length == 0)) :
                self.end = Tc.Point(self._io, self, self._root)



    class CircuitSegment(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.direction = self._io.read_bits_int_be(3)
            self.length = self._io.read_bits_int_be(5)


    class Circuit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.permanent_id = self._io.read_u8le()
            self.kind = KaitaiStream.resolve_enum(Tc.CircuitKind, self._io.read_u1())
            self.color = self._io.read_u1()
            self.comment = Tc.String(self._io, self, self._root)
            self.path = Tc.CircuitPath(self._io, self, self._root)


    class Component(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.kind = KaitaiStream.resolve_enum(Tc.ComponentKind, self._io.read_u2le())
            self.position = Tc.Point(self._io, self, self._root)
            self.rotation = self._io.read_u1()
            self.permanent_id = self._io.read_u8le()
            self.custom_string = Tc.String(self._io, self, self._root)
            if  (( ((self.kind.value > 63) and (self.kind.value < 69)) ) or (self.kind.value == 94)) :
                self.program_name = Tc.String(self._io, self, self._root)

            if self.kind.value == 92:
                self.custom_id = self._io.read_u8le()




