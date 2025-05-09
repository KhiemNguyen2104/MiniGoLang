.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static c I

.method public static println(I)V
Label0:
.var 0 is a I from Label0 to Label1
	iload_0
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static nestedConditions(III)V
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
	iload_0
	iload_1
	if_icmple Label3
Label4:
	iload_0
	iload_2
	if_icmple Label7
Label8:
	iload_0
	invokestatic MiniGoClass/println(I)V
Label9:
	goto Label6
Label7:
Label10:
	iload_1
	iload_2
	if_icmple Label13
Label14:
	iload_1
	invokestatic MiniGoClass/println(I)V
Label15:
	goto Label12
Label13:
Label16:
	iload_2
	invokestatic MiniGoClass/println(I)V
Label17:
Label12:
Label11:
Label6:
Label5:
	goto Label2
Label3:
Label18:
	iload_1
	iload_2
	if_icmple Label21
Label22:
	iload_1
	invokestatic MiniGoClass/println(I)V
Label23:
	goto Label20
Label21:
Label24:
	iload_2
	invokestatic MiniGoClass/println(I)V
Label25:
Label20:
Label19:
Label2:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static print()V
Label0:
	getstatic MiniGoClass/c I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	bipush 23
	istore_1
.var 2 is b I from Label0 to Label1
	bipush 21
	istore_2
.var 3 is c I from Label0 to Label1
	bipush 33
	istore_3
	invokestatic MiniGoClass/print()V
	iload_1
	iload_2
	iload_3
	invokestatic MiniGoClass/nestedConditions(III)V
Label1:
	return
.limit stack 3
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
	iconst_1
	putstatic MiniGoClass.c I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
