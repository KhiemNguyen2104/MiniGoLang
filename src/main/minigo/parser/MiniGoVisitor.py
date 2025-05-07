# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decllist.
    def visitDecllist(self, ctx:MiniGoParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#end_stmt.
    def visitEnd_stmt(self, ctx:MiniGoParser.End_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_expl.
    def visitVar_decl_expl(self, ctx:MiniGoParser.Var_decl_explContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_value.
    def visitVar_value(self, ctx:MiniGoParser.Var_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_type.
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_list.
    def visitDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension.
    def visitDimension(self, ctx:MiniGoParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#size.
    def visitSize(self, ctx:MiniGoParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_infer.
    def visitVar_decl_infer(self, ctx:MiniGoParser.Var_decl_inferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_nil.
    def visitVar_decl_nil(self, ctx:MiniGoParser.Var_decl_nilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_decl.
    def visitType_decl(self, ctx:MiniGoParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_set.
    def visitField_set(self, ctx:MiniGoParser.Field_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_list.
    def visitField_list(self, ctx:MiniGoParser.Field_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_decl.
    def visitField_decl(self, ctx:MiniGoParser.Field_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_set.
    def visitInterface_method_set(self, ctx:MiniGoParser.Interface_method_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_list.
    def visitInterface_method_list(self, ctx:MiniGoParser.Interface_method_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_decl.
    def visitInterface_method_decl(self, ctx:MiniGoParser.Interface_method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_param_set.
    def visitInterface_method_param_set(self, ctx:MiniGoParser.Interface_method_param_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_param_list.
    def visitInterface_method_param_list(self, ctx:MiniGoParser.Interface_method_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_param.
    def visitInterface_method_param(self, ctx:MiniGoParser.Interface_method_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#id_list.
    def visitId_list(self, ctx:MiniGoParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_set.
    def visitParam_set(self, ctx:MiniGoParser.Param_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_list.
    def visitParam_list(self, ctx:MiniGoParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_body.
    def visitFunc_body(self, ctx:MiniGoParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_set.
    def visitStmt_set(self, ctx:MiniGoParser.Stmt_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_list.
    def visitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ope_relation.
    def visitOpe_relation(self, ctx:MiniGoParser.Ope_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr8.
    def visitExpr8(self, ctx:MiniGoParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argument_set.
    def visitArgument_set(self, ctx:MiniGoParser.Argument_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argument_list.
    def visitArgument_list(self, ctx:MiniGoParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argument.
    def visitArgument(self, ctx:MiniGoParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#prim_literal.
    def visitPrim_literal(self, ctx:MiniGoParser.Prim_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_int.
    def visitLiteral_int(self, ctx:MiniGoParser.Literal_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_bool.
    def visitLiteral_bool(self, ctx:MiniGoParser.Literal_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access_list.
    def visitAccess_list(self, ctx:MiniGoParser.Access_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access.
    def visitAccess(self, ctx:MiniGoParser.AccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_access.
    def visitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_access.
    def visitStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ope_assign.
    def visitOpe_assign(self, ctx:MiniGoParser.Ope_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rhs.
    def visitRhs(self, ctx:MiniGoParser.RhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_array.
    def visitLiteral_array(self, ctx:MiniGoParser.Literal_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#full_array_literal.
    def visitFull_array_literal(self, ctx:MiniGoParser.Full_array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#partial_array_literal.
    def visitPartial_array_literal(self, ctx:MiniGoParser.Partial_array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element_set.
    def visitArray_element_set(self, ctx:MiniGoParser.Array_element_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element_list.
    def visitArray_element_list(self, ctx:MiniGoParser.Array_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_struct.
    def visitLiteral_struct(self, ctx:MiniGoParser.Literal_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_element_set.
    def visitStruct_element_set(self, ctx:MiniGoParser.Struct_element_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_element_list.
    def visitStruct_element_list(self, ctx:MiniGoParser.Struct_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_element.
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#matched.
    def visitMatched(self, ctx:MiniGoParser.MatchedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unmatched.
    def visitUnmatched(self, ctx:MiniGoParser.UnmatchedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt_body.
    def visitIf_stmt_body(self, ctx:MiniGoParser.If_stmt_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_stmt_list.
    def visitElse_stmt_list(self, ctx:MiniGoParser.Else_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_stmt_body.
    def visitElse_stmt_body(self, ctx:MiniGoParser.Else_stmt_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_basic.
    def visitFor_basic(self, ctx:MiniGoParser.For_basicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_icu.
    def visitFor_icu(self, ctx:MiniGoParser.For_icuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init.
    def visitInit(self, ctx:MiniGoParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update.
    def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_range.
    def visitFor_range(self, ctx:MiniGoParser.For_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_instance.
    def visitArray_instance(self, ctx:MiniGoParser.Array_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#value.
    def visitValue(self, ctx:MiniGoParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_body.
    def visitFor_body(self, ctx:MiniGoParser.For_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_stmt.
    def visitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call_stmt.
    def visitFunc_call_stmt(self, ctx:MiniGoParser.Func_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call_stmt.
    def visitMethod_call_stmt(self, ctx:MiniGoParser.Method_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)



del MiniGoParser