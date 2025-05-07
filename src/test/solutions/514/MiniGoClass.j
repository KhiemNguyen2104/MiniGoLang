.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static last_name Ljava/lang/String;
.field static final d I
.field static final ar [[I
.field static first_name Ljava/lang/String;
.field static x F

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [[F from Label0 to Label1
	iconst_2
	iconst_3
	multianewarray [[F 2
	dup
	iconst_0
	iconst_3
	newarray float
	dup
	iconst_0
	getstatic MiniGoClass/d I
	iconst_3
	multianewarray [[I 2
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 13
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	aastore
	iconst_0
	aaload
	iconst_0
	iaload
	i2f
	fastore
	dup
	iconst_1
	getstatic MiniGoClass/d I
	iconst_3
	multianewarray [[I 2
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 13
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	aastore
	iconst_0
	aaload
	iconst_1
	iaload
	i2f
	fastore
	dup
	iconst_2
	getstatic MiniGoClass/d I
	iconst_3
	multianewarray [[I 2
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 13
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	aastore
	iconst_0
	aaload
	iconst_2
	iaload
	i2f
	fastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray float
	dup
	iconst_0
	getstatic MiniGoClass/d I
	iconst_3
	multianewarray [[I 2
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 13
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	aastore
	iconst_1
	aaload
	iconst_0
	iaload
	i2f
	fastore
	dup
	iconst_1
	getstatic MiniGoClass/d I
	iconst_3
	multianewarray [[I 2
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 13
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	aastore
	iconst_1
	aaload
	iconst_1
	iaload
	i2f
	fastore
	dup
	iconst_2
	getstatic MiniGoClass/d I
	iconst_3
	multianewarray [[I 2
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 13
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	aastore
	iconst_1
	aaload
	iconst_2
	iaload
	i2f
	fastore
	aastore
	astore_1
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	getstatic MiniGoClass/last_name Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	ldc " "
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	getstatic MiniGoClass/first_name Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iconst_0
	aaload
	iconst_0
	faload
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 15
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
	ldc "Khiem"
	putstatic MiniGoClass.last_name Ljava/lang/String;
	iconst_2
	putstatic MiniGoClass.d I
	iconst_2
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
	dup
	iconst_1
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_2
	iastore
	aastore
	putstatic MiniGoClass.ar [[I
	ldc "Nguyen Phuc Gia"
	putstatic MiniGoClass.first_name Ljava/lang/String;
	iconst_1
	i2f
	fconst_1
	fadd
	putstatic MiniGoClass.x F
Label1:
	return
.limit stack 11
.limit locals 0
.end method
