.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static people [LPerson;

.method public static checkEvenOdd(I)V
Label0:
.var 0 is num I from Label0 to Label1
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpne Label3
Label4:
	ldc "Even number"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label5:
	goto Label2
Label3:
Label6:
	ldc "Odd number"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label7:
Label2:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label4 to Label5
	iconst_0
	istore_1
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
	getstatic MiniGoClass/people [LPerson;
	iload_1
	aaload
	getfield Person.age I
	invokestatic MiniGoClass/checkEvenOdd(I)V
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 2
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
	bipush 21
	putfield Person.age I
	aastore
	dup
	iconst_2
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Anh"
	putfield Person.name Ljava/lang/String;
	dup
	bipush 23
	putfield Person.age I
	aastore
	putstatic MiniGoClass.people [LPerson;
Label1:
	return
.limit stack 7
.limit locals 0
.end method
