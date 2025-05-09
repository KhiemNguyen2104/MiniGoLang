.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final Pi F
.field static final E I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i LInt; from Label0 to Label1
	new Int
	dup
	invokespecial Int/<init>()V
	dup
	iconst_3
	putfield Int.num I
	astore_1
	aload_1
	invokevirtual Int/Exp()F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <clinit>()V
Label0:
	ldc 3.14
	putstatic MiniGoClass.Pi F
	iconst_2
	putstatic MiniGoClass.E I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
