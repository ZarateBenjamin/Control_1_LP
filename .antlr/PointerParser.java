// Generated from c:\\Users\\zarat\\Desktop\\Año 4 S2\\Leng-Progra\\Control_1_LP\\Pointer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PointerParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, ID=14, INT=15, WS=16;
	public static final int
		RULE_start = 0, RULE_instruction = 1, RULE_selectPointer = 2, RULE_advance = 3, 
		RULE_toggleDraw = 4, RULE_rotate = 5, RULE_lookAt = 6, RULE_repeat = 7, 
		RULE_intVal = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "instruction", "selectPointer", "advance", "toggleDraw", "rotate", 
			"lookAt", "repeat", "intVal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'select'", "'avanza'", "','", "'dibuja'", "'desplaza'", "'rota'", 
			"'('", "')'", "'mirar'", "'a'", "'repite'", "':'", "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, "ID", "INT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Pointer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PointerParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public List<InstructionContext> instruction() {
			return getRuleContexts(InstructionContext.class);
		}
		public InstructionContext instruction(int i) {
			return getRuleContext(InstructionContext.class,i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(21);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__8) | (1L << T__10))) != 0)) {
				{
				{
				setState(18);
				instruction();
				}
				}
				setState(23);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstructionContext extends ParserRuleContext {
		public SelectPointerContext selectPointer() {
			return getRuleContext(SelectPointerContext.class,0);
		}
		public AdvanceContext advance() {
			return getRuleContext(AdvanceContext.class,0);
		}
		public ToggleDrawContext toggleDraw() {
			return getRuleContext(ToggleDrawContext.class,0);
		}
		public RotateContext rotate() {
			return getRuleContext(RotateContext.class,0);
		}
		public LookAtContext lookAt() {
			return getRuleContext(LookAtContext.class,0);
		}
		public RepeatContext repeat() {
			return getRuleContext(RepeatContext.class,0);
		}
		public InstructionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruction; }
	}

	public final InstructionContext instruction() throws RecognitionException {
		InstructionContext _localctx = new InstructionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instruction);
		try {
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(24);
				selectPointer();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(25);
				advance();
				}
				break;
			case T__3:
			case T__4:
				enterOuterAlt(_localctx, 3);
				{
				setState(26);
				toggleDraw();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 4);
				{
				setState(27);
				rotate();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 5);
				{
				setState(28);
				lookAt();
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 6);
				{
				setState(29);
				repeat();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SelectPointerContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(PointerParser.INT, 0); }
		public SelectPointerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectPointer; }
	}

	public final SelectPointerContext selectPointer() throws RecognitionException {
		SelectPointerContext _localctx = new SelectPointerContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_selectPointer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(T__0);
			setState(33);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AdvanceContext extends ParserRuleContext {
		public List<IntValContext> intVal() {
			return getRuleContexts(IntValContext.class);
		}
		public IntValContext intVal(int i) {
			return getRuleContext(IntValContext.class,i);
		}
		public AdvanceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_advance; }
	}

	public final AdvanceContext advance() throws RecognitionException {
		AdvanceContext _localctx = new AdvanceContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_advance);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(T__1);
			setState(36);
			intVal();
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(37);
				match(T__2);
				setState(38);
				intVal();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ToggleDrawContext extends ParserRuleContext {
		public ToggleDrawContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_toggleDraw; }
	}

	public final ToggleDrawContext toggleDraw() throws RecognitionException {
		ToggleDrawContext _localctx = new ToggleDrawContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_toggleDraw);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			_la = _input.LA(1);
			if ( !(_la==T__3 || _la==T__4) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RotateContext extends ParserRuleContext {
		public List<IntValContext> intVal() {
			return getRuleContexts(IntValContext.class);
		}
		public IntValContext intVal(int i) {
			return getRuleContext(IntValContext.class,i);
		}
		public AdvanceContext advance() {
			return getRuleContext(AdvanceContext.class,0);
		}
		public RotateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rotate; }
	}

	public final RotateContext rotate() throws RecognitionException {
		RotateContext _localctx = new RotateContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_rotate);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			match(T__5);
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(44);
				match(T__6);
				setState(45);
				advance();
				setState(46);
				match(T__7);
				}
			}

			setState(50);
			intVal();
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(51);
				match(T__2);
				setState(52);
				intVal();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LookAtContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(PointerParser.INT, 0); }
		public LookAtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lookAt; }
	}

	public final LookAtContext lookAt() throws RecognitionException {
		LookAtContext _localctx = new LookAtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_lookAt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(T__8);
			setState(56);
			match(T__9);
			setState(57);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RepeatContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(PointerParser.INT, 0); }
		public List<InstructionContext> instruction() {
			return getRuleContexts(InstructionContext.class);
		}
		public InstructionContext instruction(int i) {
			return getRuleContext(InstructionContext.class,i);
		}
		public RepeatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeat; }
	}

	public final RepeatContext repeat() throws RecognitionException {
		RepeatContext _localctx = new RepeatContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_repeat);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(T__10);
			setState(60);
			match(INT);
			setState(61);
			match(T__11);
			setState(63); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(62);
					instruction();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(65); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntValContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(PointerParser.INT, 0); }
		public IntValContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intVal; }
	}

	public final IntValContext intVal() throws RecognitionException {
		IntValContext _localctx = new IntValContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_intVal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(67);
				match(T__12);
				}
			}

			setState(70);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22K\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26"+
		"\n\2\f\2\16\2\31\13\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\5"+
		"\3\5\3\5\3\5\5\5*\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\63\n\7\3\7\3\7\3"+
		"\7\5\78\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\6\tB\n\t\r\t\16\tC\3\n\5\n"+
		"G\n\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2\6\7\2L\2\27\3\2"+
		"\2\2\4 \3\2\2\2\6\"\3\2\2\2\b%\3\2\2\2\n+\3\2\2\2\f-\3\2\2\2\169\3\2\2"+
		"\2\20=\3\2\2\2\22F\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26\31\3\2\2\2\27"+
		"\25\3\2\2\2\27\30\3\2\2\2\30\3\3\2\2\2\31\27\3\2\2\2\32!\5\6\4\2\33!\5"+
		"\b\5\2\34!\5\n\6\2\35!\5\f\7\2\36!\5\16\b\2\37!\5\20\t\2 \32\3\2\2\2 "+
		"\33\3\2\2\2 \34\3\2\2\2 \35\3\2\2\2 \36\3\2\2\2 \37\3\2\2\2!\5\3\2\2\2"+
		"\"#\7\3\2\2#$\7\21\2\2$\7\3\2\2\2%&\7\4\2\2&)\5\22\n\2\'(\7\5\2\2(*\5"+
		"\22\n\2)\'\3\2\2\2)*\3\2\2\2*\t\3\2\2\2+,\t\2\2\2,\13\3\2\2\2-\62\7\b"+
		"\2\2./\7\t\2\2/\60\5\b\5\2\60\61\7\n\2\2\61\63\3\2\2\2\62.\3\2\2\2\62"+
		"\63\3\2\2\2\63\64\3\2\2\2\64\67\5\22\n\2\65\66\7\5\2\2\668\5\22\n\2\67"+
		"\65\3\2\2\2\678\3\2\2\28\r\3\2\2\29:\7\13\2\2:;\7\f\2\2;<\7\21\2\2<\17"+
		"\3\2\2\2=>\7\r\2\2>?\7\21\2\2?A\7\16\2\2@B\5\4\3\2A@\3\2\2\2BC\3\2\2\2"+
		"CA\3\2\2\2CD\3\2\2\2D\21\3\2\2\2EG\7\17\2\2FE\3\2\2\2FG\3\2\2\2GH\3\2"+
		"\2\2HI\7\21\2\2I\23\3\2\2\2\t\27 )\62\67CF";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}