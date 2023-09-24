# Generated from Pointer.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PointerParser import PointerParser
else:
    from PointerParser import PointerParser

# This class defines a complete listener for a parse tree produced by PointerParser.
class PointerListener(ParseTreeListener):

    # Enter a parse tree produced by PointerParser#start.
    def enterStart(self, ctx:PointerParser.StartContext):
        pass

    # Exit a parse tree produced by PointerParser#start.
    def exitStart(self, ctx:PointerParser.StartContext):
        pass


    # Enter a parse tree produced by PointerParser#instruction.
    def enterInstruction(self, ctx:PointerParser.InstructionContext):
        pass

    # Exit a parse tree produced by PointerParser#instruction.
    def exitInstruction(self, ctx:PointerParser.InstructionContext):
        pass


    # Enter a parse tree produced by PointerParser#selectPointer.
    def enterSelectPointer(self, ctx:PointerParser.SelectPointerContext):
        pass

    # Exit a parse tree produced by PointerParser#selectPointer.
    def exitSelectPointer(self, ctx:PointerParser.SelectPointerContext):
        pass


    # Enter a parse tree produced by PointerParser#advance.
    def enterAdvance(self, ctx:PointerParser.AdvanceContext):
        pass

    # Exit a parse tree produced by PointerParser#advance.
    def exitAdvance(self, ctx:PointerParser.AdvanceContext):
        pass


    # Enter a parse tree produced by PointerParser#toggleDraw.
    def enterToggleDraw(self, ctx:PointerParser.ToggleDrawContext):
        pass

    # Exit a parse tree produced by PointerParser#toggleDraw.
    def exitToggleDraw(self, ctx:PointerParser.ToggleDrawContext):
        pass


    # Enter a parse tree produced by PointerParser#rotate.
    def enterRotate(self, ctx:PointerParser.RotateContext):
        pass

    # Exit a parse tree produced by PointerParser#rotate.
    def exitRotate(self, ctx:PointerParser.RotateContext):
        pass


    # Enter a parse tree produced by PointerParser#lookAt.
    def enterLookAt(self, ctx:PointerParser.LookAtContext):
        pass

    # Exit a parse tree produced by PointerParser#lookAt.
    def exitLookAt(self, ctx:PointerParser.LookAtContext):
        pass


    # Enter a parse tree produced by PointerParser#repeat.
    def enterRepeat(self, ctx:PointerParser.RepeatContext):
        pass

    # Exit a parse tree produced by PointerParser#repeat.
    def exitRepeat(self, ctx:PointerParser.RepeatContext):
        pass


    # Enter a parse tree produced by PointerParser#intVal.
    def enterIntVal(self, ctx:PointerParser.IntValContext):
        pass

    # Exit a parse tree produced by PointerParser#intVal.
    def exitIntVal(self, ctx:PointerParser.IntValContext):
        pass



del PointerParser