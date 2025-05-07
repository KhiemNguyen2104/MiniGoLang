# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u031d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\5\3\u00ce\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u00d5\n\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\5\7\u00e2\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00ee\n\t")
        buf.write("\3\n\3\n\3\n\5\n\u00f3\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u00fd\n\f\3\r\3\r\3\r\3\r\5\r\u0103\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\5\22\u0118\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\5\24")
        buf.write("\u0124\n\24\3\25\3\25\3\25\3\25\5\25\u012a\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\5\30\u013a\n\30\3\31\3\31\3\31\3\31\5\31\u0140")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u014f\n\32\3\33\3\33\5\33\u0153\n")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\5\34\u015a\n\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\5\36\u0163\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u017a\n")
        buf.write("\37\3 \3 \5 \u017e\n \3!\3!\3!\3!\3!\5!\u0185\n!\3\"\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3%\3%\5%\u0192\n%\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\5&\u01ab\n&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3")
        buf.write("(\7(\u01b8\n(\f(\16(\u01bb\13(\3)\3)\3)\3)\3)\3)\7)\u01c3")
        buf.write("\n)\f)\16)\u01c6\13)\3*\3*\3*\3*\3*\3*\3*\7*\u01cf\n*")
        buf.write("\f*\16*\u01d2\13*\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\7,")
        buf.write("\u01df\n,\f,\16,\u01e2\13,\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write("\3-\3-\3-\7-\u01f0\n-\f-\16-\u01f3\13-\3.\3.\3.\3.\3.")
        buf.write("\5.\u01fa\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\7/\u0207")
        buf.write("\n/\f/\16/\u020a\13/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\5\60\u0215\n\60\3\61\3\61\5\61\u0219\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\63\3\63\5\63\u0222\n\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u0229\n\64\3\65\3\65\3\66\3")
        buf.write("\66\3\66\3\66\3\66\5\66\u0232\n\66\3\67\3\67\38\38\39")
        buf.write("\39\39\39\39\39\39\39\39\59\u0241\n9\3:\3:\3:\3:\3:\3")
        buf.write(";\3;\3;\5;\u024b\n;\3<\3<\3<\3<\3<\7<\u0252\n<\f<\16<")
        buf.write("\u0255\13<\3=\3=\5=\u0259\n=\3>\3>\3>\3>\3?\3?\3?\3@\3")
        buf.write("@\3A\3A\3A\5A\u0267\nA\3B\3B\5B\u026b\nB\3C\3C\3C\3C\3")
        buf.write("C\3D\3D\3D\3D\3E\3E\5E\u0278\nE\3F\3F\3F\3F\3F\5F\u027f")
        buf.write("\nF\3G\3G\3G\5G\u0284\nG\3H\3H\3H\3H\3H\3I\3I\5I\u028d")
        buf.write("\nI\3J\3J\3J\3J\3J\5J\u0294\nJ\3K\3K\3K\3K\3L\3L\5L\u029c")
        buf.write("\nL\3M\3M\3M\3M\3M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3N\3N\3")
        buf.write("N\3N\3O\3O\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u02bc\nQ\3")
        buf.write("R\3R\3S\3S\3S\5S\u02c3\nS\3T\3T\3T\3T\3T\3T\3T\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\3U\3U\3U\3V\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\5V\u02e4\nV\3W\3W\3W\3W\3X\3X\3X\3X\3X\3X\3")
        buf.write("X\3X\3X\3X\3X\3X\3Y\3Y\3Y\5Y\u02f9\nY\3Z\3Z\3[\3[\3\\")
        buf.write("\3\\\3]\3]\3]\3^\3^\3^\3_\3_\5_\u0309\n_\3`\3`\3`\3a\3")
        buf.write("a\3a\3b\3b\3b\3b\3c\3c\3c\3c\3c\3c\5c\u031b\nc\3c\2\t")
        buf.write("NPRVX\\vd\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~")
        buf.write("\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write("\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2")
        buf.write("\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4")
        buf.write("\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\2\t\4")
        buf.write("\2,,==\3\2\3\6\4\2\669<<\3\2\31\36\3\2\669\3\2\64\65\3")
        buf.write("\2#(\2\u030b\2\u00c6\3\2\2\2\4\u00cd\3\2\2\2\6\u00d4\3")
        buf.write("\2\2\2\b\u00d6\3\2\2\2\n\u00dc\3\2\2\2\f\u00e1\3\2\2\2")
        buf.write("\16\u00e3\3\2\2\2\20\u00ed\3\2\2\2\22\u00f2\3\2\2\2\24")
        buf.write("\u00f4\3\2\2\2\26\u00fc\3\2\2\2\30\u0102\3\2\2\2\32\u0104")
        buf.write("\3\2\2\2\34\u0108\3\2\2\2\36\u010a\3\2\2\2 \u0110\3\2")
        buf.write("\2\2\"\u0117\3\2\2\2$\u0119\3\2\2\2&\u0123\3\2\2\2(\u0129")
        buf.write("\3\2\2\2*\u012b\3\2\2\2,\u012f\3\2\2\2.\u0139\3\2\2\2")
        buf.write("\60\u013f\3\2\2\2\62\u014e\3\2\2\2\64\u0152\3\2\2\2\66")
        buf.write("\u0159\3\2\2\28\u015b\3\2\2\2:\u0162\3\2\2\2<\u0179\3")
        buf.write("\2\2\2>\u017d\3\2\2\2@\u0184\3\2\2\2B\u0186\3\2\2\2D\u0189")
        buf.write("\3\2\2\2F\u018b\3\2\2\2H\u0191\3\2\2\2J\u01aa\3\2\2\2")
        buf.write("L\u01ac\3\2\2\2N\u01b1\3\2\2\2P\u01bc\3\2\2\2R\u01c7\3")
        buf.write("\2\2\2T\u01d3\3\2\2\2V\u01d5\3\2\2\2X\u01e3\3\2\2\2Z\u01f9")
        buf.write("\3\2\2\2\\\u01fb\3\2\2\2^\u0214\3\2\2\2`\u0218\3\2\2\2")
        buf.write("b\u021a\3\2\2\2d\u0221\3\2\2\2f\u0228\3\2\2\2h\u022a\3")
        buf.write("\2\2\2j\u0231\3\2\2\2l\u0233\3\2\2\2n\u0235\3\2\2\2p\u0240")
        buf.write("\3\2\2\2r\u0242\3\2\2\2t\u024a\3\2\2\2v\u024c\3\2\2\2")
        buf.write("x\u0258\3\2\2\2z\u025a\3\2\2\2|\u025e\3\2\2\2~\u0261\3")
        buf.write("\2\2\2\u0080\u0266\3\2\2\2\u0082\u026a\3\2\2\2\u0084\u026c")
        buf.write("\3\2\2\2\u0086\u0271\3\2\2\2\u0088\u0277\3\2\2\2\u008a")
        buf.write("\u027e\3\2\2\2\u008c\u0283\3\2\2\2\u008e\u0285\3\2\2\2")
        buf.write("\u0090\u028c\3\2\2\2\u0092\u0293\3\2\2\2\u0094\u0295\3")
        buf.write("\2\2\2\u0096\u029b\3\2\2\2\u0098\u029d\3\2\2\2\u009a\u02a6")
        buf.write("\3\2\2\2\u009c\u02af\3\2\2\2\u009e\u02b1\3\2\2\2\u00a0")
        buf.write("\u02bb\3\2\2\2\u00a2\u02bd\3\2\2\2\u00a4\u02c2\3\2\2\2")
        buf.write("\u00a6\u02c4\3\2\2\2\u00a8\u02cb\3\2\2\2\u00aa\u02e3\3")
        buf.write("\2\2\2\u00ac\u02e5\3\2\2\2\u00ae\u02e9\3\2\2\2\u00b0\u02f8")
        buf.write("\3\2\2\2\u00b2\u02fa\3\2\2\2\u00b4\u02fc\3\2\2\2\u00b6")
        buf.write("\u02fe\3\2\2\2\u00b8\u0300\3\2\2\2\u00ba\u0303\3\2\2\2")
        buf.write("\u00bc\u0308\3\2\2\2\u00be\u030a\3\2\2\2\u00c0\u030d\3")
        buf.write("\2\2\2\u00c2\u0310\3\2\2\2\u00c4\u031a\3\2\2\2\u00c6\u00c7")
        buf.write("\5\4\3\2\u00c7\u00c8\7\2\2\3\u00c8\3\3\2\2\2\u00c9\u00ca")
        buf.write("\5\6\4\2\u00ca\u00cb\5\4\3\2\u00cb\u00ce\3\2\2\2\u00cc")
        buf.write("\u00ce\5\6\4\2\u00cd\u00c9\3\2\2\2\u00cd\u00cc\3\2\2\2")
        buf.write("\u00ce\5\3\2\2\2\u00cf\u00d5\5\b\5\2\u00d0\u00d5\5\f\7")
        buf.write("\2\u00d1\u00d5\5\"\22\2\u00d2\u00d5\5<\37\2\u00d3\u00d5")
        buf.write("\5J&\2\u00d4\u00cf\3\2\2\2\u00d4\u00d0\3\2\2\2\u00d4\u00d1")
        buf.write("\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5")
        buf.write("\7\3\2\2\2\u00d6\u00d7\7\7\2\2\u00d7\u00d8\7<\2\2\u00d8")
        buf.write("\u00d9\7\"\2\2\u00d9\u00da\5\20\t\2\u00da\u00db\5\n\6")
        buf.write("\2\u00db\t\3\2\2\2\u00dc\u00dd\t\2\2\2\u00dd\13\3\2\2")
        buf.write("\2\u00de\u00e2\5\16\b\2\u00df\u00e2\5\36\20\2\u00e0\u00e2")
        buf.write("\5 \21\2\u00e1\u00de\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1")
        buf.write("\u00e0\3\2\2\2\u00e2\r\3\2\2\2\u00e3\u00e4\7\b\2\2\u00e4")
        buf.write("\u00e5\7<\2\2\u00e5\u00e6\5\22\n\2\u00e6\u00e7\7\"\2\2")
        buf.write("\u00e7\u00e8\5\20\t\2\u00e8\u00e9\5\n\6\2\u00e9\17\3\2")
        buf.write("\2\2\u00ea\u00ee\5N(\2\u00eb\u00ee\5\u0084C\2\u00ec\u00ee")
        buf.write("\5\u008eH\2\u00ed\u00ea\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ee\21\3\2\2\2\u00ef\u00f3\5\24\13\2")
        buf.write("\u00f0\u00f3\7<\2\2\u00f1\u00f3\5\26\f\2\u00f2\u00ef\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\23")
        buf.write("\3\2\2\2\u00f4\u00f5\t\3\2\2\u00f5\25\3\2\2\2\u00f6\u00f7")
        buf.write("\5\30\r\2\u00f7\u00f8\5\24\13\2\u00f8\u00fd\3\2\2\2\u00f9")
        buf.write("\u00fa\5\30\r\2\u00fa\u00fb\7<\2\2\u00fb\u00fd\3\2\2\2")
        buf.write("\u00fc\u00f6\3\2\2\2\u00fc\u00f9\3\2\2\2\u00fd\27\3\2")
        buf.write("\2\2\u00fe\u00ff\5\32\16\2\u00ff\u0100\5\30\r\2\u0100")
        buf.write("\u0103\3\2\2\2\u0101\u0103\5\32\16\2\u0102\u00fe\3\2\2")
        buf.write("\2\u0102\u0101\3\2\2\2\u0103\31\3\2\2\2\u0104\u0105\7")
        buf.write("/\2\2\u0105\u0106\5\34\17\2\u0106\u0107\7\60\2\2\u0107")
        buf.write("\33\3\2\2\2\u0108\u0109\t\4\2\2\u0109\35\3\2\2\2\u010a")
        buf.write("\u010b\7\b\2\2\u010b\u010c\7<\2\2\u010c\u010d\7\"\2\2")
        buf.write("\u010d\u010e\5\20\t\2\u010e\u010f\5\n\6\2\u010f\37\3\2")
        buf.write("\2\2\u0110\u0111\7\b\2\2\u0111\u0112\7<\2\2\u0112\u0113")
        buf.write("\5\22\n\2\u0113\u0114\5\n\6\2\u0114!\3\2\2\2\u0115\u0118")
        buf.write("\5$\23\2\u0116\u0118\5,\27\2\u0117\u0115\3\2\2\2\u0117")
        buf.write("\u0116\3\2\2\2\u0118#\3\2\2\2\u0119\u011a\7\n\2\2\u011a")
        buf.write("\u011b\7<\2\2\u011b\u011c\7\f\2\2\u011c\u011d\7\61\2\2")
        buf.write("\u011d\u011e\5(\25\2\u011e\u011f\7\62\2\2\u011f\u0120")
        buf.write("\5\n\6\2\u0120%\3\2\2\2\u0121\u0124\5(\25\2\u0122\u0124")
        buf.write("\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124")
        buf.write("\'\3\2\2\2\u0125\u0126\5*\26\2\u0126\u0127\5(\25\2\u0127")
        buf.write("\u012a\3\2\2\2\u0128\u012a\5*\26\2\u0129\u0125\3\2\2\2")
        buf.write("\u0129\u0128\3\2\2\2\u012a)\3\2\2\2\u012b\u012c\7<\2\2")
        buf.write("\u012c\u012d\5\22\n\2\u012d\u012e\5\n\6\2\u012e+\3\2\2")
        buf.write("\2\u012f\u0130\7\n\2\2\u0130\u0131\7<\2\2\u0131\u0132")
        buf.write("\7\r\2\2\u0132\u0133\7\61\2\2\u0133\u0134\5\60\31\2\u0134")
        buf.write("\u0135\7\62\2\2\u0135\u0136\5\n\6\2\u0136-\3\2\2\2\u0137")
        buf.write("\u013a\5\60\31\2\u0138\u013a\3\2\2\2\u0139\u0137\3\2\2")
        buf.write("\2\u0139\u0138\3\2\2\2\u013a/\3\2\2\2\u013b\u013c\5\62")
        buf.write("\32\2\u013c\u013d\5\60\31\2\u013d\u0140\3\2\2\2\u013e")
        buf.write("\u0140\5\62\32\2\u013f\u013b\3\2\2\2\u013f\u013e\3\2\2")
        buf.write("\2\u0140\61\3\2\2\2\u0141\u0142\7<\2\2\u0142\u0143\7-")
        buf.write("\2\2\u0143\u0144\5\64\33\2\u0144\u0145\7.\2\2\u0145\u0146")
        buf.write("\5\22\n\2\u0146\u0147\5\n\6\2\u0147\u014f\3\2\2\2\u0148")
        buf.write("\u0149\7<\2\2\u0149\u014a\7-\2\2\u014a\u014b\5\64\33\2")
        buf.write("\u014b\u014c\7.\2\2\u014c\u014d\5\n\6\2\u014d\u014f\3")
        buf.write("\2\2\2\u014e\u0141\3\2\2\2\u014e\u0148\3\2\2\2\u014f\63")
        buf.write("\3\2\2\2\u0150\u0153\5\66\34\2\u0151\u0153\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153\65\3\2\2\2\u0154")
        buf.write("\u0155\58\35\2\u0155\u0156\7*\2\2\u0156\u0157\5\66\34")
        buf.write("\2\u0157\u015a\3\2\2\2\u0158\u015a\58\35\2\u0159\u0154")
        buf.write("\3\2\2\2\u0159\u0158\3\2\2\2\u015a\67\3\2\2\2\u015b\u015c")
        buf.write("\5:\36\2\u015c\u015d\5\22\n\2\u015d9\3\2\2\2\u015e\u015f")
        buf.write("\7<\2\2\u015f\u0160\7*\2\2\u0160\u0163\5:\36\2\u0161\u0163")
        buf.write("\7<\2\2\u0162\u015e\3\2\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write(";\3\2\2\2\u0164\u0165\7\13\2\2\u0165\u0166\7<\2\2\u0166")
        buf.write("\u0167\7-\2\2\u0167\u0168\5> \2\u0168\u0169\7.\2\2\u0169")
        buf.write("\u016a\5\22\n\2\u016a\u016b\7\61\2\2\u016b\u016c\5D#\2")
        buf.write("\u016c\u016d\7\62\2\2\u016d\u016e\5\n\6\2\u016e\u017a")
        buf.write("\3\2\2\2\u016f\u0170\7\13\2\2\u0170\u0171\7<\2\2\u0171")
        buf.write("\u0172\7-\2\2\u0172\u0173\5> \2\u0173\u0174\7.\2\2\u0174")
        buf.write("\u0175\7\61\2\2\u0175\u0176\5D#\2\u0176\u0177\7\62\2\2")
        buf.write("\u0177\u0178\5\n\6\2\u0178\u017a\3\2\2\2\u0179\u0164\3")
        buf.write("\2\2\2\u0179\u016f\3\2\2\2\u017a=\3\2\2\2\u017b\u017e")
        buf.write("\5@!\2\u017c\u017e\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e?\3\2\2\2\u017f\u0180\5B\"\2\u0180\u0181")
        buf.write("\7*\2\2\u0181\u0182\5@!\2\u0182\u0185\3\2\2\2\u0183\u0185")
        buf.write("\5B\"\2\u0184\u017f\3\2\2\2\u0184\u0183\3\2\2\2\u0185")
        buf.write("A\3\2\2\2\u0186\u0187\5:\36\2\u0187\u0188\5\22\n\2\u0188")
        buf.write("C\3\2\2\2\u0189\u018a\5F$\2\u018aE\3\2\2\2\u018b\u018c")
        buf.write("\5H%\2\u018cG\3\2\2\2\u018d\u018e\5p9\2\u018e\u018f\5")
        buf.write("H%\2\u018f\u0192\3\2\2\2\u0190\u0192\5p9\2\u0191\u018d")
        buf.write("\3\2\2\2\u0191\u0190\3\2\2\2\u0192I\3\2\2\2\u0193\u0194")
        buf.write("\7\13\2\2\u0194\u0195\5L\'\2\u0195\u0196\7<\2\2\u0196")
        buf.write("\u0197\7-\2\2\u0197\u0198\5> \2\u0198\u0199\7.\2\2\u0199")
        buf.write("\u019a\5\22\n\2\u019a\u019b\7\61\2\2\u019b\u019c\5D#\2")
        buf.write("\u019c\u019d\7\62\2\2\u019d\u019e\5\n\6\2\u019e\u01ab")
        buf.write("\3\2\2\2\u019f\u01a0\7\13\2\2\u01a0\u01a1\5L\'\2\u01a1")
        buf.write("\u01a2\7<\2\2\u01a2\u01a3\7-\2\2\u01a3\u01a4\5> \2\u01a4")
        buf.write("\u01a5\7.\2\2\u01a5\u01a6\7\61\2\2\u01a6\u01a7\5D#\2\u01a7")
        buf.write("\u01a8\7\62\2\2\u01a8\u01a9\5\n\6\2\u01a9\u01ab\3\2\2")
        buf.write("\2\u01aa\u0193\3\2\2\2\u01aa\u019f\3\2\2\2\u01abK\3\2")
        buf.write("\2\2\u01ac\u01ad\7-\2\2\u01ad\u01ae\7<\2\2\u01ae\u01af")
        buf.write("\7<\2\2\u01af\u01b0\7.\2\2\u01b0M\3\2\2\2\u01b1\u01b2")
        buf.write("\b(\1\2\u01b2\u01b3\5P)\2\u01b3\u01b9\3\2\2\2\u01b4\u01b5")
        buf.write("\f\4\2\2\u01b5\u01b6\7 \2\2\u01b6\u01b8\5P)\2\u01b7\u01b4")
        buf.write("\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01baO\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc")
        buf.write("\u01bd\b)\1\2\u01bd\u01be\5R*\2\u01be\u01c4\3\2\2\2\u01bf")
        buf.write("\u01c0\f\4\2\2\u01c0\u01c1\7\37\2\2\u01c1\u01c3\5R*\2")
        buf.write("\u01c2\u01bf\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3")
        buf.write("\2\2\2\u01c4\u01c5\3\2\2\2\u01c5Q\3\2\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c7\u01c8\b*\1\2\u01c8\u01c9\5V,\2\u01c9\u01d0")
        buf.write("\3\2\2\2\u01ca\u01cb\f\4\2\2\u01cb\u01cc\5T+\2\u01cc\u01cd")
        buf.write("\5V,\2\u01cd\u01cf\3\2\2\2\u01ce\u01ca\3\2\2\2\u01cf\u01d2")
        buf.write("\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("S\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\t\5\2\2\u01d4")
        buf.write("U\3\2\2\2\u01d5\u01d6\b,\1\2\u01d6\u01d7\5X-\2\u01d7\u01e0")
        buf.write("\3\2\2\2\u01d8\u01d9\f\5\2\2\u01d9\u01da\7\24\2\2\u01da")
        buf.write("\u01df\5X-\2\u01db\u01dc\f\4\2\2\u01dc\u01dd\7\25\2\2")
        buf.write("\u01dd\u01df\5X-\2\u01de\u01d8\3\2\2\2\u01de\u01db\3\2")
        buf.write("\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1")
        buf.write("\3\2\2\2\u01e1W\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4")
        buf.write("\b-\1\2\u01e4\u01e5\5Z.\2\u01e5\u01f1\3\2\2\2\u01e6\u01e7")
        buf.write("\f\6\2\2\u01e7\u01e8\7\26\2\2\u01e8\u01f0\5Z.\2\u01e9")
        buf.write("\u01ea\f\5\2\2\u01ea\u01eb\7\27\2\2\u01eb\u01f0\5Z.\2")
        buf.write("\u01ec\u01ed\f\4\2\2\u01ed\u01ee\7\30\2\2\u01ee\u01f0")
        buf.write("\5Z.\2\u01ef\u01e6\3\2\2\2\u01ef\u01e9\3\2\2\2\u01ef\u01ec")
        buf.write("\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1")
        buf.write("\u01f2\3\2\2\2\u01f2Y\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4")
        buf.write("\u01f5\7!\2\2\u01f5\u01fa\5Z.\2\u01f6\u01f7\7\25\2\2\u01f7")
        buf.write("\u01fa\5Z.\2\u01f8\u01fa\5\\/\2\u01f9\u01f4\3\2\2\2\u01f9")
        buf.write("\u01f6\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fa[\3\2\2\2\u01fb")
        buf.write("\u01fc\b/\1\2\u01fc\u01fd\5^\60\2\u01fd\u0208\3\2\2\2")
        buf.write("\u01fe\u01ff\f\5\2\2\u01ff\u0200\7/\2\2\u0200\u0201\5")
        buf.write("N(\2\u0201\u0202\7\60\2\2\u0202\u0207\3\2\2\2\u0203\u0204")
        buf.write("\f\4\2\2\u0204\u0205\7)\2\2\u0205\u0207\5`\61\2\u0206")
        buf.write("\u01fe\3\2\2\2\u0206\u0203\3\2\2\2\u0207\u020a\3\2\2\2")
        buf.write("\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209]\3\2\2")
        buf.write("\2\u020a\u0208\3\2\2\2\u020b\u0215\5j\66\2\u020c\u0215")
        buf.write("\7<\2\2\u020d\u020e\7-\2\2\u020e\u020f\5N(\2\u020f\u0210")
        buf.write("\7.\2\2\u0210\u0215\3\2\2\2\u0211\u0215\5b\62\2\u0212")
        buf.write("\u0215\5\u0084C\2\u0213\u0215\5\u008eH\2\u0214\u020b\3")
        buf.write("\2\2\2\u0214\u020c\3\2\2\2\u0214\u020d\3\2\2\2\u0214\u0211")
        buf.write("\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0213\3\2\2\2\u0215")
        buf.write("_\3\2\2\2\u0216\u0219\7<\2\2\u0217\u0219\5b\62\2\u0218")
        buf.write("\u0216\3\2\2\2\u0218\u0217\3\2\2\2\u0219a\3\2\2\2\u021a")
        buf.write("\u021b\7<\2\2\u021b\u021c\7-\2\2\u021c\u021d\5d\63\2\u021d")
        buf.write("\u021e\7.\2\2\u021ec\3\2\2\2\u021f\u0222\5f\64\2\u0220")
        buf.write("\u0222\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0220\3\2\2\2")
        buf.write("\u0222e\3\2\2\2\u0223\u0224\5h\65\2\u0224\u0225\7*\2\2")
        buf.write("\u0225\u0226\5f\64\2\u0226\u0229\3\2\2\2\u0227\u0229\5")
        buf.write("h\65\2\u0228\u0223\3\2\2\2\u0228\u0227\3\2\2\2\u0229g")
        buf.write("\3\2\2\2\u022a\u022b\5N(\2\u022bi\3\2\2\2\u022c\u0232")
        buf.write("\5l\67\2\u022d\u0232\7:\2\2\u022e\u0232\7;\2\2\u022f\u0232")
        buf.write("\5n8\2\u0230\u0232\7\63\2\2\u0231\u022c\3\2\2\2\u0231")
        buf.write("\u022d\3\2\2\2\u0231\u022e\3\2\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0231\u0230\3\2\2\2\u0232k\3\2\2\2\u0233\u0234\t\6\2")
        buf.write("\2\u0234m\3\2\2\2\u0235\u0236\t\7\2\2\u0236o\3\2\2\2\u0237")
        buf.write("\u0241\5\f\7\2\u0238\u0241\5\b\5\2\u0239\u0241\5r:\2\u023a")
        buf.write("\u0241\5\u0096L\2\u023b\u0241\5\u00a4S\2\u023c\u0241\5")
        buf.write("\u00b8]\2\u023d\u0241\5\u00ba^\2\u023e\u0241\5\u00bc_")
        buf.write("\2\u023f\u0241\5\u00c4c\2\u0240\u0237\3\2\2\2\u0240\u0238")
        buf.write("\3\2\2\2\u0240\u0239\3\2\2\2\u0240\u023a\3\2\2\2\u0240")
        buf.write("\u023b\3\2\2\2\u0240\u023c\3\2\2\2\u0240\u023d\3\2\2\2")
        buf.write("\u0240\u023e\3\2\2\2\u0240\u023f\3\2\2\2\u0241q\3\2\2")
        buf.write("\2\u0242\u0243\5t;\2\u0243\u0244\5~@\2\u0244\u0245\5\u0080")
        buf.write("A\2\u0245\u0246\5\n\6\2\u0246s\3\2\2\2\u0247\u0248\7<")
        buf.write("\2\2\u0248\u024b\5v<\2\u0249\u024b\7<\2\2\u024a\u0247")
        buf.write("\3\2\2\2\u024a\u0249\3\2\2\2\u024bu\3\2\2\2\u024c\u024d")
        buf.write("\b<\1\2\u024d\u024e\5x=\2\u024e\u0253\3\2\2\2\u024f\u0250")
        buf.write("\f\4\2\2\u0250\u0252\5x=\2\u0251\u024f\3\2\2\2\u0252\u0255")
        buf.write("\3\2\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2\u0254")
        buf.write("w\3\2\2\2\u0255\u0253\3\2\2\2\u0256\u0259\5z>\2\u0257")
        buf.write("\u0259\5|?\2\u0258\u0256\3\2\2\2\u0258\u0257\3\2\2\2\u0259")
        buf.write("y\3\2\2\2\u025a\u025b\7/\2\2\u025b\u025c\5N(\2\u025c\u025d")
        buf.write("\7\60\2\2\u025d{\3\2\2\2\u025e\u025f\7)\2\2\u025f\u0260")
        buf.write("\7<\2\2\u0260}\3\2\2\2\u0261\u0262\t\b\2\2\u0262\177\3")
        buf.write("\2\2\2\u0263\u0267\5N(\2\u0264\u0267\5\u0084C\2\u0265")
        buf.write("\u0267\5\u008eH\2\u0266\u0263\3\2\2\2\u0266\u0264\3\2")
        buf.write("\2\2\u0266\u0265\3\2\2\2\u0267\u0081\3\2\2\2\u0268\u026b")
        buf.write("\5\u0084C\2\u0269\u026b\5\u0086D\2\u026a\u0268\3\2\2\2")
        buf.write("\u026a\u0269\3\2\2\2\u026b\u0083\3\2\2\2\u026c\u026d\5")
        buf.write("\26\f\2\u026d\u026e\7\61\2\2\u026e\u026f\5\u0088E\2\u026f")
        buf.write("\u0270\7\62\2\2\u0270\u0085\3\2\2\2\u0271\u0272\7\61\2")
        buf.write("\2\u0272\u0273\5\u0088E\2\u0273\u0274\7\62\2\2\u0274\u0087")
        buf.write("\3\2\2\2\u0275\u0278\5\u008aF\2\u0276\u0278\3\2\2\2\u0277")
        buf.write("\u0275\3\2\2\2\u0277\u0276\3\2\2\2\u0278\u0089\3\2\2\2")
        buf.write("\u0279\u027a\5\u008cG\2\u027a\u027b\7*\2\2\u027b\u027c")
        buf.write("\5\u008aF\2\u027c\u027f\3\2\2\2\u027d\u027f\5\u008cG\2")
        buf.write("\u027e\u0279\3\2\2\2\u027e\u027d\3\2\2\2\u027f\u008b\3")
        buf.write("\2\2\2\u0280\u0284\5N(\2\u0281\u0284\5\u0082B\2\u0282")
        buf.write("\u0284\5\u008eH\2\u0283\u0280\3\2\2\2\u0283\u0281\3\2")
        buf.write("\2\2\u0283\u0282\3\2\2\2\u0284\u008d\3\2\2\2\u0285\u0286")
        buf.write("\7<\2\2\u0286\u0287\7\61\2\2\u0287\u0288\5\u0090I\2\u0288")
        buf.write("\u0289\7\62\2\2\u0289\u008f\3\2\2\2\u028a\u028d\5\u0092")
        buf.write("J\2\u028b\u028d\3\2\2\2\u028c\u028a\3\2\2\2\u028c\u028b")
        buf.write("\3\2\2\2\u028d\u0091\3\2\2\2\u028e\u028f\5\u0094K\2\u028f")
        buf.write("\u0290\7*\2\2\u0290\u0291\5\u0092J\2\u0291\u0294\3\2\2")
        buf.write("\2\u0292\u0294\5\u0094K\2\u0293\u028e\3\2\2\2\u0293\u0292")
        buf.write("\3\2\2\2\u0294\u0093\3\2\2\2\u0295\u0296\7<\2\2\u0296")
        buf.write("\u0297\7+\2\2\u0297\u0298\5N(\2\u0298\u0095\3\2\2\2\u0299")
        buf.write("\u029c\5\u0098M\2\u029a\u029c\5\u009aN\2\u029b\u0299\3")
        buf.write("\2\2\2\u029b\u029a\3\2\2\2\u029c\u0097\3\2\2\2\u029d\u029e")
        buf.write("\7\16\2\2\u029e\u029f\7-\2\2\u029f\u02a0\5\u009cO\2\u02a0")
        buf.write("\u02a1\7.\2\2\u02a1\u02a2\7\61\2\2\u02a2\u02a3\5\u009e")
        buf.write("P\2\u02a3\u02a4\7\62\2\2\u02a4\u02a5\5\n\6\2\u02a5\u0099")
        buf.write("\3\2\2\2\u02a6\u02a7\7\16\2\2\u02a7\u02a8\7-\2\2\u02a8")
        buf.write("\u02a9\5\u009cO\2\u02a9\u02aa\7.\2\2\u02aa\u02ab\7\61")
        buf.write("\2\2\u02ab\u02ac\5\u009eP\2\u02ac\u02ad\7\62\2\2\u02ad")
        buf.write("\u02ae\5\u00a0Q\2\u02ae\u009b\3\2\2\2\u02af\u02b0\5N(")
        buf.write("\2\u02b0\u009d\3\2\2\2\u02b1\u02b2\5F$\2\u02b2\u009f\3")
        buf.write("\2\2\2\u02b3\u02b4\7\17\2\2\u02b4\u02bc\5\u0096L\2\u02b5")
        buf.write("\u02b6\7\17\2\2\u02b6\u02b7\7\61\2\2\u02b7\u02b8\5\u00a2")
        buf.write("R\2\u02b8\u02b9\7\62\2\2\u02b9\u02ba\5\n\6\2\u02ba\u02bc")
        buf.write("\3\2\2\2\u02bb\u02b3\3\2\2\2\u02bb\u02b5\3\2\2\2\u02bc")
        buf.write("\u00a1\3\2\2\2\u02bd\u02be\5F$\2\u02be\u00a3\3\2\2\2\u02bf")
        buf.write("\u02c3\5\u00a6T\2\u02c0\u02c3\5\u00a8U\2\u02c1\u02c3\5")
        buf.write("\u00aeX\2\u02c2\u02bf\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c2")
        buf.write("\u02c1\3\2\2\2\u02c3\u00a5\3\2\2\2\u02c4\u02c5\7\20\2")
        buf.write("\2\u02c5\u02c6\5\u009cO\2\u02c6\u02c7\7\61\2\2\u02c7\u02c8")
        buf.write("\5\u00b6\\\2\u02c8\u02c9\7\62\2\2\u02c9\u02ca\5\n\6\2")
        buf.write("\u02ca\u00a7\3\2\2\2\u02cb\u02cc\7\20\2\2\u02cc\u02cd")
        buf.write("\5\u00aaV\2\u02cd\u02ce\7,\2\2\u02ce\u02cf\5\u009cO\2")
        buf.write("\u02cf\u02d0\7,\2\2\u02d0\u02d1\5\u00acW\2\u02d1\u02d2")
        buf.write("\7\61\2\2\u02d2\u02d3\5\u00b6\\\2\u02d3\u02d4\7\62\2\2")
        buf.write("\u02d4\u02d5\5\n\6\2\u02d5\u00a9\3\2\2\2\u02d6\u02d7\7")
        buf.write("<\2\2\u02d7\u02d8\7#\2\2\u02d8\u02e4\5N(\2\u02d9\u02da")
        buf.write("\7\b\2\2\u02da\u02db\7<\2\2\u02db\u02dc\5\22\n\2\u02dc")
        buf.write("\u02dd\7\"\2\2\u02dd\u02de\5N(\2\u02de\u02e4\3\2\2\2\u02df")
        buf.write("\u02e0\7\b\2\2\u02e0\u02e1\7<\2\2\u02e1\u02e2\7\"\2\2")
        buf.write("\u02e2\u02e4\5N(\2\u02e3\u02d6\3\2\2\2\u02e3\u02d9\3\2")
        buf.write("\2\2\u02e3\u02df\3\2\2\2\u02e4\u00ab\3\2\2\2\u02e5\u02e6")
        buf.write("\7<\2\2\u02e6\u02e7\5~@\2\u02e7\u02e8\5N(\2\u02e8\u00ad")
        buf.write("\3\2\2\2\u02e9\u02ea\7\20\2\2\u02ea\u02eb\5\u00b2Z\2\u02eb")
        buf.write("\u02ec\7*\2\2\u02ec\u02ed\5\u00b4[\2\u02ed\u02ee\7#\2")
        buf.write("\2\u02ee\u02ef\7\23\2\2\u02ef\u02f0\5\u00b0Y\2\u02f0\u02f1")
        buf.write("\7\61\2\2\u02f1\u02f2\5\u00b6\\\2\u02f2\u02f3\7\62\2\2")
        buf.write("\u02f3\u02f4\5\n\6\2\u02f4\u00af\3\2\2\2\u02f5\u02f9\7")
        buf.write("<\2\2\u02f6\u02f9\5\u0084C\2\u02f7\u02f9\5N(\2\u02f8\u02f5")
        buf.write("\3\2\2\2\u02f8\u02f6\3\2\2\2\u02f8\u02f7\3\2\2\2\u02f9")
        buf.write("\u00b1\3\2\2\2\u02fa\u02fb\7<\2\2\u02fb\u00b3\3\2\2\2")
        buf.write("\u02fc\u02fd\7<\2\2\u02fd\u00b5\3\2\2\2\u02fe\u02ff\5")
        buf.write("F$\2\u02ff\u00b7\3\2\2\2\u0300\u0301\7\22\2\2\u0301\u0302")
        buf.write("\5\n\6\2\u0302\u00b9\3\2\2\2\u0303\u0304\7\21\2\2\u0304")
        buf.write("\u0305\5\n\6\2\u0305\u00bb\3\2\2\2\u0306\u0309\5\u00be")
        buf.write("`\2\u0307\u0309\5\u00c0a\2\u0308\u0306\3\2\2\2\u0308\u0307")
        buf.write("\3\2\2\2\u0309\u00bd\3\2\2\2\u030a\u030b\5b\62\2\u030b")
        buf.write("\u030c\5\n\6\2\u030c\u00bf\3\2\2\2\u030d\u030e\5\u00c2")
        buf.write("b\2\u030e\u030f\5\n\6\2\u030f\u00c1\3\2\2\2\u0310\u0311")
        buf.write("\5N(\2\u0311\u0312\7)\2\2\u0312\u0313\5b\62\2\u0313\u00c3")
        buf.write("\3\2\2\2\u0314\u0315\7\t\2\2\u0315\u031b\5\n\6\2\u0316")
        buf.write("\u0317\7\t\2\2\u0317\u0318\5N(\2\u0318\u0319\5\n\6\2\u0319")
        buf.write("\u031b\3\2\2\2\u031a\u0314\3\2\2\2\u031a\u0316\3\2\2\2")
        buf.write("\u031b\u00c5\3\2\2\28\u00cd\u00d4\u00e1\u00ed\u00f2\u00fc")
        buf.write("\u0102\u0117\u0123\u0129\u0139\u013f\u014e\u0152\u0159")
        buf.write("\u0162\u0179\u017d\u0184\u0191\u01aa\u01b9\u01c4\u01d0")
        buf.write("\u01de\u01e0\u01ef\u01f1\u01f9\u0206\u0208\u0214\u0218")
        buf.write("\u0221\u0228\u0231\u0240\u024a\u0253\u0258\u0266\u026a")
        buf.write("\u0277\u027e\u0283\u028c\u0293\u029b\u02bb\u02c2\u02e3")
        buf.write("\u02f8\u0308\u031a")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'string'", "'boolean'", 
                     "'const'", "'var'", "'return'", "'type'", "'func'", 
                     "'struct'", "'interface'", "'if'", "'else'", "'for'", 
                     "'continue'", "'break'", "'range'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'&&'", "'||'", "'!'", "'='", "':='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'.'", "','", "':'", 
                     "';'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'nil'", 
                     "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "Key_type_int", "Key_type_float", "Key_type_string", 
                      "Key_type_boolean", "Key_decl_const", "Key_decl_var", 
                      "Key_return", "Key_type", "Key_func", "Key_struct", 
                      "Key_interface", "Key_if", "Key_else", "Key_loop_for", 
                      "Key_loop_continue", "Key_loop_break", "Key_range", 
                      "Ope_plus", "Ope_minus", "Ope_multi", "Ope_div", "Ope_mod", 
                      "Ope_equal", "Ope_nequal", "Ope_let", "Ope_leq", "Ope_get", 
                      "Ope_geq", "Ope_and", "Ope_or", "Ope_not", "Ope_assign", 
                      "Ope_init", "Ope_assign_plus", "Ope_assign_minus", 
                      "Ope_assign_multi", "Ope_assign_div", "Ope_assign_mod", 
                      "Ope_select", "Comma", "Colon", "Semicolon", "Lparen", 
                      "Rparen", "Lsquare", "Rsquare", "Lcurly", "Rcurly", 
                      "Literal_nil", "Literal_true", "Literal_false", "Literal_dec", 
                      "Literal_bin", "Literal_oct", "Literal_hex", "Literal_float", 
                      "Literal_string", "Identifier", "NL", "WS", "SL_COMMENT", 
                      "ML_COMMENT", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_const_decl = 3
    RULE_end_stmt = 4
    RULE_var_decl = 5
    RULE_var_decl_expl = 6
    RULE_var_value = 7
    RULE_data_type = 8
    RULE_primitive_type = 9
    RULE_array_type = 10
    RULE_dimension_list = 11
    RULE_dimension = 12
    RULE_size = 13
    RULE_var_decl_infer = 14
    RULE_var_decl_nil = 15
    RULE_type_decl = 16
    RULE_struct_decl = 17
    RULE_field_set = 18
    RULE_field_list = 19
    RULE_field_decl = 20
    RULE_interface_decl = 21
    RULE_interface_method_set = 22
    RULE_interface_method_list = 23
    RULE_interface_method_decl = 24
    RULE_interface_method_param_set = 25
    RULE_interface_method_param_list = 26
    RULE_interface_method_param = 27
    RULE_id_list = 28
    RULE_func_decl = 29
    RULE_param_set = 30
    RULE_param_list = 31
    RULE_param = 32
    RULE_func_body = 33
    RULE_stmt_set = 34
    RULE_stmt_list = 35
    RULE_method_decl = 36
    RULE_receiver = 37
    RULE_expr = 38
    RULE_expr1 = 39
    RULE_expr2 = 40
    RULE_ope_relation = 41
    RULE_expr3 = 42
    RULE_expr4 = 43
    RULE_expr5 = 44
    RULE_expr6 = 45
    RULE_expr7 = 46
    RULE_expr8 = 47
    RULE_func_call = 48
    RULE_argument_set = 49
    RULE_argument_list = 50
    RULE_argument = 51
    RULE_prim_literal = 52
    RULE_literal_int = 53
    RULE_literal_bool = 54
    RULE_stmt = 55
    RULE_assign_stmt = 56
    RULE_lhs = 57
    RULE_access_list = 58
    RULE_access = 59
    RULE_array_access = 60
    RULE_struct_access = 61
    RULE_ope_assign = 62
    RULE_rhs = 63
    RULE_literal_array = 64
    RULE_full_array_literal = 65
    RULE_partial_array_literal = 66
    RULE_array_element_set = 67
    RULE_array_element_list = 68
    RULE_array_element = 69
    RULE_literal_struct = 70
    RULE_struct_element_set = 71
    RULE_struct_element_list = 72
    RULE_struct_element = 73
    RULE_if_stmt = 74
    RULE_matched = 75
    RULE_unmatched = 76
    RULE_condition = 77
    RULE_if_stmt_body = 78
    RULE_else_stmt_list = 79
    RULE_else_stmt_body = 80
    RULE_for_stmt = 81
    RULE_for_basic = 82
    RULE_for_icu = 83
    RULE_init = 84
    RULE_update = 85
    RULE_for_range = 86
    RULE_array_instance = 87
    RULE_index = 88
    RULE_value = 89
    RULE_for_body = 90
    RULE_break_stmt = 91
    RULE_continue_stmt = 92
    RULE_call_stmt = 93
    RULE_func_call_stmt = 94
    RULE_method_call_stmt = 95
    RULE_method_call = 96
    RULE_return_stmt = 97

    ruleNames =  [ "program", "decllist", "decl", "const_decl", "end_stmt", 
                   "var_decl", "var_decl_expl", "var_value", "data_type", 
                   "primitive_type", "array_type", "dimension_list", "dimension", 
                   "size", "var_decl_infer", "var_decl_nil", "type_decl", 
                   "struct_decl", "field_set", "field_list", "field_decl", 
                   "interface_decl", "interface_method_set", "interface_method_list", 
                   "interface_method_decl", "interface_method_param_set", 
                   "interface_method_param_list", "interface_method_param", 
                   "id_list", "func_decl", "param_set", "param_list", "param", 
                   "func_body", "stmt_set", "stmt_list", "method_decl", 
                   "receiver", "expr", "expr1", "expr2", "ope_relation", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "func_call", "argument_set", "argument_list", "argument", 
                   "prim_literal", "literal_int", "literal_bool", "stmt", 
                   "assign_stmt", "lhs", "access_list", "access", "array_access", 
                   "struct_access", "ope_assign", "rhs", "literal_array", 
                   "full_array_literal", "partial_array_literal", "array_element_set", 
                   "array_element_list", "array_element", "literal_struct", 
                   "struct_element_set", "struct_element_list", "struct_element", 
                   "if_stmt", "matched", "unmatched", "condition", "if_stmt_body", 
                   "else_stmt_list", "else_stmt_body", "for_stmt", "for_basic", 
                   "for_icu", "init", "update", "for_range", "array_instance", 
                   "index", "value", "for_body", "break_stmt", "continue_stmt", 
                   "call_stmt", "func_call_stmt", "method_call_stmt", "method_call", 
                   "return_stmt" ]

    EOF = Token.EOF
    Key_type_int=1
    Key_type_float=2
    Key_type_string=3
    Key_type_boolean=4
    Key_decl_const=5
    Key_decl_var=6
    Key_return=7
    Key_type=8
    Key_func=9
    Key_struct=10
    Key_interface=11
    Key_if=12
    Key_else=13
    Key_loop_for=14
    Key_loop_continue=15
    Key_loop_break=16
    Key_range=17
    Ope_plus=18
    Ope_minus=19
    Ope_multi=20
    Ope_div=21
    Ope_mod=22
    Ope_equal=23
    Ope_nequal=24
    Ope_let=25
    Ope_leq=26
    Ope_get=27
    Ope_geq=28
    Ope_and=29
    Ope_or=30
    Ope_not=31
    Ope_assign=32
    Ope_init=33
    Ope_assign_plus=34
    Ope_assign_minus=35
    Ope_assign_multi=36
    Ope_assign_div=37
    Ope_assign_mod=38
    Ope_select=39
    Comma=40
    Colon=41
    Semicolon=42
    Lparen=43
    Rparen=44
    Lsquare=45
    Rsquare=46
    Lcurly=47
    Rcurly=48
    Literal_nil=49
    Literal_true=50
    Literal_false=51
    Literal_dec=52
    Literal_bin=53
    Literal_oct=54
    Literal_hex=55
    Literal_float=56
    Literal_string=57
    Identifier=58
    NL=59
    WS=60
    SL_COMMENT=61
    ML_COMMENT=62
    UNCLOSE_STRING=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.decllist()
            self.state = 197
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = MiniGoParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.decl()
                self.state = 200
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def type_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Type_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.const_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.type_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.func_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 209
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_decl_const(self):
            return self.getToken(MiniGoParser.Key_decl_const, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Ope_assign(self):
            return self.getToken(MiniGoParser.Ope_assign, 0)

        def var_value(self):
            return self.getTypedRuleContext(MiniGoParser.Var_valueContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MiniGoParser.Key_decl_const)
            self.state = 213
            self.match(MiniGoParser.Identifier)
            self.state = 214
            self.match(MiniGoParser.Ope_assign)
            self.state = 215
            self.var_value()
            self.state = 216
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def Semicolon(self):
            return self.getToken(MiniGoParser.Semicolon, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_stmt" ):
                return visitor.visitEnd_stmt(self)
            else:
                return visitor.visitChildren(self)




    def end_stmt(self):

        localctx = MiniGoParser.End_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_end_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.Semicolon or _la==MiniGoParser.NL):
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


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_expl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_explContext,0)


        def var_decl_infer(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_inferContext,0)


        def var_decl_nil(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_nilContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_decl)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.var_decl_expl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.var_decl_infer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.var_decl_nil()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_explContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_decl_var(self):
            return self.getToken(MiniGoParser.Key_decl_var, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def Ope_assign(self):
            return self.getToken(MiniGoParser.Ope_assign, 0)

        def var_value(self):
            return self.getTypedRuleContext(MiniGoParser.Var_valueContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_expl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_expl" ):
                return visitor.visitVar_decl_expl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_expl(self):

        localctx = MiniGoParser.Var_decl_explContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_decl_expl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MiniGoParser.Key_decl_var)
            self.state = 226
            self.match(MiniGoParser.Identifier)
            self.state = 227
            self.data_type()
            self.state = 228
            self.match(MiniGoParser.Ope_assign)
            self.state = 229
            self.var_value()
            self.state = 230
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def literal_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_value" ):
                return visitor.visitVar_value(self)
            else:
                return visitor.visitChildren(self)




    def var_value(self):

        localctx = MiniGoParser.Var_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_value)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.full_array_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.literal_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_data_type)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Key_type_int, MiniGoParser.Key_type_float, MiniGoParser.Key_type_string, MiniGoParser.Key_type_boolean]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.primitive_type()
                pass
            elif token in [MiniGoParser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(MiniGoParser.Identifier)
                pass
            elif token in [MiniGoParser.Lsquare]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.array_type()
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


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_type_int(self):
            return self.getToken(MiniGoParser.Key_type_int, 0)

        def Key_type_float(self):
            return self.getToken(MiniGoParser.Key_type_float, 0)

        def Key_type_boolean(self):
            return self.getToken(MiniGoParser.Key_type_boolean, 0)

        def Key_type_string(self):
            return self.getToken(MiniGoParser.Key_type_string, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.Key_type_int) | (1 << MiniGoParser.Key_type_float) | (1 << MiniGoParser.Key_type_string) | (1 << MiniGoParser.Key_type_boolean))) != 0)):
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_type)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.dimension_list()
                self.state = 245
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.dimension_list()
                self.state = 248
                self.match(MiniGoParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionContext,0)


        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list" ):
                return visitor.visitDimension_list(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list(self):

        localctx = MiniGoParser.Dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dimension_list)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.dimension()
                self.state = 253
                self.dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.dimension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lsquare(self):
            return self.getToken(MiniGoParser.Lsquare, 0)

        def size(self):
            return self.getTypedRuleContext(MiniGoParser.SizeContext,0)


        def Rsquare(self):
            return self.getToken(MiniGoParser.Rsquare, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MiniGoParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(MiniGoParser.Lsquare)
            self.state = 259
            self.size()
            self.state = 260
            self.match(MiniGoParser.Rsquare)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Literal_bin(self):
            return self.getToken(MiniGoParser.Literal_bin, 0)

        def Literal_hex(self):
            return self.getToken(MiniGoParser.Literal_hex, 0)

        def Literal_oct(self):
            return self.getToken(MiniGoParser.Literal_oct, 0)

        def Literal_dec(self):
            return self.getToken(MiniGoParser.Literal_dec, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = MiniGoParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.Literal_dec) | (1 << MiniGoParser.Literal_bin) | (1 << MiniGoParser.Literal_oct) | (1 << MiniGoParser.Literal_hex) | (1 << MiniGoParser.Identifier))) != 0)):
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


    class Var_decl_inferContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_decl_var(self):
            return self.getToken(MiniGoParser.Key_decl_var, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Ope_assign(self):
            return self.getToken(MiniGoParser.Ope_assign, 0)

        def var_value(self):
            return self.getTypedRuleContext(MiniGoParser.Var_valueContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_infer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_infer" ):
                return visitor.visitVar_decl_infer(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_infer(self):

        localctx = MiniGoParser.Var_decl_inferContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_decl_infer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(MiniGoParser.Key_decl_var)
            self.state = 265
            self.match(MiniGoParser.Identifier)
            self.state = 266
            self.match(MiniGoParser.Ope_assign)
            self.state = 267
            self.var_value()
            self.state = 268
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_nilContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_decl_var(self):
            return self.getToken(MiniGoParser.Key_decl_var, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_nil

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_nil" ):
                return visitor.visitVar_decl_nil(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_nil(self):

        localctx = MiniGoParser.Var_decl_nilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var_decl_nil)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(MiniGoParser.Key_decl_var)
            self.state = 271
            self.match(MiniGoParser.Identifier)
            self.state = 272
            self.data_type()
            self.state = 273
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = MiniGoParser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type_decl)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.struct_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.interface_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_type(self):
            return self.getToken(MiniGoParser.Key_type, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Key_struct(self):
            return self.getToken(MiniGoParser.Key_struct, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MiniGoParser.Key_type)
            self.state = 280
            self.match(MiniGoParser.Identifier)
            self.state = 281
            self.match(MiniGoParser.Key_struct)
            self.state = 282
            self.match(MiniGoParser.Lcurly)
            self.state = 283
            self.field_list()
            self.state = 284
            self.match(MiniGoParser.Rcurly)
            self.state = 285
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_set

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_set" ):
                return visitor.visitField_set(self)
            else:
                return visitor.visitChildren(self)




    def field_set(self):

        localctx = MiniGoParser.Field_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_field_set)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.field_list()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)

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


    class Field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Field_declContext,0)


        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_list" ):
                return visitor.visitField_list(self)
            else:
                return visitor.visitChildren(self)




    def field_list(self):

        localctx = MiniGoParser.Field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_field_list)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.field_decl()
                self.state = 292
                self.field_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.field_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_decl" ):
                return visitor.visitField_decl(self)
            else:
                return visitor.visitChildren(self)




    def field_decl(self):

        localctx = MiniGoParser.Field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MiniGoParser.Identifier)
            self.state = 298
            self.data_type()
            self.state = 299
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_type(self):
            return self.getToken(MiniGoParser.Key_type, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Key_interface(self):
            return self.getToken(MiniGoParser.Key_interface, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(MiniGoParser.Key_type)
            self.state = 302
            self.match(MiniGoParser.Identifier)
            self.state = 303
            self.match(MiniGoParser.Key_interface)
            self.state = 304
            self.match(MiniGoParser.Lcurly)
            self.state = 305
            self.interface_method_list()
            self.state = 306
            self.match(MiniGoParser.Rcurly)
            self.state = 307
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_set

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_set" ):
                return visitor.visitInterface_method_set(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_set(self):

        localctx = MiniGoParser.Interface_method_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_interface_method_set)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.interface_method_list()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)

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


    class Interface_method_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_declContext,0)


        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_list" ):
                return visitor.visitInterface_method_list(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_list(self):

        localctx = MiniGoParser.Interface_method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_interface_method_list)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.interface_method_decl()
                self.state = 314
                self.interface_method_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.interface_method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def interface_method_param_set(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_param_setContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_decl" ):
                return visitor.visitInterface_method_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_decl(self):

        localctx = MiniGoParser.Interface_method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_interface_method_decl)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(MiniGoParser.Identifier)
                self.state = 320
                self.match(MiniGoParser.Lparen)
                self.state = 321
                self.interface_method_param_set()
                self.state = 322
                self.match(MiniGoParser.Rparen)
                self.state = 323
                self.data_type()
                self.state = 324
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.match(MiniGoParser.Identifier)
                self.state = 327
                self.match(MiniGoParser.Lparen)
                self.state = 328
                self.interface_method_param_set()
                self.state = 329
                self.match(MiniGoParser.Rparen)
                self.state = 330
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_param_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_param_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_param_set

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_param_set" ):
                return visitor.visitInterface_method_param_set(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_param_set(self):

        localctx = MiniGoParser.Interface_method_param_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_interface_method_param_set)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.interface_method_param_list()
                pass
            elif token in [MiniGoParser.Rparen]:
                self.enterOuterAlt(localctx, 2)

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


    class Interface_method_param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_param(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_paramContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def interface_method_param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_param_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_param_list" ):
                return visitor.visitInterface_method_param_list(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_param_list(self):

        localctx = MiniGoParser.Interface_method_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_interface_method_param_list)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.interface_method_param()
                self.state = 339
                self.match(MiniGoParser.Comma)
                self.state = 340
                self.interface_method_param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.interface_method_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_param" ):
                return visitor.visitInterface_method_param(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_param(self):

        localctx = MiniGoParser.Interface_method_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_interface_method_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.id_list()
            self.state = 346
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MiniGoParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_id_list)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(MiniGoParser.Identifier)
                self.state = 349
                self.match(MiniGoParser.Comma)
                self.state = 350
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(MiniGoParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_func(self):
            return self.getToken(MiniGoParser.Key_func, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def param_set(self):
            return self.getTypedRuleContext(MiniGoParser.Param_setContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def func_body(self):
            return self.getTypedRuleContext(MiniGoParser.Func_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_decl)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(MiniGoParser.Key_func)
                self.state = 355
                self.match(MiniGoParser.Identifier)
                self.state = 356
                self.match(MiniGoParser.Lparen)
                self.state = 357
                self.param_set()
                self.state = 358
                self.match(MiniGoParser.Rparen)
                self.state = 359
                self.data_type()
                self.state = 360
                self.match(MiniGoParser.Lcurly)
                self.state = 361
                self.func_body()
                self.state = 362
                self.match(MiniGoParser.Rcurly)
                self.state = 363
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.match(MiniGoParser.Key_func)
                self.state = 366
                self.match(MiniGoParser.Identifier)
                self.state = 367
                self.match(MiniGoParser.Lparen)
                self.state = 368
                self.param_set()
                self.state = 369
                self.match(MiniGoParser.Rparen)
                self.state = 370
                self.match(MiniGoParser.Lcurly)
                self.state = 371
                self.func_body()
                self.state = 372
                self.match(MiniGoParser.Rcurly)
                self.state = 373
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_set

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_set" ):
                return visitor.visitParam_set(self)
            else:
                return visitor.visitChildren(self)




    def param_set(self):

        localctx = MiniGoParser.Param_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_param_set)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.param_list()
                pass
            elif token in [MiniGoParser.Rparen]:
                self.enterOuterAlt(localctx, 2)

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


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_param_list)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.param()
                self.state = 382
                self.match(MiniGoParser.Comma)
                self.state = 383
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.id_list()
            self.state = 389
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_set(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_setContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = MiniGoParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.stmt_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_set

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_set" ):
                return visitor.visitStmt_set(self)
            else:
                return visitor.visitChildren(self)




    def stmt_set(self):

        localctx = MiniGoParser.Stmt_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stmt_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = MiniGoParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_stmt_list)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.stmt()
                self.state = 396
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_func(self):
            return self.getToken(MiniGoParser.Key_func, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def param_set(self):
            return self.getTypedRuleContext(MiniGoParser.Param_setContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def func_body(self):
            return self.getTypedRuleContext(MiniGoParser.Func_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_decl)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(MiniGoParser.Key_func)
                self.state = 402
                self.receiver()
                self.state = 403
                self.match(MiniGoParser.Identifier)
                self.state = 404
                self.match(MiniGoParser.Lparen)
                self.state = 405
                self.param_set()
                self.state = 406
                self.match(MiniGoParser.Rparen)
                self.state = 407
                self.data_type()
                self.state = 408
                self.match(MiniGoParser.Lcurly)
                self.state = 409
                self.func_body()
                self.state = 410
                self.match(MiniGoParser.Rcurly)
                self.state = 411
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.match(MiniGoParser.Key_func)
                self.state = 414
                self.receiver()
                self.state = 415
                self.match(MiniGoParser.Identifier)
                self.state = 416
                self.match(MiniGoParser.Lparen)
                self.state = 417
                self.param_set()
                self.state = 418
                self.match(MiniGoParser.Rparen)
                self.state = 419
                self.match(MiniGoParser.Lcurly)
                self.state = 420
                self.func_body()
                self.state = 421
                self.match(MiniGoParser.Rcurly)
                self.state = 422
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.Identifier)
            else:
                return self.getToken(MiniGoParser.Identifier, i)

        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.Lparen)
            self.state = 427
            self.match(MiniGoParser.Identifier)
            self.state = 428
            self.match(MiniGoParser.Identifier)
            self.state = 429
            self.match(MiniGoParser.Rparen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Ope_or(self):
            return self.getToken(MiniGoParser.Ope_or, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 434
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 435
                    self.match(MiniGoParser.Ope_or)
                    self.state = 436
                    self.expr1(0) 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def Ope_and(self):
            return self.getToken(MiniGoParser.Ope_and, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 445
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 446
                    self.match(MiniGoParser.Ope_and)
                    self.state = 447
                    self.expr2(0) 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def ope_relation(self):
            return self.getTypedRuleContext(MiniGoParser.Ope_relationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 456
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 457
                    self.ope_relation()
                    self.state = 458
                    self.expr3(0) 
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Ope_relationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ope_equal(self):
            return self.getToken(MiniGoParser.Ope_equal, 0)

        def Ope_nequal(self):
            return self.getToken(MiniGoParser.Ope_nequal, 0)

        def Ope_let(self):
            return self.getToken(MiniGoParser.Ope_let, 0)

        def Ope_leq(self):
            return self.getToken(MiniGoParser.Ope_leq, 0)

        def Ope_get(self):
            return self.getToken(MiniGoParser.Ope_get, 0)

        def Ope_geq(self):
            return self.getToken(MiniGoParser.Ope_geq, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ope_relation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpe_relation" ):
                return visitor.visitOpe_relation(self)
            else:
                return visitor.visitChildren(self)




    def ope_relation(self):

        localctx = MiniGoParser.Ope_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_ope_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.Ope_equal) | (1 << MiniGoParser.Ope_nequal) | (1 << MiniGoParser.Ope_let) | (1 << MiniGoParser.Ope_leq) | (1 << MiniGoParser.Ope_get) | (1 << MiniGoParser.Ope_geq))) != 0)):
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


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def Ope_plus(self):
            return self.getToken(MiniGoParser.Ope_plus, 0)

        def Ope_minus(self):
            return self.getToken(MiniGoParser.Ope_minus, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 478
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 476
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 470
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 471
                        self.match(MiniGoParser.Ope_plus)
                        self.state = 472
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 473
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 474
                        self.match(MiniGoParser.Ope_minus)
                        self.state = 475
                        self.expr4(0)
                        pass

             
                self.state = 480
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def Ope_multi(self):
            return self.getToken(MiniGoParser.Ope_multi, 0)

        def Ope_div(self):
            return self.getToken(MiniGoParser.Ope_div, 0)

        def Ope_mod(self):
            return self.getToken(MiniGoParser.Ope_mod, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 495
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 493
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 484
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 485
                        self.match(MiniGoParser.Ope_multi)
                        self.state = 486
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 487
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 488
                        self.match(MiniGoParser.Ope_div)
                        self.state = 489
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 490
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 491
                        self.match(MiniGoParser.Ope_mod)
                        self.state = 492
                        self.expr5()
                        pass

             
                self.state = 497
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ope_not(self):
            return self.getToken(MiniGoParser.Ope_not, 0)

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def Ope_minus(self):
            return self.getToken(MiniGoParser.Ope_minus, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr5)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Ope_not]:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(MiniGoParser.Ope_not)
                self.state = 499
                self.expr5()
                pass
            elif token in [MiniGoParser.Ope_minus]:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.match(MiniGoParser.Ope_minus)
                self.state = 501
                self.expr5()
                pass
            elif token in [MiniGoParser.Lparen, MiniGoParser.Lsquare, MiniGoParser.Literal_nil, MiniGoParser.Literal_true, MiniGoParser.Literal_false, MiniGoParser.Literal_dec, MiniGoParser.Literal_bin, MiniGoParser.Literal_oct, MiniGoParser.Literal_hex, MiniGoParser.Literal_float, MiniGoParser.Literal_string, MiniGoParser.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 502
                self.expr6(0)
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def Lsquare(self):
            return self.getToken(MiniGoParser.Lsquare, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Rsquare(self):
            return self.getToken(MiniGoParser.Rsquare, 0)

        def Ope_select(self):
            return self.getToken(MiniGoParser.Ope_select, 0)

        def expr8(self):
            return self.getTypedRuleContext(MiniGoParser.Expr8Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 516
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 508
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 509
                        self.match(MiniGoParser.Lsquare)
                        self.state = 510
                        self.expr(0)
                        self.state = 511
                        self.match(MiniGoParser.Rsquare)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 513
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 514
                        self.match(MiniGoParser.Ope_select)
                        self.state = 515
                        self.expr8()
                        pass

             
                self.state = 520
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Prim_literalContext,0)


        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def literal_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr7)
        try:
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.prim_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(MiniGoParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.match(MiniGoParser.Lparen)
                self.state = 524
                self.expr(0)
                self.state = 525
                self.match(MiniGoParser.Rparen)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 527
                self.func_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 528
                self.full_array_literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 529
                self.literal_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = MiniGoParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr8)
        try:
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(MiniGoParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def argument_set(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_setContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(MiniGoParser.Identifier)
            self.state = 537
            self.match(MiniGoParser.Lparen)
            self.state = 538
            self.argument_set()
            self.state = 539
            self.match(MiniGoParser.Rparen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument_list(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_set

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_set" ):
                return visitor.visitArgument_set(self)
            else:
                return visitor.visitChildren(self)




    def argument_set(self):

        localctx = MiniGoParser.Argument_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_argument_set)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Ope_minus, MiniGoParser.Ope_not, MiniGoParser.Lparen, MiniGoParser.Lsquare, MiniGoParser.Literal_nil, MiniGoParser.Literal_true, MiniGoParser.Literal_false, MiniGoParser.Literal_dec, MiniGoParser.Literal_bin, MiniGoParser.Literal_oct, MiniGoParser.Literal_hex, MiniGoParser.Literal_float, MiniGoParser.Literal_string, MiniGoParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.argument_list()
                pass
            elif token in [MiniGoParser.Rparen]:
                self.enterOuterAlt(localctx, 2)

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


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = MiniGoParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_argument_list)
        try:
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.argument()
                self.state = 546
                self.match(MiniGoParser.Comma)
                self.state = 547
                self.argument_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = MiniGoParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_int(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_intContext,0)


        def Literal_float(self):
            return self.getToken(MiniGoParser.Literal_float, 0)

        def Literal_string(self):
            return self.getToken(MiniGoParser.Literal_string, 0)

        def literal_bool(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_boolContext,0)


        def Literal_nil(self):
            return self.getToken(MiniGoParser.Literal_nil, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_prim_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrim_literal" ):
                return visitor.visitPrim_literal(self)
            else:
                return visitor.visitChildren(self)




    def prim_literal(self):

        localctx = MiniGoParser.Prim_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_prim_literal)
        try:
            self.state = 559
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Literal_dec, MiniGoParser.Literal_bin, MiniGoParser.Literal_oct, MiniGoParser.Literal_hex]:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.literal_int()
                pass
            elif token in [MiniGoParser.Literal_float]:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
                self.match(MiniGoParser.Literal_float)
                pass
            elif token in [MiniGoParser.Literal_string]:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.match(MiniGoParser.Literal_string)
                pass
            elif token in [MiniGoParser.Literal_true, MiniGoParser.Literal_false]:
                self.enterOuterAlt(localctx, 4)
                self.state = 557
                self.literal_bool()
                pass
            elif token in [MiniGoParser.Literal_nil]:
                self.enterOuterAlt(localctx, 5)
                self.state = 558
                self.match(MiniGoParser.Literal_nil)
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


    class Literal_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Literal_dec(self):
            return self.getToken(MiniGoParser.Literal_dec, 0)

        def Literal_bin(self):
            return self.getToken(MiniGoParser.Literal_bin, 0)

        def Literal_hex(self):
            return self.getToken(MiniGoParser.Literal_hex, 0)

        def Literal_oct(self):
            return self.getToken(MiniGoParser.Literal_oct, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_int" ):
                return visitor.visitLiteral_int(self)
            else:
                return visitor.visitChildren(self)




    def literal_int(self):

        localctx = MiniGoParser.Literal_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_literal_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.Literal_dec) | (1 << MiniGoParser.Literal_bin) | (1 << MiniGoParser.Literal_oct) | (1 << MiniGoParser.Literal_hex))) != 0)):
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


    class Literal_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Literal_false(self):
            return self.getToken(MiniGoParser.Literal_false, 0)

        def Literal_true(self):
            return self.getToken(MiniGoParser.Literal_true, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_bool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_bool" ):
                return visitor.visitLiteral_bool(self)
            else:
                return visitor.visitChildren(self)




    def literal_bool(self):

        localctx = MiniGoParser.Literal_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_literal_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.Literal_true or _la==MiniGoParser.Literal_false):
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_stmt)
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 567
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 568
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 569
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 570
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 571
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 572
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 573
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def ope_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Ope_assignContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MiniGoParser.RhsContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.lhs()
            self.state = 577
            self.ope_assign()
            self.state = 578
            self.rhs()
            self.state = 579
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def access_list(self):
            return self.getTypedRuleContext(MiniGoParser.Access_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_lhs)
        try:
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.match(MiniGoParser.Identifier)
                self.state = 582
                self.access_list(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 583
                self.match(MiniGoParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def access(self):
            return self.getTypedRuleContext(MiniGoParser.AccessContext,0)


        def access_list(self):
            return self.getTypedRuleContext(MiniGoParser.Access_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_access_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_list" ):
                return visitor.visitAccess_list(self)
            else:
                return visitor.visitChildren(self)



    def access_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Access_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_access_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.access()
            self._ctx.stop = self._input.LT(-1)
            self.state = 593
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Access_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_access_list)
                    self.state = 589
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 590
                    self.access() 
                self.state = 595
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess" ):
                return visitor.visitAccess(self)
            else:
                return visitor.visitChildren(self)




    def access(self):

        localctx = MiniGoParser.AccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_access)
        try:
            self.state = 598
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Lsquare]:
                self.enterOuterAlt(localctx, 1)
                self.state = 596
                self.array_access()
                pass
            elif token in [MiniGoParser.Ope_select]:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
                self.struct_access()
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


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lsquare(self):
            return self.getToken(MiniGoParser.Lsquare, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Rsquare(self):
            return self.getToken(MiniGoParser.Rsquare, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(MiniGoParser.Lsquare)
            self.state = 601
            self.expr(0)
            self.state = 602
            self.match(MiniGoParser.Rsquare)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ope_select(self):
            return self.getToken(MiniGoParser.Ope_select, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_access" ):
                return visitor.visitStruct_access(self)
            else:
                return visitor.visitChildren(self)




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.Ope_select)
            self.state = 605
            self.match(MiniGoParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ope_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ope_init(self):
            return self.getToken(MiniGoParser.Ope_init, 0)

        def Ope_assign_div(self):
            return self.getToken(MiniGoParser.Ope_assign_div, 0)

        def Ope_assign_minus(self):
            return self.getToken(MiniGoParser.Ope_assign_minus, 0)

        def Ope_assign_mod(self):
            return self.getToken(MiniGoParser.Ope_assign_mod, 0)

        def Ope_assign_multi(self):
            return self.getToken(MiniGoParser.Ope_assign_multi, 0)

        def Ope_assign_plus(self):
            return self.getToken(MiniGoParser.Ope_assign_plus, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ope_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpe_assign" ):
                return visitor.visitOpe_assign(self)
            else:
                return visitor.visitChildren(self)




    def ope_assign(self):

        localctx = MiniGoParser.Ope_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_ope_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.Ope_init) | (1 << MiniGoParser.Ope_assign_plus) | (1 << MiniGoParser.Ope_assign_minus) | (1 << MiniGoParser.Ope_assign_multi) | (1 << MiniGoParser.Ope_assign_div) | (1 << MiniGoParser.Ope_assign_mod))) != 0)):
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


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def literal_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_rhs)
        try:
            self.state = 612
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 609
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
                self.full_array_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 611
                self.literal_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def partial_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Partial_array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_array" ):
                return visitor.visitLiteral_array(self)
            else:
                return visitor.visitChildren(self)




    def literal_array(self):

        localctx = MiniGoParser.Literal_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_literal_array)
        try:
            self.state = 616
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Lsquare]:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self.full_array_literal()
                pass
            elif token in [MiniGoParser.Lcurly]:
                self.enterOuterAlt(localctx, 2)
                self.state = 615
                self.partial_array_literal()
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


    class Full_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def array_element_set(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_setContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_full_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFull_array_literal" ):
                return visitor.visitFull_array_literal(self)
            else:
                return visitor.visitChildren(self)




    def full_array_literal(self):

        localctx = MiniGoParser.Full_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_full_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.array_type()
            self.state = 619
            self.match(MiniGoParser.Lcurly)
            self.state = 620
            self.array_element_set()
            self.state = 621
            self.match(MiniGoParser.Rcurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Partial_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def array_element_set(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_setContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_partial_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPartial_array_literal" ):
                return visitor.visitPartial_array_literal(self)
            else:
                return visitor.visitChildren(self)




    def partial_array_literal(self):

        localctx = MiniGoParser.Partial_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_partial_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.match(MiniGoParser.Lcurly)
            self.state = 624
            self.array_element_set()
            self.state = 625
            self.match(MiniGoParser.Rcurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element_set

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_set" ):
                return visitor.visitArray_element_set(self)
            else:
                return visitor.visitChildren(self)




    def array_element_set(self):

        localctx = MiniGoParser.Array_element_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_array_element_set)
        try:
            self.state = 629
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Ope_minus, MiniGoParser.Ope_not, MiniGoParser.Lparen, MiniGoParser.Lsquare, MiniGoParser.Lcurly, MiniGoParser.Literal_nil, MiniGoParser.Literal_true, MiniGoParser.Literal_false, MiniGoParser.Literal_dec, MiniGoParser.Literal_bin, MiniGoParser.Literal_oct, MiniGoParser.Literal_hex, MiniGoParser.Literal_float, MiniGoParser.Literal_string, MiniGoParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 627
                self.array_element_list()
                pass
            elif token in [MiniGoParser.Rcurly]:
                self.enterOuterAlt(localctx, 2)

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


    class Array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_list" ):
                return visitor.visitArray_element_list(self)
            else:
                return visitor.visitChildren(self)




    def array_element_list(self):

        localctx = MiniGoParser.Array_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_array_element_list)
        try:
            self.state = 636
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 631
                self.array_element()
                self.state = 632
                self.match(MiniGoParser.Comma)
                self.state = 633
                self.array_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 635
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def literal_array(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_arrayContext,0)


        def literal_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_array_element)
        try:
            self.state = 641
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 638
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 639
                self.literal_array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 640
                self.literal_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def struct_element_set(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_element_setContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_struct" ):
                return visitor.visitLiteral_struct(self)
            else:
                return visitor.visitChildren(self)




    def literal_struct(self):

        localctx = MiniGoParser.Literal_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_literal_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.match(MiniGoParser.Identifier)
            self.state = 644
            self.match(MiniGoParser.Lcurly)
            self.state = 645
            self.struct_element_set()
            self.state = 646
            self.match(MiniGoParser.Rcurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_element_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element_set

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_element_set" ):
                return visitor.visitStruct_element_set(self)
            else:
                return visitor.visitChildren(self)




    def struct_element_set(self):

        localctx = MiniGoParser.Struct_element_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_struct_element_set)
        try:
            self.state = 650
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 648
                self.struct_element_list()
                pass
            elif token in [MiniGoParser.Rcurly]:
                self.enterOuterAlt(localctx, 2)

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


    class Struct_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def struct_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_element_list" ):
                return visitor.visitStruct_element_list(self)
            else:
                return visitor.visitChildren(self)




    def struct_element_list(self):

        localctx = MiniGoParser.Struct_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_struct_element_list)
        try:
            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 652
                self.struct_element()
                self.state = 653
                self.match(MiniGoParser.Comma)
                self.state = 654
                self.struct_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 656
                self.struct_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Colon(self):
            return self.getToken(MiniGoParser.Colon, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_element" ):
                return visitor.visitStruct_element(self)
            else:
                return visitor.visitChildren(self)




    def struct_element(self):

        localctx = MiniGoParser.Struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_struct_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 659
            self.match(MiniGoParser.Identifier)
            self.state = 660
            self.match(MiniGoParser.Colon)
            self.state = 661
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matched(self):
            return self.getTypedRuleContext(MiniGoParser.MatchedContext,0)


        def unmatched(self):
            return self.getTypedRuleContext(MiniGoParser.UnmatchedContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_if_stmt)
        try:
            self.state = 665
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.matched()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 664
                self.unmatched()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_if(self):
            return self.getToken(MiniGoParser.Key_if, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def if_stmt_body(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_matched

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatched" ):
                return visitor.visitMatched(self)
            else:
                return visitor.visitChildren(self)




    def matched(self):

        localctx = MiniGoParser.MatchedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_matched)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.match(MiniGoParser.Key_if)
            self.state = 668
            self.match(MiniGoParser.Lparen)
            self.state = 669
            self.condition()
            self.state = 670
            self.match(MiniGoParser.Rparen)
            self.state = 671
            self.match(MiniGoParser.Lcurly)
            self.state = 672
            self.if_stmt_body()
            self.state = 673
            self.match(MiniGoParser.Rcurly)
            self.state = 674
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnmatchedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_if(self):
            return self.getToken(MiniGoParser.Key_if, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def if_stmt_body(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def else_stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unmatched

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnmatched" ):
                return visitor.visitUnmatched(self)
            else:
                return visitor.visitChildren(self)




    def unmatched(self):

        localctx = MiniGoParser.UnmatchedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_unmatched)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
            self.match(MiniGoParser.Key_if)
            self.state = 677
            self.match(MiniGoParser.Lparen)
            self.state = 678
            self.condition()
            self.state = 679
            self.match(MiniGoParser.Rparen)
            self.state = 680
            self.match(MiniGoParser.Lcurly)
            self.state = 681
            self.if_stmt_body()
            self.state = 682
            self.match(MiniGoParser.Rcurly)
            self.state = 683
            self.else_stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmt_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_set(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_setContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt_body" ):
                return visitor.visitIf_stmt_body(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt_body(self):

        localctx = MiniGoParser.If_stmt_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_if_stmt_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self.stmt_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_else(self):
            return self.getToken(MiniGoParser.Key_else, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def else_stmt_body(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmt_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt_list" ):
                return visitor.visitElse_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt_list(self):

        localctx = MiniGoParser.Else_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_else_stmt_list)
        try:
            self.state = 697
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 689
                self.match(MiniGoParser.Key_else)
                self.state = 690
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 691
                self.match(MiniGoParser.Key_else)
                self.state = 692
                self.match(MiniGoParser.Lcurly)
                self.state = 693
                self.else_stmt_body()
                self.state = 694
                self.match(MiniGoParser.Rcurly)
                self.state = 695
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmt_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_set(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_setContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt_body" ):
                return visitor.visitElse_stmt_body(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt_body(self):

        localctx = MiniGoParser.Else_stmt_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_else_stmt_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            self.stmt_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_basic(self):
            return self.getTypedRuleContext(MiniGoParser.For_basicContext,0)


        def for_icu(self):
            return self.getTypedRuleContext(MiniGoParser.For_icuContext,0)


        def for_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_for_stmt)
        try:
            self.state = 704
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 701
                self.for_basic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 702
                self.for_icu()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 703
                self.for_range()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_basicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_for(self):
            return self.getToken(MiniGoParser.Key_loop_for, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def for_body(self):
            return self.getTypedRuleContext(MiniGoParser.For_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_basic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_basic" ):
                return visitor.visitFor_basic(self)
            else:
                return visitor.visitChildren(self)




    def for_basic(self):

        localctx = MiniGoParser.For_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_for_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(MiniGoParser.Key_loop_for)
            self.state = 707
            self.condition()
            self.state = 708
            self.match(MiniGoParser.Lcurly)
            self.state = 709
            self.for_body()
            self.state = 710
            self.match(MiniGoParser.Rcurly)
            self.state = 711
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_icuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_for(self):
            return self.getToken(MiniGoParser.Key_loop_for, 0)

        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.Semicolon)
            else:
                return self.getToken(MiniGoParser.Semicolon, i)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def for_body(self):
            return self.getTypedRuleContext(MiniGoParser.For_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_icu

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_icu" ):
                return visitor.visitFor_icu(self)
            else:
                return visitor.visitChildren(self)




    def for_icu(self):

        localctx = MiniGoParser.For_icuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_for_icu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 713
            self.match(MiniGoParser.Key_loop_for)
            self.state = 714
            self.init()
            self.state = 715
            self.match(MiniGoParser.Semicolon)
            self.state = 716
            self.condition()
            self.state = 717
            self.match(MiniGoParser.Semicolon)
            self.state = 718
            self.update()
            self.state = 719
            self.match(MiniGoParser.Lcurly)
            self.state = 720
            self.for_body()
            self.state = 721
            self.match(MiniGoParser.Rcurly)
            self.state = 722
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Ope_init(self):
            return self.getToken(MiniGoParser.Ope_init, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Key_decl_var(self):
            return self.getToken(MiniGoParser.Key_decl_var, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def Ope_assign(self):
            return self.getToken(MiniGoParser.Ope_assign, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = MiniGoParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_init)
        try:
            self.state = 737
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 724
                self.match(MiniGoParser.Identifier)
                self.state = 725
                self.match(MiniGoParser.Ope_init)
                self.state = 726
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 727
                self.match(MiniGoParser.Key_decl_var)
                self.state = 728
                self.match(MiniGoParser.Identifier)
                self.state = 729
                self.data_type()
                self.state = 730
                self.match(MiniGoParser.Ope_assign)
                self.state = 731
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 733
                self.match(MiniGoParser.Key_decl_var)
                self.state = 734
                self.match(MiniGoParser.Identifier)
                self.state = 735
                self.match(MiniGoParser.Ope_assign)
                self.state = 736
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def ope_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Ope_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
            self.match(MiniGoParser.Identifier)
            self.state = 740
            self.ope_assign()
            self.state = 741
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_for(self):
            return self.getToken(MiniGoParser.Key_loop_for, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def value(self):
            return self.getTypedRuleContext(MiniGoParser.ValueContext,0)


        def Ope_init(self):
            return self.getToken(MiniGoParser.Ope_init, 0)

        def Key_range(self):
            return self.getToken(MiniGoParser.Key_range, 0)

        def array_instance(self):
            return self.getTypedRuleContext(MiniGoParser.Array_instanceContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def for_body(self):
            return self.getTypedRuleContext(MiniGoParser.For_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range" ):
                return visitor.visitFor_range(self)
            else:
                return visitor.visitChildren(self)




    def for_range(self):

        localctx = MiniGoParser.For_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_for_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
            self.match(MiniGoParser.Key_loop_for)
            self.state = 744
            self.index()
            self.state = 745
            self.match(MiniGoParser.Comma)
            self.state = 746
            self.value()
            self.state = 747
            self.match(MiniGoParser.Ope_init)
            self.state = 748
            self.match(MiniGoParser.Key_range)
            self.state = 749
            self.array_instance()
            self.state = 750
            self.match(MiniGoParser.Lcurly)
            self.state = 751
            self.for_body()
            self.state = 752
            self.match(MiniGoParser.Rcurly)
            self.state = 753
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_instance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_instance" ):
                return visitor.visitArray_instance(self)
            else:
                return visitor.visitChildren(self)




    def array_instance(self):

        localctx = MiniGoParser.Array_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_array_instance)
        try:
            self.state = 758
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 755
                self.match(MiniGoParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 756
                self.full_array_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 757
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = MiniGoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 760
            self.match(MiniGoParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 762
            self.match(MiniGoParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_set(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_setContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_body" ):
                return visitor.visitFor_body(self)
            else:
                return visitor.visitChildren(self)




    def for_body(self):

        localctx = MiniGoParser.For_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_for_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 764
            self.stmt_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_break(self):
            return self.getToken(MiniGoParser.Key_loop_break, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 766
            self.match(MiniGoParser.Key_loop_break)
            self.state = 767
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_continue(self):
            return self.getToken(MiniGoParser.Key_loop_continue, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 769
            self.match(MiniGoParser.Key_loop_continue)
            self.state = 770
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_stmtContext,0)


        def method_call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Method_call_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_call_stmt)
        try:
            self.state = 774
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 772
                self.func_call_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 773
                self.method_call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = MiniGoParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776
            self.func_call()
            self.state = 777
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call_stmt" ):
                return visitor.visitMethod_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_call_stmt(self):

        localctx = MiniGoParser.Method_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_method_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 779
            self.method_call()
            self.state = 780
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Ope_select(self):
            return self.getToken(MiniGoParser.Ope_select, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 782
            self.expr(0)
            self.state = 783
            self.match(MiniGoParser.Ope_select)
            self.state = 784
            self.func_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_return(self):
            return self.getToken(MiniGoParser.Key_return, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_return_stmt)
        try:
            self.state = 792
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 786
                self.match(MiniGoParser.Key_return)
                self.state = 787
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 788
                self.match(MiniGoParser.Key_return)
                self.state = 789
                self.expr(0)
                self.state = 790
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[38] = self.expr_sempred
        self._predicates[39] = self.expr1_sempred
        self._predicates[40] = self.expr2_sempred
        self._predicates[42] = self.expr3_sempred
        self._predicates[43] = self.expr4_sempred
        self._predicates[45] = self.expr6_sempred
        self._predicates[58] = self.access_list_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def access_list_sempred(self, localctx:Access_listContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




