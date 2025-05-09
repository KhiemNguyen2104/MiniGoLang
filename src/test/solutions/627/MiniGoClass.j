.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static getCurrentTime()I
Label0:
	bipush 12
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is c LCache; from Label0 to Label1
	aconst_null
	astore_1
	new Cache
	dup
	invokespecial Cache/<init>()V
	dup
	aconst_null
	putfield Cache.data [Ljava/lang/String;
	dup
	aconst_null
	putfield Cache.timestamp [I
	dup
	iconst_0
	putfield Cache.size I
	dup
	bipush 100
	putfield Cache.capacity I
	astore_1
	aload_1
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "1"
	aastore
	dup
	iconst_1
	ldc "2"
	aastore
	dup
	iconst_2
	ldc "3"
	aastore
	putfield Cache.data [Ljava/lang/String;
	aload_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	ineg
	iastore
	dup
	iconst_1
	iconst_1
	ineg
	iastore
	dup
	iconst_2
	iconst_1
	ineg
	iastore
	putfield Cache.timestamp [I
	aload_1
	iconst_1
	ldc "value1"
	invokevirtual Cache/put(ILjava/lang/String;)V
	aload_1
	iconst_2
	ldc "value2"
	invokevirtual Cache/put(ILjava/lang/String;)V
	aload_1
	iconst_1
	invokevirtual Cache/get(I)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iconst_2
	invokevirtual Cache/get(I)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
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
