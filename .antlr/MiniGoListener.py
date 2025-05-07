# Generated from d:/Educational_program/242/CO3005-Principles of Programming Languages/Project/CO3005-Principles of Programming Languages/Assignment-4/assignment4/initial/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#decllist.
    def enterDecllist(self, ctx:MiniGoParser.DecllistContext):
        pass

    # Exit a parse tree produced by MiniGoParser#decllist.
    def exitDecllist(self, ctx:MiniGoParser.DecllistContext):
        pass


    # Enter a parse tree produced by MiniGoParser#decl.
    def enterDecl(self, ctx:MiniGoParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#decl.
    def exitDecl(self, ctx:MiniGoParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#const_decl.
    def enterConst_decl(self, ctx:MiniGoParser.Const_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#const_decl.
    def exitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#end_stmt.
    def enterEnd_stmt(self, ctx:MiniGoParser.End_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#end_stmt.
    def exitEnd_stmt(self, ctx:MiniGoParser.End_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_decl.
    def enterVar_decl(self, ctx:MiniGoParser.Var_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_decl.
    def exitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_decl_expl.
    def enterVar_decl_expl(self, ctx:MiniGoParser.Var_decl_explContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_decl_expl.
    def exitVar_decl_expl(self, ctx:MiniGoParser.Var_decl_explContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_value.
    def enterVar_value(self, ctx:MiniGoParser.Var_valueContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_value.
    def exitVar_value(self, ctx:MiniGoParser.Var_valueContext):
        pass


    # Enter a parse tree produced by MiniGoParser#data_type.
    def enterData_type(self, ctx:MiniGoParser.Data_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#data_type.
    def exitData_type(self, ctx:MiniGoParser.Data_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primitive_type.
    def enterPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primitive_type.
    def exitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_type.
    def enterArray_type(self, ctx:MiniGoParser.Array_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_type.
    def exitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#dimension_list.
    def enterDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#dimension_list.
    def exitDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#dimension.
    def enterDimension(self, ctx:MiniGoParser.DimensionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#dimension.
    def exitDimension(self, ctx:MiniGoParser.DimensionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#size.
    def enterSize(self, ctx:MiniGoParser.SizeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#size.
    def exitSize(self, ctx:MiniGoParser.SizeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_decl_infer.
    def enterVar_decl_infer(self, ctx:MiniGoParser.Var_decl_inferContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_decl_infer.
    def exitVar_decl_infer(self, ctx:MiniGoParser.Var_decl_inferContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_decl_nil.
    def enterVar_decl_nil(self, ctx:MiniGoParser.Var_decl_nilContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_decl_nil.
    def exitVar_decl_nil(self, ctx:MiniGoParser.Var_decl_nilContext):
        pass


    # Enter a parse tree produced by MiniGoParser#type_decl.
    def enterType_decl(self, ctx:MiniGoParser.Type_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#type_decl.
    def exitType_decl(self, ctx:MiniGoParser.Type_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_decl.
    def enterStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_decl.
    def exitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_set.
    def enterField_set(self, ctx:MiniGoParser.Field_setContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_set.
    def exitField_set(self, ctx:MiniGoParser.Field_setContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_list.
    def enterField_list(self, ctx:MiniGoParser.Field_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_list.
    def exitField_list(self, ctx:MiniGoParser.Field_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_decl.
    def enterField_decl(self, ctx:MiniGoParser.Field_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_decl.
    def exitField_decl(self, ctx:MiniGoParser.Field_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_decl.
    def enterInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_decl.
    def exitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_method_set.
    def enterInterface_method_set(self, ctx:MiniGoParser.Interface_method_setContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_method_set.
    def exitInterface_method_set(self, ctx:MiniGoParser.Interface_method_setContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_method_list.
    def enterInterface_method_list(self, ctx:MiniGoParser.Interface_method_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_method_list.
    def exitInterface_method_list(self, ctx:MiniGoParser.Interface_method_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_method_decl.
    def enterInterface_method_decl(self, ctx:MiniGoParser.Interface_method_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_method_decl.
    def exitInterface_method_decl(self, ctx:MiniGoParser.Interface_method_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_method_param_set.
    def enterInterface_method_param_set(self, ctx:MiniGoParser.Interface_method_param_setContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_method_param_set.
    def exitInterface_method_param_set(self, ctx:MiniGoParser.Interface_method_param_setContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_method_param_list.
    def enterInterface_method_param_list(self, ctx:MiniGoParser.Interface_method_param_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_method_param_list.
    def exitInterface_method_param_list(self, ctx:MiniGoParser.Interface_method_param_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_method_param.
    def enterInterface_method_param(self, ctx:MiniGoParser.Interface_method_paramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_method_param.
    def exitInterface_method_param(self, ctx:MiniGoParser.Interface_method_paramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#id_list.
    def enterId_list(self, ctx:MiniGoParser.Id_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#id_list.
    def exitId_list(self, ctx:MiniGoParser.Id_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#func_decl.
    def enterFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_decl.
    def exitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param_set.
    def enterParam_set(self, ctx:MiniGoParser.Param_setContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param_set.
    def exitParam_set(self, ctx:MiniGoParser.Param_setContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param_list.
    def enterParam_list(self, ctx:MiniGoParser.Param_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param_list.
    def exitParam_list(self, ctx:MiniGoParser.Param_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param.
    def enterParam(self, ctx:MiniGoParser.ParamContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param.
    def exitParam(self, ctx:MiniGoParser.ParamContext):
        pass


    # Enter a parse tree produced by MiniGoParser#func_body.
    def enterFunc_body(self, ctx:MiniGoParser.Func_bodyContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_body.
    def exitFunc_body(self, ctx:MiniGoParser.Func_bodyContext):
        pass


    # Enter a parse tree produced by MiniGoParser#stmt_set.
    def enterStmt_set(self, ctx:MiniGoParser.Stmt_setContext):
        pass

    # Exit a parse tree produced by MiniGoParser#stmt_set.
    def exitStmt_set(self, ctx:MiniGoParser.Stmt_setContext):
        pass


    # Enter a parse tree produced by MiniGoParser#stmt_list.
    def enterStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#stmt_list.
    def exitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_decl.
    def enterMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_decl.
    def exitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#receiver.
    def enterReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass

    # Exit a parse tree produced by MiniGoParser#receiver.
    def exitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expr.
    def enterExpr(self, ctx:MiniGoParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expr.
    def exitExpr(self, ctx:MiniGoParser.ExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expr1.
    def enterExpr1(self, ctx:MiniGoParser.Expr1Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr1.
    def exitExpr1(self, ctx:MiniGoParser.Expr1Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr2.
    def enterExpr2(self, ctx:MiniGoParser.Expr2Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr2.
    def exitExpr2(self, ctx:MiniGoParser.Expr2Context):
        pass


    # Enter a parse tree produced by MiniGoParser#ope_relation.
    def enterOpe_relation(self, ctx:MiniGoParser.Ope_relationContext):
        pass

    # Exit a parse tree produced by MiniGoParser#ope_relation.
    def exitOpe_relation(self, ctx:MiniGoParser.Ope_relationContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expr3.
    def enterExpr3(self, ctx:MiniGoParser.Expr3Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr3.
    def exitExpr3(self, ctx:MiniGoParser.Expr3Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr4.
    def enterExpr4(self, ctx:MiniGoParser.Expr4Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr4.
    def exitExpr4(self, ctx:MiniGoParser.Expr4Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr5.
    def enterExpr5(self, ctx:MiniGoParser.Expr5Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr5.
    def exitExpr5(self, ctx:MiniGoParser.Expr5Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr6.
    def enterExpr6(self, ctx:MiniGoParser.Expr6Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr6.
    def exitExpr6(self, ctx:MiniGoParser.Expr6Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr7.
    def enterExpr7(self, ctx:MiniGoParser.Expr7Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr7.
    def exitExpr7(self, ctx:MiniGoParser.Expr7Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr8.
    def enterExpr8(self, ctx:MiniGoParser.Expr8Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr8.
    def exitExpr8(self, ctx:MiniGoParser.Expr8Context):
        pass


    # Enter a parse tree produced by MiniGoParser#func_call.
    def enterFunc_call(self, ctx:MiniGoParser.Func_callContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_call.
    def exitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        pass


    # Enter a parse tree produced by MiniGoParser#argument_set.
    def enterArgument_set(self, ctx:MiniGoParser.Argument_setContext):
        pass

    # Exit a parse tree produced by MiniGoParser#argument_set.
    def exitArgument_set(self, ctx:MiniGoParser.Argument_setContext):
        pass


    # Enter a parse tree produced by MiniGoParser#argument_list.
    def enterArgument_list(self, ctx:MiniGoParser.Argument_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#argument_list.
    def exitArgument_list(self, ctx:MiniGoParser.Argument_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#argument.
    def enterArgument(self, ctx:MiniGoParser.ArgumentContext):
        pass

    # Exit a parse tree produced by MiniGoParser#argument.
    def exitArgument(self, ctx:MiniGoParser.ArgumentContext):
        pass


    # Enter a parse tree produced by MiniGoParser#prim_literal.
    def enterPrim_literal(self, ctx:MiniGoParser.Prim_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#prim_literal.
    def exitPrim_literal(self, ctx:MiniGoParser.Prim_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal_int.
    def enterLiteral_int(self, ctx:MiniGoParser.Literal_intContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal_int.
    def exitLiteral_int(self, ctx:MiniGoParser.Literal_intContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal_bool.
    def enterLiteral_bool(self, ctx:MiniGoParser.Literal_boolContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal_bool.
    def exitLiteral_bool(self, ctx:MiniGoParser.Literal_boolContext):
        pass


    # Enter a parse tree produced by MiniGoParser#stmt.
    def enterStmt(self, ctx:MiniGoParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#stmt.
    def exitStmt(self, ctx:MiniGoParser.StmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_stmt.
    def enterAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_stmt.
    def exitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#lhs.
    def enterLhs(self, ctx:MiniGoParser.LhsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#lhs.
    def exitLhs(self, ctx:MiniGoParser.LhsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#access_list.
    def enterAccess_list(self, ctx:MiniGoParser.Access_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#access_list.
    def exitAccess_list(self, ctx:MiniGoParser.Access_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#access.
    def enterAccess(self, ctx:MiniGoParser.AccessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#access.
    def exitAccess(self, ctx:MiniGoParser.AccessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_access.
    def enterArray_access(self, ctx:MiniGoParser.Array_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_access.
    def exitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_access.
    def enterStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_access.
    def exitStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#ope_assign.
    def enterOpe_assign(self, ctx:MiniGoParser.Ope_assignContext):
        pass

    # Exit a parse tree produced by MiniGoParser#ope_assign.
    def exitOpe_assign(self, ctx:MiniGoParser.Ope_assignContext):
        pass


    # Enter a parse tree produced by MiniGoParser#rhs.
    def enterRhs(self, ctx:MiniGoParser.RhsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#rhs.
    def exitRhs(self, ctx:MiniGoParser.RhsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal_array.
    def enterLiteral_array(self, ctx:MiniGoParser.Literal_arrayContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal_array.
    def exitLiteral_array(self, ctx:MiniGoParser.Literal_arrayContext):
        pass


    # Enter a parse tree produced by MiniGoParser#full_array_literal.
    def enterFull_array_literal(self, ctx:MiniGoParser.Full_array_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#full_array_literal.
    def exitFull_array_literal(self, ctx:MiniGoParser.Full_array_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#partial_array_literal.
    def enterPartial_array_literal(self, ctx:MiniGoParser.Partial_array_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#partial_array_literal.
    def exitPartial_array_literal(self, ctx:MiniGoParser.Partial_array_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_element_set.
    def enterArray_element_set(self, ctx:MiniGoParser.Array_element_setContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_element_set.
    def exitArray_element_set(self, ctx:MiniGoParser.Array_element_setContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_element_list.
    def enterArray_element_list(self, ctx:MiniGoParser.Array_element_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_element_list.
    def exitArray_element_list(self, ctx:MiniGoParser.Array_element_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_element.
    def enterArray_element(self, ctx:MiniGoParser.Array_elementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_element.
    def exitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal_struct.
    def enterLiteral_struct(self, ctx:MiniGoParser.Literal_structContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal_struct.
    def exitLiteral_struct(self, ctx:MiniGoParser.Literal_structContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_element_set.
    def enterStruct_element_set(self, ctx:MiniGoParser.Struct_element_setContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_element_set.
    def exitStruct_element_set(self, ctx:MiniGoParser.Struct_element_setContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_element_list.
    def enterStruct_element_list(self, ctx:MiniGoParser.Struct_element_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_element_list.
    def exitStruct_element_list(self, ctx:MiniGoParser.Struct_element_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_element.
    def enterStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_element.
    def exitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#if_stmt.
    def enterIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#if_stmt.
    def exitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#matched.
    def enterMatched(self, ctx:MiniGoParser.MatchedContext):
        pass

    # Exit a parse tree produced by MiniGoParser#matched.
    def exitMatched(self, ctx:MiniGoParser.MatchedContext):
        pass


    # Enter a parse tree produced by MiniGoParser#unmatched.
    def enterUnmatched(self, ctx:MiniGoParser.UnmatchedContext):
        pass

    # Exit a parse tree produced by MiniGoParser#unmatched.
    def exitUnmatched(self, ctx:MiniGoParser.UnmatchedContext):
        pass


    # Enter a parse tree produced by MiniGoParser#condition.
    def enterCondition(self, ctx:MiniGoParser.ConditionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#condition.
    def exitCondition(self, ctx:MiniGoParser.ConditionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#if_stmt_body.
    def enterIf_stmt_body(self, ctx:MiniGoParser.If_stmt_bodyContext):
        pass

    # Exit a parse tree produced by MiniGoParser#if_stmt_body.
    def exitIf_stmt_body(self, ctx:MiniGoParser.If_stmt_bodyContext):
        pass


    # Enter a parse tree produced by MiniGoParser#else_stmt_list.
    def enterElse_stmt_list(self, ctx:MiniGoParser.Else_stmt_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#else_stmt_list.
    def exitElse_stmt_list(self, ctx:MiniGoParser.Else_stmt_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#else_stmt_body.
    def enterElse_stmt_body(self, ctx:MiniGoParser.Else_stmt_bodyContext):
        pass

    # Exit a parse tree produced by MiniGoParser#else_stmt_body.
    def exitElse_stmt_body(self, ctx:MiniGoParser.Else_stmt_bodyContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_stmt.
    def enterFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_stmt.
    def exitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_basic.
    def enterFor_basic(self, ctx:MiniGoParser.For_basicContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_basic.
    def exitFor_basic(self, ctx:MiniGoParser.For_basicContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_icu.
    def enterFor_icu(self, ctx:MiniGoParser.For_icuContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_icu.
    def exitFor_icu(self, ctx:MiniGoParser.For_icuContext):
        pass


    # Enter a parse tree produced by MiniGoParser#init.
    def enterInit(self, ctx:MiniGoParser.InitContext):
        pass

    # Exit a parse tree produced by MiniGoParser#init.
    def exitInit(self, ctx:MiniGoParser.InitContext):
        pass


    # Enter a parse tree produced by MiniGoParser#update.
    def enterUpdate(self, ctx:MiniGoParser.UpdateContext):
        pass

    # Exit a parse tree produced by MiniGoParser#update.
    def exitUpdate(self, ctx:MiniGoParser.UpdateContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_range.
    def enterFor_range(self, ctx:MiniGoParser.For_rangeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_range.
    def exitFor_range(self, ctx:MiniGoParser.For_rangeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_instance.
    def enterArray_instance(self, ctx:MiniGoParser.Array_instanceContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_instance.
    def exitArray_instance(self, ctx:MiniGoParser.Array_instanceContext):
        pass


    # Enter a parse tree produced by MiniGoParser#index.
    def enterIndex(self, ctx:MiniGoParser.IndexContext):
        pass

    # Exit a parse tree produced by MiniGoParser#index.
    def exitIndex(self, ctx:MiniGoParser.IndexContext):
        pass


    # Enter a parse tree produced by MiniGoParser#value.
    def enterValue(self, ctx:MiniGoParser.ValueContext):
        pass

    # Exit a parse tree produced by MiniGoParser#value.
    def exitValue(self, ctx:MiniGoParser.ValueContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_body.
    def enterFor_body(self, ctx:MiniGoParser.For_bodyContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_body.
    def exitFor_body(self, ctx:MiniGoParser.For_bodyContext):
        pass


    # Enter a parse tree produced by MiniGoParser#break_stmt.
    def enterBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#break_stmt.
    def exitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continue_stmt.
    def enterContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continue_stmt.
    def exitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#call_stmt.
    def enterCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#call_stmt.
    def exitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#func_call_stmt.
    def enterFunc_call_stmt(self, ctx:MiniGoParser.Func_call_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_call_stmt.
    def exitFunc_call_stmt(self, ctx:MiniGoParser.Func_call_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_call_stmt.
    def enterMethod_call_stmt(self, ctx:MiniGoParser.Method_call_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_call_stmt.
    def exitMethod_call_stmt(self, ctx:MiniGoParser.Method_call_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_call.
    def enterMethod_call(self, ctx:MiniGoParser.Method_callContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_call.
    def exitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        pass


    # Enter a parse tree produced by MiniGoParser#return_stmt.
    def enterReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#return_stmt.
    def exitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        pass



del MiniGoParser