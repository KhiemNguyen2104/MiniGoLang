.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static names [Ljava/lang/String;
.field static arr [F

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
.var 2 is e LEmail; from Label4 to Label5
	new Email
	dup
	invokespecial Email/<init>()V
	dup
	getstatic MiniGoClass/names [Ljava/lang/String;
	iload_1
	aaload
	putfield Email.name Ljava/lang/String;
	astore_2
	aload_2
	invokevirtual Email/toString()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
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
.limit stack 5
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
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Andres"
	aastore
	dup
	iconst_1
	ldc "Brown"
	aastore
	dup
	iconst_2
	ldc "Laura"
	aastore
	putstatic MiniGoClass.names [Ljava/lang/String;
	iconst_3
	newarray float
	dup
	iconst_0
	fconst_1
	fastore
	dup
	iconst_1
	ldc 3.0
	fastore
	dup
	iconst_2
	ldc 4.0
	fastore
	putstatic MiniGoClass.arr [F
Label1:
	return
.limit stack 6
.limit locals 0
.end method
