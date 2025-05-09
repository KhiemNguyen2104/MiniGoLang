.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static arr [[I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is b Z from Label0 to Label1
	iconst_1
	istore_2
	invokestatic io/getInt()I
	istore_1
	iload_1
	getstatic MiniGoClass/arr [[I
	iconst_1
	aaload
	iconst_1
	iaload
	iadd
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
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
	iconst_2
	iconst_2
	multianewarray [[I 2
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	aastore
	putstatic MiniGoClass.arr [[I
Label1:
	return
.limit stack 11
.limit locals 0
.end method
