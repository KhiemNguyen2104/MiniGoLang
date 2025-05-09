.source Rectangle.java
.class public Rectangle
.super java.lang.Object
.field length I
.field width I

.method public <init>()V
.var 0 is this LRectangle; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public Circum(I)I
Label0:
.var 0 is r LRectangle; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	aload_0
	getfield Rectangle.length I
	aload_0
	getfield Rectangle.width I
	iadd
	iconst_2
	imul
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public Area()F
Label0:
.var 0 is r LRectangle; from Label0 to Label1
	aload_0
	getfield Rectangle.length I
	aload_0
	getfield Rectangle.width I
	imul
	i2f
	fconst_1
	fmul
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method
