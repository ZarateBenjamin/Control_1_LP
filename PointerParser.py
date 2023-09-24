# Generated from Pointer.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,73,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,40,8,3,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,3,5,49,8,5,1,5,1,5,1,5,3,5,54,8,5,1,6,1,
        6,1,6,1,6,1,7,1,7,1,7,1,7,4,7,64,8,7,11,7,12,7,65,1,8,3,8,69,8,8,
        1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,4,5,74,0,21,1,0,
        0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,35,1,0,0,0,8,41,1,0,0,0,10,43,1,
        0,0,0,12,55,1,0,0,0,14,59,1,0,0,0,16,68,1,0,0,0,18,20,3,2,1,0,19,
        18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,
        0,23,21,1,0,0,0,24,31,3,4,2,0,25,31,3,6,3,0,26,31,3,8,4,0,27,31,
        3,10,5,0,28,31,3,12,6,0,29,31,3,14,7,0,30,24,1,0,0,0,30,25,1,0,0,
        0,30,26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,3,1,
        0,0,0,32,33,5,1,0,0,33,34,5,15,0,0,34,5,1,0,0,0,35,36,5,2,0,0,36,
        39,3,16,8,0,37,38,5,3,0,0,38,40,3,16,8,0,39,37,1,0,0,0,39,40,1,0,
        0,0,40,7,1,0,0,0,41,42,7,0,0,0,42,9,1,0,0,0,43,48,5,6,0,0,44,45,
        5,7,0,0,45,46,3,6,3,0,46,47,5,8,0,0,47,49,1,0,0,0,48,44,1,0,0,0,
        48,49,1,0,0,0,49,50,1,0,0,0,50,53,3,16,8,0,51,52,5,3,0,0,52,54,3,
        16,8,0,53,51,1,0,0,0,53,54,1,0,0,0,54,11,1,0,0,0,55,56,5,9,0,0,56,
        57,5,10,0,0,57,58,5,15,0,0,58,13,1,0,0,0,59,60,5,11,0,0,60,61,5,
        15,0,0,61,63,5,12,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,65,1,0,0,0,
        65,63,1,0,0,0,65,66,1,0,0,0,66,15,1,0,0,0,67,69,5,13,0,0,68,67,1,
        0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,5,15,0,0,71,17,1,0,0,0,7,
        21,30,39,48,53,65,68
    ]

class PointerParser ( Parser ):

    grammarFileName = "Pointer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select'", "'avanza'", "','", "'dibuja'", 
                     "'desplaza'", "'rota'", "'('", "')'", "'mirar'", "'a'", 
                     "'repite'", "':'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS" ]

    RULE_start = 0
    RULE_instruction = 1
    RULE_selectPointer = 2
    RULE_advance = 3
    RULE_toggleDraw = 4
    RULE_rotate = 5
    RULE_lookAt = 6
    RULE_repeat = 7
    RULE_intVal = 8

    ruleNames =  [ "start", "instruction", "selectPointer", "advance", "toggleDraw", 
                   "rotate", "lookAt", "repeat", "intVal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    ID=14
    INT=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PointerParser.InstructionContext)
            else:
                return self.getTypedRuleContext(PointerParser.InstructionContext,i)


        def getRuleIndex(self):
            return PointerParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = PointerParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2678) != 0):
                self.state = 18
                self.instruction()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectPointer(self):
            return self.getTypedRuleContext(PointerParser.SelectPointerContext,0)


        def advance(self):
            return self.getTypedRuleContext(PointerParser.AdvanceContext,0)


        def toggleDraw(self):
            return self.getTypedRuleContext(PointerParser.ToggleDrawContext,0)


        def rotate(self):
            return self.getTypedRuleContext(PointerParser.RotateContext,0)


        def lookAt(self):
            return self.getTypedRuleContext(PointerParser.LookAtContext,0)


        def repeat(self):
            return self.getTypedRuleContext(PointerParser.RepeatContext,0)


        def getRuleIndex(self):
            return PointerParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = PointerParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.selectPointer()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.advance()
                pass
            elif token in [4, 5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.toggleDraw()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.rotate()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 28
                self.lookAt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 29
                self.repeat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectPointerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PointerParser.INT, 0)

        def getRuleIndex(self):
            return PointerParser.RULE_selectPointer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectPointer" ):
                listener.enterSelectPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectPointer" ):
                listener.exitSelectPointer(self)




    def selectPointer(self):

        localctx = PointerParser.SelectPointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectPointer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(PointerParser.T__0)
            self.state = 33
            self.match(PointerParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdvanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intVal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PointerParser.IntValContext)
            else:
                return self.getTypedRuleContext(PointerParser.IntValContext,i)


        def getRuleIndex(self):
            return PointerParser.RULE_advance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdvance" ):
                listener.enterAdvance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdvance" ):
                listener.exitAdvance(self)




    def advance(self):

        localctx = PointerParser.AdvanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_advance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(PointerParser.T__1)
            self.state = 36
            self.intVal()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 37
                self.match(PointerParser.T__2)
                self.state = 38
                self.intVal()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToggleDrawContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PointerParser.RULE_toggleDraw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToggleDraw" ):
                listener.enterToggleDraw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToggleDraw" ):
                listener.exitToggleDraw(self)




    def toggleDraw(self):

        localctx = PointerParser.ToggleDrawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_toggleDraw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RotateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intVal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PointerParser.IntValContext)
            else:
                return self.getTypedRuleContext(PointerParser.IntValContext,i)


        def advance(self):
            return self.getTypedRuleContext(PointerParser.AdvanceContext,0)


        def getRuleIndex(self):
            return PointerParser.RULE_rotate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRotate" ):
                listener.enterRotate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRotate" ):
                listener.exitRotate(self)




    def rotate(self):

        localctx = PointerParser.RotateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rotate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(PointerParser.T__5)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 44
                self.match(PointerParser.T__6)
                self.state = 45
                self.advance()
                self.state = 46
                self.match(PointerParser.T__7)


            self.state = 50
            self.intVal()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 51
                self.match(PointerParser.T__2)
                self.state = 52
                self.intVal()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LookAtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PointerParser.INT, 0)

        def getRuleIndex(self):
            return PointerParser.RULE_lookAt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLookAt" ):
                listener.enterLookAt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLookAt" ):
                listener.exitLookAt(self)




    def lookAt(self):

        localctx = PointerParser.LookAtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lookAt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(PointerParser.T__8)
            self.state = 56
            self.match(PointerParser.T__9)
            self.state = 57
            self.match(PointerParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PointerParser.INT, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PointerParser.InstructionContext)
            else:
                return self.getTypedRuleContext(PointerParser.InstructionContext,i)


        def getRuleIndex(self):
            return PointerParser.RULE_repeat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)




    def repeat(self):

        localctx = PointerParser.RepeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_repeat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(PointerParser.T__10)
            self.state = 60
            self.match(PointerParser.INT)
            self.state = 61
            self.match(PointerParser.T__11)
            self.state = 63 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 62
                    self.instruction()

                else:
                    raise NoViableAltException(self)
                self.state = 65 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PointerParser.INT, 0)

        def getRuleIndex(self):
            return PointerParser.RULE_intVal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntVal" ):
                listener.enterIntVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntVal" ):
                listener.exitIntVal(self)




    def intVal(self):

        localctx = PointerParser.IntValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_intVal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 67
                self.match(PointerParser.T__12)


            self.state = 70
            self.match(PointerParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





