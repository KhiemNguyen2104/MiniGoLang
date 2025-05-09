.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static c LCircle;
.field static final Pi F

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/Pi F
	invokestatic io/putFloatLn(F)V
	getstatic MiniGoClass/c LCircle;
	invokevirtual Circle/CirArea()F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 1
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
	new Circle
	dup
	invokespecial Circle/<init>()V
	dup
	ldc 5.12
	putfield Circle.radius F
	putstatic MiniGoClass.c LCircle;
	ldc 3.14
	putstatic MiniGoClass.Pi F
Label1:
	return
.limit stack 3
.limit locals 0
.end method
