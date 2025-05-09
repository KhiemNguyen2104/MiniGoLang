.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static x F

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/x F
	iconst_1
	i2f
	fadd
	putstatic MiniGoClass.x F
	ldc "This is a string"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MiniGoClass/x F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
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
	ldc 1.2
	putstatic MiniGoClass.x F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
