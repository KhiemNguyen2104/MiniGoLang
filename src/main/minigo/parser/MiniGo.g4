//2211573

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.last_token_type = None

def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit()
        if result.text[-1] == '\n' or result.text[-1] == '\r':
            result.text = result.text[0:-1]
        raise UncloseString(result.text[0:])
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(self.text)
    else:
        self.last_token_type = tk
        return super().emit()

def check_previous_token_for_newline_token(self):
    return self.last_token_type in {
        self.Identifier,
        self.Literal_nil,
        self.Literal_true,
        self.Literal_false,
        self.Literal_dec,
        self.Literal_oct,
        self.Literal_bin,
        self.Literal_hex,
        self.Literal_float,
        self.Literal_string,
        self.Key_type_int,
        self.Key_type_float,
        self.Key_type_string,
        self.Key_type_boolean,
        self.Key_return,
        self.Key_loop_continue,
        self.Key_loop_break,
        self.Rparen,
        self.Rsquare,
        self.Rcurly
    }

def replace_newline_char(self):
    if (self.check_previous_token_for_newline_token()):
        self.text = ';'
        self.type = self.Semicolon
    else:
        self.skip()

def check_illegal_escape(self):
    str = self.text
    i = 0
    while i < len(str):
        if str[i] == '\\' and i != len(str) - 1 and str[i+1] == '\\':
            i += 2
        elif str[i] == '\\' and i != len(str) - 1 and not (str[i + 1] in {'t', 'r', 'n'}):
            raise IllegalEscape(str[:i+2])
        else:
            i += 1
}

options{
	language = Python3;
}

// fragment

fragment Digit: [0-9];

fragment Exp: [eE] [-+]? Digit+;

fragment Escape: '\\' .;

