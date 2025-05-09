.source Person.java
.class public Person
.super java.lang.Object
.field birth_year I

.method public <init>()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public cal_age(I)I
Label0:
.var 0 is p LPerson; from Label0 to Label1
.var 1 is current_year I from Label0 to Label1
	aload_0
	getfield Person.birth_year I
	iload_1
	isub
	ineg
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method
