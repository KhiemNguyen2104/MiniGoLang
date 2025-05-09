.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final Pi F
.field static final Maxsize F

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/Maxsize F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 1
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
	iconst_1
	i2f
	ldc 140.0
	fadd
	ldc 34.3
	fdiv
	bipush 54
	iconst_4
	irem
	i2f
	fmul
	putstatic MiniGoClass.Maxsize F
Label1:
	return
.limit stack 3
.limit locals 0
.end method
