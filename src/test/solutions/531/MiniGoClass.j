.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I
.field static d F
.field static b I
.field static c Ljava/lang/String;

.method public static toString(I)Ljava/lang/String;
Label0:
.var 0 is n I from Label0 to Label1
	iload_0
	iconst_0
	if_icmpne Label3
Label4:
	ldc "0"
	areturn
Label5:
	goto Label2
Label3:
Label6:
	iload_0
	iconst_1
	if_icmpne Label9
Label10:
	ldc "1"
	areturn
Label11:
	goto Label8
Label9:
Label12:
	iload_0
	iconst_2
	if_icmpne Label15
Label16:
	ldc "2"
	areturn
Label17:
	goto Label14
Label15:
Label18:
	iload_0
	iconst_3
	if_icmpne Label21
Label22:
	ldc "3"
	areturn
Label23:
	goto Label20
Label21:
Label24:
	iload_0
	iconst_4
	if_icmpne Label27
Label28:
	ldc "4"
	areturn
Label29:
	goto Label26
Label27:
Label30:
	iload_0
	iconst_5
	if_icmpne Label33
Label34:
	ldc "5"
	areturn
Label35:
	goto Label32
Label33:
Label36:
	iload_0
	bipush 6
	if_icmpne Label39
Label40:
	ldc "6"
	areturn
Label41:
	goto Label38
Label39:
Label42:
	iload_0
	bipush 7
	if_icmpne Label45
Label46:
	ldc "7"
	areturn
Label47:
	goto Label44
Label45:
Label48:
	iload_0
	bipush 8
	if_icmpne Label51
Label52:
	ldc "8"
	areturn
Label53:
	goto Label50
Label51:
Label54:
	iload_0
	bipush 9
	if_icmpne Label57
Label58:
	ldc "9"
	areturn
Label59:
Label57:
Label55:
Label50:
Label49:
Label44:
Label43:
Label38:
Label37:
Label32:
Label31:
Label26:
Label25:
Label20:
Label19:
Label14:
Label13:
Label8:
Label7:
Label2:
	ldc ""
	areturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static combine(IILjava/lang/String;)Ljava/lang/String;
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c Ljava/lang/String; from Label0 to Label1
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	iload_0
	invokestatic MiniGoClass/toString(I)Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	iload_1
	invokestatic MiniGoClass/toString(I)Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	aload_2
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	areturn
Label1:
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/a I
	getstatic MiniGoClass/b I
	getstatic MiniGoClass/c Ljava/lang/String;
	invokestatic MiniGoClass/combine(IILjava/lang/String;)Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	getstatic MiniGoClass/d F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 3
.limit locals 1
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
	putstatic MiniGoClass.a I
	iconst_3
	i2f
	putstatic MiniGoClass.d F
	iconst_3
	putstatic MiniGoClass.b I
	ldc "hello"
	putstatic MiniGoClass.c Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method
