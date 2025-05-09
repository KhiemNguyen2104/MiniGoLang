.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static calculateArea(FF)F
Label0:
.var 0 is width F from Label0 to Label1
.var 1 is height F from Label0 to Label1
.var 2 is area F from Label0 to Label1
	fconst_0
	fstore_2
	fload_0
	fload_1
	fmul
	fstore_2
	fload_2
	freturn
Label1:
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is d F from Label0 to Label1
	fconst_1
	ldc 20.0
	invokestatic MiniGoClass/calculateArea(FF)F
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
