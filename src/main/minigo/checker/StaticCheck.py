"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
import copy

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor, Utils):
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
            [
                (Symbol("getInt", MType([],IntType())), Function()),
                (Symbol("putInt", MType([IntType()], VoidType())), Function()),
                (Symbol("putIntLn", MType([IntType()], VoidType())), Function()),
                (Symbol("getFloat", MType([], FloatType())), Function()),
                (Symbol('putFloat', MType([FloatType()], VoidType())), Function()),
                (Symbol('putFloatLn', MType([FloatType()], VoidType())), Function()),
                (Symbol('getBool', MType([], BoolType())), Function()),
                (Symbol('putBool', MType([BoolType()], VoidType())), Function()),
                (Symbol('putBoolLn', MType([BoolType()], VoidType())), Function()),
                (Symbol('getString', MType([], StringType())), Function()),
                (Symbol('putString', MType([StringType()], VoidType())), Function()),
                (Symbol('putStringLn', MType([StringType()], VoidType())), Function()),
                (Symbol('putLn', MType([], VoidType())), Function())
            ]
        ]
        self.globIdx = 0
        self.VarConstDeclIdx = []
        self.funcIdx = 0
        self.FuncMethodIdx = []
        self.decls = []
 
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
            return ArrayLiteral(
                copy.deepcopy(l.dimens),
                copy.deepcopy(l.eleType),
                reduce(lambda acc, ele: [acc] * ele, [i.value for i in l.dimens][::-1], self.DefaultVal(l.eleType, c))
            )
        elif type(l) is StructType:
            check = self.lookup(l.name, c['env'][-1])
            if check is None:
                raise Undeclared(Identifier(), l.name)
            if type(check[1]) is not Type:
                raise TypeError(f"Invalid type definition: {str(check[0])}")
            return StructLiteral(
                check[0].mtype.name,
                reduce(lambda acc, ele: [(ele[0], self.DefaultVal(ele[1], c))] + acc, check[0].mtype.elements, [])
            )
        elif type(l) is InterfaceType:
            for i in range(len(c['env'][-1])):
                if type(c['env'][-1][i][1]) is Type and type(c['env'][-1][i][0].mtype) is StructType:
                    if self.MatchType(l, c['env'][-1][i][0].mtype, c):
                        return self.DefaultVal(c['env'][-1][i][0].mtype, c)
                    
            raise TypeError("Default value: No suitable StructType for " + str(l))
        
        raise TypeError("Default value: Invalid type " + str(l))

    def MatchType(self, t1, t2, c):
        # print(f"Check matching types: {str(t1)}, {str(t2)}")
        
        if type(t1) is InterfaceType:
            if type(t2) is InterfaceType:
                return t1.name == t2.name
            elif type(t2) is StructType:
                methods = t2.methods
                pros = t1.methods
                for pro in pros:
                    method = next(filter(lambda x: x.fun.name == pro.name, methods), None)
                    if method is None:
                        return False
                    else:
                        meth_params = method.fun.params
                        pro_params = pro.params
                        if len(meth_params) != len(pro_params):
                            return False
                        else:
                            for i in range(len(meth_params)):
                                if not self.MatchType(meth_params[i].parType, pro_params[i], c):
                                    return False
                return True
            else:
                return False
        elif type(t1) is StructType:
            if type(t2) is StructType:
                return t1.name == t2.name
            else:
                return False
        elif type(t1) is ArrayType:
            t1 = self.visit(t1, c)
            if type(t2) is ArrayType:
                t2 = self.visit(t2, c)
                if not self.MatchType(t1.eleType, t2.eleType, c):
                    return False
                if len(t1.dimens) != len(t2.dimens):
                    return False
                else:
                    for i in range(len(t1.dimens)):
                        if t1.dimens[i].value != t2.dimens[i].value:
                            return False
                return True
            else:
                return False
        elif type(t1) is FloatType:
            return type(t2) is FloatType or type(t2) is IntType
        else:
            return type(t1) is type(t2)

    def ArrayValueCheck(self, rootAST, ast, arr, dimens, eleType, c):
        # print(f"Check array: {str(arr)} with dimens {str(dimens)} and type {str(eleType)}")
        
        d = [i.value for i in dimens]

        if len(d) == 1:
            arrLength = len(arr)
            for i in range(len(arr)):
                c['inExpr'] = True
                arr[i] = self.visit(arr[i], c)
                c['inExpr'] = False

                if not self.MatchType(eleType, self.TypeOfLit(arr[i], c), c):
                    raise TypeMismatch(rootAST)
                if type(self.TypeOfLit(arr[i], c)) is IntType and type(eleType) is FloatType:
                    arr[i] = FloatLiteral(float(arr[i].value))
            arr = arr + [self.DefaultVal(eleType, c)] * (d[0] - arrLength)
        else:
            arrLength = len(arr)
            for i in range(len(arr)):
                if type(arr[i]) is not list:
                    raise TypeMismatch(rootAST)
                else:
                    arr[i] = self.ArrayValueCheck(rootAST, ast, arr[i], dimens[1:], eleType, c)
            arr = arr + reduce(lambda acc, ele: [acc] * ele, d[1::-1], self.DefaultVal(eleType, c)) * (d[0] - arrLength)

        # print(f"Array after checking: {str(arr)}")

        return arr


    def BinOp(self, left, op, right):
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        elif op == '%':
            return left % right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
        elif op == '&&':
            return left and right
        elif op == '||':
            return left or right
        else:
            raise TypeError("Invalid operation for BinaryOp")

    def fetchEnv(self, ast, c):
        # print(f"Check {str(ast)}\nData: " + "[" + ','.join("[" + ','.join(f"({str(i[0])}, {str(i[1])})" for i in j) + "]" for j in c['env']) + "]" + ", globScan: " + str(c['globScan']) + ", inExpr: " + str(c['inExpr']), end="\n\n")
        # print("VarDecl and ConstDecl indices: ", self.VarConstDeclIdx)
        # print("Global env len: ", len(c['env'][0]))
        # print("The next VarDecl or ConstDecl: ", self.globIdx)
        # print("The next FuncDecl or MethodDecl: ", self.funcIdx, "\n")
        pass

    def check(self):
        return self.visit(self.ast, self.global_envi)

#region Example
    # def visitProgram(self, ast, c):
    #     reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.decl,c)
    #     return c

    # def visitVarDecl(self, ast, c):
    #     res = self.lookup(ast.varName, c, lambda x: x.name)
    #     if not res is None:
    #         raise Redeclared(Variable(), ast.varName) 
    #     if ast.varInit:
    #         initType = self.visit(ast.varInit, c)
    #         if ast.varType is None:
    #             ast.varType = initType
    #         if not type(ast.varType) is type(initType):
    #             raise TypeMismatch(rootAST)
    #     return Symbol(ast.varName, ast.varType,None)

    # def visitFuncDecl(self, ast, c):
    #     res = self.lookup(ast.name, c, lambda x: x.name)
    #     if not res is None:
    #         raise Redeclared(Function(), ast.name)
    #     return Symbol(ast.name, MType([], ast.retType))

    # def visitIntLiteral(self, ast, c):
    #     return IntType()
    
    # def visitFloatLiteral(self, ast, c):
    #     return FloatType()
    
    # def visitId(self,ast,c):
    #     res = self.lookup(ast.name, c, lambda x: x.name)
    #     if res is None:
    #         raise Undeclared(Identifier(), ast.name)
    #     return res.mtype
