.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static arr [[LPerson;

.method public static BMI(FF)F
Label0:
.var 0 is height F from Label0 to Label1
.var 1 is weight F from Label0 to Label1
	fload_1
	fload_0
	fload_0
	fmul
	fdiv
	freturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label4 to Label5
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_1
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
.var 2 is j I from Label10 to Label11
	iconst_0
	istore_2
Label10:
	iload_2
	iconst_1
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label9
.var 3 is bmi F from Label10 to Label11
	getstatic MiniGoClass/arr [[LPerson;
	iload_1
	aaload
	iload_2
	aaload
	getfield Person.height F
	getstatic MiniGoClass/arr [[LPerson;
	iload_1
	aaload
	iload_2
	aaload
	getfield Person.weight F
	invokestatic MiniGoClass/BMI(FF)F
	fstore_3
	fload_3
	ldc 18.5
	fcmpl
	ifge Label15
Label16:
	ldc "Underweight"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label17:
	goto Label14
Label15:
Label18:
	ldc 18.5
	fload_3
	fcmpl
	ifgt Label21
	fload_3
	ldc 25.0
	fcmpl
	ifge Label21
Label22:
	ldc "Normal"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label23:
	goto Label20
Label21:
Label24:
	ldc 25.0
	fload_3
	fcmpl
	ifgt Label27
	fload_3
	ldc 29.0
	fcmpl
	ifge Label27
Label28:
	ldc "Pre-obese"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label29:
	goto Label26
Label27:
Label30:
	ldc "Obese"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label31:
Label26:
Label25:
Label20:
Label19:
Label14:
Label8:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label11:
Label9:
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
.limit stack 8
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
	iconst_2
	iconst_2
	multianewarray [[LPerson; 2
	dup
	iconst_0
	iconst_2
	anewarray Person
	dup
	iconst_0
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc 1.7
	putfield Person.height F
	dup
	ldc 70.0
	putfield Person.weight F
	aastore
	dup
	iconst_1
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc 1.48
	putfield Person.height F
	dup
	ldc 42.0
	putfield Person.weight F
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray Person
	dup
	iconst_0
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc 1.61
	putfield Person.height F
	dup
	ldc 67.0
	putfield Person.weight F
	aastore
	dup
	iconst_1
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc 1.765
	putfield Person.height F
	dup
	ldc 90.0
	putfield Person.weight F
	aastore
	aastore
	putstatic MiniGoClass.arr [[LPerson;
Label1:
	return
.limit stack 13
.limit locals 0
.end method
