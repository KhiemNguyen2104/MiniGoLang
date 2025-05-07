.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final x I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label4 to Label5
	iconst_0
	istore_1
Label4:
	iload_1
	getstatic MiniGoClass/x I
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	iload_1
	bipush 52
	if_icmpne Label9
Label10:
	goto Label2
Label11:
Label9:
	iload_1
	invokestatic io/putIntLn(I)V
Label2:
	iload_1
	iconst_2
	iadd
	istore_1
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 2
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
	bipush 15
	putstatic MiniGoClass.x I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