fragment Char: ~["\\\n\r];

fragment Ope_for_boolean: Ope_and | Ope_or | Ope_not;

// Lexer rules

// keyword

Key_type_int: 'int';

Key_type_float: 'float';

Key_type_string: 'string';

Key_type_boolean: 'boolean';

Key_decl_const: 'const';

Key_decl_var: 'var';

Key_return: 'return';

Key_type: 'type';

Key_func: 'func';

Key_struct: 'struct';

Key_interface: 'interface';

Key_if: 'if';

Key_else: 'else';

Key_loop_for: 'for';

Key_loop_continue: 'continue';

Key_loop_break: 'break';

Key_range: 'range';

// Operator

// arithmetic Operator

Ope_plus: '+';

Ope_minus: '-';

Ope_multi: '*';

Ope_div: '/';

Ope_mod: '%';

// comparison Operator

Ope_equal: '==';

Ope_nequal: '!=';

Ope_let: '<';

Ope_leq: '<=';

Ope_get: '>';

Ope_geq: '>=';

// relational Operator

Ope_and: '&&';

Ope_or: '||';

Ope_not: '!';

// assignment Operator

Ope_assign: '=';

Ope_init: ':=';

Ope_assign_plus: '+=';

Ope_assign_minus: '-=';

Ope_assign_multi: '*=';

Ope_assign_div: '/=';

Ope_assign_mod: '%=';

// select Operator

Ope_select: '.';

// separator

Comma: ',';

Colon: ':';

Semicolon: ';';

Lparen: '(';

Rparen: ')';

Lsquare: '[';

Rsquare: ']';

Lcurly: '{';

Rcurly: '}';

// Literal

// nil Literal

Literal_nil: 'nil';

// boolean Literal

Literal_true: 'true';

Literal_false: 'false';

// integer literal

Literal_dec: '0' | [1-9] Digit*;

Literal_bin: ('0b' | '0B') [01]+;

Literal_oct: ('0o' | '0O') [0-7]+;

Literal_hex: ('0x' | '0X') [0-9a-fA-F]+;

Literal_float: ('0' | [1-9] Digit*) '.' Digit* Exp?;

// string literal

Literal_string: '"' (Char | Escape)* '"' {self.check_illegal_escape()};

// Identifier

Identifier: [A-Za-z_]+ [A-Za-z_0-9]*;

// Parser rules

// Program

// program: (vardecl | funcdecl) EOF; 

program: decllist EOF;

    decllist: decl decllist | decl;

    // Declaration

    decl: const_decl | var_decl | type_decl | func_decl | method_decl;

        // Constant declaration

        const_decl: Key_decl_const Identifier Ope_assign var_value end_stmt;
        
            end_stmt: NL | Semicolon;

        // Variable declaration

        var_decl: var_decl_expl | var_decl_infer | var_decl_nil;

            var_decl_expl: Key_decl_var Identifier data_type Ope_assign var_value end_stmt;

                var_value: expr | full_array_literal | literal_struct;

                data_type: primitive_type | Identifier | array_type;

                    primitive_type: Key_type_int | Key_type_float | Key_type_boolean | Key_type_string;

                    array_type: dimension_list primitive_type
                              | dimension_list Identifier
                              ;
                    
                        dimension_list: dimension dimension_list | dimension;

                            dimension: Lsquare size Rsquare;

                                size: Literal_bin | Literal_hex | Literal_oct | Literal_dec | Identifier;

            var_decl_infer: Key_decl_var Identifier Ope_assign var_value end_stmt;

            var_decl_nil: Key_decl_var Identifier data_type end_stmt;

        // Type declaration

        type_decl: struct_decl | interface_decl;

            struct_decl: Key_type Identifier Key_struct Lcurly field_list Rcurly end_stmt;

                field_set: field_list | ;

                    field_list: field_decl field_list | field_decl;

                        field_decl: Identifier data_type end_stmt;

            interface_decl: Key_type Identifier Key_interface Lcurly interface_method_list Rcurly end_stmt;

                interface_method_set: interface_method_list | ;

                    interface_method_list: interface_method_decl interface_method_list | interface_method_decl;

                        interface_method_decl: Identifier Lparen interface_method_param_set Rparen data_type end_stmt
                                            |  Identifier Lparen interface_method_param_set Rparen end_stmt;

                            interface_method_param_set: interface_method_param_list | ;

                                interface_method_param_list: interface_method_param Comma interface_method_param_list | interface_method_param;

                                    interface_method_param: id_list data_type;

                                        id_list: Identifier Comma id_list | Identifier;

        // Function and method declaration

        func_decl: Key_func Identifier Lparen param_set Rparen data_type Lcurly func_body Rcurly end_stmt
                |  Key_func Identifier Lparen param_set Rparen Lcurly func_body Rcurly end_stmt;

            param_set: param_list | ;

                param_list: param Comma param_list | param;

                    param: id_list data_type;
            
            func_body: stmt_set;

                stmt_set: stmt_list;

                stmt_list: stmt stmt_list | stmt;

        method_decl: Key_func receiver Identifier Lparen param_set Rparen data_type Lcurly func_body Rcurly end_stmt
                |    Key_func receiver Identifier Lparen param_set Rparen Lcurly func_body Rcurly end_stmt;

            receiver: Lparen Identifier Identifier Rparen;

// Expression

    expr: expr Ope_or expr1 | expr1;

    expr1: expr1 Ope_and expr2 | expr2;

    expr2: expr2 ope_relation expr3 | expr3;

        ope_relation: Ope_equal | Ope_nequal | Ope_let | Ope_leq | Ope_get | Ope_geq;

    expr3: expr3 Ope_plus expr4 | expr3 Ope_minus expr4 | expr4;

    expr4: expr4 Ope_multi expr5 | expr4 Ope_div expr5 | expr4 Ope_mod expr5 | expr5;

    expr5: Ope_not expr5 | Ope_minus expr5 | expr6;

    expr6: expr6 Lsquare expr Rsquare | expr6 Ope_select expr8 | expr7;

    expr7: prim_literal | Identifier | Lparen expr Rparen | func_call | full_array_literal | literal_struct;

    expr8: Identifier | func_call;

        func_call: Identifier Lparen argument_set Rparen;

            argument_set: argument_list | ;

            argument_list: argument Comma argument_list | argument;

                argument: expr;

        prim_literal: literal_int | Literal_float | Literal_string | literal_bool | Literal_nil;

            literal_int: Literal_dec | Literal_bin | Literal_hex | Literal_oct;

            literal_bool: Literal_false | Literal_true;

// Statement

    stmt: var_decl | const_decl | assign_stmt | if_stmt | for_stmt | break_stmt | continue_stmt | call_stmt | return_stmt;

        assign_stmt: lhs ope_assign rhs end_stmt;

            lhs: Identifier access_list | Identifier;

            access_list: access_list access | access;
            
                access: array_access | struct_access;

                    array_access: Lsquare expr Rsquare;

                    struct_access: Ope_select Identifier;

            ope_assign: Ope_init | Ope_assign_div | Ope_assign_minus | Ope_assign_mod | Ope_assign_multi | Ope_assign_plus;

            rhs: expr | full_array_literal | literal_struct;

                literal_array: full_array_literal | partial_array_literal;

                    full_array_literal: array_type Lcurly array_element_set Rcurly;
                
                    partial_array_literal: Lcurly array_element_set Rcurly;

                        array_element_set: array_element_list | ;

                        array_element_list: array_element Comma array_element_list | array_element;

                            array_element: expr | literal_array | literal_struct;

                literal_struct: Identifier Lcurly struct_element_set Rcurly;

                    struct_element_set: struct_element_list | ;

                    struct_element_list: struct_element Comma struct_element_list | struct_element;

                        struct_element: Identifier Colon expr;

        if_stmt: matched | unmatched;
        
            matched: Key_if Lparen condition Rparen Lcurly if_stmt_body Rcurly end_stmt;

            unmatched: Key_if Lparen condition Rparen Lcurly if_stmt_body Rcurly else_stmt_list;

                condition: expr;

                if_stmt_body: stmt_set;

                else_stmt_list: Key_else if_stmt
                            |   Key_else Lcurly else_stmt_body Rcurly end_stmt
                            ;

                    else_stmt_body: stmt_set;

        for_stmt: for_basic 
                | for_icu // for with initialization, condition and update
                | for_range;

            for_basic: Key_loop_for condition Lcurly for_body Rcurly end_stmt;

            for_icu: Key_loop_for init Semicolon condition Semicolon update Lcurly for_body Rcurly end_stmt;

                init: Identifier Ope_init expr
                    | Key_decl_var Identifier data_type Ope_assign expr
                    | Key_decl_var Identifier Ope_assign expr
                    ;

                update: Identifier ope_assign expr;

            for_range: Key_loop_for index Comma value Ope_init Key_range array_instance Lcurly for_body Rcurly end_stmt;

                array_instance: Identifier | full_array_literal | expr;

                index: Identifier;

                value: Identifier;

                for_body: stmt_set;

        break_stmt: Key_loop_break end_stmt;

        continue_stmt: Key_loop_continue end_stmt;

        call_stmt: func_call_stmt | method_call_stmt;

            func_call_stmt: func_call end_stmt;

            method_call_stmt: method_call end_stmt;
                
                method_call: expr Ope_select func_call;

        return_stmt: Key_return end_stmt | Key_return expr end_stmt;

NL: [\n\r]+ { self.replace_newline_char() }; // replace or replace new lines

WS: [ \t]+ -> skip; // skip spaces, tabs 

SL_COMMENT: '//' ~[\n\r]* -> skip; // skip single line comments

ML_COMMENT: '/*' .*? '*/' -> skip; // skip multi lines comments

UNCLOSE_STRING: '"' (Char | Escape)* (EOF | [\n\r]);

ERROR_CHAR: .;