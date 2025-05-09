.source Email.java
.class public Email
.super java.lang.Object
.field name Ljava/lang/String;

.method public <init>()V
.var 0 is this LEmail; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public toString()Ljava/lang/String;
Label0:
.var 0 is e LEmail; from Label0 to Label1
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	aload_0
	getfield Email.name Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	ldc "@Xmail.com"
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	areturn
Label1:
.limit stack 4
.limit locals 1
.end method
