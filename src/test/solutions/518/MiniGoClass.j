.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static x [La;

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label2:
Label4:
	iload_1
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	ldc "Element "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	invokestatic io/putInt(I)V
	ldc ": "
	invokestatic io/putString(Ljava/lang/String;)V
	getstatic MiniGoClass/x [La;
	iload_1
	aaload
	getfield a.hello LHello;
	getfield Hello.hi LHi;
	getfield Hi.Goodbye [I
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label5:
Label3:
Label1:
	return
.limit stack 3
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
	iconst_3
	anewarray a
	dup
	iconst_0
	new a
	dup
	invokespecial a/<init>()V
	dup
	new Hello
	dup
	invokespecial Hello/<init>()V
	dup
	new Hi
	dup
	invokespecial Hi/<init>()V
	dup
	bipush 6
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 6
	iastore
	putfield Hi.Goodbye [I
	putfield Hello.hi LHi;
	putfield a.hello LHello;
	aastore
	dup
	iconst_1
	new a
	dup
	invokespecial a/<init>()V
	dup
	new Hello
	dup
	invokespecial Hello/<init>()V
	dup
	new Hi
	dup
	invokespecial Hi/<init>()V
	dup
	bipush 6
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
	dup
	iconst_3
	bipush 10
	iastore
	dup
	iconst_4
	bipush 11
	iastore
	dup
	iconst_5
	bipush 12
	iastore
	putfield Hi.Goodbye [I
	putfield Hello.hi LHi;
	putfield a.hello LHello;
	aastore
	dup
	iconst_2
	new a
	dup
	invokespecial a/<init>()V
	dup
	new Hello
	dup
	invokespecial Hello/<init>()V
	dup
	new Hi
	dup
	invokespecial Hi/<init>()V
	dup
	bipush 6
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
	dup
	iconst_3
	bipush 16
	iastore
	dup
	iconst_4
	bipush 17
	iastore
	dup
	iconst_5
	bipush 18
	iastore
	putfield Hi.Goodbye [I
	putfield Hello.hi LHi;
	putfield a.hello LHello;
	aastore
	putstatic MiniGoClass.x [La;
Label1:
	return
.limit stack 17
.limit locals 0
.end method
