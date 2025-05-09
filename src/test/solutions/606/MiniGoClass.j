.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static population I
.field static GDP F
.field static x I
.field static str1 Ljava/lang/String;
.field static str2 Ljava/lang/String;
.field static final str Ljava/lang/String;

.method public static avGDP(FI)F
Label0:
.var 0 is GDP F from Label0 to Label1
.var 1 is poppy I from Label0 to Label1
	fload_0
	iload_1
	i2f
	fdiv
	freturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is str3 Ljava/lang/String; from Label0 to Label1
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	getstatic MiniGoClass/str Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	ldc "1"
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	astore_1
.var 2 is i F from Label0 to Label1
	fconst_0
	fstore_2
.var 3 is gdp F from Label0 to Label1
	getstatic MiniGoClass/GDP F
	iconst_2
	invokestatic MiniGoClass/avGDP(FI)F
	fstore_3
	bipush 15
	putstatic MiniGoClass.x I
.var 4 is boo Z from Label0 to Label1
	fload_2
	fconst_2
	fcmpl
	iflt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore 4
	iload 4
	invokestatic io/putBoolLn(Z)V
	fconst_1
	invokestatic io/putFloatLn(F)V
	fconst_2
	invokestatic io/putFloatLn(F)V
	getstatic MiniGoClass/GDP F
	invokestatic io/putFloatLn(F)V
	getstatic MiniGoClass/str Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	invokestatic io/putLn()V
	aload_1
	invokestatic io/putStringLn(Ljava/lang/String;)V
	fload_3
	invokestatic io/putFloatLn(F)V
	getstatic MiniGoClass/x I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
.limit locals 5
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
	ldc 52161
	putstatic MiniGoClass.population I
	ldc 1.425
	getstatic MiniGoClass/population I
	i2f
	fadd
	iconst_2
	i2f
	fmul
	iconst_1
	i2f
	fdiv
	putstatic MiniGoClass.GDP F
	iconst_0
	putstatic MiniGoClass.x I
	ldc "Hello, "
	putstatic MiniGoClass.str1 Ljava/lang/String;
	ldc "World!"
	putstatic MiniGoClass.str2 Ljava/lang/String;
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	getstatic MiniGoClass/str1 Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	getstatic MiniGoClass/str2 Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	putstatic MiniGoClass.str Ljava/lang/String;
Label1:
	return
.limit stack 4
.limit locals 0
.end method
