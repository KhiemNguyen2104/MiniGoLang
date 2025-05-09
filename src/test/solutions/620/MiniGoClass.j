.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo(II[[Ljava/lang/String;LCircle;LCircle;)F
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is d I from Label0 to Label1
.var 2 is b [[Ljava/lang/String; from Label0 to Label1
.var 3 is c LCircle; from Label0 to Label1
.var 4 is e LCircle; from Label0 to Label1
	aload_2
	iconst_0
	aaload
	iconst_1
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
.var 5 is rec_area I from Label0 to Label1
	iload_0
	iload_1
	iadd
	iconst_2
	imul
	istore 5
.var 6 is cir_area F from Label0 to Label1
	aload 4
	getfield Circle.radius F
	aload 4
	getfield Circle.radius F
	fmul
	ldc 3.14
	fmul
	fstore 6
.var 7 is c F from Label0 to Label1
	fconst_1
	aload 4
	getfield Circle.radius F
	fmul
	fstore 7
	aload 4
	ldc 1.2
	putfield Circle.radius F
	fload 7
	freturn
Label1:
.limit stack 3
.limit locals 8
.end method

.method public static foo1()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [[Ljava/lang/String; from Label0 to Label1
	iconst_2
	iconst_2
	multianewarray [[Ljava/lang/String; 2
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "a"
	aastore
	dup
	iconst_1
	ldc "b"
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "c"
	aastore
	dup
	iconst_1
	ldc "d"
	aastore
	aastore
	astore_1
.var 2 is c LCircle; from Label0 to Label1
	new Circle
	dup
	invokespecial Circle/<init>()V
	dup
	ldc 3.12
	putfield Circle.radius F
	astore_2
	iconst_1
	iconst_2
	aload_1
	aload_2
	aload_2
	invokestatic MiniGoClass/foo(II[[Ljava/lang/String;LCircle;LCircle;)F
	invokestatic io/putFloatLn(F)V
	aload_2
	getfield Circle.radius F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 11
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
