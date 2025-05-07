'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from CodeGenError import *
from AST import Type as ASTType
from AST import *
import copy


class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType(ASTType):
    def __init__(self, name):
        #value: Id
        self.name = name

    def accept(self, v, param):
        return super().accept(v, param)

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.VarConstIdx = []
        self.FuncIdx = []
        self.VarConstGlobIdx = 0
        self.FuncGlobIdx = 0
        self.GlobVarTable = []
        self.structEmitters = []
        self.interfaceEmitters = []

    def init(self):
        mem = [
            (Symbol("getInt", MType([], IntType()), CName("io", True)), None),
            (Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)), None),
            (Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)), None),
            (Symbol("getFloat", MType([], FloatType()), CName("io", True)), None),
            (Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)), None),
            (Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)), None),
            (Symbol("getBool", MType([], BoolType()), CName("io", True)), None),
            (Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)), None),
            (Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)), None),
            (Symbol("getString", MType([], StringType()), CName("io", True)), None),
            (Symbol("putString", MType([StringType()], VoidType()), CName("io", True)), None),
            (Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)), None),
            (Symbol("putLn", MType([], VoidType()), CName("io", True)), None)
        ]

        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
    def lookup(self, name: str, env):
        return next(filter(lambda x: x[0].name == name, env), None)

    def TypeOfLit(self, l, c):
        if type(l) is IntLiteral:
            return IntType()
        elif type(l) is FloatLiteral:
            return FloatType()
        elif type(l) is StringLiteral:
            return StringType()
        elif type(l) is BooleanLiteral:
            return BoolType()
        elif type(l) is ArrayLiteral:
            return ArrayType(copy.deepcopy(l.dimens), copy.deepcopy(l.eleType))
        elif type(l) is StructLiteral:
            check = self.lookup(l.name, c['env'][-1])
            if check is None:
                raise Undeclared(Identifier(), l.name)
            return check[0].mtype
        elif type(l) is list:
            if type(l[0]) is ArrayType:
                dimens = [IntLiteral(len(l))] + l[0].dimens
                return ArrayType(dimens, l[0].eleType)
            else:
                return ArrayType([IntLiteral(len(l))], self.TypeOfLit(l[0], c))

        raise TypeError("Fetching type: Invalid literal " + str(l))
    
    def DefaultVal(self, l, c):
        if type(l) is IntType:
            return IntLiteral(0)
        elif type(l) is FloatType:
            return FloatLiteral(0.0)
        elif type(l) is StringType:
            return StringLiteral("")
        elif type(l) is BoolType:
            return BooleanLiteral(False)
        elif type(l) is ArrayType:
            # return ArrayLiteral(
            #     copy.deepcopy(l.dimens),
            #     copy.deepcopy(l.eleType),
            #     reduce(lambda acc, ele: [acc] * ele, [i.value for i in l.dimens][::-1], self.DefaultVal(l.eleType, c))
            # )
            return NilLiteral()
        elif type(l) is StructType:
            # check = self.lookup(l.name, c['env'][-1])
            # if check is None:
            #     raise Undeclared(Identifier(), l.name)
            # if type(check[1]) is not Type:
            #     raise TypeError(f"Invalid type definition: {str(check[0])}")
            # return StructLiteral(
            #     check[0].mtype.name,
            #     reduce(lambda acc, ele: [(ele[0], self.DefaultVal(ele[1], c))] + acc, check[0].mtype.elements, [])
            # )
            return NilLiteral()
        elif type(l) is InterfaceType:
            # for i in range(len(c['env'][-1])):
            #     if type(c['env'][-1][i][1]) is Type and type(c['env'][-1][i][0].mtype) is StructType:
            #         if self.MatchType(l, c['env'][-1][i][0].mtype, c):
            #             return self.DefaultVal(c['env'][-1][i][0].mtype, c)
            return NilLiteral()
                    
            raise TypeError("Default value: No suitable StructType for " + str(l))
        
        raise TypeError("Default value: Invalid type " + str(l))
        
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def emitClassInit(self, o):
        frame = Frame("<clinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), False, frame))
        frame.enterScope(True)  
        # self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        # self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        o['isLeft'] = False
        o['frame'] = frame

        for globVar in self.GlobVarTable:
            # print("Glob variable: ", globVar)
            val = None
            typ = None
            code = None
            if type(globVar[1]) is NilLiteral:
                typ = globVar[2]
                code = self.emit.emitPUSHNULL(o['frame'])
            else:
                val, typ, code = self.visit(globVar[1], o)
                if type(typ) is StructType or type(typ) is InterfaceType:
                    typ = ClassType(typ.name)
            if type(typ) is IntType and type(globVar[2]) is FloatType:
                self.emit.printout(code)
                self.emit.printout(self.emit.emitI2F(o['frame']))
                typ = globVar[2]
            elif type(typ) is ArrayType and type(globVar[2]) is ArrayType and type(typ.eleType) is IntType and type(globVar[2].eleType) is FloatType:
                convertCode = self.convertArray(globVar[2], code, o)
                self.emit.printout(convertCode)
                typ = globVar[2]
            else:
                self.emit.printout(code)
            self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}.{globVar[0]}", typ, o['frame']))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def convertArray(self, typ: ArrayType, rootCode, o):
        res = ""
        
        for i in range(len(typ.dimens)):
            typ.dimens[i] = self.visit(typ.dimens[i], o)[0]
        
        if len(typ.dimens) == 1:
            o['isLeft'] = False
            # print("ENV: ", env)
            # print("DIMENS: ", ast.dimens)
            val, t, code = self.visit(typ.dimens[0], o)
            # ast.dimens[0] = val
            res = code
            res += self.emit.emitNEWARRAY(FloatType(), o['frame'])

            l = typ.dimens[0].value

            for i in range(l):
                res += self.emit.emitDUP(o['frame'])
                res += self.visit(IntLiteral(i), o)[2]
                res += rootCode
                o['frame'].push()
                res += self.visit(IntLiteral(i), o)[2]
                res += self.emit.emitALOAD(IntType(), o['frame'])
                res += self.emit.emitI2F(o['frame'])
                res += self.emit.emitASTORE(FloatType(), o['frame'])
        else:
            o['isLeft'] = False
            finalDimens = []

            for i in range(len(typ.dimens)):
                finalDimens.append(typ.dimens[i].value)
                res += self.visit(typ.dimens[i], o)[2]

            res += self.emit.emitMULTIANEWARRAY(FloatType(), typ.dimens, o['frame'])

            l = len(finalDimens)
            totalLoops = reduce(lambda acc, ele: acc * ele, finalDimens, 1)

            for i in range(0, totalLoops, finalDimens[-1]):
                res += self.emit.emitDUP(o['frame'])
                temp = ""
                # temp = self.emit.emitDUP(o['frame'])

                for j in range(l - 1):
                    totalEle = reduce(lambda acc, ele: acc * ele, finalDimens[(j + 1):], 1)
                    # print("TE: ", totalEle)
                    remain = i % totalEle
                    quotient = int((i - remain) / totalEle)
                    # print("Q: ", quotient)
                    # indices[j] = quotient
                    i = remain
                    
                    res += self.emit.emitPUSHICONST(str(quotient), o['frame'])
                    temp += self.emit.emitPUSHICONST(str(quotient), o['frame'])
                    if (j != l - 2):
                        res += self.emit.emitALOAD(ArrayType([], IntType()), o['frame'])
                        temp += self.emit.emitALOAD(ArrayType([], IntType()), o['frame'])
                    else:
                        temp += self.emit.emitALOAD(ArrayType([], IntType()), o['frame'])

                res += self.emit.emitPUSHICONST(str(finalDimens[-1]), o['frame'])
                res += self.emit.emitNEWARRAY(FloatType(), o['frame'])

                for j in range(finalDimens[-1]):
                    res += self.emit.emitDUP(o['frame'])
                    res += self.visit(IntLiteral(j), o)[2]
                    o['frame'].push()
                    res += rootCode
                    res += temp
                    res += self.visit(IntLiteral(j), o)[2]
                    res += self.emit.emitALOAD(IntType(), o['frame'])
                    res += self.emit.emitI2F(o['frame'])
                    res += self.emit.emitASTORE(FloatType(), o['frame'])
                
                res += self.emit.emitASTORE(ArrayType([], IntType()), o['frame'])

        return res

    def evaluate(self, expr, o):
        # print("EXPR: ", str(expr))

        if type(expr) is Id:
            return self.visit(expr, o)[0]
        elif type(expr) is IntLiteral or type(expr) is FloatLiteral or type(expr) is StringLiteral or type(expr) is BooleanLiteral or type(expr) is NilLiteral:
            return expr
        elif type(expr) is StructLiteral:
            for i in range(len(expr.elements)):
                expr.elements[i] = (expr.elements[i][0], self.evaluate(expr.elements[i][1], o))

            return expr
        elif type(expr) is ArrayLiteral:
            dimens = []
            for i in range(len(expr.dimens)):
                expr.dimens[i] = self.evaluate(expr.dimens[i], o)
                dimens.append(expr.dimens[i].value)
            
            totalEle = reduce(lambda acc, ele: acc*ele, dimens, 1)

            for i in range(0, totalEle, dimens[-1]):
                value = expr.value
                for j in range(len(dimens) - 1):
                    resEle = reduce(lambda acc, ele: acc * ele, dimens[j + 1:], 1)
                    remainder = i % resEle
                    quotient = int((i - remainder)/resEle)
                    value = value[quotient]
                
                for j in range(dimens[-1]):
                    value[j] = self.evaluate(value[j], o)

            return expr
            
        elif type(expr) is BinaryOp:
            lVal = self.evaluate(expr.left, o)
            rVal = self.evaluate(expr.right, o)
            if expr.op == '+':
                if type(lVal) is not type(rVal):
                    if type(lVal) is IntLiteral:
                        return FloatLiteral(float(lVal.value) + rVal.value)
                    else:
                        return FloatLiteral(lVal.value + float(rVal.value))
                else:
                    if type(lVal) is StringLiteral:
                        return StringLiteral(lVal.value + rVal.value)
                    elif type(lVal) is IntLiteral:
                        return IntLiteral(lVal.value + rVal.value)
                    else:
                        return FloatLiteral(lVal.value + rVal.value)
            elif expr.op in ['-', '*', '/']:
                # if expr.op == '/' and rVal.value == 0:
                #     if type(rVal) is IntLiteral:
                #         rVal = IntLiteral(1)
                #     else:
                #         rVal = FloatLiteral(1.0)
                
                if expr.op == '*':
                    if type(lVal) is not type(rVal):
                        if type(lVal) is IntLiteral:
                            return FloatLiteral(float(lVal.value) * rVal.value)
                        else:
                            return FloatLiteral(lVal.value * float(rVal.value))
                    else:
                        if type(lVal) is IntLiteral:
                            return IntLiteral(lVal.value * rVal.value)
                        else:
                            return FloatLiteral(lVal.value * rVal.value)
                elif expr.op == '/':
                    if type(lVal) is not type(rVal):
                        if type(lVal) is IntLiteral:
                            return FloatLiteral(float(lVal.value) / rVal.value)
                        else:
                            return FloatLiteral(lVal.value / float(rVal.value))
                    else:
                        if type(lVal) is IntLiteral:
                            return IntLiteral(int(lVal.value / rVal.value))
                        else:
                            return FloatLiteral(lVal.value / rVal.value)
                elif expr.op == '-':
                    if type(lVal) is not type(rVal):
                        if type(lVal) is IntLiteral:
                            return FloatLiteral(float(lVal.value) - rVal.value)
                        else:
                            return FloatLiteral(lVal.value - float(rVal.value))
                    else:
                        if type(lVal) is IntLiteral:
                            return IntLiteral(lVal.value - rVal.value)
                        else:
                            return FloatLiteral(lVal.value - rVal.value)
            elif expr.op in ['==', '!=', '<', '<=', '>', '>=']:
                if expr.op == '==':
                    return BooleanLiteral(lVal.value == rVal.value)
                elif expr.op == '!=':
                    return BooleanLiteral(lVal.value != rVal.value)
                elif expr.op == '<':
                    return BooleanLiteral(lVal.value < rVal.value)
                elif expr.op == '>':
                    return BooleanLiteral(lVal.value > rVal.value)
                elif expr.op == '<=':
                    return BooleanLiteral(lVal.value <= rVal.value)
                elif expr.op == '>=':
                    return BooleanLiteral(lVal.value >= rVal.value)
            elif expr.op in ['&&', '||']:
                if expr.op == '&&':
                    return BooleanLiteral(lVal.value and rVal.value)
                elif expr.op == '||':
                    return BooleanLiteral(lVal.value or rVal.value)
        elif type(expr) is UnaryOp:
            val = self.evaluate(expr.body, o)
            if expr.op == '!':
                return BooleanLiteral(not val.value)
            elif expr.op == '-':
                if type(val) is IntLiteral:
                    return IntLiteral(int(val.value * -1))
                else:
                    return FloatLiteral(int(val.value * -1))
        elif type(expr) is ArrayCell:
            arr = self.evaluate(expr.arr, o)

            value = arr.value
            for i in expr.idx:
                t = self.evaluate(i, o)
                value = value[t.value]

            return value
        elif type(expr) is FieldAccess:
            rei = self.evaluate(expr.receiver, o)
            ele = next(filter(lambda x: x[0] == expr.field, rei.elements), None)[1]

            ele = self.evaluate(ele, o)

            return ele

    def convertType(self, typ, lit):
        if type(typ) is FloatType:
            pass
        elif type(typ) is ArrayType and type(typ.eleType) is FloatType:
            pass
        else:
            return typ, lit

    def fetchEnv(self, ast, c):
        # print(f"Check {str(ast)}\nData: " + "[" + ','.join("[" + ','.join(f"({str(i[0])}, {str(i[1])})" for i in j) + "]" for j in c['env']) + "]" + ", isLeft: " + (str(c['isLeft']) if 'isLeft' in c else ""), end="\n\n")
        # print("VarDecl and ConstDecl indices: ", self.VarConstDeclIdx)
        # print("Global env len: ", len(c['env'][0]))
        # print("The next VarDecl or ConstDecl: ", self.globIdx)
        # print("The next FuncDecl or MethodDecl: ", self.funcIdx, "\n")
        pass
    
    def visitProgram(self, ast, c):
        for i in range(len(ast.decl)):
            if type(ast.decl[i]) is VarDecl or type(ast.decl[i]) is ConstDecl:
                self.VarConstIdx.append(i)
            elif type(ast.decl[i]) is FuncDecl or type(ast.decl[i]) is MethodDecl:
                self.FuncIdx.append(i)

        env ={}
        env['env'] = [c]
        env['GlobScan'] = True
        env = reduce(lambda a,x: self.visit(x, a), [decl for decl in ast.decl if (type(decl) is StructType) or (type(decl) is InterfaceType)], env)
        env = reduce(lambda a,x: self.visit(x, a), [decl for decl in ast.decl if (type(decl) is FuncDecl) or (type(decl) is MethodDecl)], env)
        # env = reduce(lambda a,x: self.visit(x, a), [decl for decl in ast.decl if (type(decl) is VarDecl) or (type(decl) is ConstDecl)], env)
        env['GlobScan'] = False
        # env['isLeft'] = False
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a,x: self.visit(x, a), [decl for decl in ast.decl if (type(decl) is VarDecl) or (type(decl) is ConstDecl)], env)
        env = reduce(lambda a,x: self.visit(x, a), [decl for decl in ast.decl if (type(decl) is StructType) or (type(decl) is InterfaceType)], env)
        env = reduce(lambda a,x: self.visit(x, a), [decl for decl in ast.decl if (type(decl) is FuncDecl) or (type(decl) is MethodDecl)], env)
        self.emitObjectInit()
        self.emitClassInit(env)
        self.emit.printout(self.emit.emitEPILOG())

        for emitter in self.structEmitters:
            emitter.printout(emitter.emitEPILOG())

        return env

    def visitVarDecl(self, ast, o):
        if o['GlobScan']:
            return o
        
        self.fetchEnv(ast, o)

        exprType = None
        exprCode = None
        exprValue = None

        if 'frame' not in o:
            if ast.varInit:
                env = o.copy()
                env['isLeft'] = False
                exprValue, exprType, exprCode = self.visit(ast.varInit, env)
            if not exprValue:
                # raise IllegalRuntimeException("No initial value for the static field")
                exprValue = self.DefaultVal(ast.varType, o)

            self.GlobVarTable.append((ast.varName, exprValue, ast.varType))

            typ = ast.varType if exprType is None or type(exprType) is VoidType else exprType 
            val = exprValue if exprValue else self.DefaultVal(typ, o)

            if type(ast.varType) is FloatType and type(exprType) is IntType:
                exprCode += self.emit.printout(self.emit.emitI2F(o['frame']))
                typ = FloatType()
            elif type(typ) is InterfaceType and type(exprType) is StructType:
                typ = exprType
            elif type(ast.varType) is ArrayType and type(exprType) is ArrayType and type(ast.varType.eleType) is FloatType and type(exprType.eleType) is IntType:
                # exprCode = self.convertArray(ast.varType, exprCode, o['frame'])
                typ = ast.varType

            if type(typ) is StructType or type(typ) is InterfaceType:
                typ = ClassType(typ.name)

            o['env'][0].insert(len(o['env'][0]) - 13 - self.VarConstIdx[self.VarConstGlobIdx], (Symbol(ast.varName, typ, CName(self.className)), val))
            self.VarConstGlobIdx += 1
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, typ, True, False))
        else:
            frame = o['frame']
            index = frame.getNewIndex()

            if ast.varInit:
                o['isLeft'] = False
                exprValue, exprType, exprCode = self.visit(ast.varInit, o)
            
            typ = ast.varType if exprType is None or type(exprType) is VoidType else exprType 
            val = exprValue if exprValue else self.DefaultVal(typ, o)

            if type(ast.varType) is FloatType and type(exprType) is IntType:
                exprCode += self.emit.printout(self.emit.emitI2F(o['frame']))
                typ = FloatType()
            elif type(ast.varType) is ArrayType and type(exprType) is ArrayType and type(ast.varType.eleType) is FloatType and type(exprType.eleType) is IntType:
                exprCode = self.convertArray(ast.varType, exprCode, o)
                typ = ast.varType
            elif type(typ) is InterfaceType and type(exprType) is StructType:
                typ = exprType

            if type(typ) is StructType or type(typ) is InterfaceType:
                typ = ClassType(typ.name)
            
            o['env'][0] = [(Symbol(ast.varName, typ, Index(index)), val)] + o['env'][0]
            self.emit.printout(self.emit.emitVAR(index, ast.varName, typ, frame.getStartLabel(), frame.getEndLabel(), frame))

            if exprCode:
                self.emit.printout(exprCode)

                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, typ, index, frame))
            else:
                self.visit(Assign(Id(ast.varName), self.DefaultVal(ast.varType, o)), o)

        return o


    def visitConstDecl(self, ast, o):
        if o['GlobScan']:
            return o
        
        self.fetchEnv(ast, o)

        exprType = None
        exprCode = None
        exprValue = None

        if ast.iniExpr:
            env = o.copy()
            env['isLeft'] = False
            exprValue, exprType, exprCode = self.visit(ast.iniExpr, env)
        
        if 'frame' not in o:
            if not exprValue:
                raise IllegalRuntimeException("No initial value for the static field")
            
            self.GlobVarTable.append((ast.conName, exprValue, exprType))

            o['env'][0].insert(len(o['env'][0]) - 13 - self.VarConstIdx[self.VarConstGlobIdx], (Symbol(ast.conName, exprType, CName(self.className)), self.evaluate(exprValue, o)))
            self.VarConstGlobIdx += 1
            self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, exprType, True, True))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0] = [(Symbol(ast.conName, exprType, Index(index)), self.evaluate(exprValue, o))] + o['env'][0]
            self.emit.printout(self.emit.emitVAR(index, ast.conName, exprType, frame.getStartLabel(), frame.getEndLabel(), frame))
            
            self.emit.printout(exprCode)
            self.emit.printout(self.emit.emitWRITEVAR(ast.conName, exprType, index, frame))
        
        return o
    
    def visitParamDecl(self, ast, o):
        index = o['frame'].getNewIndex()
        startLabel = o['frame'].getStartLabel()
        endLabel = o['frame'].getEndLabel()
        o['env'][0] = [(Symbol(ast.parName, ast.parType, Index(index)), self.DefaultVal(ast.parType, o))] + o['env'][0]
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, startLabel, endLabel, o['frame']))
        # self.visit(Assign(Id(ast.parName), self.DefaultVal(ast.parType, o)), o)

        return o
   
    def visitFuncDecl(self, ast, o):
        self.fetchEnv(ast, o)
        
        if o['GlobScan']:
            mtype = None
            isMain = ast.name == 'main'
            
            if isMain:
                mtype = MType([ArrayType([None], StringType())], ast.retType)
            else:
                mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
            
            o['env'][0] = [(Symbol(ast.name, mtype, CName(self.className)), None)] + o['env'][0]

            return o
        else:
            frame = Frame(ast.name, ast.retType)
            isMain = ast.name == 'main'
            mtype = None

            if isMain:
                mtype = MType([ArrayType([None], StringType())], ast.retType)
            else:
                mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
            
            funcEnv = copy.deepcopy(o)
            self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True, frame))

            frame.enterScope(True)

            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

            funcEnv['frame'] = frame
            funcEnv['env'] = [[]] + funcEnv['env']
            if isMain:
                self.emit.printout(self.emit.emitVAR(funcEnv['frame'].getNewIndex(), "args", ArrayType([None],StringType()), funcEnv['frame'].getStartLabel(), funcEnv['frame'].getEndLabel(), funcEnv['frame']))
            else:
                funcEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, funcEnv)
            funcEnv['env'] = [[]] + funcEnv['env']
            funcEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.body.member, funcEnv)

            self.emit.printout(self.emit.emitLABEL(funcEnv['frame'].getEndLabel(), funcEnv['frame']))
            
            if type(ast.retType) is VoidType:
                self.emit.printout(self.emit.emitRETURN(ast.retType, funcEnv['frame'])) 
            self.emit.printout(self.emit.emitENDMETHOD(funcEnv['frame']))

            frame.exitScope()

            self.FuncGlobIdx += 1

            return o

    def visitMethodDecl(self, ast, o):
        return None

    def visitPrototype(self, ast, o):
        return None
    
    def visitIntType(self, ast, o):
        return ast
    
    def visitFloatType(self, ast, o):
        return ast
    
    def visitBoolType(self, ast, o):
        return ast
    
    def visitStringType(self, ast, o):
        return ast
    
    def visitVoidType(self, ast, o):
        return ast
    
    def visitArrayType(self, ast, o):
        return ast
    
    def visitStructType(self, ast, o):
        if o['GlobScan']:
            o['env'][0] = [(Symbol(ast.name, ast, CName(self.className)), None)] + o['env'][0]

            return o
        else:
            newEmitter = Emitter(self.path + "/" + ast.name + ".j")
            self.structEmitters.append(newEmitter)

            newEmitter.printout(newEmitter.emitPROLOG(ast.name, "java.lang.Object"))
            frame = Frame("<init>", VoidType())

            for i in range(len(ast.elements)):
                newEmitter.printout(newEmitter.emitATTRIBUTE(ast.elements[i][0], ast.elements[i][1], False, False))

            newEmitter.printout(newEmitter.emitMETHOD("<init>", MType([], VoidType()), False, frame))
            frame.enterScope(True)  
            newEmitter.printout(newEmitter.emitVAR(frame.getNewIndex(), "this", ClassType(ast.name), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
            
            newEmitter.printout(newEmitter.emitLABEL(frame.getStartLabel(), frame))
            newEmitter.printout(newEmitter.emitREADVAR("this", ClassType(ast.name), 0, frame))  
            newEmitter.printout(newEmitter.emitINVOKESPECIAL(frame))

            newEmitter.printout(newEmitter.emitLABEL(frame.getEndLabel(), frame))
            newEmitter.printout(newEmitter.emitRETURN(VoidType(), frame))
            newEmitter.printout(newEmitter.emitENDMETHOD(frame))

            frame.exitScope()

            return o


    def visitInterfaceType(self, ast, o):
        return None
    
    def visitBlock(self, ast, o):
        pass
 
    def visitAssign(self, ast, o):
        if 'frame' in o:
            env = o.copy()
            env['isLeft'] = False

            rVal, rType, rCode = self.visit(ast.rhs, env)
            res = ""

            if type(ast.lhs) is Id:
                sym = next(filter(lambda x: x is not None, [self.lookup(ast.lhs.name, env) for env in o['env']]), None)

                if sym is None:
                    self.visit(VarDecl(ast.lhs.name, None, ast.rhs), env)
                    return o
                else:
                    env['isLeft'] = True
                    lVal, lType, lCode = self.visit(ast.lhs, env)
                    env['isLeft'] = False

                    if type(lType) is FloatType and type(rType) is IntType:
                        rCode += self.emit.emitI2F(env['frame'])

                    res += rCode + lCode
            elif type(ast.lhs) is ArrayCell:
                arrayCell = ast.lhs
                
                env['isLeft']= False
                arrVal, arrType, arrCode = self.visit(arrayCell.arr, env)
                rVal, rType, rCode = self.visit(ast.rhs, env)

                res += arrCode

                for i in range(len(arrayCell.idx)):
                    env['isLeft'] = False
                    val, typ, code = self.visit(arrayCell.idx[i], env)
                    res += code

                    if i != len(arrayCell.idx) - 1:
                        res += self.emit.emitALOAD(arrType, env['frame'])
                    else:
                        if type(rType) is FloatType and type(arrType.eleType) is IntType:
                            rCode += self.emit.emitI2F(env['frame'])

                        res += rCode + self.emit.emitASTORE(arrType.eleType, env['frame'])
            elif type(ast.lhs) is FieldAccess:
                reiVal, reiType, reiCode = self.visit(ast.lhs.receiver, env)

                res = ""
                typ = None

                if type(reiType) is StructType:
                    typ = next(filter(lambda x: x[0] == ast.lhs.field, reiType.elements), None)[1]
                elif type(reiType) is ClassType:
                    sym = next(filter(lambda x: x[0].name == reiType.name, env['env'][-1]), None)
                    typ = next(filter(lambda x: x[0] == ast.lhs.field, sym[0].mtype.elements), None)[1]

                if type(rType) is FloatType and type(typ) is IntType:
                    rCode += self.emit.emitI2F(env['frame'])

                res += reiCode + rCode
                res += self.emit.emitPUTFIELD(f"{reiType.name}.{ast.lhs.field}", typ, env['frame'])

            self.emit.printout(res)

            return o
        else:
            raise IllegalRuntimeException("No frame for the assignment statement.")
   
    def visitIf(self, ast, o):
        env = o.copy()
        env['isLeft'] = False

        # bodyEnv = env.copy()
        # bodyEnv['env'] = [[]] + bodyEnv['env']
        
        labelT = env['frame'].getNewLabel()
        labelF = env['frame'].getNewLabel()
        # labelO = env['frame'].getNewLabel()

        if type(ast.expr) is BinaryOp:
            if ast.expr.op in ['&&', '||']:
                lCode = []
                lType = None
                rCode = []
                rType = None

                if type(ast.expr.left) is BinaryOp and ast.expr.left.op not in ['&&', '||']:
                    _, t, code = self.visit(ast.expr.left.left, env)
                    lCode.append(code)
                    _, t, code = self.visit(ast.expr.left.right, env)
                    lCode.append(code)
                    lType = BinaryOp(ast.expr.left.op, t, t)
                else:
                    _, _, code = self.visit(ast.expr.left, env)
                    lCode.append(code)
                
                if type(ast.expr.right) is BinaryOp and ast.expr.right.op not in ['&&', '||']:
                    _, t, code = self.visit(ast.expr.right.left, env)
                    rCode.append(code)
                    _, t, code = self.visit(ast.expr.right.right, env)
                    rCode.append(code)
                    rType = BinaryOp(ast.expr.right.op, t, t)
                else:
                    _, _, code = self.visit(ast.expr.right, env)
                    rCode.append(code)

                self.emit.printout(self.emit.emitSHORTCIRCUIT(ast.expr.op, BoolType(), lCode, rCode, lType, rType, labelT, labelF, env['frame']))
                if ast.expr.op == '&&':
                    # self.emit.printout(self.emit.emitLABEL(labelT, env['frame']))
                    # res += self.emit.emitPUSHICONST(1, env['frame'])
                    bodyEnv = env.copy()
                    bodyEnv['env'] = [[]] + bodyEnv['env']

                    bodyEnv['frame'].enterScope(False)
                    self.emit.printout(self.emit.emitLABEL(bodyEnv['frame'].getStartLabel(), bodyEnv['frame']))
                    if type(ast.thenStmt) is not Block:
                        bodyEnv = self.visit(ast.thenStmt, env)
                    else:
                        bodyEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.thenStmt.member, bodyEnv)
                    self.emit.printout(self.emit.emitLABEL(bodyEnv['frame'].getEndLabel(), bodyEnv['frame']))
                    bodyEnv['frame'].exitScope()

                    if ast.elseStmt:
                        self.emit.printout(self.emit.emitGOTO(labelT, env['frame']))
                        self.emit.printout(self.emit.emitLABEL(labelF, env['frame']))
                    # res += self.emit.emitPUSHICONST(0, env['frame'])
                        elseEnv = env.copy()
                        elseEnv['env'] = [[]] + elseEnv['env']
                        
                        elseEnv['frame'].enterScope(False)
                        self.emit.printout(self.emit.emitLABEL(elseEnv['frame'].getStartLabel(), elseEnv['frame']))
                        if type(ast.elseStmt) is not Block:
                            elseEnv = self.visit(ast.elseStmt, env)
                        else:
                            elseEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.elseStmt.member, elseEnv)
                        self.emit.printout(self.emit.emitLABEL(elseEnv['frame'].getEndLabel(), elseEnv['frame']))
                        elseEnv['frame'].exitScope()

                        self.emit.printout(self.emit.emitLABEL(labelT, env['frame']))
                    else:
                        self.emit.printout(self.emit.emitLABEL(labelF, env['frame']))
                else:
                    self.emit.printout(self.emit.emitLABEL(labelF, env['frame']))
                    # res += self.emit.emitPUSHICONST(1, env['frame'])

                    if ast.elseStmt:
                    # res += self.emit.emitPUSHICONST(0, env['frame'])
                        elseEnv = env.copy()
                        elseEnv['env'] = [[]] + elseEnv['env']
                        
                        elseEnv['frame'].enterScope(False)
                        self.emit.printout(self.emit.emitLABEL(elseEnv['frame'].getStartLabel(), elseEnv['frame']))
                        if type(ast.elseStmt) is not Block:
                            elseEnv = self.visit(ast.elseStmt, env)
                        else:
                            elseEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.elseStmt.member, elseEnv)
                        self.emit.printout(self.emit.emitLABEL(elseEnv['frame'].getEndLabel(), elseEnv['frame']))
                        elseEnv['frame'].exitScope()

                    self.emit.printout(self.emit.emitGOTO(labelF, env['frame']))
                    self.emit.printout(self.emit.emitLABEL(labelT, env['frame']))

                    bodyEnv = env.copy()
                    bodyEnv['env'] = [[]] + bodyEnv['env']

                    bodyEnv['frame'].enterScope(False)
                    self.emit.printout(self.emit.emitLABEL(bodyEnv['frame'].getStartLabel(), bodyEnv['frame']))
                    if type(ast.thenStmt) is not Block:
                        bodyEnv = self.visit(ast.thenStmt, env)
                    else:
                        bodyEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.thenStmt.member, bodyEnv)
                    self.emit.printout(self.emit.emitLABEL(bodyEnv['frame'].getEndLabel(), bodyEnv['frame']))
                    bodyEnv['frame'].exitScope()

                    self.emit.printout(self.emit.emitLABEL(labelF, env['frame']))
            else:
                lVal, lType, lCode = self.visit(ast.expr.left, env)
                rVal, rType, rCode = self.visit(ast.expr.right, env)
                
                self.emit.printout(lCode)
                self.emit.printout(rCode)

                self.emit.printout(self.emit.emitRELOP(ast.expr.op, lType, labelT, labelF, env['frame']))

                bodyEnv = env.copy()
                bodyEnv['env'] = [[]] + bodyEnv['env']

                bodyEnv['frame'].enterScope(False)
                self.emit.printout(self.emit.emitLABEL(bodyEnv['frame'].getStartLabel(), bodyEnv['frame']))
                if type(ast.thenStmt) is not Block:
                    bodyEnv = self.visit(ast.thenStmt, env)
                else:
                    bodyEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.thenStmt.member, bodyEnv)
                self.emit.printout(self.emit.emitLABEL(bodyEnv['frame'].getEndLabel(), bodyEnv['frame']))
                bodyEnv['frame'].exitScope()

                if ast.elseStmt:
                    self.emit.printout(self.emit.emitGOTO(labelT, env['frame']))
                    self.emit.printout(self.emit.emitLABEL(labelF, env['frame']))
                # res += self.emit.emitPUSHICONST(0, env['frame'])
                    elseEnv = env.copy()
                    elseEnv['env'] = [[]] + elseEnv['env']
                    
                    elseEnv['frame'].enterScope(False)
                    self.emit.printout(self.emit.emitLABEL(elseEnv['frame'].getStartLabel(), elseEnv['frame']))
                    if type(ast.elseStmt) is not Block:
                        elseEnv = self.visit(ast.elseStmt, env)
                    else:
                        elseEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.elseStmt.member, elseEnv)
                    self.emit.printout(self.emit.emitLABEL(elseEnv['frame'].getEndLabel(), elseEnv['frame']))
                    elseEnv['frame'].exitScope()

                    self.emit.printout(self.emit.emitLABEL(labelT, env['frame']))
                else:
                    self.emit.printout(self.emit.emitLABEL(labelF, env['frame']))
        else:
            _, _, code = self.visit(ast.expr, env)
            self.emit.printout(code)
            self.emit.printout(self.emit.emitIFFALSE(labelF, env['frame']))

            bodyEnv = env.copy()
            bodyEnv['env'] = [[]] + bodyEnv['env']

            bodyEnv['frame'].enterScope(False)
            self.emit.printout(self.emit.emitLABEL(bodyEnv['frame'].getStartLabel(), bodyEnv['frame']))
            if type(ast.thenStmt) is not Block:
                bodyEnv = self.visit(ast.thenStmt, env)
            else:
                bodyEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.thenStmt.member, bodyEnv)
            self.emit.printout(self.emit.emitLABEL(bodyEnv['frame'].getEndLabel(), bodyEnv['frame']))
            bodyEnv['frame'].exitScope()

            if ast.elseStmt:
                self.emit.printout(self.emit.emitGOTO(labelT, env['frame']))
                self.emit.printout(self.emit.emitLABEL(labelF, env['frame']))
            # res += self.emit.emitPUSHICONST(0, env['frame'])
                elseEnv = env.copy()
                elseEnv['env'] = [[]] + elseEnv['env']
                
                elseEnv['frame'].enterScope(False)
                self.emit.printout(self.emit.emitLABEL(elseEnv['frame'].getStartLabel(), elseEnv['frame']))
                if type(ast.elseStmt) is not Block:
                    elseEnv = self.visit(ast.elseStmt, env)
                else:
                    elseEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.elseStmt.member, elseEnv)
                self.emit.printout(self.emit.emitLABEL(elseEnv['frame'].getEndLabel(), elseEnv['frame']))
                elseEnv['frame'].exitScope()

                self.emit.printout(self.emit.emitLABEL(labelT, env['frame']))
            else:
                self.emit.printout(self.emit.emitLABEL(labelF, env['frame']))

        return o
    
    def visitForBasic(self, ast, o):
        env = o.copy()
        env['isLeft'] = False

        env['frame'].enterLoop()
        env['frame'].enterScope(False)
        conLabel = env['frame'].getContinueLabel()
        brkLabel = env['frame'].getBreakLabel()
        
        _, _, code = self.visit(ast.cond, env)
        self.emit.printout(self.emit.emitLABEL(conLabel, env['frame']))
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))

        self.emit.printout(code)
        self.emit.printout(self.emit.emitIFFALSE(brkLabel, env['frame']))

        # print("BEFORE LOOP: ", len(env['env']))

        bodyEnv = env.copy()
        bodyEnv['env'] = [[]] + bodyEnv['env']

        # print("SUBENV LEN: ", len(bodyEnv['env']))

        bodyEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.loop.member, bodyEnv)
        self.emit.printout(self.emit.emitGOTO(conLabel, bodyEnv['frame']))

        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        self.emit.printout(self.emit.emitLABEL(brkLabel, env['frame']))
        env['frame'].exitScope()
        env['frame'].exitLoop()

        # print("AFTER LOOP: ", len(env['env']))

        return o
 
    def visitForStep(self, ast, o):
        env = o.copy()
        env['isLeft'] = False

        env['frame'].enterLoop()
        env['frame'].enterScope(False)
        conLabel = env['frame'].getContinueLabel()
        brkLabel = env['frame'].getBreakLabel()
        
        bodyEnv = env.copy()
        bodyEnv['env'] = [[]] + bodyEnv['env']
        
        bodyEnv = self.visit(ast.init, bodyEnv)
        _, _, code = self.visit(ast.cond, bodyEnv)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))

        self.emit.printout(code)
        self.emit.printout(self.emit.emitIFFALSE(brkLabel, env['frame']))

        # print("BEFORE LOOP: ", len(env['env']))

        # print("SUBENV LEN: ", len(bodyEnv['env']))

        bodyEnv = reduce(lambda acc, ele: self.visit(ele, acc), ast.loop.member, bodyEnv)
        self.emit.printout(self.emit.emitLABEL(conLabel, env['frame']))
        bodyEnv = self.visit(ast.upda, bodyEnv)

        self.emit.printout(self.emit.emitGOTO(env['frame'].getStartLabel(), env['frame']))

        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        self.emit.printout(self.emit.emitLABEL(brkLabel, env['frame']))
        env['frame'].exitScope()
        env['frame'].exitLoop()

        return o

    def visitForEach(self, ast, o):
        pass

    def visitContinue(self, ast, o):
        if 'frame' in o:
            self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(), o['frame']))

            return o
        else:
            raise IllegalRuntimeException("No frame for the break statement.")
    
    def visitBreak(self, ast, o):
        if 'frame' in o:
            self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(), o['frame']))

            return o
        else:
            raise IllegalRuntimeException("No frame for the break statement.")
    
    def visitReturn(self, ast, o):
        if 'frame' in o:
            env = o.copy()
            env['isLeft'] = False

            if ast.expr:
                val, typ, code = self.visit(ast.expr, env)
                self.emit.printout(code)
                self.emit.printout(self.emit.emitRETURN(typ, env['frame']))

            return o
        else:
            raise IllegalRuntimeException("No frame for the return statement.")

    def visitBinaryOp(self, ast, o):
        if 'frame' in o:
            env = o.copy()
            env['isLeft'] = False

            res = ""
            val = None
            typ = None

            if ast.op in ['+', '-']:
                lVal, lType, lCode = self.visit(ast.left, env)
                rVal, rType, rCode = self.visit(ast.right, env)
                
                if type(lType) is IntType and type(rType) is FloatType:
                    typ = FloatType()
                    # val = FloatLiteral(float(lVal.value + rVal.value)) if ast.op == '+' else FloatLiteral(float(lVal.value - rVal.value))
                    res += lCode + self.emit.emitI2F(env['frame']) + rCode + self.emit.emitADDOP(ast.op, typ, env['frame'])
                elif type(rType) is IntType and type(lType) is FloatType:
                    typ = FloatType()
                    # val = FloatLiteral(float(lVal.value + rVal.value)) if ast.op == '+' else FloatLiteral(float(lVal.value - rVal.value))
                    res += lCode + rCode + self.emit.emitI2F(env['frame']) + self.emit.emitADDOP(ast.op, typ, env['frame'])
                else:
                    if type(lType) is StringType:
                        typ = StringType()
                        val = StringLiteral(lVal.value + rVal.value)
                        res += self.emit.emitNEW(ClassType('java/lang/StringBuilder'), env['frame'])
                        res += self.emit.emitDUP(env['frame'])
                        res += self.emit.emitINVOKESPECIAL(env['frame'], "java/lang/StringBuilder/<init>", MType([], VoidType()))
                        res += lCode
                        res += self.emit.emitINVOKEVIRTUAL("java/lang/StringBuilder/append", MType([StringType()], ClassType('java/lang/StringBuilder')), env['frame'])
                        res += rCode
                        res += self.emit.emitINVOKEVIRTUAL("java/lang/StringBuilder/append", MType([StringType()], ClassType('java/lang/StringBuilder')), env['frame'])
                        res += self.emit.emitINVOKEVIRTUAL("java/lang/StringBuilder/toString", MType([], StringType()), env['frame'])
                    else:
                        typ = lType
                        # if type(typ) is IntType:
                        #     val = IntLiteral(lVal.value + rVal.value) if ast.op == '+' else IntLiteral(lVal.value - rVal.value)
                        # else:
                        #     val = FloatLiteral(lVal.value + rVal.value) if ast.op == '+' else FloatLiteral(lVal.value - rVal.value)
                        res += lCode + rCode + self.emit.emitADDOP(ast.op, typ, env['frame'])
            elif ast.op in ['*', '/']:
                lVal, lType, lCode = self.visit(ast.left, env)
                rVal, rType, rCode = self.visit(ast.right, env)
                
                if type(lType) is IntType and type(rType) is FloatType:
                    typ = FloatType()
                    # val = FloatLiteral(float(lVal.value * rVal.value)) if ast.op == '*' else FloatLiteral(float(lVal.value / rVal.value))
                    res += lCode + self.emit.emitI2F(env['frame']) + rCode + self.emit.emitMULOP(ast.op, typ, env['frame'])
                elif type(rType) is IntType and type(lType) is FloatType:
                    typ = FloatType()
                    # val = FloatLiteral(float(lVal.value * rVal.value)) if ast.op == '*' else FloatLiteral(float(lVal.value / rVal.value))
                    res += lCode + rCode + self.emit.emitI2F(env['frame']) + self.emit.emitMULOP(ast.op, typ, env['frame'])
                else:
                    typ = lType
                    # if type(typ) is IntType:
                    #     val = IntLiteral(lVal.value * rVal.value) if ast.op == '*' else IntLiteral(lVal.value / rVal.value)
                    # else:
                    #     val = FloatLiteral(lVal.value * rVal.value) if ast.op == '*' else FloatLiteral(lVal.value / rVal.value)
                    res += lCode + rCode + self.emit.emitMULOP(ast.op, typ, env['frame'])
            elif ast.op == '%':
                lVal, lType, lCode = self.visit(ast.left, env)
                rVal, rType, rCode = self.visit(ast.right, env)

                # val = IntLiteral(lVal.value % rVal.value)
                typ = IntType()
                
                res += lCode + rCode
                res += self.emit.emitMOD(env['frame'])

            elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
                lVal, lType, lCode = self.visit(ast.left, env)
                rVal, rType, rCode = self.visit(ast.right, env)
                

                typ = BoolType()
                # if type(lType) is StringType:
                #     pass
                # else:
                res += lCode + rCode + self.emit.emitREOP(ast.op, lType, env['frame'])

            elif ast.op in ['&&', '||']:
                labelT = env['frame'].getNewLabel()
                labelF = env['frame'].getNewLabel()
                labelO = env['frame'].getNewLabel()

                typ = BoolType()

                lCode = []
                lType = None
                rCode = []
                rType = None

                if type(ast.left) is BinaryOp and ast.left.op not in ['&&', '||']:
                    _, t, code = self.visit(ast.left.left, env)
                    lCode.append(code)
                    _, t, code = self.visit(ast.left.right, env)
                    lCode.append(code)
                    lType = BinaryOp(ast.left.op, t, t)
                else:
                    _, _, code = self.visit(ast.left, env)
                    lCode.append(code)
                
                if type(ast.right) is BinaryOp and ast.right.op not in ['&&', '||']:
                    _, t, code = self.visit(ast.right.left, env)
                    rCode.append(code)
                    _, t, code = self.visit(ast.right.right, env)
                    rCode.append(code)
                    rType = BinaryOp(ast.right.op, t, t)
                else:
                    _, _, code = self.visit(ast.right, env)
                    rCode.append(code)

                res += self.emit.emitSHORTCIRCUIT(ast.op, BoolType(), lCode, rCode, lType, rType, labelT, labelF, env['frame'])
                if ast.op == '&&':
                    # res += self.emit.emitLABEL(labelT, env['frame'])
                    res += self.emit.emitPUSHICONST(1, env['frame'])
                    res += self.emit.emitGOTO(labelO, env['frame'])
                    res += self.emit.emitLABEL(labelF, env['frame'])
                    res += self.emit.emitPUSHICONST(0, env['frame'])
                    res += self.emit.emitLABEL(labelO, env['frame'])
                else:
                    # res += self.emit.emitLABEL(labelF, env['frame'])
                    res += self.emit.emitPUSHICONST(0, env['frame'])
                    res += self.emit.emitGOTO(labelO, env['frame'])
                    res += self.emit.emitLABEL(labelT, env['frame'])
                    res += self.emit.emitPUSHICONST(1, env['frame'])
                    res += self.emit.emitLABEL(labelO, env['frame'])
                env['frame'].pop()

            return val, typ, res
        else:
            lVal, lType, lCode = self.visit(ast.left, o)
            rVal, rType, rCode = self.visit(ast.right, o)

            # val = None
            typ = None

            if ast.op in ['+', '-']:
                if type(lType) is IntType and type(rType) is FloatType:
                    typ = FloatType()
                    # val = FloatLiteral(float(lVal.value + rVal.value)) if ast.op == '+' else FloatLiteral(float(lVal.value - rVal.value))
                elif type(rType) is IntType and type(lType) is FloatType:
                    typ = FloatType()
                    # val = FloatLiteral(float(lVal.value + rVal.value)) if ast.op == '+' else FloatLiteral(float(lVal.value - rVal.value))
                else:
                    if type(lType) is StringType:
                        typ = StringType()
                        # val = StringLiteral(lVal.value + rVal.value)
                    else:
                        typ = lType
                        # if type(typ) is IntType:
                        #     val = IntLiteral(lVal.value + rVal.value) if ast.op == '+' else IntLiteral(lVal.value - rVal.value)
                        # else:
                        #     val = FloatLiteral(lVal.value + rVal.value) if ast.op == '+' else FloatLiteral(lVal.value - rVal.value)
            elif ast.op in ['*', '/']:
                if type(lType) is IntType and type(rType) is FloatType:
                    typ = FloatType()
                    # val = FloatLiteral(float(lVal.value * rVal.value)) if ast.op == '*' else FloatLiteral(float(lVal.value / rVal.value))
                elif type(rType) is IntType and type(lType) is FloatType:
                    typ = FloatType()
                    # val = FloatLiteral(float(lVal.value * rVal.value)) if ast.op == '*' else FloatLiteral(float(lVal.value / rVal.value))
                else:
                    typ = lType
                    # if type(typ) is IntType:
                    #     val = IntLiteral(lVal.value * rVal.value) if ast.op == '*' else IntLiteral(lVal.value / rVal.value)
                    # else:
                    #     val = FloatLiteral(lVal.value * rVal.value) if ast.op == '*' else FloatLiteral(lVal.value / rVal.value)
            
            elif ast.op == '%':
                typ = IntType()
            elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
                typ = BoolType()
                # if type(lType) is StringType:
                #     pass
                # else:
            elif ast.op in ['&&', '||']:
                typ = BoolType()

            return ast, typ, None
    
    def visitUnaryOp(self, ast, o):
        if 'frame' in o:
            env = o.copy()
            env['isLeft'] = False
            exprVal, exprType, exprCode = self.visit(ast.body, env)

            if ast.op == '-':
                return exprVal, exprType, exprCode + self.emit.emitNEGOP(exprType, env['frame'])
            else:
                return exprVal, exprType, exprCode + self.emit.emitNOT(exprType, env['frame'])
        else:
            env = o.copy()
            env['isLeft'] = False

            exprVal, exprType, exprCode = self.visit(ast.body, env)
            return ast, exprType, None
    
    def visitFuncCall(self, ast, o):
        self.fetchEnv(ast, o)

        if 'frame' in o:
            sym = next(filter(lambda x: x[0].name == ast.funName, o['env'][-1]), None)

            env = o.copy()
            env['isLeft'] = False

            res = ""

            for i in range(len(ast.args)):
                t = self.visit(ast.args[i], env)
                # print("Result: ", t[2])
                res += t[2]

            # [self.emit.printout(self.visit(x, env)[0])[2] for x in ast.args]

            res += self.emit.emitINVOKESTATIC(f"{sym[0].value.value}/{ast.funName}", sym[0].mtype, o['frame'])

            if type(sym[0].mtype.rettype) is VoidType:
                self.emit.printout(res)
                return o
            else:
                return self.DefaultVal(sym[0].mtype.rettype, env), sym[0].mtype.rettype, res
        else:
            sym = next(filter(lambda x: x[0].name == ast.funName, o['env'][-1]), None)

            return ast, sym[0].mtype.rettype, None

    def visitMethCall(self, ast, o):
        return None
    
    def visitId(self, ast, o):
        self.fetchEnv(ast, o)
        
        sym = next(filter(lambda x: x is not None, [self.lookup(ast.name, env) for env in o['env']]), None)

        if type(sym[0].value) is Index:
            if o['isLeft']:
                return sym[1], sym[0].mtype, self.emit.emitWRITEVAR(ast.name, sym[0].mtype, sym[0].value.value, o['frame'])
            else:
                return sym[1], sym[0].mtype, self.emit.emitREADVAR(ast.name, sym[0].mtype, sym[0].value.value, o['frame'])
        else:
            if 'frame' in o:
                if o['isLeft']:
                    return sym[1], sym[0].mtype, self.emit.emitPUTSTATIC(f"{sym[0].value.value}.{ast.name}", sym[0].mtype, o['frame'])
                else:
                    return sym[1], sym[0].mtype, self.emit.emitGETSTATIC(f"{sym[0].value.value}/{ast.name}", sym[0].mtype, o['frame']) 
            else:
                entry = next(filter(lambda x: x[0] == ast.name, self.GlobVarTable), None)
                return entry[1], sym[0].mtype, None
    
    def visitArrayCell(self, ast, o):
        self.fetchEnv(ast, o)
        
        if 'frame' in o:
            env = o.copy()
            env['isLeft'] = False
            # print("ENV: ", str(env))
            arrVal, arrTyp, arrCode = self.visit(ast.arr, env)
            resType = None
            if (len(ast.idx) == len(arrTyp.dimens)):
                resType = arrTyp.eleType
                if type(arrTyp.eleType) is Id:
                    sym = next(filter(lambda x: x[0].name == arrTyp.eleType.name, env['env'][-1]), None)
                    resType = ClassType(sym[0].name)
            else:
                resType = ArrayType(copy.deepcopy(arrTyp.dimens[len(ast.idx):]), arrTyp.eleType)
            res = arrCode
            for i in range(len(ast.idx)):
                env['isLeft'] = False
                val, typ, code = self.visit(ast.idx[i], env)
                res += code
                if i == len(ast.idx) - 1:
                    res += self.emit.emitALOAD(resType, env['frame'])
                else:
                    res += self.emit.emitALOAD(arrTyp, env['frame'])

            return None, resType, res
        else:
            env = o.copy()
            arrVal, arrTyp, arrCode = self.visit(ast.arr, env)
            resType = arrVal.eleType if len(ast.idx) == len(arrVal.dimens) else ArrayType(copy.deepcopy(arrVal.dimens[len(ast.idx):]), arrVal.eleType)

            if type(arrTyp.eleType) is Id:
                sym = next(filter(lambda x: x[0].name == arrTyp.eleType.name, env['env'][-1]), None)
                resType = ClassType(sym[0].name)

            return ast, resType, None
    
    def visitFieldAccess(self, ast, o):
        if 'frame' in o:
            env = o.copy()
            env['isLeft'] = False
            reiVal, reiType, reiCode = self.visit(ast.receiver, env)

            res = ""
            typ = None

            if type(reiType) is StructType:
                typ = next(filter(lambda x: x[0] == ast.field, reiType.elements), None)[1]
            elif type(reiType) is ClassType:
                sym = next(filter(lambda x: x[0].name == reiType.name, env['env'][-1]), None)
                typ = next(filter(lambda x: x[0] == ast.field, sym[0].mtype.elements), None)[1]

            res += reiCode
            res += self.emit.emitGETFIELD(f"{reiType.name}.{ast.field}", typ, env['frame'])

            return None, typ, res
        else:
            env = o.copy()
            env['isLeft'] = False
            reiVal, reiType, reiCode = self.visit(ast.reiceiver, env)

            typ = None

            if type(reiType) is StructType:
                typ = next(filter(lambda x: x[0] == ast.field, reiType.elements), None)[1]
            elif type(reiType) is ClassType:
                sym = next(filter(lambda x: x[0].name == reiType.name, env['env'][-1]), None)
                typ = next(filter(lambda x: x[0] == ast.field, sym[0].mtype.elements), None)[1]

            return ast, typ, None
    
    def visitIntLiteral(self, ast, o):
        if 'frame' in o:
            return ast, IntType(), self.emit.emitPUSHICONST(str(ast.value), o['frame'])
        else:
            return ast, IntType(), None
    
    def visitFloatLiteral(self, ast, o):
        if 'frame' in o:
            return ast, FloatType(), self.emit.emitPUSHFCONST(str(ast.value), o['frame'])
        else:
            return ast, FloatType(), None
    
    def visitBooleanLiteral(self, ast, o):
        if 'frame' in o:
            val = "true" if ast.value else "false"
            
            return ast, BoolType(), self.emit.emitPUSHICONST(val, o['frame'])
        else:
            return ast, BoolType(), None
    
    def visitStringLiteral(self, ast, o):
        if 'frame' in o:
            return ast, StringType(), self.emit.emitSTRINGLIT(str(ast.value), o['frame'])
        else:
            return ast, StringType(), None

    def visitArrayLiteral(self, ast, o):
        self.fetchEnv(ast, o)
        
        if 'frame' in o:
            dimens = copy.deepcopy(ast.dimens)
            for i in range(len(dimens)):
                dimens[i] = self.visit(dimens[i], o)[0]
            
            if len(ast.dimens) == 1:
                env = o.copy()
                env['isLeft'] = False
                # print("ENV: ", env)
                # print("DIMENS: ", ast.dimens)
                val, typ, code = self.visit(ast.dimens[0], env)
                # ast.dimens[0] = val
                res = code
                eleType = ast.eleType

                if type(eleType) is Id:
                    sym = next(filter(lambda x: x[0].name == eleType.name, env['env'][-1]), None)
                    eleType = ClassType(sym[0].name)

                frame = env['frame']
                # if type(ast.eleType) is not StringType and type(ast.eleType) is not StructType and type(ast.eleType) is not InterfaceType:
                if type(eleType) is not ClassType and type(eleType) is not StringType:
                    res += self.emit.emitNEWARRAY(eleType, frame)
                else:
                    # eleType = ClassType(ast.eleType.name) if type(ast.eleType) is StructType or type(ast.eleType) is InterfaceType else ast.eleType
                    res += self.emit.emitANEWARRAY(eleType, frame)
                values = ast.value
                for i in range(len(values)):
                    res += self.emit.emitDUP(frame)
                    res += self.visit(IntLiteral(i), env)[2]
                    res += self.visit(values[i], env)[2]
                    res += self.emit.emitASTORE(eleType, frame)
                
                return ast, ArrayType(dimens, ast.eleType), res
            else:
                env = o.copy()
                env['isLeft'] = False
                finalDimens = []
                res = ""

                for i in range(len(ast.dimens)):
                    val, typ, code = self.visit(copy.deepcopy(ast.dimens[i]), env)
                    finalDimens.append(val.value)
                    res += code
                
                eleType = ast.eleType
                if type(eleType) is Id:
                    sym = next(filter(lambda x: x[0].name == eleType.name, env['env'][-1]), None)
                    eleType = ClassType(sym[0].name)
                # eleType = ClassType(ast.eleType.name) if type(ast.eleType) is StructType or type(ast.eleType) is InterfaceType else ast.eleType

                res += self.emit.emitMULTIANEWARRAY(eleType, ast.dimens, env['frame'])

                # print("Final dimens: ", finalDimens)
                l = len(finalDimens)
                totalLoops = reduce(lambda acc, ele: acc * ele, finalDimens, 1)

                for i in range(0, totalLoops, finalDimens[-1]):
                    # print("I: ", i)
                    res += self.emit.emitDUP(env['frame'])

                    value = ast.value
                    # indices = [0]*(l - 1)
                    for j in range(l - 1):
                        totalEle = reduce(lambda acc, ele: acc * ele, finalDimens[(j + 1):], 1)
                        # print("TE: ", totalEle)
                        remain = i % totalEle
                        quotient = int((i - remain) / totalEle)
                        # print("Q: ", quotient)
                        # indices[j] = quotient
                        i = remain
                        value = value[quotient]
                        
                        res += self.emit.emitPUSHICONST(str(quotient), env['frame'])
                        if (j != l - 2):
                            res += self.emit.emitALOAD(ArrayType([], IntType()), env['frame'])

                    array = ArrayLiteral([IntLiteral(finalDimens[-1])], ast.eleType, value)
                    tempVal, tempType, tempCode = self.visit(array, env)
                    res += tempCode
                    res += self.emit.emitASTORE(ArrayType([], IntType()), env['frame'])

                # res += self.emit.emitPOP(env['frame'])  

                return ast, ArrayType(dimens, ast.eleType), res
        else:
            dimens = copy.deepcopy(ast.dimens)
            for i in range(len(dimens)):
                dimens[i] = self.visit(dimens[i], o)[0]

            if type(ast.eleType) is Id:
                sym = next(filter(lambda x: x[0].name == ast.eleType.name, o['env'][-1]), None)
                ast.eleType = ClassType(sym[0].name)

            return ast, ArrayType(dimens, ast.eleType), None

    def visitStructLiteral(self, ast, o):
        if 'frame' in o:
            env = o.copy()
            env['isLeft'] = False

            res = ""
            typ = copy.deepcopy(next(filter(lambda x: x[0].name == ast.name, o['env'][-1]), None))

            structElements = typ[0].mtype.elements

            res += self.emit.emitNEW(ClassType(ast.name), env['frame'])
            res += self.emit.emitDUP(env['frame'])
            res += self.emit.emitINVOKESPECIAL(env['frame'], f"{ast.name}/<init>", MType([], VoidType()))

            for i in range(len(structElements)):
                ele = next(filter(lambda x: x[0] == structElements[i][0], ast.elements), None)

                if ele is not None:
                    res += self.emit.emitDUP(env['frame'])
                    eleVal, eleType, eleCode = self.visit(ele[1], env)
                    res += eleCode
                    res += self.emit.emitPUTFIELD(f"{ast.name}.{ast.elements[i][0]}", eleType, env['frame'])
                else:
                    res += self.emit.emitDUP(env['frame'])
                    eleVal, eleType, eleCode = self.visit(self.DefaultVal(structElements[i][1], env), env)
                    res += eleCode
                    res += self.emit.emitPUTFIELD(f"{ast.name}.{structElements[i][0]}", structElements[i][1], env['frame'])

            return ast, typ[0].mtype, res
        else:
            typ = next(filter(lambda x: x[0].name == ast.name, o['env'][-1]), None)
            return ast, typ[0].mtype, None

    def visitNilLiteral(self, ast, o):
        if 'frame' in o:
            return ast, VoidType(), self.emit.emitPUSHNULL(o['frame'])
        else:
            return ast, VoidType(), None