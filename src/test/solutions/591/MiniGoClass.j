.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo()V
Label0:
.var 0 is x I from Label0 to Label1
	iconst_3
	bipush 7
	imul
	iconst_2
	iadd
	iconst_1
	ineg
	isub
	bipush 8
	idiv
	iconst_5
	iconst_4
	irem
	iadd
	istore_0
	iload_0
	bipush 10
	if_icmpge Label3
Label4:
	iload_0
	invokestatic io/putIntLn(I)V
Label5:
	goto Label2
Label3:
Label6:
	iload_0
	iconst_0
	if_icmpge Label9
Label10:
	iload_0
	iconst_1
	iadd
	istore_0
	iload_0
	invokestatic io/putInt(I)V
Label11:
	goto Label8
Label9:
Label12:
	bipush 10
	invokestatic io/putIntLn(I)V
Label13:
Label8:
Label7:
Label2:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is p LPerson; from Label0 to Label1
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	sipush 2004
	putfield Person.birth_year I
	astore_1
	aload_1
	sipush 2025
	invokevirtual Person/cal_age(I)I
	invokestatic io/putIntLn(I)V
	invokestatic MiniGoClass/foo()V
Label1:
	return
.limit stack 4
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
