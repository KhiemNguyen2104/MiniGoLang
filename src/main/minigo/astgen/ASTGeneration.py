from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program([i for i in self.visit(ctx.decllist())])
    
    def visitDecllist(self, ctx: MiniGoParser.DecllistContext):
        if (ctx.getChildCount() == 2):
            return [self.visit(ctx.decl())] + self.visit(ctx.decllist())
        else:
            return [self.visit(ctx.decl())]

    def visitDecl(self, ctx: MiniGoParser.DeclContext):
        if (ctx.const_decl()):
            return self.visit(ctx.const_decl())
        elif (ctx.var_decl()):
            return self.visit(ctx.var_decl())
        elif (ctx.type_decl()):
            return self.visit(ctx.type_decl())
        elif (ctx.func_decl()):
            return self.visit(ctx.func_decl())
        elif (ctx.method_decl()):
            return self.visit(ctx.method_decl())
        else:
            raise SyntaxError("Invalid declaration syntax.")

    def visitConst_decl(self, ctx: MiniGoParser.Const_declContext):
        const_name = ctx.Identifier().getText()
        const_value = self.visit(ctx.var_value())
        
        return ConstDecl(
            const_name,
            None,
            const_value
        )

    def visitEnd_stmt(self, ctx: MiniGoParser.End_stmtContext):
        pass

    def visitVar_decl(self, ctx: MiniGoParser.Var_declContext):
        if (ctx.var_decl_expl()):
            return self.visit(ctx.var_decl_expl())
        elif (ctx.var_decl_infer()):
            return self.visit(ctx.var_decl_infer())
        elif (ctx.var_decl_nil()):
            return self.visit(ctx.var_decl_nil())
        else:
            raise SyntaxError("Invlad variable delcaration syntax.")

    def visitVar_decl_expl(self, ctx: MiniGoParser.Var_decl_explContext):
        var_name = ctx.Identifier().getText()
        var_type = self.visit(ctx.data_type())
        var_value = self.visit(ctx.var_value())

        # print("Variable name: ", var_name)
        # print("Variable type: ", var_type)
        # print("Variable value: ", var_value)

        return VarDecl(
            var_name,
            var_type,
            var_value,
        )

    def visitVar_value(self, ctx: MiniGoParser.Var_valueContext):
        if (ctx.expr()):
            return self.visit(ctx.expr())
        elif (ctx.full_array_literal()):
            return self.visit(ctx.full_array_literal())
        elif (ctx.literal_struct()):
            return self.visit(ctx.literal_struct())
        else:
            raise SyntaxError("Invalid variable value.")

    def visitData_type(self, ctx: MiniGoParser.Data_typeContext):
        if (ctx.primitive_type()):
            return self.visit(ctx.primitive_type())
        elif (ctx.Identifier()):
            return Id(ctx.Identifier().getText())
        elif (ctx.array_type()):
            return self.visit(ctx.array_type())
        else:
            raise SyntaxError("Invalid data type.")

    def visitPrimitive_type(self, ctx: MiniGoParser.Primitive_typeContext):
        if (ctx.Key_type_int()):
            return IntType()
        elif (ctx.Key_type_float()):
            return FloatType()
        elif (ctx.Key_type_boolean()):
            return BoolType()
        elif (ctx.Key_type_string()):
            return StringType()
        else:
            raise SyntaxError("Invalid primitive type.")

    def visitArray_type(self, ctx: MiniGoParser.Array_typeContext):
        dimens = self.visit(ctx.dimension_list())
        ele_type = None
        if (ctx.primitive_type()):
            ele_type = self.visit(ctx.primitive_type())
        elif (ctx.Identifier()):
            ele_type = Id(ctx.Identifier().getText())
        else:
            raise SyntaxError("Invalid array element type.")

        return ArrayType(dimens, ele_type)

    def visitDimension_list(self, ctx: MiniGoParser.Dimension_listContext):
        if (ctx.getChildCount() == 2):
            return [self.visit(ctx.dimension())] + self.visit(ctx.dimension_list())
        elif (ctx.getChildCount() == 1 and ctx.dimension()):
            return [self.visit(ctx.dimension())]
        else:
            raise SyntaxError("Invalid dimension list of an array.")

    def visitDimension(self, ctx: MiniGoParser.DimensionContext):
        return self.visit(ctx.size())

    def visitSize(self, ctx: MiniGoParser.SizeContext):
        if (ctx.Identifier()):
            return Id(ctx.Identifier().getText())
        elif (ctx.getChildCount() == 1):
            return IntLiteral(int(ctx.getChild(0).getText()))
        else:
            raise SyntaxError("Invalid array size.")

    def visitVar_decl_infer(self, ctx: MiniGoParser.Var_decl_inferContext):
        var_name = ctx.Identifier().getText()
        var_type = None
        var_init = self.visit(ctx.var_value())

        # print("Variable name: ", var_name)
        # print("Variable type: ", var_type)
        # print("Variable value: ", var_init)

        return VarDecl(
            var_name,
            var_type,
            var_init
        )

    def visitVar_decl_nil(self, ctx: MiniGoParser.Var_decl_nilContext):
        var_name = ctx.Identifier().getText()
        var_type = self.visit(ctx.data_type())
        var_init = None

        # print("Variable name: ", var_name)
        # print("Variable type: ", var_type)
        # print("Variable value: ", var_init)

        return VarDecl(
            var_name,
            var_type,
            var_init
        )

    def visitType_decl(self, ctx: MiniGoParser.Type_declContext):
        if (ctx.struct_decl()):
            return self.visit(ctx.struct_decl())
        elif (ctx.interface_decl()):
            return self.visit(ctx.interface_decl())
        else:
            raise SyntaxError("Invalid type declaration.")

    def visitStruct_decl(self, ctx: MiniGoParser.Struct_declContext):
        struct_name = ctx.Identifier().getText()
        elements = self.visit(ctx.field_list())

        return StructType(
            struct_name,
            elements,
            [] # Check the comparison with `None`.
        )


    def visitField_set(self, ctx: MiniGoParser.Field_setContext):
        if (ctx.filed_list()):
            return self.visit(ctx.field_list())
        return None

    def visitField_list(self, ctx: MiniGoParser.Field_listContext):
        # print("Field declaration: ", self.visit(ctx.field_decl()))
        if (ctx.getChildCount() == 2):
            return [self.visit(ctx.field_decl())] + self.visit(ctx.field_list())
        elif (ctx.getChildCount() == 1):
           return [self.visit(ctx.field_decl())]
        else:
            raise SyntaxError("Invalid field list declaration.")

    def visitField_decl(self, ctx: MiniGoParser.Field_declContext):
        ele = tuple([ctx.Identifier().getText(), self.visit(ctx.data_type())])
        # print("ID: ", ctx.Identifier().getText())
        # print("Type: ", str(self.visit(ctx.data_type())))
        
        # print("Field: ", (("(" + str(i) + str(j) + ")") for i, j in ele))
        return ele

    def visitInterface_decl(self, ctx: MiniGoParser.Interface_declContext):
        interface_name = ctx.Identifier().getText()
        methods = self.visit(ctx.interface_method_list())

        return InterfaceType(
            interface_name,
            methods
        )

    def visitInterface_method_set(self, ctx: MiniGoParser.Interface_method_setContext):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.interface_method_list())
        else:
            return None

    def visitInterface_method_list(self, ctx: MiniGoParser.Interface_method_listContext):
        if (ctx.getChildCount() == 2):
            return [self.visit(ctx.interface_method_decl())] + self.visit(ctx.interface_method_list())
        elif (ctx.getChildCount() == 1 and ctx.interface_method_decl()):
            return [self.visit(ctx.interface_method_decl())]
        else:
            raise SyntaxError("Invalid interface method delcaration.")

    def visitInterface_method_decl(self, ctx: MiniGoParser.Interface_method_declContext):
        method_name = ctx.Identifier().getText()
        params = self.visit(ctx.interface_method_param_set())
        method_type = None
        if (ctx.data_type()):
            method_type = self.visit(ctx.data_type())
        else:
            method_type = VoidType()
        
        return Prototype(
            method_name,
            params,
            method_type
        )


    def visitInterface_method_param_set(self, ctx: MiniGoParser.Interface_method_param_setContext):
        if (ctx.getChildCount() == 0):
            return []
        else:
            return self.visit(ctx.interface_method_param_list())

    # Each parameter is a list inluding the same elements which are Types
    def visitInterface_method_param_list(self, ctx: MiniGoParser.Interface_method_param_listContext):
        if (ctx.getChildCount() == 3):
            return self.visit(ctx.interface_method_param()) + self.visit(ctx.interface_method_param_list())
        elif (ctx.getChildCount() == 1 and ctx.interface_method_param()):
            return self.visit(ctx.interface_method_param())
        else:
            raise SyntaxError("Invalid interface method parameter set.")

    def visitInterface_method_param(self, ctx: MiniGoParser.Interface_method_paramContext):
        id_list = self.visit(ctx.id_list())
        param_type = self.visit(ctx.data_type())

        params = [param_type] * len(id_list)

        return params

    def visitId_list(self, ctx: MiniGoParser.Id_listContext):
        if (ctx.getChildCount() == 3):
            return [Id(ctx.Identifier().getText())] + self.visit(ctx.id_list())
        elif (ctx.getChildCount() == 1 and ctx.Identifier()):
            return [Id(ctx.Identifier().getText())]
        else:
            raise SyntaxError("Invalid ID list")

    def visitFunc_decl(self, ctx: MiniGoParser.Func_declContext):
        func_name = ctx.Identifier().getText()
        params = self.visit(ctx.param_set())
        func_type = None
        if (ctx.data_type()):
            func_type = self.visit(ctx.data_type())
        else:
            func_type = VoidType()
        func_body = self.visit(ctx.func_body())

        return FuncDecl(
            func_name,
            params,
            func_type,
            func_body
        )


    def visitParam_set(self, ctx: MiniGoParser.Param_setContext):
        if (ctx.getChildCount() == 1):
            # print("Parameter list: ", str(self.visit(ctx.param_list())))
            return self.visit(ctx.param_list())
        elif (ctx.getChildCount() == 0):
            # print("No parameter")
            return []
        else:
            raise SyntaxError("Invalid parameter set")

    # Each function's parameter is a list of objects including name and type.
    def visitParam_list(self, ctx: MiniGoParser.Param_listContext):
        # print("Parameter: ", str(self.visit(ctx.param())))
        if (ctx.getChildCount() == 3):
            return self.visit(ctx.param()) + self.visit(ctx.param_list())
        elif (ctx.getChildCount() == 1 and ctx.param()):
            return self.visit(ctx.param())
        # else:
        #     raise SyntaxError("Invalid parameter list")

    def visitParam(self, ctx: MiniGoParser.ParamContext):
        params = []
        id_list = self.visit(ctx.id_list())
        param_type = self.visit(ctx.data_type())

        # print("ID list: ", str(id_list))
        # print("Type: ", str(param_type))

        for i in range(len(id_list)):
            params = params + [ParamDecl(id_list[i].name, param_type)]

        # print("Parameter: ", str(params))

        return params

    def visitFunc_body(self, ctx: MiniGoParser.Func_bodyContext):
        return self.visit(ctx.stmt_set())

    def visitStmt_set(self, ctx: MiniGoParser.Stmt_setContext):
        # print("Block: ", str(Block(self.visit(ctx.stmt_list()))))
        return Block(self.visit(ctx.stmt_list()))

    def visitStmt_list(self, ctx: MiniGoParser.Stmt_listContext):
        # print("Stmt: ", str(self.visit(ctx.stmt())))
        if (ctx.getChildCount() == 2):
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmt_list())
        elif (ctx.getChildCount() == 1 and ctx.stmt()):
            return [self.visit(ctx.stmt())]
        else:
            raise SyntaxError("Invalid statement list.")

    def visitMethod_decl(self, ctx: MiniGoParser.Method_declContext):
        receiver, rei_type = self.visit(ctx.receiver())

        func_name = ctx.Identifier().getText()
        params = self.visit(ctx.param_set())
        func_type = None
        if (ctx.data_type()):
            func_type = self.visit(ctx.data_type())
        else:
            func_type = VoidType()
        func_body = self.visit(ctx.func_body())

        return MethodDecl(
            receiver,
            rei_type,
            FuncDecl(func_name, params, func_type, func_body)
        )
    
    def visitReceiver(self, ctx: MiniGoParser.ReceiverContext):
        return ctx.Identifier(0).getText(), Id(ctx.Identifier(1).getText())

    def visitExpr(self, ctx: MiniGoParser.ExprContext):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr1())
        else:
            return BinaryOp(
                ctx.Ope_or().getText(),
                self.visit(ctx.expr()),
                self.visit(ctx.expr1())
            )

    def visitExpr1(self, ctx: MiniGoParser.Expr1Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr2())
        else:
            return BinaryOp(
                ctx.Ope_and().getText(),
                self.visit(ctx.expr1()),
                self.visit(ctx.expr2())
            )

    def visitExpr2(self, ctx: MiniGoParser.Expr2Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr3())
        else:
            return BinaryOp(
                self.visit(ctx.ope_relation()),
                self.visit(ctx.expr2()),
                self.visit(ctx.expr3())
            )

    def visitOpe_relation(self, ctx: MiniGoParser.Ope_relationContext):
        return ctx.getChild(0).getText()

    def visitExpr3(self, ctx: MiniGoParser.Expr3Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr4())
        else:
            return BinaryOp(
                ctx.getChild(1).getText(), # Operators are always at the second position.
                self.visit(ctx.expr3()),
                self.visit(ctx.expr4())
            )

    def visitExpr4(self, ctx: MiniGoParser.Expr4Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr5())
        else:
            return BinaryOp(
                ctx.getChild(1).getText(), # Operators are always at the second position.
                self.visit(ctx.expr4()),
                self.visit(ctx.expr5())
            )

    def visitExpr5(self, ctx: MiniGoParser.Expr5Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr6())
        else:
            return UnaryOp(
                ctx.getChild(0).getText(),
                self.visit(ctx.expr5())
            )

    def visitExpr6(self, ctx: MiniGoParser.Expr6Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr7())
        elif (ctx.Lsquare() and ctx.Rsquare()):
            exprs = [self.visit(ctx.expr())]
            visit_node = ctx.expr6()
            while (visit_node.Lsquare() and visit_node.Rsquare()):
                exprs = [self.visit(visit_node.expr())] + exprs
                visit_node = visit_node.expr6()
            return ArrayCell(
                self.visit(visit_node),
                exprs
            )
        else:
            if (ctx.expr8().Identifier()):
                return FieldAccess(
                    self.visit(ctx.expr6()),
                    ctx.expr8().Identifier().getText()
                )
            else:
                func_call = self.visit(ctx.expr8().func_call())
                return MethCall(
                    self.visit(ctx.expr6()),
                    func_call.funName,
                    func_call.args
                )


    def visitExpr7(self, ctx: MiniGoParser.Expr7Context):
        if (ctx.prim_literal()):
            return self.visit(ctx.getChild(0))
        elif (ctx.Identifier()):
            return Id(ctx.Identifier().getText())
        elif (ctx.func_call()):
            return self.visit(ctx.func_call())
        elif (ctx.expr()):
            return self.visit(ctx.expr())
        elif (ctx.full_array_literal()):
            return self.visit(ctx.full_array_literal())
        elif (ctx.literal_struct()):
            return self.visit(ctx.literal_struct())

    def visitExpr8(self, ctx: MiniGoParser.Expr8Context):
        pass

    def visitFunc_call(self, ctx: MiniGoParser.Func_callContext):
        fun_name = ctx.Identifier().getText()
        args = self.visit(ctx.argument_set())

        return FuncCall(
            fun_name,
            args
        )

    def visitArgument_set(self, ctx: MiniGoParser.Argument_setContext):
        if (ctx.getChildCount() == 0):
            return []
        else:
            return self.visit(ctx.argument_list())

    def visitArgument_list(self, ctx: MiniGoParser.Argument_listContext):
        if (ctx.getChildCount() == 1):
            return [self.visit(ctx.argument())]
        else:
            return [self.visit(ctx.argument())] + self.visit(ctx.argument_list())

    def visitArgument(self, ctx: MiniGoParser.ArgumentContext):
        return self.visit(ctx.expr())

    def visitPrim_literal(self, ctx: MiniGoParser.Prim_literalContext):
        if (ctx.literal_int()):
            return self.visit(ctx.literal_int())
        elif (ctx.Literal_float()):
            return FloatLiteral(float(ctx.Literal_float().getText()))
        elif (ctx.Literal_string()):
            return StringLiteral(ctx.Literal_string().getText().replace('"', ''))
        elif (ctx.literal_bool()):
            return self.visit(ctx.literal_bool())
        else:
            return NilLiteral()

    def visitLiteral_int(self, ctx: MiniGoParser.Literal_intContext):
        if (ctx.Literal_dec()):
            return IntLiteral(int(ctx.getChild(0).getText()))
        elif (ctx.Literal_bin()):
            return IntLiteral(int(ctx.getChild(0).getText(), 2))
        elif (ctx.Literal_hex()):
            return IntLiteral(int(ctx.getChild(0).getText(), 16))
        else:
            return IntLiteral(int(ctx.getChild(0).getText(), 8))

    def visitLiteral_bool(self, ctx: MiniGoParser.Literal_boolContext):
        if (ctx.Literal_false()):
            return BooleanLiteral(False)
        else:
            return BooleanLiteral(True)

    def visitStmt(self, ctx: MiniGoParser.StmtContext):
        if (ctx.var_decl()):
            return self.visit(ctx.var_decl())
        elif (ctx.const_decl()):
            return self.visit(ctx.const_decl())
        elif (ctx.assign_stmt()):
            return self.visit(ctx.assign_stmt())
        elif (ctx.if_stmt()):
            # print("If stmt: ", str(self.visit(ctx.if_stmt())))
            return self.visit(ctx.if_stmt())
        elif (ctx.for_stmt()):
            return self.visit(ctx.for_stmt())
        elif (ctx.break_stmt()):
            return self.visit(ctx.break_stmt())
        elif (ctx.continue_stmt()):
            return self.visit(ctx.continue_stmt())
        elif (ctx.call_stmt()):
            return self.visit(ctx.call_stmt())
        elif (ctx.return_stmt()):
            return self.visit(ctx.return_stmt())
        else:
            raise SyntaxError("Invalid statement")

    def visitAssign_stmt(self, ctx: MiniGoParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.rhs())

        # print("Left: ", lhs)
        # print("Assign Ope: ", self.visit(ctx.ope_assign()))
        # print("Right: ", rhs)

        if (ctx.ope_assign().Ope_init()):
            return Assign(lhs, rhs)
        elif (ctx.ope_assign().Ope_assign_div()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_div().getText()[0],
                    lhs,
                    rhs    
                )
            )
        elif (ctx.ope_assign().Ope_assign_minus()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_minus().getText()[0],
                    lhs,
                    rhs    
                )
            )
        elif (ctx.ope_assign().Ope_assign_multi()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_multi().getText()[0],
                    lhs,
                    rhs    
                )
            )
        elif (ctx.ope_assign().Ope_assign_plus()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_plus().getText()[0],
                    lhs,
                    rhs    
                )
            )
        elif (ctx.ope_assign().Ope_assign_mod()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_mod().getText()[0],
                    lhs,
                    rhs    
                )
            )

    def visitLhs(self, ctx: MiniGoParser.LhsContext):
        if (ctx.getChildCount() == 1):
            return Id(ctx.Identifier().getText())
        else:
            accesses = self.visit(ctx.access_list())
            exprs = []
            flag = False
            result = Id(ctx.Identifier().getText())
            for i in accesses:
                if (i.array_access()):
                   flag = True
                   exprs = exprs + [self.visit(i.array_access().expr())]
                else:
                    if (flag):
                        result = FieldAccess(ArrayCell(result, exprs), i.struct_access().Identifier().getText())
                        flag = False
                        exprs = []
                    else:
                        result = FieldAccess(result, i.struct_access().Identifier().getText())
            
            if (exprs):
                result = ArrayCell(result, exprs)

            return result 

    def visitAccess_list(self, ctx: MiniGoParser.Access_listContext):
        if (ctx.getChildCount() == 1):
            return [ctx.access()]
        else:
            return self.visit(ctx.access_list()) + [ctx.access()]

    def visitAccess(self, ctx: MiniGoParser.AccessContext):
        pass

    def visitArray_access(self, ctx: MiniGoParser.Array_accessContext):
        pass

    def visitStruct_access(self, ctx: MiniGoParser.Struct_accessContext):
        pass

    def visitOpe_assign(self, ctx: MiniGoParser.Ope_assignContext):
        return ctx.getChild(0).getText()

    def visitRhs(self, ctx: MiniGoParser.RhsContext):
        return self.visit(ctx.getChild(0))

    def visitLiteral_array(self, ctx: MiniGoParser.Literal_arrayContext):
        return self.visit(ctx.getChild(0))

    def visitFull_array_literal(self, ctx: MiniGoParser.Full_array_literalContext):
        array_type = self.visit(ctx.array_type())
        element_set = self.visit(ctx.array_element_set())
        
        return ArrayLiteral(
            array_type.dimens,
            array_type.eleType,
            element_set
        )

    def visitPartial_array_literal(self, ctx: MiniGoParser.Partial_array_literalContext):
        
        return self.visit(ctx.array_element_set())

    def visitArray_element_set(self, ctx: MiniGoParser.Array_element_setContext):
        if (ctx.getChildCount() == 0):
            return []
        else:
            return self.visit(ctx.array_element_list())

    def visitArray_element_list(self, ctx: MiniGoParser.Array_element_listContext):
        if (ctx.getChildCount() == 1):
            return [self.visit(ctx.array_element())]
        else:
            return [self.visit(ctx.array_element())] + self.visit(ctx.array_element_list())

    def visitArray_element(self, ctx: MiniGoParser.Array_elementContext):
        return self.visit(ctx.getChild(0))

    def visitLiteral_struct(self, ctx: MiniGoParser.Literal_structContext):
        struct_name = ctx.Identifier().getText()
        elements = self.visit(ctx.struct_element_set())

        return StructLiteral(
            struct_name,
            elements
        )

    def visitStruct_element_set(self, ctx: MiniGoParser.Struct_element_setContext):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.struct_element_list())
        else:
            return []

    def visitStruct_element_list(self, ctx: MiniGoParser.Struct_element_listContext):
        if (ctx.getChildCount() == 1):
            return [self.visit(ctx.struct_element())]
        else:
            return [self.visit(ctx.struct_element())] + self.visit(ctx.struct_element_list())

    def visitStruct_element(self, ctx: MiniGoParser.Struct_elementContext):
        return tuple([ctx.Identifier().getText(), self.visit(ctx.expr())])

    def visitIf_stmt(self, ctx: MiniGoParser.If_stmtContext):
        return self.visit(ctx.getChild(0))

    def visitMatched(self, ctx: MiniGoParser.MatchedContext):
        condition = self.visit(ctx.condition())
        if_stmt_body = self.visit(ctx.if_stmt_body())

        # print("Condition: ", str(condition), " have type ", type(condition))
        # print("Body: ", str(if_stmt_body), " have type ", type(if_stmt_body))

        return If(
            condition,
            if_stmt_body,
            None
        )

    def visitUnmatched(self, ctx: MiniGoParser.UnmatchedContext):
        condition = self.visit(ctx.condition())
        if_stmt_body = self.visit(ctx.if_stmt_body())
        else_stmt_body = self.visit(ctx.else_stmt_list())

        return If(
            condition,
            if_stmt_body,
            else_stmt_body
        )

    def visitCondition(self, ctx: MiniGoParser.ConditionContext):
        return self.visit(ctx.expr())

    def visitIf_stmt_body(self, ctx: MiniGoParser.If_stmt_bodyContext):
        return self.visit(ctx.stmt_set())

    def visitElse_stmt_list(self, ctx: MiniGoParser.Else_stmt_listContext):
        if (ctx.getChildCount() == 2):
            return self.visit(ctx.if_stmt())
        else:
            return self.visit(ctx.else_stmt_body())

    # Visit a parse tree produced by MiniGoParser#else_stmt_body.
    def visitElse_stmt_body(self, ctx:MiniGoParser.Else_stmt_bodyContext):
        return self.visit(ctx.stmt_set())

    def visitFor_stmt(self, ctx: MiniGoParser.For_stmtContext):
        return self.visit(ctx.getChild(0))

    def visitFor_basic(self, ctx: MiniGoParser.For_basicContext):
        condition = self.visit(ctx.condition())
        for_body = self.visit(ctx.for_body())

        return ForBasic(
            condition,
            for_body
        )

    def visitFor_icu(self, ctx: MiniGoParser.For_icuContext):
        init = self.visit(ctx.init())
        condition = self.visit(ctx.condition())
        update = self.visit(ctx.update())
        for_body = self.visit(ctx.for_body())

        return ForStep(
            init,
            condition,
            update,
            for_body
        )

    def visitInit(self, ctx: MiniGoParser.InitContext):
        if (ctx.Key_decl_var()):
            if (ctx.data_type()):
                return VarDecl(
                    ctx.Identifier().getText(),
                    self.visit(ctx.data_type()),
                    self.visit(ctx.expr())
                )
            else:
                return VarDecl(
                    ctx.Identifier().getText(),
                    None,
                    self.visit(ctx.expr())
                )
        else:
            lhs = Id(ctx.Identifier().getText())
            rhs = self.visit(ctx.expr())

            return Assign(
                lhs,
                rhs
            )

    def visitUpdate(self, ctx: MiniGoParser.UpdateContext):
        lhs = Id(ctx.Identifier().getText())
        rhs = self.visit(ctx.expr())

        if (ctx.ope_assign().Ope_init()):
            return Assign(lhs, rhs)
        elif (ctx.ope_assign().Ope_assign_div()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_div().getText()[0],
                    lhs,
                    rhs    
                )
            )
        elif (ctx.ope_assign().Ope_assign_minus()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_minus().getText()[0],
                    lhs,
                    rhs    
                )
            )
        elif (ctx.ope_assign().Ope_assign_multi()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_multi().getText()[0],
                    lhs,
                    rhs    
                )
            )
        elif (ctx.ope_assign().Ope_assign_plus()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_plus().getText()[0],
                    lhs,
                    rhs    
                )
            )
        elif (ctx.ope_assign().Ope_assign_mod()):
            return Assign(
                lhs,
                BinaryOp(
                    ctx.ope_assign().Ope_assign_mod().getText()[0],
                    lhs,
                    rhs    
                )
            )

    def visitFor_range(self, ctx: MiniGoParser.For_rangeContext):
        idx = self.visit(ctx.index())
        value = self.visit(ctx.value())
        arr = self.visit(ctx.array_instance())
        for_body = self.visit(ctx.for_body())

        return ForEach(
            idx,
            value,
            arr,
            for_body
        )

    def visitArray_instance(self, ctx: MiniGoParser.Array_instanceContext):
        if (ctx.Identifier()):
            return Id(ctx.Identifier().getText())
        elif (ctx.full_array_literal()):
            return self.visit(ctx.full_array_literal())
        elif (ctx.expr()):
            return self.visit(ctx.expr())

    def visitIndex(self, ctx: MiniGoParser.IndexContext):
        return Id(ctx.Identifier().getText())

    def visitValue(self, ctx: MiniGoParser.ValueContext):
        return Id(ctx.Identifier().getText())

    def visitFor_body(self, ctx: MiniGoParser.For_bodyContext):
        return self.visit(ctx.stmt_set())

    def visitBreak_stmt(self, ctx: MiniGoParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: MiniGoParser.Continue_stmtContext):
        return Continue()

    def visitCall_stmt(self, ctx: MiniGoParser.Call_stmtContext):
        return self.visit(ctx.getChild(0))

    def visitFunc_call_stmt(self, ctx: MiniGoParser.Func_call_stmtContext):
        return self.visit(ctx.func_call())

    def visitMethod_call_stmt(self, ctx: MiniGoParser.Method_call_stmtContext):
        return self.visit(ctx.method_call())

    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        receiver = self.visit(ctx.expr())
        func_call = self.visit(ctx.func_call())

        return MethCall(
            receiver,
            func_call.funName,
            func_call.args
        )

    def visitReturn_stmt(self, ctx: MiniGoParser.Return_stmtContext):
        if (ctx.expr()):
            return Return(self.visit(ctx.expr()))
        else:
            return Return(None)
