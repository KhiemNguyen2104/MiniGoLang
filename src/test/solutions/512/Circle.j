.source Circle.java
.class public Circle
.super java.lang.Object
.field radius F

.method public <init>()V
.var 0 is this LCircle; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public CirArea()F
Label0:
.var 0 is c LCircle; from Label0 to Label1
	aload_0
	getfield Circle.radius F
	aload_0
	getfield Circle.radius F
	fmul
	getstatic MiniGoClass/Pi F
	fmul
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public CirPerimeter()F
Label0:
.var 0 is c LCircle; from Label0 to Label1
	aload_0
	getfield Circle.radius F
	iconst_2
	i2f
	fmul
	getstatic MiniGoClass/Pi F
	fmul
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method
