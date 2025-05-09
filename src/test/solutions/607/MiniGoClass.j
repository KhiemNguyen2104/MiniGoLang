.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static d I
.field static arr_2 [F
.field static multiArr [[[I
.field static x Ljava/lang/String;
.field static final idx I
.field static arr [I
.field static final y I
.field static final z I

.method public static print(Ljava/lang/String;)V
Label0:
.var 0 is a Ljava/lang/String; from Label0 to Label1
	aload_0
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static One()I
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b [I from Label0 to Label1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 11
	iastore
	dup
	iconst_2
	bipush 12
	iastore
	astore_1
.var 2 is boo Z from Label0 to Label1
	iconst_0
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_2
.var 3 is ARR [[I from Label0 to Label1
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
	astore_3
.var 4 is idx I from Label0 to Label1
	iconst_1
	istore 4
.var 5 is val I from Label0 to Label1
	iconst_2
	bipush 6
	imul
	istore 5
.var 6 is y I from Label0 to Label1
	aload_3
	iconst_0
	aaload
	iconst_0
	iaload
	istore 6
	aload_3
	iconst_0
	aaload
	iconst_1
	bipush 9
	iastore
	getstatic MiniGoClass/arr [I
	iconst_1
	bipush 21
	iastore
	iload 4
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/x Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload 6
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/z I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/arr_2 [F
	iconst_1
	faload
	invokestatic io/putFloatLn(F)V
	iload 5
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/arr [I
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
	aload_3
	iconst_0
	aaload
	iconst_1
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 12
.limit locals 7
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
	putstatic MiniGoClass.d I
	iconst_3
	newarray float
	dup
	iconst_0
	fconst_1
	fastore
	dup
	iconst_1
	fconst_2
	ldc 3.0
	fadd
	fastore
	dup
	iconst_2
	ldc 3.3
	fastore
	putstatic MiniGoClass.arr_2 [F
	iconst_4
	getstatic MiniGoClass/d I
	iconst_3
	multianewarray [[[I 3
	dup
	iconst_0
	aaload
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iconst_1
	iadd
	iconst_1
	isub
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_0
	aaload
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	aastore
	dup
	iconst_1
	aaload
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 7
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
	dup
	iconst_1
	aaload
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 11
	iastore
	dup
	iconst_2
	bipush 12
	iastore
	aastore
	dup
	iconst_2
	aaload
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 13
	iastore
	dup
	iconst_1
	bipush 14
	iastore
	dup
	iconst_2
	bipush 15
	iastore
	aastore
	dup
	iconst_2
	aaload
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 16
	iastore
	dup
	iconst_1
	bipush 17
	iastore
	dup
	iconst_2
	bipush 18
	iastore
	aastore
	dup
	iconst_3
	aaload
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 19
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 21
	iastore
	aastore
	dup
	iconst_3
	aaload
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 22
	iastore
	dup
	iconst_1
	bipush 23
	iastore
	dup
	iconst_2
	bipush 24
	iastore
	aastore
	putstatic MiniGoClass.multiArr [[[I
	ldc "abc"
	putstatic MiniGoClass.x Ljava/lang/String;
	iconst_1
	iconst_1
	ineg
	isub
	iconst_1
	isub
	putstatic MiniGoClass.idx I
	iconst_3
	newarray int
	dup
	iconst_0
	getstatic MiniGoClass/idx I
	iastore
	dup
	iconst_1
	sipush 431
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	putstatic MiniGoClass.arr [I
	getstatic MiniGoClass/arr [I
	iconst_1
	iaload
	putstatic MiniGoClass.y I
	getstatic MiniGoClass/multiArr [[[I
	iconst_1
	aaload
	iconst_1
	aaload
	iconst_2
	iaload
	putstatic MiniGoClass.z I
Label1:
	return
.limit stack 19
.limit locals 0
.end method
