.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a LA; from Label0 to Label1
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_4
	putfield A.a I
	astore_1
.var 2 is d I from Label0 to Label1
	aload_1
	iconst_1
	iconst_1
	iadd
	iconst_3
	invokevirtual A/b(II)I
	istore_2
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 3
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
