.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static counter I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	fconst_1
	getstatic MiniGoClass/counter I
	i2f
	fadd
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
	iconst_0
	putstatic MiniGoClass.counter I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
