.source A.java
.class public A
.super java.lang.Object
.field a I

.method public <init>()V
.var 0 is this LA; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public b(II)I
Label0:
.var 0 is a LA; from Label0 to Label1
.var 1 is c I from Label0 to Label1
.var 2 is d I from Label0 to Label1
	iload_1
	iload_2
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 3
.end method