#endregion

    def visitProgram(self, ast, c):
        self.decls = copy.deepcopy(ast.decl)

        for i in range(len(ast.decl)):
            if type(ast.decl[i]) is VarDecl or type(ast.decl[i]) is ConstDecl:
                self.VarConstDeclIdx.append(i)
            if type(ast.decl[i]) is FuncDecl or type(ast.decl[i]) is MethodDecl:
                self.FuncMethodIdx.append(i)
        
        c = {'env': c, 'globScan': False, 'inExpr': False}
        c = reduce(lambda acc, ele: self.visit(ele, acc), [d for d in ast.decl if type(d) is StructType or type(d) is InterfaceType], {'env': c['env'], 'globScan': True, 'inExpr': False})
        c = reduce(lambda acc, ele: self.visit(ele, acc), [d for d in ast.decl if type(d) is StructType or type(d) is InterfaceType], {'env': c['env'], 'globScan': False, 'inExpr': False})
        c = reduce(lambda acc, ele: self.visit(ele, acc), [d for d in ast.decl if type(d) is not StructType and type(d) is not InterfaceType], {'env': c['env'], 'globScan': True, 'inExpr': False})
        c = reduce(lambda acc, ele: self.visit(ele, acc), [d for d in ast.decl if type(d) is not StructType and type(d) is not InterfaceType], {'env': c['env'], 'globScan': False, 'inExpr': False})
        return c

    def visitVarDecl(self, ast, c):
        self.fetchEnv(ast, c)

        rootAST = copy.deepcopy(ast)

        # print("ROOTAST: ", str(ast))

        if c['globScan']:
            return c
        else:
            res = None
            if len(c['env']) > 1:
                res = self.lookup(ast.varName, c['env'][0])
                if res is not None:
                    raise Redeclared(Variable(), ast.varName)
            else:
                l = len(c['env'][0]) - 13
                res = self.lookup(ast.varName, c['env'][0][l - self.VarConstDeclIdx[self.globIdx]:])
                if res is not None:
                    raise Redeclared(Variable(), ast.varName)
                else:
                    res = self.lookup(ast.varName, c['env'][0][0:l - self.VarConstDeclIdx[self.globIdx]])
                    if res is not None:
                        raise Redeclared(res[1], ast.varName)
                    
            if ast.varInit is not None:
                c['inExpr'] = True
                val = self.visit(ast.varInit, c) # visit an Expression should return a literal or a symbol.
                c['inExpr'] = False
                expr = None
                if type(val) is tuple:
                    # print("Val: " + str(val[0]))
                    expr = val[0].mtype
                    # print("Check id of val.value1: ", id(val[0].value))
                    val = val[0].value
                    if not val:
                        raise TypeMismatch(rootAST)
                    # print("Check id of val.value2: ", id(val))
# region ArrayCell&FieldAccess
                # elif type(val) is ArrayCell:
                #     if type(val.arr) is tuple:
                #         expr = val.arr[0].mtype
                #         idxList = [i.value for i in val.idx]
                #         val = val.arr[0].value.value
                #         for i in idxList:
                #             val = val[i]
                #     else:
                #         expr = self.TypeOfLit(val.arr, c)
                #         idxList = [i.value for i in val.idx]
                #         val = val.arr.value
                #         for i in idxList:
                #             val = val[i]
                # elif type(val) is FieldAccess:
                #     if type(val.receiver) is tuple:
                #         val = next(filter(lambda x: x[0] == val.field, val.receiver[0].value.elements), None)[1]
# endregion
                else:
                    expr = self.TypeOfLit(val, c)
                if ast.varType is None:
                    ast.varType = expr
                else:
                    if type(ast.varType) is Id:
                        check_und = self.lookup(ast.varType.name, c['env'][-1])
                        if check_und is None:
                            raise Undeclared(Identifier(), ast.varType.name)
                        else:
                            if type(check_und[1]) is not Type:
                                raise TypeMismatch(rootAST)
                        ast.varType = check_und[0].mtype
                    if not self.MatchType(ast.varType, expr, c):
                        raise TypeMismatch(rootAST)
                    if type(expr) is IntType and type(ast.varType) is FloatType:
                        val = FloatLiteral(float(val.value))

#region VarDecl body
                    # if type(ast.varType) is ArrayType:
                    #     if type(expr) is not ArrayType:
                    #         raise TypeMismatch(rootAST)
                    #     else:
                    #         if len(ast.varType.dimens) != len(expr.dimens):
                    #             raise TypeMismatch(rootAST)
                    #         else:
                    #             ast.varType = self.visit(ast.varType, c)

                    #             for i in range(len(ast.varType.dimens)):
                    #                 if ast.varType.dimens[i].value != expr.dimens[i].value:
                    #                     raise TypeMismatch(rootAST)
                                    
                    #             if type(ast.varType.eleType) is FloatType:
                    #                 if type(expr.eleType) is not FloatType and type(expr.eleType) is not IntType:
                    #                     raise TypeMismatch(rootAST)
                    #             elif type(ast.varType.eleType) is StructType:
                    #                 if type(expr) is not StructType:
                    #                     raise TypeMismatch(rootAST)
                    #                 else:
                    #                     if expr.name != ast.varType.name:
                    #                         raise TypeMismatch(rootAST)
                    #             elif type(ast.varType.eleType) is InterfaceType:
                    #                 if type(expr) is InterfaceType:
                    #                     if expr.name != ast.varType.eleType.name:
                    #                         raise TypeMismatch(rootAST)
                    #                 elif type(expr) is StructType:
                    #                     for method in expr.methods:
                    #                         check_imp = next(filter(lambda x: x.name == method.fun.name, ast.varType.eleType.methods), None)
                    #                         if check_imp is None:
                    #                             raise TypeMismatch(rootAST)
                    #             else:
                    #                 if type(expr.eleType) is not type(ast.varType.eleType):
                    #                     raise TypeMismatch(rootAST)
                    # elif type(ast.varType) is StructType:
                    #     if type(expr) is not StructType:
                    #         raise TypeMismatch(rootAST)
                    #     else:
                    #         if expr.name != ast.varType.name:
                    #             raise TypeMismatch(rootAST)
                    # elif type(ast.varType) is InterfaceType:
                    #     if type(expr) is InterfaceType:
                    #         if expr.name != ast.varType.name:
                    #             raise TypeMismatch(rootAST)
                    #     elif type(expr) is StructType:
                    #         for method in expr.methods:
                    #             check_imp = next(filter(lambda x: x.name == method.fun.name, ast.varType.methods), None)
                    #             if check_imp is None:
                    #                 raise TypeMismatch(rootAST)
                    # else:
                    #     if type(ast.varType) is FloatType:
                    #         if type(expr) is not FloatType and type(expr) is not IntType:
                    #             raise TypeMismatch(rootAST)
                    #     else:
                    #         if type(expr) is not type(ast.varType):
                    #             raise TypeMismatch(rootAST)
