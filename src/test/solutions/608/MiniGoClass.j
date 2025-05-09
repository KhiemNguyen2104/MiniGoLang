.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is recs [LRectangle; from Label0 to Label1
	iconst_3
	anewarray Rectangle
	dup
	iconst_0
	new Rectangle
	dup
	invokespecial Rectangle/<init>()V
	dup
	bipush 10
	putfield Rectangle.length I
	dup
	bipush 20
	putfield Rectangle.width I
	aastore
	dup
	iconst_1
	new Rectangle
	dup
	invokespecial Rectangle/<init>()V
	dup
	iconst_5
	putfield Rectangle.length I
	dup
	iconst_1
	putfield Rectangle.width I
	aastore
	dup
	iconst_2
	new Rectangle
	dup
	invokespecial Rectangle/<init>()V
	dup
	iconst_4
	putfield Rectangle.length I
	dup
	iconst_3
	putfield Rectangle.width I
	aastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	ldc "Check the rectangle "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	invokestatic io/putIntLn(I)V
.var 3 is cir I from Label4 to Label5
	aload_1
	iload_2
	aaload
	iconst_1
	invokevirtual Rectangle/Circum(I)I
	istore_3
	iload_3
	iconst_5
	if_icmple Label9
Label10:
	ldc "Area: "
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	iload_2
	aaload
	invokevirtual Rectangle/Area()F
	invokestatic io/putFloatLn(F)V
Label11:
	goto Label8
Label9:
Label12:
	ldc "It is so small!"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label13:
Label8:
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 9
.limit locals 4
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
