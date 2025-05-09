.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a Z
.field static b Z
.field static c Z

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/a Z
	ifne Label8
	getstatic MiniGoClass/b Z
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifeq Label12
	getstatic MiniGoClass/a Z
	ifeq Label17
	iconst_0
	ifgt Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifeq Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifeq Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifne Label8
	iconst_0
	goto Label10
Label8:
	iconst_1
Label10:
	ifeq Label6
	getstatic MiniGoClass/b Z
	ifne Label24
	getstatic MiniGoClass/a Z
	ifne Label24
	iconst_0
	goto Label26
Label24:
	iconst_1
Label26:
	ifne Label21
	getstatic MiniGoClass/b Z
	ifeq Label28
	getstatic MiniGoClass/a Z
	ifgt Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifeq Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifgt Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifne Label21
	iconst_0
	goto Label23
Label21:
	iconst_1
Label23:
	ifeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifne Label2
	getstatic MiniGoClass/a Z
	ifne Label37
	getstatic MiniGoClass/b Z
	ifne Label37
	iconst_0
	goto Label39
Label37:
	iconst_1
Label39:
	ifgt Label40
	iconst_1
	goto Label41
Label40:
	iconst_0
Label41:
	ifeq Label35
	getstatic MiniGoClass/a Z
	ifgt Label48
	iconst_1
	goto Label49
Label48:
	iconst_0
Label49:
	ifne Label45
	getstatic MiniGoClass/b Z
	ifne Label45
	iconst_0
	goto Label47
Label45:
	iconst_1
Label47:
	ifgt Label50
	iconst_1
	goto Label51
Label50:
	iconst_0
Label51:
	ifeq Label43
	getstatic MiniGoClass/a Z
	ifeq Label53
	getstatic MiniGoClass/b Z
	ifgt Label55
	iconst_1
	goto Label56
Label55:
	iconst_0
Label56:
	ifeq Label53
	iconst_1
	goto Label54
Label53:
	iconst_0
Label54:
	ifeq Label43
	iconst_1
	goto Label44
Label43:
	iconst_0
Label44:
	ifeq Label35
	iconst_1
	goto Label36
Label35:
	iconst_0
Label36:
	ifne Label2
	iconst_0
	goto Label4
Label2:
	iconst_1
Label4:
	ifgt Label57
	iconst_1
	goto Label58
Label57:
	iconst_0
Label58:
	putstatic MiniGoClass.c Z
	getstatic MiniGoClass/c Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 6
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
	iconst_0
	putstatic MiniGoClass.a Z
	iconst_1
	putstatic MiniGoClass.b Z
	iconst_0
	putstatic MiniGoClass.c Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
