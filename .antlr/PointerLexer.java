// Generated from c:\\Users\\zarat\\Desktop\\Año 4 S2\\Leng-Progra\\Control_1_LP\\Pointer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PointerLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, ID=14, INT=15, WS=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "ID", "INT", "WS"
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


	public PointerLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Pointer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22|\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3"+
		"\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\7\17b\n\17\f\17\16\17e\13\17\3\20\5"+
		"\20h\n\20\3\20\6\20k\n\20\r\20\16\20l\3\20\6\20p\n\20\r\20\16\20q\5\20"+
		"t\n\20\3\21\6\21w\n\21\r\21\16\21x\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13"+
		"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3\2\6\5\2"+
		"C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2\u0081\2\3\3\2\2\2"+
		"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2"+
		"\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2"+
		"\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5*\3\2\2"+
		"\2\7\61\3\2\2\2\t\63\3\2\2\2\13:\3\2\2\2\rC\3\2\2\2\17H\3\2\2\2\21J\3"+
		"\2\2\2\23L\3\2\2\2\25R\3\2\2\2\27T\3\2\2\2\31[\3\2\2\2\33]\3\2\2\2\35"+
		"_\3\2\2\2\37s\3\2\2\2!v\3\2\2\2#$\7u\2\2$%\7g\2\2%&\7n\2\2&\'\7g\2\2\'"+
		"(\7e\2\2()\7v\2\2)\4\3\2\2\2*+\7c\2\2+,\7x\2\2,-\7c\2\2-.\7p\2\2./\7|"+
		"\2\2/\60\7c\2\2\60\6\3\2\2\2\61\62\7.\2\2\62\b\3\2\2\2\63\64\7f\2\2\64"+
		"\65\7k\2\2\65\66\7d\2\2\66\67\7w\2\2\678\7l\2\289\7c\2\29\n\3\2\2\2:;"+
		"\7f\2\2;<\7g\2\2<=\7u\2\2=>\7r\2\2>?\7n\2\2?@\7c\2\2@A\7|\2\2AB\7c\2\2"+
		"B\f\3\2\2\2CD\7t\2\2DE\7q\2\2EF\7v\2\2FG\7c\2\2G\16\3\2\2\2HI\7*\2\2I"+
		"\20\3\2\2\2JK\7+\2\2K\22\3\2\2\2LM\7o\2\2MN\7k\2\2NO\7t\2\2OP\7c\2\2P"+
		"Q\7t\2\2Q\24\3\2\2\2RS\7c\2\2S\26\3\2\2\2TU\7t\2\2UV\7g\2\2VW\7r\2\2W"+
		"X\7k\2\2XY\7v\2\2YZ\7g\2\2Z\30\3\2\2\2[\\\7<\2\2\\\32\3\2\2\2]^\7/\2\2"+
		"^\34\3\2\2\2_c\t\2\2\2`b\t\3\2\2a`\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2"+
		"\2d\36\3\2\2\2ec\3\2\2\2fh\7/\2\2gf\3\2\2\2gh\3\2\2\2hj\3\2\2\2ik\t\4"+
		"\2\2ji\3\2\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2\2\2mt\3\2\2\2np\t\4\2\2on\3\2"+
		"\2\2pq\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2sg\3\2\2\2so\3\2\2\2t \3\2"+
		"\2\2uw\t\5\2\2vu\3\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\b\21"+
		"\2\2{\"\3\2\2\2\t\2cglqsx\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}