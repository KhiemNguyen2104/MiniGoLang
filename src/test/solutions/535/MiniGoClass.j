.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static d I
.field static a I

.method public static testIfStatement(I)V
Label0:
.var 0 is x I from Label0 to Label1
	iload_0
	bipush 10
	if_icmple Label3
Label4:
	ldc "x is greater than 10"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label5:
	goto Label2
Label3:
Label6:
	ldc "x is smaller than or equal to 10"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label7:
Label2:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static Three()I
Label0:
	iconst_3
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	bipush 7
	iastore
	dup
	iconst_2
	bipush 11
	iastore
	astore_1
.var 2 is i I from Label4 to Label5
	iconst_0
	istore_2
Label4:
	iload_2
	invokestatic MiniGoClass/Three()I
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	aload_1
	iload_2
	iaload
	invokestatic MiniGoClass/testIfStatement(I)V
Label2:
	iload_2
	iconst_2
	iadd
	istore_2
	goto Label4
Label5:
Label3:
	getstatic MiniGoClass/a I
	invokestatic io/putInt(I)V
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
	bipush 10
	putstatic MiniGoClass.d I
	iconst_1
	invokestatic MiniGoClass/Three()I
	iadd
	putstatic MiniGoClass.a I
Label1:
	return
.limit stack 2
.limit locals 0
.end method
