.source Calculator.java
.class public Calculator
.super java.lang.Object
.field value I

.method public <init>()V
.var 0 is this LCalculator; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public Add(I)I
Label0:
.var 0 is c LCalculator; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	aload_0
	aload_0
	getfield Calculator.value I
	iload_1
	iadd
	putfield Calculator.value I
.var 2 is p LPerson; from Label0 to Label1
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Khiem"
	putfield Person.name Ljava/lang/String;
	dup
	bipush 21
	putfield Person.age I
	astore_2
	aload_2
	ldc "Developer"
	invokevirtual Person/work(Ljava/lang/String;)V
	aload_2
	getfield Person.age I
	invokestatic io/putIntLn(I)V
	aload_0
	getfield Calculator.value I
	ireturn
Label1:
.limit stack 3
.limit locals 3
.end method