#endregion
                if len(c['env']) > 1:
                    return {
                        'env': [[(Symbol(ast.varName, ast.varType, val), Variable())] + c['env'][0]] + c['env'][1:],
                        'globScan': c['globScan'],
                        'inExpr': False
                    }
                else:
                    c['env'][0].insert(len(c['env'][0]) - 13 - self.VarConstDeclIdx[self.globIdx], (Symbol(ast.varName, ast.varType, val), Variable()))
                    self.globIdx = self.globIdx + 1
                    return c
            else:
                if type(ast.varType) is Id:
                    check_und = self.lookup(ast.varType.name, c['env'][-1])
                    if check_und is None:
                        raise Undeclared(Identifier(), ast.varType.name)
                    else:
                        if type(check_und[1]) is not Type:
                            raise TypeMismatch(rootAST)
                    ast.varType = check_und[0].mtype
                elif type(ast.varType) is ArrayType:
                    ast.varType = self.visit(ast.varType, c)

                if len(c['env']) > 1:
                    return {
                        'env': [[(Symbol(ast.varName, ast.varType, self.DefaultVal(ast.varType, c)), Variable())] + c['env'][0]] + c['env'][1:],
                        'globScan': c['globScan'],
                        'inExpr': False
                    }
                else:
                    c['env'][0].insert(len(c['env'][0]) - 13 - self.VarConstDeclIdx[self.globIdx], (Symbol(ast.varName, ast.varType, self.DefaultVal(ast.varType, c)), Variable()))
                    self.globIdx = self.globIdx + 1
                    return c

    def visitConstDecl(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        if c['globScan']:
            return c
        else:
            res = None
            if len(c['env']) > 1:
                res = self.lookup(ast.conName, c['env'][0])
                if res is not None:
                    raise Redeclared(Constant(), ast.conName)
            else:
                l = len(c['env'][0]) - 13
                res = self.lookup(ast.conName, c['env'][0][l - self.VarConstDeclIdx[self.globIdx]:])
                if res is not None:
                    raise Redeclared(Constant(), ast.conName)
                else:
                    res = self.lookup(ast.conName, c['env'][0][0:l - self.VarConstDeclIdx[self.globIdx]])
                    if res is not None:
                        raise Redeclared(res[1], ast.conName)
                    
            c['inExpr'] = True
            val = self.visit(ast.iniExpr, c) # visit an Expression should return a literal or a tuple(Symbol, Kind).
            c['inExpr'] = False
            expr = None
            if type(val) is tuple:
                if type(val[1]) is not Constant:
                    raise TypeMismatch(rootAST)
                expr = val[0].mtype
                # print("Check id of val.value 1: ", id(val[0].value))
                val = val[0].value
                if not val:
                    raise TypeMismatch(rootAST)
                # print("Check id of val.value 2: ", id(val))
            else:
                expr = self.TypeOfLit(val, c)

            if type(expr) is ArrayType or type(expr) is StructType:
                raise TypeMismatch(rootAST)

            if len(c['env']) > 1:
                return {
                    'env': [[(Symbol(ast.conName, expr, val), Constant())] + c['env'][0]] + c['env'][1:],
                    'globScan': c['globScan'],
                    'inExpr': False
                }
            else:
                c['env'][0].insert(len(c['env'][0]) - 13 - self.VarConstDeclIdx[self.globIdx], (Symbol(ast.conName, expr, val), Constant()))
                self.globIdx = self.globIdx + 1
                return c
   
    def visitFuncDecl(self, ast, c):
        self.fetchEnv(ast, c)

        rootAST = copy.deepcopy(ast)

        if c['globScan']:
            res = self.lookup(ast.name, c['env'][0])
            if res is not None:
                raise Redeclared(Function(), ast.name)
            else:
                for param in ast.params:
                    check_red = list(filter(lambda x: x.parName == param.parName, ast.params))
                    if (len(check_red) > 1):
                        raise Redeclared(Parameter(), param.parName)
                    if type(param.parType) is Id:
                        check_und = self.lookup(param.parType.name, c['env'][-1])
                        if check_und is None:
                            raise Undeclared(Identifier(), param.parType.name)
                        else:
                            if type(check_und[1]) is not Type:
                                raise TypeMismatch(rootAST)
                        param.parType = check_und[0].mtype
                    elif type(param.parType) is ArrayType:
                        param.parType = self.visit(param.parType, c)
                
                if type(ast.retType) is Id:
                    check_und = self.lookup(ast.retType.name, c['env'][-1])
                    if check_und is None:
                        raise Undeclared(Identifier(), ast.retType.name)
                    else:
                        if type(check_und[1]) is not Type:
                            raise TypeMismatch(rootAST) 
                    ast.retType = check_und[0].mtype
                elif type(ast.retType) is ArrayType:
                    ast.retType = self.visit(ast.retType, c)

                return {
                    'env': [[(Symbol(ast.name, MType([param.parType for param in ast.params], ast.retType)), Function())] + c['env'][0]] + c['env'][1:],
                    'globScan': c['globScan'],
                    'inExpr': c['inExpr']
                }
        else:
            paramSymbols = []
            for param in ast.params:
                paramSymbols = [(Symbol(param.parName, param.parType, self.DefaultVal(param.parType, c)), Parameter())] + paramSymbols
            
            func_env = {
                'env': [[], paramSymbols] + c['env'],
                'globScan': c['globScan'],
                'inExpr': c['inExpr']
            }

            for stmt in ast.body.member:
                func_env = self.visit(stmt, func_env)
            func_env['env'] = func_env['env'][2:]
            self.funcIdx += 1
            return c


    def visitMethodDecl(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        if c['globScan']:
            rec = self.lookup(ast.recType.name, c['env'][-1])
            if rec is None:
                raise Undeclared(Identifier(), ast.recType.name)
            else:
                if type(rec[0].mtype) is not StructType:
                    raise TypeMismatch(rootAST)

                rec = rec[0]
                res = next(filter(lambda x: x.fun.name == ast.fun.name, rec.mtype.methods), None)
                if res is not None:
                    raise Redeclared(Method(), ast.fun.name)
                else:
                    res = next(filter(lambda x: x[0] == ast.fun.name, rec.mtype.elements), None)
                    if res is not None:
                        raise Redeclared(Method(), ast.fun.name)
                    self.visit(ast.fun, c)
                    rec.mtype.methods = [ast] + rec.mtype.methods
                return c
        else:
            paramSymbols = []
            for param in ast.fun.params:
                paramSymbols = [(Symbol(param.parName, param.parType,  self.DefaultVal(param.parType, c)), Parameter())] + paramSymbols
            
            rec = self.lookup(ast.recType.name, c['env'][-1])[0]

            func_env = {
                'env': [[], paramSymbols, [(Symbol(ast.receiver, rec.mtype, self.DefaultVal(rec.mtype, c)), Parameter())]] + c['env'],
                'globScan': c['globScan'],
                'inExpr': c['inExpr']
            }

            for stmt in ast.fun.body.member:
                func_env = self.visit(stmt, func_env)
            func_env['env'] = func_env['env'][3:]
            self.funcIdx += 1
            return c

    def visitPrototype(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        for param in ast.params:
            if type(param) is Id:
                check_und = self.lookup(param.name, c['env'][-1])
                if check_und is None:
                    raise Undeclared(Identifier(), param.name)
                else:
                    if type(check_und[1]) is not Type:
                        raise TypeMismatch(rootAST)
                param = check_und[0].mtype
            elif type(param) is ArrayType:
                param = self.visit(param, c)

        if type(ast.retType) is Id:
            check_und = self.lookup(ast.retType.name, c['env'][-1])
            if check_und is None:
                raise Undeclared(Identifier(), ast.retType.name)
            else:
                if type(check_und[1]) is not Type:
                    raise TypeMismatch(rootAST)
            ast.retType = check_und[0].mtype
        elif type(ast.retType) is ArrayType:
            ast.retType = self.visit(ast.retType, c)

        return ast
    
    def visitIntType(self, ast, c):
        return ast
    
    def visitFloatType(self, ast, c):
        return ast
    
    def visitBoolType(self, ast, c):
        return ast
    
    def visitStringType(self, ast, c):
        return ast
    
    def visitVoidType(self, ast, c):
        return ast
    
    def visitArrayType(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        c['inExpr'] = True

        for i in range(len(ast.dimens)):
            if type(ast.dimens[i]) is Id:
                check_und = next(iter([self.lookup(ast.dimens[i].name, c) for c in c['env']]), None)
                if check_und is None:
                    raise Undeclared(Identifier(), ast.dimens[i].name)
                else:
                    if type(check_und[1]) is not Constant or type(check_und[0].mtype) is not IntType:
                        raise TypeMismatch(rootAST)
                    ast.dimens[i] = check_und[0].value
            elif type(self.TypeOfLit(ast.dimens[i], c)) is not IntType:
                raise TypeMismatch(rootAST)

        if type(ast.eleType) is Id:
            check_und = self.lookup(ast.eleType.name, c['env'][-1])
            if check_und is None:
                raise Undeclared(Identifier(), ast.eleType.name)
            else:
                if type(check_und[0].mtype) is not StructType:
                    raise TypeMismatch(rootAST)
            ast.eleType = check_und[0].mtype

        c['inExpr'] = False
        return ast
    
    def visitStructType(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        if c['globScan']:
            res = self.lookup(ast.name, c['env'][0])
            if res is not None:
                raise Redeclared(Type(), ast.name)
            else:
                return {
                    'env': [[(Symbol(ast.name, ast), Type())] + c['env'][0]] + c['env'][1:],
                    'globScan': c['globScan'],
                    'inExpr': c['inExpr']
                }
        else:
            res = self.lookup(ast.name, c['env'][0])[0]
            
            elements = []

            for ele in res.mtype.elements:
                check_red = list(filter(lambda x: x[0] == ele[0], res.mtype.elements))

                if len(check_red) > 1:
                    raise Redeclared(Field(), ele[0])
                
                if type(ele[1]) is ArrayType:
                    e = ele[1]
                    e = self.visit(e, c)
                    elements.append((ele[0], e))
                elif type(ele[1]) is Id:
                    check_und = self.lookup(ele[1].name, c['env'][-1])
                    if check_und is None:
                        raise Undeclared(Identifier(), ele[1].name)
                    else:
                        if type(check_und[1]) is not Type:
                            raise TypeMismatch(rootAST)
                    elements.append((ele[0], check_und[0].mtype))
                else:
                    elements.append((ele[0], ele[1]))

            res.mtype.elements = elements
            
            c['inExpr'] = False
            return c
                    
    def visitInterfaceType(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        if c['globScan']:
            res = self.lookup(ast.name, c['env'][0])
            if res is not None:
                raise Redeclared(Type(), ast.name)
            else:
                return {
                    'env': [[(Symbol(ast.name, ast), Type())] + c['env'][0]] + c['env'][1:],
                    'globScan': c['globScan'],
                    'inExpr': c['inExpr']
                }
        else:
            res = self.lookup(ast.name, c['env'][0])[0]

            for pro in res.mtype.methods:
                check_red = list(filter(lambda x: x.name == pro.name, res.mtype.methods))
                if len(check_red) > 1:
                    raise Redeclared(Prototype(), pro.name)
                
                pro = self.visit(pro, c)

            return c

    
    def visitBlock(self, ast, c):
        pass
 
    def visitAssign(self, ast, c):
        self.fetchEnv(ast, c)

        rootAST = copy.deepcopy(ast)

        rootL = copy.deepcopy(ast.lhs)

        if type(ast.lhs) is Id:
            check_und = next(iter([self.lookup(ast.lhs.name, env) for env in c['env']]), None)
            if check_und is None:
                c['inExpr'] = True
                rhs = self.visit(ast.rhs, c)
                c['inExpr'] = False
                
                if type(rhs) is tuple:
                    if type(rhs[1]) is Type or type(rhs[1]) is Function:
                        raise TypeMismatch(rootAST)
                    else:
                        c['env'][0] = [(Symbol(ast.lhs.name, rhs[0].mtype, rhs[0].value), Variable())] + c['env'][0]
                else:
                    rhsType = self.TypeOfLit(rhs, c)
                    c['env'][0] = [(Symbol(ast.lhs.name, rhsType, rhs), Variable())] + c['env'][0]
            else:
                if type(check_und[1]) is not Variable and type(check_und[1]) is not Parameter:
                    raise TypeMismatch(rootAST)
                else:
                    c['inExpr'] = True
                    rhs = self.visit(ast.rhs, c)
                    c['inExpr'] = False

                    if type(rhs) is tuple:
                        if type(rhs[1]) is Type or type(rhs[1]) is Function:
                            raise TypeMismatch(rootAST)
                        else:
                            if not self.MatchType(check_und[0].mtype, rhs[0].mtype, c):
                                raise TypeMismatch(rootAST)
                            else:
                                check_und[0].value = rhs[0].value
                    else:
                        rhsType = self.TypeOfLit(rhs, c)
                        if not self.MatchType(check_und[0].mtype, rhsType, c):
                            raise TypeMismatch(rootAST)
                        else:
                            check_und[0].value = rhs
            return c
        else:
            # lhs = self.visit(ast.lhs, c)

            c['inExpr'] = True
            rhs = self.visit(ast.rhs, c)
            c['inExpr'] = False

            rhsType = None

            if type(rhs) is tuple:
                rhsType = rhs[0].mtype
                rhs = rhs[0].value
            else:
                rhsType = self.TypeOfLit(rhs, c)

            if type(ast.lhs) is ArrayCell:
                c['inExpr'] = True
                ast.lhs.arr = self.visit(ast.lhs.arr, c)
                c['inExpr'] = False

                if type(ast.lhs.arr) is not tuple and type(ast.lhs.arr) is not ArrayLiteral:
                    raise TypeMismatch(rootAST)
                else:
                    if type(ast.lhs.arr) is tuple:
                        if type(ast.lhs.arr[0].mtype) is not ArrayType:
                            raise TypeMismatch(rootL)
                        val = ast.lhs.arr[0].value
                        if len(ast.lhs.idx) > len(ast.lhs.arr[0].mtype.dimens):
                            raise TypeMismatch(rootL)
                        
                        for i in range(len(ast.lhs.idx)):
                            c['inExpr'] = True
                            ast.lhs.idx[i] = self.visit(ast.lhs.idx[i], c)
                            if type(ast.lhs.idx[i]) is tuple:
                                if type(ast.lhs.idx[i][0].mtype) is not IntType:
                                    raise TypeMismatch(rootL)
                                ast.lhs.idx[i] = ast.lhs.idx[i][0].value
                            else:
                                if type(self.TypeOfLit(ast.lhs.idx[i], c)) is not IntType:
                                    raise TypeMismatch(rootL)
                            c['inExpr'] = False

                        idxList = [a.value for a in ast.lhs.idx]
                        val = ast.lhs.arr[0].value
                        for i in range(len(idxList) - 1):
                            if idxList[i] < 0 or idxList[i] >= ast.lhs.arr[0].mtype.dimens[i].value:
                                raise TypeMismatch(rootL)
                            val = val[idxList[i]]

                        if idxList[len(idxList) - 1] < 0 or idxList[len(idxList) - 1] >= ast.lhs.arr[0].mtype.dimens[len(idxList) - 1].value:
                            raise TypeMismatch(rootL)

                        lhsType = None
                        if type(val[idxList[len(idxList) - 1]]) is list:
                            lhsType = ArrayType(ast.lhs.arr[0].mtype.dimens[len(idxList):], ast.lhs.arr[0].mtype.eleType)
                            if not self.MatchType(lhsType, rhsType, c):
                                raise TypeMismatch(rootAST)
                            val[idxList[len(idxList) - 1]] = rhs.value
                        else:
                            if not self.MatchType(self.TypeOfLit(val[idxList[len(idxList) - 1]], c), rhsType, c):
                                raise TypeMismatch(rootAST)
                            val[idxList[len(idxList) - 1]] = FloatLiteral(float(rhs.value)) if type(self.TypeOfLit(val[idxList[len(idxList) - 1]], c)) is FloatType and type(rhsType) is IntType else rhs
                    else:
                        val = ast.lhs.arr.value
                        if len(ast.lhs.idx) > len(ast.lhs.arr.dimens):
                            raise TypeMismatch(rootL)
                        
                        for i in range(len(ast.lhs.idx)):
                            c['inExpr'] = True
                            ast.lhs.idx[i] = self.visit(ast.lhs.idx[i], c)
                            if type(ast.lhs.idx[i]) is tuple:
                                if type(ast.lhs.idx[i][0].mtype) is not IntType:
                                    raise TypeMismatch(rootL)
                                ast.lhs.idx[i] = ast.lhs.idx[i][0].value
                            else:
                                if type(self.TypeOfLit(ast.lhs.idx[i], c)) is not IntType:
                                    raise TypeMismatch(rootL)
                            c['inExpr'] = False

                        idxList = [a.value for a in ast.lhs.idx]
                        val = ast.lhs.arr.value
                        for i in range(len(idxList) - 1):
                            if idxList[i] < 0 or idxList[i] >= ast.lhs.arr.dimens[i].value:
                                raise TypeMismatch(rootL)
                            val = val[idxList[i]]

                        if idxList[len(idxList) - 1] < 0 or idxList[len(idxList) - 1] >= ast.lhs.arr.dimens[len(idxList) - 1].value:
                            raise TypeMismatch(rootL)

                        idx = idxList[len(idxList) - 1]

                        lhsType = None
                        if type(val[idx]) is list:
                            lhsType = ArrayType(ast.lhs.arr.dimens[len(idxList):], ast.lhs.arr.eleType)
                            if not self.MatchType(lhsType, rhsType, c):
                                raise TypeMismatch(rootAST)
                            val[idx] = rhs.value
                        else:
                            if not self.MatchType(self.TypeOfLit(val[idx], c), rhsType, c):
                                raise TypeMismatch(rootAST)
                            val[idx] = FloatLiteral(float(rhs.value)) if type(self.TypeOfLit(val[idx], c)) is FloatType and type(rhsType) is IntType else rhs
            elif type(ast.lhs) is FieldAccess:
                c['inExpr'] = True
                ast.lhs.receiver = self.visit(ast.lhs.receiver, c)
                c['inExpr'] = False

                val = None

                if type(ast.lhs.receiver) is not tuple:
                    raise TypeMismatch(rootAST)
                else:
                    if type(ast.lhs.receiver[1]) is not Variable and type(ast.lhs.receiver[1]) is not Constant and type(ast.lhs.receiver[1]) is not Parameter or type(ast.lhs.receiver[0].mtype) is not StructType:
                        raise TypeMismatch(rootL)
                    else:
                        check = next(filter(lambda x: x[0] == ast.lhs.field, ast.lhs.receiver[0].value.elements), None)
                        if check is None:
                            raise Undeclared(Field(), ast.field)
                    
                    fieldType = next(filter(lambda x: x[0] == ast.lhs.field, ast.lhs.receiver[0].mtype.elements), None)[1]
                    if not self.MatchType(fieldType, rhsType, c):
                        raise TypeMismatch(rootAST)
                    
                    check = (check[0], rhs)
            else:
                raise TypeError("Invalid LHS: " + str(ast.lhs))
            
            c['inExpr'] = False
            return c

   
    def visitIf(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        c['inExpr'] = True
        expr = self.visit(ast.expr, c)
        c['inExpr'] = False

        if type(expr) is tuple:
            if type(expr[0].mtype) is not BoolType:
                raise TypeMismatch(rootAST)
        else:
            if type(self.TypeOfLit(expr, c)) is not BoolType:
                raise TypeMismatch(rootAST)
            
            body_env = {
                'env': [[]] + c['env'],
                'globScan': c['globScan'],
                'inExpr': c['inExpr']
            }

            if type(ast.thenStmt) is Block:
                reduce(lambda acc, ele: self.visit(ele, acc), ast.thenStmt.member, body_env)
            elif type(ast.thenStmt) is Stmt:
                body_env = self.visit(ast.thenStmt, body_env)

            if ast.elseStmt:
                body_env = {
                    'env': [[]] + c['env'],
                    'globScan': c['globScan'],
                    'inExpr': c['inExpr']
                }
                if type(ast.elseStmt) is Block:
                    reduce(lambda acc, ele: self.visit(ele, acc), ast.elseStmt.member, body_env)
                else:
                    body_env = self.visit(ast.elseStmt, body_env)

        return c
    
    def visitForBasic(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        c['inExpr'] = True
    
        cond = self.visit(ast.cond, c)

        if type(cond) is tuple:
            if type(cond[0].mtype) is not BoolType:
                raise TypeMismatch(rootAST)
        else:
            if type(self.TypeOfLit(cond, c)) is not BoolType:
                raise TypeMismatch(rootAST) 

        c['inExpr'] = False

        for_env = {
            'env': [[]] + c['env'],
            'globScan': c['globScan'],
            'inExpr': c['inExpr']
        }

        for stmt in ast.loop.member:
            for_env = self.visit(stmt, for_env)

        for_env['env'] = for_env['env'][1:]
        return for_env
 
    def visitForStep(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        for_env = {
            'env': [[]] + c['env'],
            'globScan': c['globScan'],
            'inExpr': c['inExpr'],
        }

        for_env = self.visit(ast.init, for_env)

        for_env['inExpr'] = True

        cond = self.visit(ast.cond, for_env)
        
        if type(cond) is tuple:
            if type(cond[0].mtype) is not BoolType:
                raise TypeMismatch(rootAST)
        else:
            if type(self.TypeOfLit(cond, for_env)) is not BoolType:
                raise TypeMismatch(rootAST)

        for_env['inExpr'] = False

        self.visit(ast.upda, copy.deepcopy(for_env))

        for stmt in ast.loop.member:
            for_env = self.visit(stmt, for_env)

        for_env['env'] = for_env['env'][1:]

        return for_env


    def visitForEach(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        idx = self.visit(ast.idx, c)
        val = self.visit(ast.value, c)

        if type(idx[0].mtype) is not IntType:
            raise TypeMismatch(rootAST)
        
        if type(val[1]) is Type or type(val[1]) is Function:
            raise TypeMismatch(rootAST)
        valType = val[0].mtype        

        c['inExpr'] = True

        arr = self.visit(ast.arr, c)

        c['inExpr'] = False

        if type(arr) is tuple:
            if type(arr[0].mtype) is not ArrayType:
                raise TypeMismatch(rootAST)
            if type(arr[0].mtype.eleType) is not type(valType):
                raise TypeMismatch(rootAST)
            
            val[0].value = arr[0].value.value[0] if len(arr[0].value.dimens) > 0 else None
        else:
            if type(arr.eleType) is not type(valType):
                raise TypeMismatch(rootAST)
            val[0].value = arr.value[0] if len(arr.dimens) > 0 else None

        idx[0].value = IntLiteral(0)

        for_env = {
            'env': [[]] + c['env'],
            'globScan': c['globScan'],
            'inExpr': c['inExpr']
        }

        for stmt in ast.loop.member:
            for_env = self.visit(stmt, for_env)

        for_env['env'] = for_env['env'][1:]

        return for_env

    def visitContinue(self, ast, c):
        pass
    
    def visitBreak(self, ast, c):
        pass
    
    def visitReturn(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        func = copy.deepcopy(self.decls[self.FuncMethodIdx[self.funcIdx]])

        if type(func) is FuncDecl:
            if type(func.retType) is VoidType:
                if ast.expr is not None:
                    raise TypeMismatch(rootAST)
                return c
            else:
                if ast.expr is None:
                    raise TypeMismatch(rootAST)
                
                c['inExpr'] = True
                expr = self.visit(ast.expr, c)
                c['inExpr'] = False
                exprType = None

                func.retType = self.visit(func.retType, c)

                if type(func.retType) is tuple:
                    func.retType = func.retType[0].mtype

                if type(expr) is tuple:
                    if type(expr[1]) is Type or type(expr[1]) is Function:
                        raise TypeMismatch(rootAST)
                    
                    exprType = expr[0].mtype
                    expr = expr[0].value
                else:
                    exprType = self.TypeOfLit(expr, c)

                # print("EXPR: ", expr)
                # print("FUNCTYPE: ", func.retType)
                # print("RTYPE: ", exprType)

                if type(func.retType) is not type(exprType):
                    raise TypeMismatch(rootAST)
                
                return c
        elif type(func) is MethodDecl:
            func = func.fun
            if type(func.retType) is VoidType:
                if ast.expr is not None:
                    raise TypeMismatch(rootAST)
                return c
            else:
                if ast.expr is None:
                    raise TypeMismatch(rootAST)
                
                c['inExpr'] = True
                expr = self.visit(ast.expr, c)
                c['inExpr'] = False
                exprType = None

                func.retType = self.visit(func.retType, c)

                if type(func.retType) is tuple:
                    func.retType = func.retType[0].mtype

                if type(expr) is tuple:
                    if type(expr[1]) is Type or type(expr[1]) is Function:
                        raise TypeMismatch(rootAST)
                    
                    exprType = expr[0].mtype
                    expr = expr[0].value
                else:
                    exprType = self.TypeOfLit(expr, c)

                # print("EXPR: ", expr)
                # print("FUNCTYPE: ", func.retType)
                # print("RTYPE: ", exprType)

                if type(func.retType) is not type(exprType):
                    raise TypeMismatch(rootAST)
                
            return c
        else:
            raise TypeError("Invalid Return: Function not found\n")


    def visitBinaryOp(self, ast, c):
        self.fetchEnv(ast, c)

        rootAST = copy.deepcopy(ast)

        c['inExpr'] = True

        left = self.visit(ast.left, c)
        lType = None

        c['inExpr'] = True

        right = self.visit(ast.right, c)
        rType = None

        c['inExpr'] = False

        if type(left) is tuple:
            if type(left[1]) is Type or type(left[1]) is Function:
                raise TypeMismatch(rootAST)
            else:
                lType = left[0].mtype
                left = left[0].value
        else:
            lType = self.TypeOfLit(left, c)

        if type(right) is tuple:
            if type(right[1]) is Type or type(right[1]) is Function:
                raise TypeMismatch(rootAST)
            else:
                rType = right[0].mtype
                right = right[0].value
        else:
            rType = self.TypeOfLit(right, c)

        if ast.op in ['+', '-', '*', '/', '%']:
            if ast.op == '+':
                if type(lType) is StringType:
                    if type(rType) is not StringType:
                        raise TypeMismatch(rootAST)
                    else:
                        return StringLiteral(left.value + right.value)
                elif type(lType) is IntType:
                    if type(rType) is IntType:
                        return IntLiteral(left.value + right.value)
                    elif type(rType) is FloatType:
                        return FloatLiteral(float(left.value) + right.value)
                    else:
                        raise TypeMismatch(rootAST)
                elif type(lType) is FloatType:
                    if type(rType) is IntType:
                        return FloatLiteral(left.value + float(right.value))
                    elif type(rType) is FloatType:
                        return FloatLiteral(left.value + right.value)
                    else:
                        raise TypeMismatch(rootAST)
                else:
                    raise TypeMismatch(rootAST)
            elif ast.op in ['-', '*']:
                if type(lType) is IntType:
                    if type(rType) is IntType:
                        return IntLiteral(self.BinOp(left.value, ast.op, right.value))
                    elif type(rType) is FloatType:
                        return FloatLiteral(self.BinOp(float(left.value), ast.op, right.value))
                    else:
                        raise TypeMismatch(rootAST)
                elif type(lType) is FloatType:
                    if type(rType) is IntType:
                        return FloatLiteral(self.BinOp(left.value, ast.op, float(right.value)))
                    elif type(rType) is FloatType:
                        return FloatLiteral(self.BinOp(left.value, ast.op, right.value))
                    else:
                        raise TypeMismatch(rootAST)
                else:
                    raise TypeMismatch(rootAST)
            elif ast.op == '/':
                if type(lType) is IntType:
                    if type(rType) is IntType:
                        return IntLiteral(int(left.value / right.value)) if right.value != 0 else IntLiteral(int(left.value))
                    elif type(rType) is FloatType:
                        return FloatLiteral(float(left.value) / right.value) if right.value != 0 else FloatLiteral(float(left.value))
                    else:
                        raise TypeMismatch(rootAST)
                elif type(lType) is FloatType:
                    if type(rType) is IntType:
                        return FloatLiteral(left.value / float(right.value)) if right.value != 0 else FloatLiteral(float(left.value))
                    elif type(rType) is FloatType:
                        return FloatLiteral(left.value / right.value) if right.value != 0 else FloatLiteral(float(left.value))
                    else:
                        raise TypeMismatch(rootAST)
                else:
                    raise TypeMismatch(rootAST)
            elif ast.op =='%':
                if type(lType) is not IntType or type(rType) is not IntType:
                    raise TypeMismatch(rootAST)
                else:
                    return IntLiteral(self.BinOp(left.value, ast.op, right.value)) if right.value != 0 else IntLiteral(0)
            else:
                raise TypeError("Invalid operator for BinaryOp")
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            if type(lType) is StringType:
                if type(rType) is not StringType:
                    raise TypeMismatch(rootAST)
                else:
                    return BooleanLiteral(self.BinOp(left.value, ast.op, right.value))
            elif type(lType) is IntType:
                if type(rType) is not IntType:
                    raise TypeMismatch(rootAST)
                else:
                    return BooleanLiteral(self.BinOp(left.value, ast.op, right.value))
            elif type(lType) is FloatType:
                if type(rType) is not FloatType:
                    raise TypeMismatch(rootAST)
                else:
                    return BooleanLiteral(self.BinOp(left.value, ast.op, right.value))
            else:
                raise TypeMismatch(rootAST)
        elif ast.op in ['&&', '||']:
            if type(lType) is not BoolType or type(rType) is not BoolType:
                raise TypeMismatch(rootAST)
            
            return BooleanLiteral(self.BinOp(left.value, ast.op, right.value))
        else:
            raise TypeError("Invalid operator for BinaryOp")
    
    def visitUnaryOp(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        c['inExpr'] = True

        ex = self.visit(ast.body, c)
        exType = None

        c['inExpr'] = False

        if type(ex) is tuple:
            if type(ex[1]) is Type or type(ex[1]) is Function:
                raise TypeMismatch(rootAST)
            exType = ex[0].mtype
            ex = ex[0].value
        else:
            exType = self.TypeOfLit(ex, c)

        if ast.op == '!':
            if type(exType) is not BoolType:
                raise TypeMismatch(rootAST)
            return BooleanLiteral(not ex.value)
        elif ast.op == '-':
            if type(exType) is IntType:
                return IntLiteral(ex.value * -1)
            elif type(exType) is FloatType:
                return FloatLiteral(float(ex.value * -1))
            else:
                raise TypeMismatch(rootAST)
    
    def visitFuncCall(self, ast, c):
        self.fetchEnv(ast, c)

        rootAST = copy.deepcopy(ast)

        func = next(filter(lambda y: y is not None, [next(filter(lambda x: type(x[1]) is Function and x[0].name == ast.funName, env), None) for env in c['env']]), None)

        if func is None:
            raise Undeclared(Function(), ast.funName)

        if c['inExpr']:
            if type(func[0].mtype.rettype) is VoidType:
                raise TypeMismatch(rootAST)
            
            c['inExpr'] = True

            argTypes = []

            for i in range(len(ast.args)):
                ast.args[i] = self.visit(ast.args[i], c)
                if type(ast.args[i]) is tuple:
                    argTypes.append(ast.args[i][0].mtype)
                else:
                    argTypes.append(self.TypeOfLit(ast.args[i], c))

            c['inExpr'] = False

            if len(argTypes) != len(func[0].mtype.partype):
                raise TypeMismatch(rootAST)
            else:
                for i in range(len(argTypes)):
                    if type(argTypes[i]) is not type(func[0].mtype.partype[i]):
                        raise TypeMismatch(rootAST)

            return self.DefaultVal(func[0].mtype.rettype, c)
        else:
            if type(func[0].mtype.rettype) is not VoidType:
                raise TypeMismatch(rootAST)
            
            c['inExpr'] = True

            argTypes = []

            for i in range(len(ast.args)):
                ast.args[i] = self.visit(ast.args[i], c)
                if type(ast.args[i]) is tuple:
                    argTypes.append(ast.args[i][0].mtype)
                else:
                    argTypes.append(self.TypeOfLit(ast.args[i], c))

            c['inExpr'] = False

            if len(argTypes) != len(func[0].mtype.partype):
                raise TypeMismatch(rootAST)
            else:
                for i in range(len(argTypes)):
                    if type(argTypes[i]) is not type(func[0].mtype.partype[i]):
                        raise TypeMismatch(rootAST)

            return c

    def visitMethCall(self, ast, c):
        self.fetchEnv(ast, c)

        rootAST = copy.deepcopy(ast)

        if c['inExpr']:
            c['inExpr'] = True

            rei = self.visit(ast.receiver, c)
            methods = None

            c['inExpr'] = False

            if type(rei) is tuple:
                if type(rei[0].mtype) is not StructType and type(rei[0].mtype) is not InterfaceType:
                    raise TypeMismatch(rootAST)
                else:
                    methods = rei[0].mtype.methods
            else:
                if type(rei) is not StructLiteral:
                    raise TypeMismatch(rootAST)
                methods = rei.methods

            method = next(filter(lambda x: x.name == ast.metName if type(x) is AST.Prototype else x.fun.name == ast.metName, methods), None)
            if method is None:
                raise Undeclared(Method(), ast.metName)
            else:
                retType = method.retType if type(method) is AST.Prototype else method.fun.retType
                if type(retType) is VoidType:
                    raise TypeMismatch(rootAST)
                params = method.params if type(method) is AST.Prototype else [t.parType for t in method.fun.params]

                args = []
                for arg in ast.args:
                    c['inExpr'] = True

                    arg = self.visit(arg, c)

                    if type(arg) is tuple:
                        if type(arg[1]) is Type or type(arg[1]) is Function:
                            raise TypeMismatch(rootAST)
                        args.append(arg[0].mtype)
                    else:
                        args.append(self.TypeOfLit(arg, c))

                    c['inExpr'] = False

                if len(args) != len(params):
                    raise TypeMismatch(rootAST)
                else:
                    for i in range(len(args)):
                        if type(args[i]) is not type(params[i]):
                            raise TypeMismatch(rootAST)
                
            return self.DefaultVal(retType, c)
        else:
            c['inExpr'] = True

            rei = self.visit(ast.receiver, c)
            methods = None

            c['inExpr'] = False

            if type(rei) is tuple:
                if type(rei[0].mtype) is not StructType and type(rei[0].mtype) is not InterfaceType:
                    raise TypeMismatch(rootAST)
                else:
                    methods = rei[0].mtype.methods
            else:
                if type(rei) is not StructLiteral:
                    raise TypeMismatch(rootAST)
                methods = rei.methods

            if len(methods) == 0:
                raise Undeclared(Method(), ast.metName)

            # print("METHODS: ", str(methods[0]))

            method = None

            if type(methods[0]) is AST.Prototype:
                method = next(filter(lambda x: x.name == ast.metName, methods), None)
            else:
                method = next(filter(lambda x: x.fun.name == ast.metName, methods), None)

            if method is None:
                raise Undeclared(Method(), ast.metName)
            else:
                retType = method.retType if type(method) is AST.Prototype else method.fun.retType
                if type(retType) is not VoidType:
                    raise TypeMismatch(rootAST)
                params = method.params if type(method) is AST.Prototype else [t.parType for t in method.fun.params]

                args = []
                for arg in ast.args:
                    c['inExpr'] = True

                    arg = self.visit(arg, c)

                    if type(arg) is tuple:
                        if type(arg[1]) is Type or type(arg[1]) is Function:
                            raise TypeMismatch(rootAST)
                        args.append(arg[0].mtype)
                    else:
                        args.append(self.TypeOfLit(arg, c))

                    c['inExpr'] = False

                if len(args) != len(params):
                    raise TypeMismatch(rootAST)
                else:
                    for i in range(len(args)):
                        if type(args[i]) is not type(params[i]):
                            raise TypeMismatch(rootAST)
                
            return c
    
    def visitId(self, ast, c):
        self.fetchEnv(ast, c)

        # rootAST = copy.deepcopy(ast)

        check_und = next(filter(lambda x: x is not None, [self.lookup(ast.name, env) for env in c['env']]), None)
        if check_und is None:
            raise Undeclared(Identifier(), ast.name)
        return check_und
    
    def visitArrayCell(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        c['inExpr'] = True
        ast.arr = self.visit(ast.arr, c)
        c['inExpr'] = False

        dimens = []
        val = None
        if type(ast.arr) is tuple:
            if type(ast.arr[0].mtype) is not ArrayType:
                raise TypeMismatch(rootAST)
            dimens = ast.arr[0].mtype.dimens
            val = ast.arr[0].value.value
        elif type(self.TypeOfLit(ast.arr, c)) is not ArrayType:
            raise TypeMismatch(rootAST)
        else:
            dimens = ast.arr.dimens
            val = ast.arr.value
        
        for i in range(len(ast.idx)):

            c['inExpr'] = True

            ast.idx[i] = self.visit(ast.idx[i], c)

            c['inExpr'] = False

            if type(ast.idx[i]) is tuple:
                if type(ast.idx[i][0].mtype) is not IntType:
                    raise TypeMismatch(rootAST)
                else:
                    ast.idx[i] = ast.idx[i][0].value
            else:
                iType = self.TypeOfLit(ast.idx[i], c)
                if type(iType) is not IntType:
                    raise TypeMismatch(rootAST)

        idxList = [i.value for i in ast.idx]
        dimens = [i.value for i in dimens]

        for i in range(len(idxList)):
            if idxList[i] < 0 or idxList[i] >= dimens[i]:
                raise TypeMismatch(rootAST)
            val = val[idxList[i]]

        c['inExpr'] = False
        return val
    
    def visitFieldAccess(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        c['inExpr'] = True
        receiver = self.visit(ast.receiver, c)
        c['inExpr'] = False

        val = None

        if type(receiver) is tuple:
            if type(receiver[1]) is not Variable and type(receiver[1]) is not Constant and type(receiver[1]) is not Parameter:
                raise TypeMismatch(rootAST)
            else:
                if type(receiver[0].mtype) is not StructType:
                    raise TypeMismatch(rootAST)
                elements = None
                if type(receiver[1]) is Parameter:
                    elements = self.DefaultVal(receiver[0].mtype, c).elements
                else:
                    elements = receiver[0].value.elements
                check = next(filter(lambda x: x[0] == ast.field, elements), None)
                if check is None:
                    raise Undeclared(Field(), ast.field)
                val = check[1]
        else:
            check = next(filter(lambda x: x[0] == ast.field, receiver.elements), None)
            if check is None:
                raise Undeclared(Field(), ast.field)
            val = check[1]

        return val
                

    def visitIntLiteral(self, ast, c):
        return ast
    
    def visitFloatLiteral(self, ast, c):
        return ast
    
    def visitBooleanLiteral(self, ast, c):
        return ast
    
    def visitStringLiteral(self, ast, c):
        return ast

    def visitArrayLiteral(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        c['inExpr'] = True

        for i in range(len(ast.dimens)):
            if type(ast.dimens[i]) is Id:
                check_und = next(iter([self.lookup(ast.dimens[i].name, c) for c in c['env']]), None)
                if check_und is None:
                    raise Undeclared(Identifier(), ast.dimens[i].name)
                else:
                    if type(check_und[1]) is not Constant or type(check_und[0].mtype) is not IntType:
                        raise TypeMismatch(rootAST)
                    ast.dimens[i] = check_und[0].value
            elif type(self.TypeOfLit(ast.dimens[i], c)) is not IntType:
                raise TypeMismatch(rootAST)

        if type(ast.eleType) is Id:
            check_und = self.lookup(ast.eleType.name, c['env'][-1])
            if check_und is None:
                raise Undeclared(Identifier(), ast.eleType.name)
            else:
                if type(check_und[0].mtype) is not StructType:
                    raise TypeMismatch(rootAST)
            ast.eleType = check_und[0].mtype

        # print("Dimension: ", [str(i) for i in ast.dimens])

        ast.value = self.ArrayValueCheck(rootAST, ast, ast.value, ast.dimens, ast.eleType, c)

        c['inExpr'] = False

        return ast

    def visitStructLiteral(self, ast, c):
        self.fetchEnv(ast, c)
        
        rootAST = copy.deepcopy(ast)

        check_und = self.lookup(ast.name, c['env'][-1])
        if check_und is None:
            raise Undeclared(Identifier(), ast.name)
        else:
            if type(check_und[0].mtype) is not StructType:
                raise TypeMismatch(rootAST)
            fields = check_und[0].mtype.elements

            # if len(fields) < len(ast.elements):
            #     raise TypeMismatch(rootAST)
            
            elements = []

            for i in range(len(ast.elements)):
                field = next(filter(lambda x: x[0] == ast.elements[i][0], fields), None)
                if field is None:
                    raise Undeclared(Field(), ast.elements[i][0])
                else:
                    c['inExpr'] = True

                    name = ast.elements[i][0]
                    expr = copy.deepcopy(ast.elements[i][1])
                    expr = self.visit(expr, c)

                    c['inExpr'] = False

                    if type(expr) is tuple:
                        if not self.MatchType(field[1], expr[0].mtype, c):
                            raise TypeMismatch(rootAST)
                    else:
                        t = self.TypeOfLit(expr, c)
                        if not self.MatchType(t, field[1], c):
                            raise TypeMismatch(rootAST)
                        
                    elements.append((name, expr))
                        
            for i in range(len(fields)):
                ele = next(filter(lambda x: x[0] == fields[i][0], ast.elements), None)
                if ele is None:
                    elements = [(fields[i][0], self.DefaultVal(fields[i][1], c))] + elements
            
            ast.elements = elements

            return ast

    def visitNilLiteral(self, ast, c):
        return ast