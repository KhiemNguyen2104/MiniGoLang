.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static arr [F

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
	iconst_5
	newarray float
	dup
	iconst_0
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	dup
	iconst_3
	bipush 40
	iastore
	dup
	iconst_4
	bipush 50
	iastore
	iconst_0
	iaload
	i2f
	fastore
	dup
	iconst_1
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	dup
	iconst_3
	bipush 40
	iastore
	dup
	iconst_4
	bipush 50
	iastore
	iconst_1
	iaload
	i2f
	fastore
	dup
	iconst_2
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	dup
	iconst_3
	bipush 40
	iastore
	dup
	iconst_4
	bipush 50
	iastore
	iconst_2
	iaload
	i2f
	fastore
	dup
	iconst_3
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	dup
	iconst_3
	bipush 40
	iastore
	dup
	iconst_4
	bipush 50
	iastore
	iconst_3
	iaload
	i2f
	fastore
	dup
	iconst_4
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	dup
	iconst_3
	bipush 40
	iastore
	dup
	iconst_4
	bipush 50
	iastore
	iconst_4
	iaload
	i2f
	fastore
	putstatic MiniGoClass.arr [F
.var 2 is value F from Label0 to Label1
	getstatic MiniGoClass/arr [F
	iconst_1
	iconst_2
	iload_1
	iconst_3
	isub
	imul
	iconst_4
	idiv
	iadd
	faload
	fstore_2
	fload_2
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 10
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
	aconst_null
	putstatic MiniGoClass.arr [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
