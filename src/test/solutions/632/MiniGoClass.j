.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final c I
.field static arr [[I

.method public static add(II)I
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
	iload_0
	iload_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/arr [[I
	iconst_0
	aaload
	iconst_0
	iaload
	bipush 12
	invokestatic MiniGoClass/add(II)I
	invokestatic io/putInt(I)V
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
	iconst_1
	putstatic MiniGoClass.c I
	getstatic MiniGoClass/c I
	iconst_1
	multianewarray [[I 2
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	aastore
	putstatic MiniGoClass.arr [[I
Label1:
	return
.limit stack 10
.limit locals 0
.end method
