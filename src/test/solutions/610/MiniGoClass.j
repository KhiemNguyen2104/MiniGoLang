.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a Z
.field static test1 Z
.field static test2 Z

.method public static One(Z)I
Label0:
.var 0 is flag Z from Label0 to Label1
	iload_0
	ifle Label3
Label4:
	iconst_1
	ireturn
Label5:
Label3:
	iconst_1
	ineg
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [[I from Label0 to Label1
	iconst_2
	iconst_3
	multianewarray [[I 2
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	aastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is flag Z from Label0 to Label1
	iconst_0
	ifeq Label3
	iconst_1
	ifgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifeq Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	istore 4
	iload_2
	iload_3
	iadd
	invokestatic io/putIntLn(I)V
.var 5 is boo Z from Label0 to Label1
	iconst_1
	invokestatic MiniGoClass/One(Z)I
	bipush 17
	ineg
	bipush 16
	iadd
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	istore 5
.var 6 is check I from Label0 to Label1
	iconst_0
	invokestatic MiniGoClass/One(Z)I
	istore 6
	iconst_0
	ifeq Label17
	iload 6
	iconst_1
	if_icmpne Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifeq Label14
	iload_2
	iload_3
	iadd
	iconst_0
	if_icmpeq Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifne Label11
	iload_2
	iload_3
	if_icmpne Label11
Label12:
Label19:
	iload_2
	iconst_0
	if_icmpne Label22
Label23:
.var 7 is newVar I from Label23 to Label24
	iconst_2
	istore 7
	iload_2
	iconst_1
	iadd
	invokestatic io/putIntLn(I)V
	iload 6
	iconst_1
	iadd
	invokestatic io/putIntLn(I)V
Label24:
	goto Label21
Label22:
Label25:
.var 7 is newVar I from Label25 to Label26
	iconst_3
	istore 7
	getstatic MiniGoClass/test1 Z
	invokestatic io/putBoolLn(Z)V
	getstatic MiniGoClass/test2 Z
	invokestatic io/putBoolLn(Z)V
Label26:
Label21:
Label20:
	goto Label12
Label11:
Label27:
.var 7 is newVar I from Label27 to Label28
	iconst_1
	istore 7
	iload 5
	invokestatic io/putBoolLn(Z)V
	getstatic MiniGoClass/a Z
	invokestatic io/putBoolLn(Z)V
Label28:
Label12:
Label1:
	return
.limit stack 16
.limit locals 8
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
	fconst_1
	fneg
	ldc 4.2
	fcmpl
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	putstatic MiniGoClass.a Z
	iconst_1
	iconst_2
	if_icmpeq Label9
	iconst_3
	iconst_4
	if_icmpeq Label9
	iconst_0
	goto Label11
Label9:
	iconst_1
Label11:
	ifeq Label7
	ldc 3.0
	ldc 5.6
	fcmpl
	ifeq Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	putstatic MiniGoClass.test1 Z
	iconst_1
	iconst_2
	if_icmpgt Label12
	ldc "abc"
	ldc "abc"
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifeq Label12
	iconst_0
	goto Label14
Label12:
	iconst_1
Label14:
	putstatic MiniGoClass.test2 Z
Label1:
	return
.limit stack 7
.limit locals 0
.end method
