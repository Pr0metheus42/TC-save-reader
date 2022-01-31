from construct import *
from construct.lib import *

tc__point = Struct(
	'x' / Int16sl,
	'y' / Int16sl,
)

tc__string = Struct(
	'len' / Int64ul,
	'content' / FixedSized(this.len, GreedyString(encoding='utf8')),
)

tc__circuit_path = Struct(
	'start' / LazyBound(lambda: tc__point),
	'body' / RepeatUntil(lambda obj_, list_, this: obj_.length == 0, LazyBound(lambda: tc__circuit_segment)),
	'end' / If( ((this.body[-1].direction == 1) and (this.body[-1].length == 0)) , LazyBound(lambda: tc__point)),
)

tc__circuit_segment = Struct(
	'direction' / ???,
	'length' / ???,
)

tc__circuit = Struct(
	'permanent_id' / Int64ul,
	'kind' / tc__circuit_kind(Int8ub),
	'color' / Int8ub,
	'comment' / LazyBound(lambda: tc__string),
	'path' / LazyBound(lambda: tc__circuit_path),
)

tc__component = Struct(
	'kind' / tc__component_kind(Int16ul),
	'position' / LazyBound(lambda: tc__point),
	'rotation' / Int8ub,
	'permanent_id' / Int64ul,
	'custom_string' / LazyBound(lambda: tc__string),
	'program_name' / If( (( ((this.kind.value > 63) and (this.kind.value < 69)) ) or (this.kind.value == 94)) , LazyBound(lambda: tc__string)),
	'custom_id' / If(this.kind.value == 92, Int64ul),
)

def tc__circuit_kind(subcon):
	return Enum(subcon,
		ck_bit=0,
		ck_byte=1,
		ck_qword=2,
	)

def tc__component_kind(subcon):
	return Enum(subcon,
		error=0,
		false=1,
		true=2,
		buffer=3,
		not=4,
		and=5,
		and3=6,
		nand=7,
		or=8,
		or3=9,
		nor=10,
		xor=11,
		xnor=12,
		bytecounter=13,
		virtualbytecounter=14,
		qwordcounter=15,
		virtualqwordcounter=16,
		ram=17,
		virtualram=18,
		qwordram=19,
		virtualqwordram=20,
		stack=21,
		virtualstack=22,
		register=23,
		virtualregister=24,
		registerred=25,
		virtualregisterred=26,
		registerredplus=27,
		virtualregisterredplus=28,
		qwordregister=29,
		virtualqwordregister=30,
		byteswitch=31,
		bytemux=32,
		decoder1=33,
		decoder3=34,
		byteconstant=35,
		bytenot=36,
		byteor=37,
		byteand=38,
		bytexor=39,
		byteequal=40,
		bytelessu=41,
		bytelessi=42,
		byteneg=43,
		byteadd=44,
		bytemul=45,
		bytesplitter=46,
		bytemaker=47,
		qwordsplitter=48,
		qwordmaker=49,
		fulladder=50,
		bitmemory=51,
		virtualbitmemory=52,
		srlatch=53,
		random=54,
		clock=55,
		waveformgenerator=56,
		httpclient=57,
		asciiscreen=58,
		keypad=59,
		filerom=60,
		halt=61,
		circuitcluster=62,
		screen=63,
		program1=64,
		program1red=65,
		program2=66,
		program3=67,
		program4=68,
		levelgate=69,
		input1=70,
		input2=71,
		input3=72,
		input4=73,
		input1bconditions=74,
		input1b=75,
		inputqword=76,
		input1bcode=77,
		input1_1b=78,
		output1=79,
		output1sum=80,
		output1car=81,
		output1aval=82,
		output1bval=83,
		output2=84,
		output3=85,
		output4=86,
		output1b=87,
		outputqword=88,
		output1_1b=89,
		outputcounter=90,
		inputoutput=91,
		custom=92,
		virtualcustom=93,
		qwordprogram=94,
		delaybuffer=95,
		virtualdelaybuffer=96,
		console=97,
		byteshl=98,
		byteshr=99,
		qwordconstant=100,
		qwordnot=101,
		qwordor=102,
		qwordand=103,
		qwordxor=104,
		qwordneg=105,
		qwordadd=106,
		qwordmul=107,
		qwordequal=108,
		qwordlessu=109,
		qwordlessi=110,
		qwordshl=111,
		qwordshr=112,
		qwordmux=113,
		qwordswitch=114,
		statebit=115,
		statebyte=116,
	)

tc = Struct(
	'magic' / FixedSized(1, GreedyBytes),
	'save_version' / Int64sl,
	'nand' / Int32ul,
	'delay' / Int32ul,
	'custom_visible' / Int8ub,
	'clock_speed' / Int32ul,
	'nesting_level' / Int8ub,
	'dependcy_count' / Int64ul,
	'dependecies' / Array(this.dependcy_count, Int64ul),
	'description' / LazyBound(lambda: tc__string),
	'unpacked' / Int8ub,
	'camera_position' / LazyBound(lambda: tc__point),
	'cached_design' / Int8ub,
	'component_count' / Int64ul,
	'components' / Array(this.component_count, LazyBound(lambda: tc__component)),
	'circuit_count' / Int64ul,
	'circuits' / Array(this.circuit_count, LazyBound(lambda: tc__circuit)),
)

_schema = tc
