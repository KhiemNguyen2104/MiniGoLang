# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01ea\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\3\3\3\5\3\u0092\n\3\3\3")
        buf.write("\6\3\u0095\n\3\r\3\16\3\u0096\3\4\3\4\3\4\3\5\3\5\3\6")
        buf.write("\3\6\3\6\5\6\u00a1\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-")
        buf.write("\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3")
        buf.write("\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\3\67\38\3")
        buf.write("8\38\38\38\39\39\39\39\39\39\3:\3:\3:\7:\u0165\n:\f:\16")
        buf.write(":\u0168\13:\5:\u016a\n:\3;\3;\3;\3;\5;\u0170\n;\3;\6;")
        buf.write("\u0173\n;\r;\16;\u0174\3<\3<\3<\3<\5<\u017b\n<\3<\6<\u017e")
        buf.write("\n<\r<\16<\u017f\3=\3=\3=\3=\5=\u0186\n=\3=\6=\u0189\n")
        buf.write("=\r=\16=\u018a\3>\3>\3>\7>\u0190\n>\f>\16>\u0193\13>\5")
        buf.write(">\u0195\n>\3>\3>\7>\u0199\n>\f>\16>\u019c\13>\3>\5>\u019f")
        buf.write("\n>\3?\3?\3?\7?\u01a4\n?\f?\16?\u01a7\13?\3?\3?\3?\3@")
        buf.write("\6@\u01ad\n@\r@\16@\u01ae\3@\7@\u01b2\n@\f@\16@\u01b5")
        buf.write("\13@\3A\6A\u01b8\nA\rA\16A\u01b9\3A\3A\3B\6B\u01bf\nB")
        buf.write("\rB\16B\u01c0\3B\3B\3C\3C\3C\3C\7C\u01c9\nC\fC\16C\u01cc")
        buf.write("\13C\3C\3C\3D\3D\3D\3D\7D\u01d4\nD\fD\16D\u01d7\13D\3")
        buf.write("D\3D\3D\3D\3D\3E\3E\3E\7E\u01e1\nE\fE\16E\u01e4\13E\3")
        buf.write("E\5E\u01e7\nE\3F\3F\3\u01d5\2G\3\2\5\2\7\2\t\2\13\2\r")
        buf.write("\3\17\4\21\5\23\6\25\7\27\b\31\t\33\n\35\13\37\f!\r#\16")
        buf.write("%\17\'\20)\21+\22-\23/\24\61\25\63\26\65\27\67\309\31")
        buf.write(";\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)[*]+_,a")
        buf.write("-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8y9{:};\177<\u0081")
        buf.write("=\u0083>\u0085?\u0087@\u0089A\u008bB\3\2\17\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\6\2\f\f\17\17$$^^\3\2\63;\3\2\62\63\3\2")
        buf.write("\629\5\2\62;CHch\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17")
        buf.write("\17\4\2\13\13\"\"\4\3\f\f\17\17\2\u01fe\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\3\u008d\3\2\2\2\5\u008f\3\2\2\2\7\u0098\3\2\2\2\t\u009b")
        buf.write("\3\2\2\2\13\u00a0\3\2\2\2\r\u00a2\3\2\2\2\17\u00a6\3\2")
        buf.write("\2\2\21\u00ac\3\2\2\2\23\u00b3\3\2\2\2\25\u00bb\3\2\2")
        buf.write("\2\27\u00c1\3\2\2\2\31\u00c5\3\2\2\2\33\u00cc\3\2\2\2")
        buf.write("\35\u00d1\3\2\2\2\37\u00d6\3\2\2\2!\u00dd\3\2\2\2#\u00e7")
        buf.write("\3\2\2\2%\u00ea\3\2\2\2\'\u00ef\3\2\2\2)\u00f3\3\2\2\2")
        buf.write("+\u00fc\3\2\2\2-\u0102\3\2\2\2/\u0108\3\2\2\2\61\u010a")
        buf.write("\3\2\2\2\63\u010c\3\2\2\2\65\u010e\3\2\2\2\67\u0110\3")
        buf.write("\2\2\29\u0112\3\2\2\2;\u0115\3\2\2\2=\u0118\3\2\2\2?\u011a")
        buf.write("\3\2\2\2A\u011d\3\2\2\2C\u011f\3\2\2\2E\u0122\3\2\2\2")
        buf.write("G\u0125\3\2\2\2I\u0128\3\2\2\2K\u012a\3\2\2\2M\u012c\3")
        buf.write("\2\2\2O\u012f\3\2\2\2Q\u0132\3\2\2\2S\u0135\3\2\2\2U\u0138")
        buf.write("\3\2\2\2W\u013b\3\2\2\2Y\u013e\3\2\2\2[\u0140\3\2\2\2")
        buf.write("]\u0142\3\2\2\2_\u0144\3\2\2\2a\u0146\3\2\2\2c\u0148\3")
        buf.write("\2\2\2e\u014a\3\2\2\2g\u014c\3\2\2\2i\u014e\3\2\2\2k\u0150")
        buf.write("\3\2\2\2m\u0152\3\2\2\2o\u0156\3\2\2\2q\u015b\3\2\2\2")
        buf.write("s\u0169\3\2\2\2u\u016f\3\2\2\2w\u017a\3\2\2\2y\u0185\3")
        buf.write("\2\2\2{\u0194\3\2\2\2}\u01a0\3\2\2\2\177\u01ac\3\2\2\2")
        buf.write("\u0081\u01b7\3\2\2\2\u0083\u01be\3\2\2\2\u0085\u01c4\3")
        buf.write("\2\2\2\u0087\u01cf\3\2\2\2\u0089\u01dd\3\2\2\2\u008b\u01e8")
        buf.write("\3\2\2\2\u008d\u008e\t\2\2\2\u008e\4\3\2\2\2\u008f\u0091")
        buf.write("\t\3\2\2\u0090\u0092\t\4\2\2\u0091\u0090\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0095\5\3\2\2")
        buf.write("\u0094\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094\3")
        buf.write("\2\2\2\u0096\u0097\3\2\2\2\u0097\6\3\2\2\2\u0098\u0099")
        buf.write("\7^\2\2\u0099\u009a\13\2\2\2\u009a\b\3\2\2\2\u009b\u009c")
        buf.write("\n\5\2\2\u009c\n\3\2\2\2\u009d\u00a1\5E#\2\u009e\u00a1")
        buf.write("\5G$\2\u009f\u00a1\5I%\2\u00a0\u009d\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\f\3\2\2\2\u00a2\u00a3")
        buf.write("\7k\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5\7v\2\2\u00a5\16")
        buf.write("\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9")
        buf.write("\7q\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7v\2\2\u00ab\20")
        buf.write("\3\2\2\2\u00ac\u00ad\7u\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af")
        buf.write("\7t\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7i\2\2\u00b2\22\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7p\2\2\u00ba\24")
        buf.write("\3\2\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0\7v\2\2\u00c0\26")
        buf.write("\3\2\2\2\u00c1\u00c2\7x\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\30\3\2\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7p\2\2\u00cb\32\3\2\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7{\2\2\u00ce\u00cf\7r\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\34\3\2\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3")
        buf.write("\7w\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7e\2\2\u00d5\36")
        buf.write("\3\2\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7e\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc \3\2\2\2\u00dd\u00de\7k\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7h\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5")
        buf.write("\7e\2\2\u00e5\u00e6\7g\2\2\u00e6\"\3\2\2\2\u00e7\u00e8")
        buf.write("\7k\2\2\u00e8\u00e9\7h\2\2\u00e9$\3\2\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee&\3\2\2\2\u00ef\u00f0\7h\2\2\u00f0\u00f1")
        buf.write("\7q\2\2\u00f1\u00f2\7t\2\2\u00f2(\3\2\2\2\u00f3\u00f4")
        buf.write("\7e\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7w\2\2\u00fa\u00fb\7g\2\2\u00fb*\3\2\2\2\u00fc\u00fd")
        buf.write("\7d\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7m\2\2\u0101,\3\2\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7c\2\2\u0104\u0105\7p\2\2\u0105\u0106")
        buf.write("\7i\2\2\u0106\u0107\7g\2\2\u0107.\3\2\2\2\u0108\u0109")
        buf.write("\7-\2\2\u0109\60\3\2\2\2\u010a\u010b\7/\2\2\u010b\62\3")
        buf.write("\2\2\2\u010c\u010d\7,\2\2\u010d\64\3\2\2\2\u010e\u010f")
        buf.write("\7\61\2\2\u010f\66\3\2\2\2\u0110\u0111\7\'\2\2\u01118")
        buf.write("\3\2\2\2\u0112\u0113\7?\2\2\u0113\u0114\7?\2\2\u0114:")
        buf.write("\3\2\2\2\u0115\u0116\7#\2\2\u0116\u0117\7?\2\2\u0117<")
        buf.write("\3\2\2\2\u0118\u0119\7>\2\2\u0119>\3\2\2\2\u011a\u011b")
        buf.write("\7>\2\2\u011b\u011c\7?\2\2\u011c@\3\2\2\2\u011d\u011e")
        buf.write("\7@\2\2\u011eB\3\2\2\2\u011f\u0120\7@\2\2\u0120\u0121")
        buf.write("\7?\2\2\u0121D\3\2\2\2\u0122\u0123\7(\2\2\u0123\u0124")
        buf.write("\7(\2\2\u0124F\3\2\2\2\u0125\u0126\7~\2\2\u0126\u0127")
        buf.write("\7~\2\2\u0127H\3\2\2\2\u0128\u0129\7#\2\2\u0129J\3\2\2")
        buf.write("\2\u012a\u012b\7?\2\2\u012bL\3\2\2\2\u012c\u012d\7<\2")
        buf.write("\2\u012d\u012e\7?\2\2\u012eN\3\2\2\2\u012f\u0130\7-\2")
        buf.write("\2\u0130\u0131\7?\2\2\u0131P\3\2\2\2\u0132\u0133\7/\2")
        buf.write("\2\u0133\u0134\7?\2\2\u0134R\3\2\2\2\u0135\u0136\7,\2")
        buf.write("\2\u0136\u0137\7?\2\2\u0137T\3\2\2\2\u0138\u0139\7\61")
        buf.write("\2\2\u0139\u013a\7?\2\2\u013aV\3\2\2\2\u013b\u013c\7\'")
        buf.write("\2\2\u013c\u013d\7?\2\2\u013dX\3\2\2\2\u013e\u013f\7\60")
        buf.write("\2\2\u013fZ\3\2\2\2\u0140\u0141\7.\2\2\u0141\\\3\2\2\2")
        buf.write("\u0142\u0143\7<\2\2\u0143^\3\2\2\2\u0144\u0145\7=\2\2")
        buf.write("\u0145`\3\2\2\2\u0146\u0147\7*\2\2\u0147b\3\2\2\2\u0148")
        buf.write("\u0149\7+\2\2\u0149d\3\2\2\2\u014a\u014b\7]\2\2\u014b")
        buf.write("f\3\2\2\2\u014c\u014d\7_\2\2\u014dh\3\2\2\2\u014e\u014f")
        buf.write("\7}\2\2\u014fj\3\2\2\2\u0150\u0151\7\177\2\2\u0151l\3")
        buf.write("\2\2\2\u0152\u0153\7p\2\2\u0153\u0154\7k\2\2\u0154\u0155")
        buf.write("\7n\2\2\u0155n\3\2\2\2\u0156\u0157\7v\2\2\u0157\u0158")
        buf.write("\7t\2\2\u0158\u0159\7w\2\2\u0159\u015a\7g\2\2\u015ap\3")
        buf.write("\2\2\2\u015b\u015c\7h\2\2\u015c\u015d\7c\2\2\u015d\u015e")
        buf.write("\7n\2\2\u015e\u015f\7u\2\2\u015f\u0160\7g\2\2\u0160r\3")
        buf.write("\2\2\2\u0161\u016a\7\62\2\2\u0162\u0166\t\6\2\2\u0163")
        buf.write("\u0165\5\3\2\2\u0164\u0163\3\2\2\2\u0165\u0168\3\2\2\2")
        buf.write("\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u016a\3")
        buf.write("\2\2\2\u0168\u0166\3\2\2\2\u0169\u0161\3\2\2\2\u0169\u0162")
        buf.write("\3\2\2\2\u016at\3\2\2\2\u016b\u016c\7\62\2\2\u016c\u0170")
        buf.write("\7d\2\2\u016d\u016e\7\62\2\2\u016e\u0170\7D\2\2\u016f")
        buf.write("\u016b\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0172\3\2\2\2")
        buf.write("\u0171\u0173\t\7\2\2\u0172\u0171\3\2\2\2\u0173\u0174\3")
        buf.write("\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175v")
        buf.write("\3\2\2\2\u0176\u0177\7\62\2\2\u0177\u017b\7q\2\2\u0178")
        buf.write("\u0179\7\62\2\2\u0179\u017b\7Q\2\2\u017a\u0176\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u017e\t")
        buf.write("\b\2\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u017f\u0180\3\2\2\2\u0180x\3\2\2\2\u0181\u0182")
        buf.write("\7\62\2\2\u0182\u0186\7z\2\2\u0183\u0184\7\62\2\2\u0184")
        buf.write("\u0186\7Z\2\2\u0185\u0181\3\2\2\2\u0185\u0183\3\2\2\2")
        buf.write("\u0186\u0188\3\2\2\2\u0187\u0189\t\t\2\2\u0188\u0187\3")
        buf.write("\2\2\2\u0189\u018a\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b")
        buf.write("\3\2\2\2\u018bz\3\2\2\2\u018c\u0195\7\62\2\2\u018d\u0191")
        buf.write("\t\6\2\2\u018e\u0190\5\3\2\2\u018f\u018e\3\2\2\2\u0190")
        buf.write("\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u018c\3")
        buf.write("\2\2\2\u0194\u018d\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u019a")
        buf.write("\7\60\2\2\u0197\u0199\5\3\2\2\u0198\u0197\3\2\2\2\u0199")
        buf.write("\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2")
        buf.write("\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019f\5")
        buf.write("\5\3\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2\2\2\u019f|")
        buf.write("\3\2\2\2\u01a0\u01a5\7$\2\2\u01a1\u01a4\5\t\5\2\u01a2")
        buf.write("\u01a4\5\7\4\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3")
        buf.write("\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01a9")
        buf.write("\7$\2\2\u01a9\u01aa\b?\2\2\u01aa~\3\2\2\2\u01ab\u01ad")
        buf.write("\t\n\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b3\3\2\2\2")
        buf.write("\u01b0\u01b2\t\13\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u0080\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b8\t\f\2\2")
        buf.write("\u01b7\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01b7\3")
        buf.write("\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc")
        buf.write("\bA\3\2\u01bc\u0082\3\2\2\2\u01bd\u01bf\t\r\2\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c0\u01c1\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\b")
        buf.write("B\4\2\u01c3\u0084\3\2\2\2\u01c4\u01c5\7\61\2\2\u01c5\u01c6")
        buf.write("\7\61\2\2\u01c6\u01ca\3\2\2\2\u01c7\u01c9\n\f\2\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3")
        buf.write("\2\2\2\u01cd\u01ce\bC\4\2\u01ce\u0086\3\2\2\2\u01cf\u01d0")
        buf.write("\7\61\2\2\u01d0\u01d1\7,\2\2\u01d1\u01d5\3\2\2\2\u01d2")
        buf.write("\u01d4\13\2\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2")
        buf.write("\2\u01d5\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d8")
        buf.write("\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01d9\7,\2\2\u01d9")
        buf.write("\u01da\7\61\2\2\u01da\u01db\3\2\2\2\u01db\u01dc\bD\4\2")
        buf.write("\u01dc\u0088\3\2\2\2\u01dd\u01e2\7$\2\2\u01de\u01e1\5")
        buf.write("\t\5\2\u01df\u01e1\5\7\4\2\u01e0\u01de\3\2\2\2\u01e0\u01df")
        buf.write("\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e3\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e5\u01e7\t\16\2\2\u01e6\u01e5\3\2\2\2\u01e7\u008a")
        buf.write("\3\2\2\2\u01e8\u01e9\13\2\2\2\u01e9\u008c\3\2\2\2\35\2")
        buf.write("\u0091\u0096\u00a0\u0166\u0169\u016f\u0174\u017a\u017f")
        buf.write("\u0185\u018a\u0191\u0194\u019a\u019e\u01a3\u01a5\u01ae")
        buf.write("\u01b3\u01b9\u01c0\u01ca\u01d5\u01e0\u01e2\u01e6\5\3?")
        buf.write("\2\3A\3\b\2\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Key_type_int = 1
    Key_type_float = 2
    Key_type_string = 3
    Key_type_boolean = 4
    Key_decl_const = 5
    Key_decl_var = 6
    Key_return = 7
    Key_type = 8
    Key_func = 9
    Key_struct = 10
    Key_interface = 11
    Key_if = 12
    Key_else = 13
    Key_loop_for = 14
    Key_loop_continue = 15
    Key_loop_break = 16
    Key_range = 17
    Ope_plus = 18
    Ope_minus = 19
    Ope_multi = 20
    Ope_div = 21
    Ope_mod = 22
    Ope_equal = 23
    Ope_nequal = 24
    Ope_let = 25
    Ope_leq = 26
    Ope_get = 27
    Ope_geq = 28
    Ope_and = 29
    Ope_or = 30
    Ope_not = 31
    Ope_assign = 32
    Ope_init = 33
    Ope_assign_plus = 34
    Ope_assign_minus = 35
    Ope_assign_multi = 36
    Ope_assign_div = 37
    Ope_assign_mod = 38
    Ope_select = 39
    Comma = 40
    Colon = 41
    Semicolon = 42
    Lparen = 43
    Rparen = 44
    Lsquare = 45
    Rsquare = 46
    Lcurly = 47
    Rcurly = 48
    Literal_nil = 49
    Literal_true = 50
    Literal_false = 51
    Literal_dec = 52
    Literal_bin = 53
    Literal_oct = 54
    Literal_hex = 55
    Literal_float = 56
    Literal_string = 57
    Identifier = 58
    NL = 59
    WS = 60
    SL_COMMENT = 61
    ML_COMMENT = 62
    UNCLOSE_STRING = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'string'", "'boolean'", "'const'", "'var'", 
            "'return'", "'type'", "'func'", "'struct'", "'interface'", "'if'", 
            "'else'", "'for'", "'continue'", "'break'", "'range'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'&&'", "'||'", "'!'", "'='", "':='", "'+='", "'-='", 
            "'*='", "'/='", "'%='", "'.'", "','", "':'", "';'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'nil'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "Key_type_int", "Key_type_float", "Key_type_string", "Key_type_boolean", 
            "Key_decl_const", "Key_decl_var", "Key_return", "Key_type", 
            "Key_func", "Key_struct", "Key_interface", "Key_if", "Key_else", 
            "Key_loop_for", "Key_loop_continue", "Key_loop_break", "Key_range", 
            "Ope_plus", "Ope_minus", "Ope_multi", "Ope_div", "Ope_mod", 
            "Ope_equal", "Ope_nequal", "Ope_let", "Ope_leq", "Ope_get", 
            "Ope_geq", "Ope_and", "Ope_or", "Ope_not", "Ope_assign", "Ope_init", 
            "Ope_assign_plus", "Ope_assign_minus", "Ope_assign_multi", "Ope_assign_div", 
            "Ope_assign_mod", "Ope_select", "Comma", "Colon", "Semicolon", 
            "Lparen", "Rparen", "Lsquare", "Rsquare", "Lcurly", "Rcurly", 
            "Literal_nil", "Literal_true", "Literal_false", "Literal_dec", 
            "Literal_bin", "Literal_oct", "Literal_hex", "Literal_float", 
            "Literal_string", "Identifier", "NL", "WS", "SL_COMMENT", "ML_COMMENT", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "Digit", "Exp", "Escape", "Char", "Ope_for_boolean", "Key_type_int", 
                  "Key_type_float", "Key_type_string", "Key_type_boolean", 
                  "Key_decl_const", "Key_decl_var", "Key_return", "Key_type", 
                  "Key_func", "Key_struct", "Key_interface", "Key_if", "Key_else", 
                  "Key_loop_for", "Key_loop_continue", "Key_loop_break", 
                  "Key_range", "Ope_plus", "Ope_minus", "Ope_multi", "Ope_div", 
                  "Ope_mod", "Ope_equal", "Ope_nequal", "Ope_let", "Ope_leq", 
                  "Ope_get", "Ope_geq", "Ope_and", "Ope_or", "Ope_not", 
                  "Ope_assign", "Ope_init", "Ope_assign_plus", "Ope_assign_minus", 
                  "Ope_assign_multi", "Ope_assign_div", "Ope_assign_mod", 
                  "Ope_select", "Comma", "Colon", "Semicolon", "Lparen", 
                  "Rparen", "Lsquare", "Rsquare", "Lcurly", "Rcurly", "Literal_nil", 
                  "Literal_true", "Literal_false", "Literal_dec", "Literal_bin", 
                  "Literal_oct", "Literal_hex", "Literal_float", "Literal_string", 
                  "Identifier", "NL", "WS", "SL_COMMENT", "ML_COMMENT", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input=None, output:TextIO = sys.stdout):
            super().__init__(input, output)
            self.checkVersion("4.9.2")
            self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
            self._actions = None
            self._predicates = None
            self.last_token_type = None

    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit()
            if result.text[-1] == '\n' or result.text[-1] == '\r':
                result.text = result.text[0:-1]
            raise UncloseString(result.text[0:])
        elif tk == self.ERROR_CHAR:
            result = super().emit()
            raise ErrorToken(self.text)
        else:
            self.last_token_type = tk
            return super().emit()

    def check_previous_token_for_newline_token(self):
        return self.last_token_type in {
            self.Identifier,
            self.Literal_nil,
            self.Literal_true,
            self.Literal_false,
            self.Literal_dec,
            self.Literal_oct,
            self.Literal_bin,
            self.Literal_hex,
            self.Literal_float,
            self.Literal_string,
            self.Key_type_int,
            self.Key_type_float,
            self.Key_type_string,
            self.Key_type_boolean,
            self.Key_return,
            self.Key_loop_continue,
            self.Key_loop_break,
            self.Rparen,
            self.Rsquare,
            self.Rcurly
        }

    def replace_newline_char(self):
        if (self.check_previous_token_for_newline_token()):
            self.text = ';'
            self.type = self.Semicolon
        else:
            self.skip()

    def check_illegal_escape(self):
        str = self.text
        i = 0
        while i < len(str):
            if str[i] == '\\' and i != len(str) - 1 and str[i+1] == '\\':
                i += 2
            elif str[i] == '\\' and i != len(str) - 1 and not (str[i + 1] in {'t', 'r', 'n'}):
                raise IllegalEscape(str[:i+2])
            else:
                i += 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[61] = self.Literal_string_action 
            actions[63] = self.NL_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def Literal_string_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.check_illegal_escape()
     

    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.replace_newline_char() 
     


