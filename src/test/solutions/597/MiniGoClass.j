.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final b Z
.field static final t I
.field static final d I
.field static arr [[I

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
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is flag Z from Label0 to Label1
	iconst_0
	istore_3
.var 4 is k [I from Label0 to Label1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iconst_1
	iadd
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	astore 4
.var 5 is l I from Label0 to Label1
	aload 4
	iconst_0
	iaload
	istore 5
.var 6 is subArr [I from Label0 to Label1
	iload 5
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	astore 6
Label2:
Label4:
	iload_1
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
Label10:
	iload_2
	iconst_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label9
	getstatic MiniGoClass/arr [[I
	iload_1
	aaload
	iload_2
	iaload
	iconst_5
	if_icmple Label15
Label16:
	iconst_1
	istore_3
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label17:
Label15:
	iload_1
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label11:
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	iconst_0
	istore_2
	goto Label2
Label5:
Label3:
Label1:
	return
.limit stack 6
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
	iconst_1
	iconst_4
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	putstatic MiniGoClass.b Z
	iconst_1
	putstatic MiniGoClass.t I
	iconst_3
	getstatic MiniGoClass/t I
	iadd
	iconst_1
	ineg
	iconst_2
	imul
	isub
	iconst_3
	isub
	putstatic MiniGoClass.d I
	iconst_2
	getstatic MiniGoClass/d I
	multianewarray [[I 2
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 7
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
	putstatic MiniGoClass.arr [[I
Label1:
	return
.limit stack 11
.limit locals 0
.end method
