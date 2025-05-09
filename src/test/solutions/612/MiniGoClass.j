.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final i I
.field static final j I
.field static arr [[[Z

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/arr [[[Z
	iconst_1
	iconst_1
	iadd
	aaload
	iconst_2
	aaload
	iconst_0
	baload
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 3
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
	iconst_1
	iadd
	iconst_1
	iadd
	putstatic MiniGoClass.i I
	iconst_2
	iconst_1
	ineg
	ineg
	imul
	putstatic MiniGoClass.j I
	iconst_3
	getstatic MiniGoClass/i I
	getstatic MiniGoClass/j I
	multianewarray [[[Z 3
	dup
	iconst_0
	aaload
	iconst_0
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	dup
	iconst_0
	aaload
	iconst_1
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	dup
	iconst_0
	aaload
	iconst_2
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	dup
	iconst_1
	aaload
	iconst_0
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	dup
	iconst_1
	aaload
	iconst_1
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	dup
	iconst_1
	aaload
	iconst_2
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	dup
	iconst_2
	aaload
	iconst_0
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	dup
	iconst_2
	aaload
	iconst_1
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	dup
	iconst_2
	aaload
	iconst_2
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	putstatic MiniGoClass.arr [[[Z
Label1:
	return
.limit stack 19
.limit locals 0
.end method
