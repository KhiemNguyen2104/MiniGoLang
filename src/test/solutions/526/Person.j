.source Person.java
.class public Person
.super java.lang.Object
.field name Ljava/lang/String;
.field age I

.method public <init>()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public eat(Ljava/lang/String;)V
Label0:
.var 0 is p LPerson; from Label0 to Label1
.var 1 is food Ljava/lang/String; from Label0 to Label1
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	ldc "I am eating "
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	aload_1
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public work(Ljava/lang/String;)V
Label0:
.var 0 is p LPerson; from Label0 to Label1
.var 1 is job Ljava/lang/String; from Label0 to Label1
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	ldc "I am working "
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	aload_1
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method
