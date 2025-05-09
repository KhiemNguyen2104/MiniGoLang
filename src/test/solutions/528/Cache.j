.source Cache.java
.class public Cache
.super java.lang.Object
.field data [Ljava/lang/String;
.field timestamp [I
.field size I
.field capacity I

.method public <init>()V
.var 0 is this LCache; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public get(I)Ljava/lang/String;
Label0:
.var 0 is c LCache; from Label0 to Label1
.var 1 is key I from Label0 to Label1
	iload_1
	iconst_0
	if_icmplt Label5
	iload_1
	aload_0
	getfield Cache.size I
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifeq Label3
	aload_0
	getfield Cache.timestamp [I
	iload_1
	iaload
	iconst_0
	if_icmple Label3
Label7:
	aload_0
	getfield Cache.timestamp [I
	iload_1
	invokestatic MiniGoClass/getCurrentTime()I
	iastore
	aload_0
	getfield Cache.data [Ljava/lang/String;
	iload_1
	aaload
	areturn
Label8:
Label3:
	ldc ""
	areturn
Label1:
.limit stack 7
.limit locals 2
.end method

.method public put(ILjava/lang/String;)V
Label0:
.var 0 is c LCache; from Label0 to Label1
.var 1 is key I from Label0 to Label1
.var 2 is value Ljava/lang/String; from Label0 to Label1
	iload_1
	iconst_0
	if_icmplt Label3
	iload_1
	aload_0
	getfield Cache.capacity I
	if_icmpge Label3
Label4:
	aload_0
	getfield Cache.data [Ljava/lang/String;
	iload_1
	aload_2
	aastore
	aload_0
	getfield Cache.timestamp [I
	iload_1
	invokestatic MiniGoClass/getCurrentTime()I
	iastore
	iload_1
	aload_0
	getfield Cache.size I
	if_icmplt Label7
Label8:
	aload_0
	iload_1
	iconst_1
	iadd
	putfield Cache.size I
Label9:
Label7:
Label5:
Label3:
Label1:
	return
.limit stack 7
.limit locals 3
.end method

.method public clear()V
Label0:
.var 0 is c LCache; from Label0 to Label1
.var 1 is i I from Label4 to Label5
	iconst_0
	istore_1
Label4:
	iload_1
	aload_0
	getfield Cache.capacity I
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	aload_0
	getfield Cache.data [Ljava/lang/String;
	iload_1
	ldc ""
	aastore
	aload_0
	getfield Cache.timestamp [I
	iload_1
	iconst_0
	iastore
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label3:
	aload_0
	iconst_0
	putfield Cache.size I
Label1:
	return
.limit stack 6
.limit locals 2
.end method
