.source Int.java
.class public Int
.super java.lang.Object
.field num I

.method public <init>()V
.var 0 is this LInt; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public Exp()F
Label0:
.var 0 is i LInt; from Label0 to Label1
	aload_0
	aload_0
	getfield Int.num I
	getstatic MiniGoClass/E I
	invokevirtual Int/Pow(II)F
	freturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public Pow(II)F
Label0:
.var 0 is i LInt; from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is e I from Label0 to Label1
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is prod F from Label0 to Label1
	fconst_1
	fstore 4
Label2:
Label4:
	iload_3
	iload_1
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	fload 4
	iload_2
	i2f
	fmul
	fstore 4
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label5:
Label3:
	fload 4
	freturn
Label1:
.limit stack 2
.limit locals 5
.end method
