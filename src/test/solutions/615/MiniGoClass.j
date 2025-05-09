.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a LPerson;
.field static ARR [LPerson;
.field static final d I
.field static arr [I
.field static nullArr [F

.method public static change(Ljava/lang/String;)V
Label0:
.var 0 is str Ljava/lang/String; from Label0 to Label1
	ldc "Ha"
	astore_0
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is s Ljava/lang/String; from Label0 to Label1
	ldc "1"
	astore_1
	getstatic MiniGoClass/a LPerson;
	getfield Person.age I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/ARR [LPerson;
	iconst_1
	aaload
	putstatic MiniGoClass.a LPerson;
	aload_1
	invokestatic MiniGoClass/change(Ljava/lang/String;)V
.var 2 is i I from Label4 to Label5
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_5
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	getstatic MiniGoClass/arr [I
	iload_2
	iaload
	invokestatic io/putIntLn(I)V
	iload_2
	iconst_2
	if_icmpne Label9
Label10:
	goto Label3
Label11:
Label9:
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label3:
	getstatic MiniGoClass/a LPerson;
	ldc "Tan Lo Regulus"
	putfield Person.name Ljava/lang/String;
	getstatic MiniGoClass/a LPerson;
	getfield Person.name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
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
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Khiem"
	putfield Person.name Ljava/lang/String;
	dup
	iconst_0
	putfield Person.age I
	putstatic MiniGoClass.a LPerson;
	iconst_2
	anewarray Person
	dup
	iconst_0
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Khiem"
	putfield Person.name Ljava/lang/String;
	dup
	bipush 21
	putfield Person.age I
	aastore
	dup
	iconst_1
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Bao"
	putfield Person.name Ljava/lang/String;
	dup
	bipush 20
	putfield Person.age I
	aastore
	putstatic MiniGoClass.ARR [LPerson;
	iconst_3
	putstatic MiniGoClass.d I
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	getstatic MiniGoClass/d I
	iadd
	bipush 6
	isub
	iastore
	dup
	iconst_1
	iconst_2
	iconst_2
	iadd
	iastore
	dup
	iconst_2
	iconst_3
	getstatic MiniGoClass/d I
	imul
	getstatic MiniGoClass/d I
	imul
	iastore
	putstatic MiniGoClass.arr [I
	aconst_null
	putstatic MiniGoClass.nullArr [F
Label1:
	return
.limit stack 7
.limit locals 0
.end method
