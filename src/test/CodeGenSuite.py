import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
#     def test_int_literal(self):
#         input = """func main() {putInt(5);};"""
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,501))

#     def test_local_var(self):
#         input = """func main() {var a int = 20;  putInt(a);};"""
#         expect = "20"
#         self.assertTrue(TestCodeGen.test(input,expect,502))

#     def test_gllobal_var(self):
#         input = """var a int = 10; func main() { putInt(a);};"""
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,503))

#     def test_int_ast(self):
#         input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
#         expect = "25"
#         self.assertTrue(TestCodeGen.test(input,expect,504))

#     def test_local_var_ast(self):
#         input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
#         expect = "500"
#         self.assertTrue(TestCodeGen.test(input,expect,505))
    
#     def test_global_var_ast(self):  
#         input = Program([VarDecl("a",IntType(),IntLiteral(5000)),VarDecl("b", None, Id("a")),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
#         expect = "5000"
#         self.assertTrue(TestCodeGen.test(input,expect,506))
    
#     def test_int_literal_2(self):
#         input = """
#             var population int = 0O145701
#             var GDP float = (1.425 + population) * 2 / 1
#             var x int
#             var str1 = "Hello, "
#             var str2 = "World!"
#             const str = str1 + str2

#             func avGDP(GDP float, poppy int) float {
#                 return GDP/poppy;
#             }

#             func main() {
#                 var str3 = str + "1"
#                 var i float
#                 const gdp = avGDP(GDP, 2)

#                 x := 15

#                 var boo = i >= 2.0

#                 putBoolLn(boo)
#                 putFloatLn(1.0);
#                 putFloatLn(2.0);
#                 putFloatLn(GDP)
#                 putString(str)
#                 putLn();
#                 putStringLn(str3)
#                 putFloatLn(gdp)
#                 putInt(x)

#                 return
#             }
#         """
#         expect = """false
# 1.0
# 2.0
# 104324.85
# Hello, World!
# Hello, World!1
# 52162.426
# 15"""
#         self.assertTrue(TestCodeGen.test(input,expect,507))

#     def test_int_literal_3(self):
#         input = """
#             var d = 2
#             var arr_2 [3]float = [3]float{1.0, 2.0 + 3.0, 3.3}
#             var multiArr [4][2][3]int = [4][d][3]int{{{1, 2 + 1 - 1, 3}, {4, 5, 6}}, {{7, 8, 9}, {10, 11, 12}}, {{13, 14, 15}, {16, 17, 18}}, {{19, 20, 21}, {22, 23, 24}}}
#             var x = "abc"
#             const idx = 1 - -1 - One()
#             var arr [3]int = [3]int{idx, 0X1AF, 0B11}
#             const y = arr[1]
#             const z = multiArr[1][1][2]

#             func print(a string) {
#                 putString(a)
#             }

#             func One() int {
#                 return 1;
#             }

#             func main() {
#                 const b = [3]int{10, 11, 12}
#                 const boo = !false
                
#                 var ARR = [2][2]int{{1, 2}, {3, 4}}

#                 var idx int = 1;
#                 var val int = 2 * 6;
#                 var y = ARR[0][0]
#                 ARR[0][1] := 9
#                 arr[1] := 21
#                 putIntLn(idx)
#                 putStringLn(x)
#                 putIntLn(y)
#                 putIntLn(z)
#                 putFloatLn(arr_2[1])
#                 putIntLn(val)
#                 putIntLn(arr[1])
#                 putInt(ARR[0][1])
#             }
#         """
#         expect = """1
# abc
# 1
# 12
# 5.0
# 12
# 21
# 9"""
#         self.assertTrue(TestCodeGen.test(input,expect,508))

    # def test_int_literal_4(self):
    #     input = """
    #         type Shape interface {
    #             Circum(a int) int;
    #             Area() float;
    #         }

    #         type Rectangle struct {
    #             length int;
    #             width int;
    #         }

    #         func (r Rectangle) Circum(a int) int {
    #             return (r.length + r.width) * 2;
    #         }

    #         func (r Rectangle) Area() float {
    #             return r.length * r.width * 1.0
    #         }

    #         func main() {
    #             recs := [3]Rectangle{
    #                 Rectangle{length: 0B1010, width: 20},
    #                 Rectangle{length: 0b101, width: 0X1},
    #                 Rectangle{length: 4, width: 3}}

    #             var idx int;                    

    #             for idx, val := range recs {
    #                 putString("Check the rectangle ")
    #                 putIntLn(idx)
    #                 var cir = val.Circum(1)
    #                 if (cir > 5) {
    #                     putString("Area: ")
    #                     putFloatLn(val.Area())
    #                 } else {
    #                     putStringLn("It is so small!")
    #                 }
    #             }
    #         }
    #     """
    #     expect = f"Undeclared Identifier: val\n"
    #     # print(expect)
    #     self.assertTrue(TestCodeGen.test(input,expect, 408))

#     def test_float_literal_1(self):
#         input = """
#             type Person struct {
#                 height float;
#                 weight float
#             }
            
#             var arr = [2][2]Person{
#                 {Person{height: 17.0e-1, weight: 7.0E1}, Person{height: 148.0E-2, weight: 0.42e2}},
#                 {Person{height: 16.1E-1, weight: 6700.0e-2}, Person{height: 1765.0E-3, weight: 90.0}}}
            
#             func BMI(height, weight float) float {
#                 return weight / (height * height)
#             }

#             func main() {
#                 for i := 0; i <= 1; i += 1 {
#                     for var j = 0; j <= 1; j += 1 {
#                         bmi := BMI(arr[i][j].height, arr[i][j].weight);
#                         if (bmi < 18.5) {
#                             putStringLn("Underweight")
#                         } else if (18.5 <= bmi && bmi < 25.0) {
#                             putStringLn("Normal")
#                         } else if (25.0 <= bmi && bmi < 29.0) {
#                             putStringLn("Pre-obese")
#                         } else {
#                             putStringLn("Obese")
#                         }
#                     }
#                 }
#             }
#         """
#         expect = """Normal
# Normal
# Pre-obese
# Pre-obese
# """
#         self.assertTrue(TestCodeGen.test(input, expect, 510))

#     def test_var_decl_1(self):
#         """Test wrong variable declarations with arrays"""
#         input = """
#             var a = !(-1.0 <= 4.2)
#             var test1 = (1 == 2 || 3 == 4) && (3.0 != 5.6)
#             var test2 = (1 > 2) || ("abc" == "abc")
            
#             func One(flag boolean) int {
#                 if (flag) {
#                     return 1;
#                 }
#                 return -1;
#             }
            
#             func main() {
#                 arr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
#                 var i int = 0;
#                 var j int = 0;
#                 var flag boolean = false && !true;
#                 /*
#                 for i < 4 {
#                     for j < 4 {
#                         if (arr[i][j] > 5) {
#                             flag := true
#                             break
#                         }
#                     }
#                     i += 1;
#                     j := 0;
#                 }
#                 */
#                 putIntLn(i + j);

#                 const boo = !(One(true) < -17 + 16)

#                 var check = One(false)

#                 if (false && check == 1 && i + j != 0 || i != j) {
#                     const newVar = 1

#                     putBoolLn(boo)
#                     putBoolLn(a)
#                 } else if (i == 0) {
#                     const newVar = 2

#                     putIntLn(i + 1)
#                     putIntLn(check + 1)
#                 } else {
#                     var newVar = 3

#                     putBoolLn(test1)
#                     putBoolLn(test2)
#                 }
#             }
#         """
#         expect = """0
# 1
# 0
# """
#         self.assertTrue(TestCodeGen.test(input, expect, 511))

    # def test_var_decl_2(self):
    #     """Test variable declarations with structs"""
    #     input = """
    #         type Circle struct {
    #             radius float
    #         }
            
    #         var c Circle = Circle{radius: 5.12}

    #         const Pi = 3.14;

    #         func (c Circle) CirArea() float {
    #             return c.radius * c.radius * Pi;
    #         }

    #         func main() {
    #             putFloatLn(Pi);

    #             putFloatLn(c.CirArea())
    #         }

    #         var c = 1
    #     """
    #     expect = f"Redeclared Variable: c\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 411))

    # def test_var_decl_3(self):
    #     """Test wrong variable declarations with structs"""
    #     input = """
    #         const i = 1 + 1 + 1
    #         const j = 2 * (-(-1))
    #         var arr = [3][i][j]boolean{
    #                     {{true, false}, {true, true}, {false, true}},
    #                     {{false, false}, {true, false}, {true, true}},
    #                     {{true, true}, {false, true}, {false, false}}}

    #         func main() {
    #             putBool(arr[1 + 1][2][0])

    #             return
    #         }
    #     """
    #     expect = """false"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_var_dec_4(self):
        """Test variable declarations with strings"""
        input = """
            var last_name = "Khiem";
            const d = 2
            const ar = [d][1]int{{1}, {2}}
            var first_name string = "Nguyen Phuc Gia";

            func main() {
                var arr [2][3]float = [d][3]int{{13, 2, 3}, {5, 8, 9}}
                putStringLn(last_name + " " + first_name);
                putFloatLn(arr[0][0])
            }

            var x = (1 + 1.0);
        """
        expect = """Khiem Nguyen Phuc Gia
13.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    # def test_const_decl(self):
    #     """Test wrong variable declarations with strings"""
    #     input = """
    #         const Pi = 314.0E-2
    #         const E = 0.2718e1

    #         type Int struct {
    #             num int
    #         }

    #         func (i Int) Exp() float {
    #             return i.Pow(i.num, E)
    #         }

    #         func (i Int) Pow(n, e float) float {
    #             var i = 0
    #             var prod float = 1.0;
    #             for i < n {
    #                 prod *= e
    #             }

    #             return prod
    #         }

    #         func main() {
    #             var i = Int{num: 3};

    #             putFloatLn(i.Exp())
    #         }
    #     """
    #     expect = f"Type Mismatch: {str(MethCall(Id('i'), 'Pow', [FieldAccess(Id('i'), 'num'), Id('E')]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 414))

#     def test_var_decl_5(self):
#         input = """
#             type Person struct {
#                 name string
#                 age int
#             }    
        
#             func change(str string) {
#                 str := "Ha"
#             }

#             var a = Person{name: "Khiem"}
#             var ARR = [2]Person{Person{name: "Khiem", age: 21}, Person{name: "Bao", age: 20}}
            
#             const d = 3
#             var arr [d]int = [3]int{1 + d - 6, 2 + 2, 3 * d * d}
#             var nullArr [2]float

#             func main() {
#                 var s = "1"
#                 putIntLn(a.age)
#                 a := ARR[1]
#                 change(s)
                
#                 for i := 0; i < 5; i += 1 {
#                     putIntLn(arr[i])
#                     if (i == 2) {
#                         break
#                     }
#                 }

#                 a.name := "Tan Lo Regulus"

#                 putStringLn(a.name)

#                 return
#             }
#         """
#         expect = """0
# -2
# 4
# 27
# Tan Lo Regulus
# """
#         self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test_struct_decl(self):
    #     input = """
    #         var names [3]string = [3]string{"Andres", "Brown", "Laura"}

    #         type Email struct {
    #             name string
    #         }

    #         func (e Email) toString() string {
    #             return e.name + "@Xmail.com"
    #         }

    #         func main() {
    #             for i := 0; i < 3; i += 1 {
    #                 var e Email = Email{name: names[i]}
    #                 putStringLn(e.toString())
    #             }
    #         }

    #         var arr [3]float = [3]float{1.0, 3.0, 4.0 + true}
    #     """
    #     expect = f"Type Mismatch: {str(BinaryOp('+', FloatLiteral(4.0), BooleanLiteral(True)))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 416))

    # def test_assign_stmt_1(self):
    #     input = """

    #         type a struct {
    #             hello Hello
    #         }

    #         type Hello struct {
    #             hi Hi
    #         }

    #         type Hi struct {
    #             Goodbye [6][6][6][7]int
    #         }
            
    #         var x = [3][4]a{}

    #         func main() {    
    #             x[2][3].hello.hi.Goodbye[3][4][5][6] := 120;
                
    #             putIntLn(x[2][3].hello.hi.Goodbye[3][4][5][6])
    #         }

    #         var d int = "1"
    #     """
    #     expect = f"Type Mismatch: {str(VarDecl('d', IntType(), StringLiteral('1')))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 417))

#     def test_const_decl_2(self):
#         input = """
#             const Pi = 3.14

#             const Maxsize = (1 + 1.4E2)/34.3*(54 % 4);

#             func main() {
#                 putFloat(Maxsize)
#             }
#         """
#         expect = """8.221575"""
#         self.assertTrue(TestCodeGen.test(input, expect, 519))

#     def test_continue(self):
#         input = """
#             const x = 15;

#             func main() {
#                 for var i int = 0; i < x; i += 2 {
#                     if (i == 52) {
#                         continue;
#                     }

#                     putIntLn(i);
#                 }

#             }
#         """
#         expect = """0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# """
#         self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test_func_decl_1(self):
    #     input = """            
    #         type Circle struct {
    #             radius float
    #         }
            
    #         func foo(a, d int, b [5][6]string, c, e Circle) float {
    #             putStringLn(b[3][1]);

    #             rec_area := (a + d)*2;

    #             var cir_area = e.radius*e.radius*3.14;

    #             var c float = 1.0 * c.radius

    #             return c;
    #         }

    #         func foo1() { return; }

    #         func main() {
    #             return foo1();
    #         }
    #     """
    #     expect = f"Type Mismatch: {str(Return(FuncCall('foo1', [])))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 420))

    # def test_bool_literal(self):
    #     input = """            
    #         var a = false
    #         var b boolean = true
    #         var c boolean

    #         func main() {
    #             c := !((a || (!b && (a == !false))) && ((b || a) == !(b && !a)) || !(a == b) && (!(!a || b) == (a && !b)))

    #             putBoolLn(c)
    #             putStringLn(c)
    #         }
    #     """
    #     expect = f"Type Mismatch: {str(BinaryOp('==', Id('a'), UnaryOp('!', BooleanLiteral(False))))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 421))

    # def test_expression_1(self):
    #     input = """            
    #         type Circle struct {
    #             radius float
    #         }
            
    #         func foo(a, d int, b [5][6]string, c, e Circle) float {
    #             putStringLn(b[3][1]);
    #             var c float = 7.0 * c.radius

    #             rec_area := (a + d)*2;

    #             var cir_area = e.radius*e.radius*3.14;

    #             return c + 1;
    #         }

    #         func foo1() { return 1; }
    #     """
    #     expect = f"Type Mismatch: {str(Return(IntLiteral(1)))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 422))

    # def test321(self):
    #     input = """func main () int { x := 1 ; return "a"; };"""
    #     expect = f"Type Mismatch: {str(Return(StringLiteral('a')))}\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,423))

    # def test322(self):
    #     input = """func main (a int, b float) { x += 1 ; return; };"""
    #     expect = f"Undeclared Identifier: x\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,424))

    # def test323(self):
    #     input = """
    #     type Calculator struct {
    #         value int
    #     }
        
    #     type HumanAct interface {
    #         eat(food string);
    #         work(job string);
    #     }

    #     type Person struct {
    #         name string
    #         age int
    #     }

    #     func (p Person) eat(food string) {
    #         putStringLn("I am eating " + food)
    #         return ;
    #     }

    #     func (p Person) work(job string) {
    #         putStringLn("I am working " + job)
    #         return ;
    #     }

    #     func (c Calculator) Add(x int) int {
    #         c.value += x;
    #         var p HumanAct = Person{name: "Khiem", age: 21};

    #         p.work("Developer")
    #         putIntLn(p.age);

    #         return c.value;
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FieldAccess(Id('p'), 'age'))}\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,425))

    # def test324(self):
    #     input = """
    #     type A struct {
    #         a int
    #     }

    #     func (a A) b(c, d int) int {
    #         return c + d
    #     }
        
    #     func main () { 
    #         var a A = A{a: 4}
    #         var d = a.b(1+1, 3)
    #         a.b(1+1, 3)
    #     };
    #     """
    #     expect = f"Type Mismatch: {str(MethCall(Id('a'), 'b', [BinaryOp('+', IntLiteral(1), IntLiteral(1)), IntLiteral(3)]))}\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,426))

    # def test325(self):
    #     input = """
    #         type Cache struct {
    #             data [100]string;
    #             timestamp [100]int;
    #             size int;
    #             capacity int;
    #         }
            
    #         func (c Cache) get(key int) string {
    #             if (key >= 0 && key < c.size && c.timestamp[key] > 0) {
    #                 c.timestamp[key] := getCurrentTime()
    #                 return c.data[key]
    #             }
    #             return ""
    #         }
            
    #         func (c Cache) put(key int, value string) {
    #             if (key >= 0 && key < c.capacity) {
    #                 c.data[key] := value
    #                 c.timestamp[key] := getCurrentTime()
    #                 if (key >= c.size) {
    #                     c.size := key + 1
    #                 }
    #                 return 
    #             }
    #             return 
    #         }
    #         func (c Cache) clear() {
    #             for i := 0; i < c.capacity; i += 1 {
    #                 c.data[i] := ""
    #                 c.timestamp[i] := 0
    #             }
    #             c.size := 0
    #         }
    #         func getCurrentTime() int {
    #             return 0
    #         }
    #         func main() {
    #             var c Cache
    #             c := Cache{size: 0, capacity: 100}
    #             c.put(1, "value1")
    #             c.put(2, "value2")
    #             putStringLn(c.get(1))
    #             putStringLn(c.get(2))
    #         }

    #         var loi string = -1
    #     """
    #     expect = f"Type Mismatch: {str(VarDecl('loi', StringType(), UnaryOp('-', IntLiteral(1))))}\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,427))

    # def test326(self):
    #     """Simple variable declaration"""
    #     input = """var x int = 5;"""
    #     expect = f""
    #     self.assertTrue(TestCodeGen.test(input, expect, 428))

    # def test327(self):
    #     """Variable declaration without initialization"""
    #     input = """var counter int;"""
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 429))

    # def test328(self):
    #     """Multiple variable declarations"""
    #     input = """
    #     var a int = 10
    #     var b float = 3.14
    #     var c string = "hello"

    #     func combine(a int, b float, c string) string {
    #         return a + b + c
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(BinaryOp('+', BinaryOp('+', Id('a'), Id('b')), Id('c')))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 430))

    # def test329(self):
    #     """Simple function declaration"""
    #     input = """
    #     func greet() {
    #         println("Hello, world!")
    #     }
    #     """
    #     expect = f"Undeclared Function: println\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 431))

    # def test330(self):
    #     """Function with parameters and return type"""
    #     input = """
    #     func add(a int, b int) int {
    #         return a + b
    #     }

    #     var c = 1

    #     var arr = [c][1]int{{1}}
    #     """
    #     expect = f"Type Mismatch: {str(ArrayLiteral([Id('c'), IntLiteral(1)], IntType(), [[IntLiteral(1)]]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 432))

    # def test331(self):
    #     """Function with multiple statements"""
    #     input = """
    #     func calculateArea(width float, height float) float {
    #         var area float
    #         area := width * height
    #         return area
    #     }

    #     func main() {
    #         var d float = calculateArea(1.0, 2.0E14)

    #         putFloatLn(d)
    #         putLn()
    #         putInt(1.0)
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('putInt', [FloatLiteral(1.0)]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 433))

    # def test332(self):
    #     """Simple if statement"""
    #     input = """
    #     func testIfStatement(x int) {
    #         if (x > 10) {
    #             putStringLn("x is greater than 10")
    #         }
    #     }

    #     var d = 10

    #     var a = 1 + testIfStatement(d)
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('testIfStatement', [Id('d')]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 434))

    # def test333(self):
    #     """If-else statement"""
    #     input = """
    #     func checkEvenOdd(num int) {
    #         if (num % 2 == 0) {
    #             putStringLn("Even number")
    #         } else {
    #             putStringLn("Odd number")
    #         }
    #     }

    #     type Person struct {
    #         name string
    #         name int
    #     }
    #     """
    #     expect = f"Redeclared Field: name\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 435))

    # def test334(self):
    #     """If-else if-else statement"""
    #     input = """
    #     func gradeScore(score int) {
    #         if (score >= 90) {
    #             putStringLn("Grade A")
    #         } else if (score >= 80) {
    #             putStringLn("Grade B")
    #         } else if (score >= 70) {
    #             putStringLn("Grade C")
    #         } else {
    #             putStringLn("Grade D")
    #         }
    #     }

    #     func foo(a int, a string) {
    #         putIntLn(a)
    #     }
    #     """
    #     expect = f"Redeclared Parameter: a\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 436))

    # def test335(self):
    #     """Simple for loop"""
    #     input = """
    #     func countToTen() {
    #         for i := 1; i <= 10; i += 1 {
    #             putIntLn(i)
    #         }
    #     }
    #     """
    #     expect = f""
    #     self.assertTrue(TestCodeGen.test(input, expect, 437))

    # def test336(self):
    #     """For loop without initialization and update"""
    #     input = """
    #     var c = 0

    #     func getNextValue() int {
    #         c += 1
    #         return c - 1
    #     }
        
    #     func waitForCondition(x int) {
    #         for x < 100 {
    #             x := getNextValue()
    #         }

    #         putStringLn(x)
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('putStringLn', [Id('x')]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 438))

    # def test337(self):
    #     """For each loop"""
    #     input = """
    #     func sumArray(numbers [5]int) int {
    #         sum := 0
    #         var idx int
    #         value := 1
    #         for idx, value := range numbers {
    #             sum += value
    #         }
    #         return sum
    #     }

    #     var c = 1 || false
    #     """
    #     expect = f"Type Mismatch: {str(BinaryOp('||', IntLiteral(1), BooleanLiteral(False)))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 439))

    # def test338(self):
    #     """Array declaration and initialization"""
    #     input = """
    #     func testArrays() {
    #         numbers := [5]int{1, 2, 3, 4}
    #         putIntLn(numbers[2])
    #         getFloat()
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('getFloat', []))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 440))

    # def test339(self):
    #     """Multidimensional array"""
    #     input = """
    #     func testMatrix() {
    #         matrix := [2][3]int{{1, 2, 3}, {4, 5, 6}}
    #         putIntLn(matrix[1])
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('putIntLn', [ArrayCell(Id('matrix'), [IntLiteral(1)])]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 441))

    # def test340(self):
    #     """Simple struct type declaration"""
    #     input = """
    #     type Person struct {
    #         name string
    #         age int
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 441))

    # def test341(self):
    #     """Struct instantiation"""
    #     input = """
    #     type Person struct {
    #         name string
    #         age int
    #     }

    #     func (p Person) name() string{
    #         return p.nme
    #     }
        
    #     func createPerson() {
    #         p := Person{name: "John", age: 30}
    #         putStringLn(p.name)
    #     }
    #     """
    #     expect = f"Redeclared Method: name\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 442))

    # def test342(self):
    #     """Interface type declaration"""
    #     input = """
    #     type Shape interface {
    #         area() float
    #         perimeter() float
    #     }

    #     type Circle struct {
    #         radius float
    #     }

    #     func (c Circle) area() float {
    #         return c.radius * c.radius * 3.14
    #     }

    #     func main() {
    #         var a Shape = Circle{radius: 12.4}

    #         putFloatLn(a.area())
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(VarDecl('a', Id('Shape'), StructLiteral('Circle', [('radius', FloatLiteral(12.4))])))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 443))

    # def testJhin(self):
    #     """Interface type declaration"""
    #     input = """
    #     type Shape interface {
    #         area() float
    #         perimeter() float
    #     }

    #     type Circle struct {
    #         radius float
    #     }

    #     func (c Circle) perimeter() float {
    #         return c.radius * 2 * 3.14
    #     }

    #     func (c Circle) area() float {
    #         return c.radius * c.radius * 3.14
    #     }

    #     func main() {
    #         var a Shape = Circle{radius: 12.4}

    #         putIntLn(a.area())
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('putIntLn', [MethCall(Id('a'), 'area', [])]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 444))

    # def test343(self):
    #     """Method declaration"""
    #     input = """
    #     type Person struct {
    #         name int
    #     }
        
    #     func (p Person) greet() string {
    #         return "Hello, my name is " + p.name
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(BinaryOp('+', StringLiteral("Hello, my name is "), FieldAccess(Id('p'), 'name')))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 445))

    # def test344(self):
    #     """Method with parameters"""
    #     input = """
    #         type Circle struct {
    #             radius float
    #         }
            
    #         func (c Circle) scale(factor float) {
    #             c.radius *= factor
    #         }
    #     """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 446))

    # def test345(self):
    #     """Complex expressions"""
    #     input = """
    #     func complexCalculation(a int, b int, c int) float {
    #         return (a * b + c) / (a - b) * c % a
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(Return(BinaryOp('%', BinaryOp('*', BinaryOp('/', BinaryOp('+', BinaryOp('*', Id('a'), Id('b')), Id('c')), BinaryOp('-', Id('a'), Id('b'))), Id('c')), Id('a'))))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 447))

    # def test346(self):
    #     """Boolean expressions"""
    #     input = """
    #     func complexCondition(a int, b int) boolean {
    #         return a > b && a % 2 == 0 || b < 10 && b != 0
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 448))

    # def test347(self):
    #     """Complex nested method calls"""
    #     input = """
    #     func processData() {
    #         result := putInt(1)
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('putInt', [IntLiteral(1)]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 449))

    # def test348(self):
    #     """Complex field access and method calls"""
    #     input = """
    #         var c = 1

    #         func c(f float) {
    #             putFloatLn(f)
    #         }
    #     """
    #     expect = f"Redeclared Function: c\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 450))

    # def test349(self):
    #     """Recursive function"""
    #     input = """
    #     func factorial(n int) int {
    #         if (n <= 1) {
    #             return 1
    #         }
    #         return n * factorial(n - 1 * 1.0)
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('factorial', [BinaryOp('-', Id('n'), BinaryOp('*', IntLiteral(1), FloatLiteral(1.0)))]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 451))

    # def test350(self):
    #     """Complex program with multiple features"""
    #     input = """
    #     type BankAccount struct {
    #         owner string
    #         balance float
    #         transactions [100]Transaction
    #         transactionCount int
    #     }
        
    #     type Transaction struct {
    #         date string
    #         amount float
    #         description string
    #     }
        
    #     func getCurrentDate() string {
    #         return "01/01/2025"
    #     }

    #     func (account BankAccount) deposit(amount float) boolean {
    #         if (amount <= 0.0) {
    #             return false
    #         }
            
    #         account.balance += amount
    #         account.transactions[account.transactionCount] := Transaction{
    #             date: getCurrentDate(),
    #             amount: amount,
    #             description: "Deposit"}
    #         account.transactionCount += 1
            
    #         return true
    #     }
        
    #     func (account BankAccount) withdraw(amount float) boolean {
    #         if (amount <= 0.0 || amount > account.balance) {
    #             return false
    #         }
            
    #         account.balance -= amount
    #         account.transactions[account.transactionCount] := Transaction{
    #             date: getCurrentDate(),
    #             amount: -amount,
    #             description: "Withdrawal"}
    #         account.transactionCount += 1
            
    #         return true
    #     }
        
    #     func main() {
    #         myAccount := BankAccount{
    #             owner: "John Doe",
    #             balance: 1000.0,
    #             transactionCount: 0}
            
    #         a := myAccount.deposit(500.0)
    #         b := myAccount.withdraw(200.0)
            
    #         println("Current balance:", myAccount.balance)
    #     }
    #     """
    #     expect = f"Undeclared Function: println\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 452))

    # def test351(self):
    #     """Testing empty function body"""
    #     input = """func emptyFunction() { return; };"""
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 453))

    # def test352(self):
    #     """Testing function with multiple return statements"""
    #     input = """
    #     func max(a int, b int) int {
    #         if (a > b) {
    #             return a
    #         }
    #         return b
    #     }

    #     func main() {
    #         max(1, 2)
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('max', [IntLiteral(1), IntLiteral(2)]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 454))

    # def test353(self):
    #     """Testing function with multi-level return expression"""
    #     input = """
    #     func complexReturn(a int, b int, c int) int {
    #         return a + (b * (c - a)) / (b + c)
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 455))

    # def test354(self):
    #     """Testing complex nested if-else statements"""
    #     input = """
    #     func println(a int) {
    #         putIntLn(a)
    #     }
        
    #     func nestedConditions(a int, b int, c int) {
    #         if (a > b) {
    #             if (a > c) {
    #                 println(a)
    #             } else {
    #                 if (b > c) {
    #                     println(b)
    #                 } else {
    #                     println(c)
    #                 }
    #             }
    #         } else if (b > c) {
    #             println(b)
    #         } else {
    #             println(c)
    #         }
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 456))

    # def test355(self):
    #     """Testing complex for loop with break and continue"""
    #     input = """
    #     func processNumbers(arr [10]int) {
    #         for i := 0; i < 10; i += 1 {
    #             if (arr[i] == 0) {
    #                 continue
    #             }
    #             if (arr[i] < 0) {
    #                 break
    #             }
    #             println(arr[i])
    #         }
    #     }
    #     """
    #     expect = f"Undeclared Function: println\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 457))

    # def test356(self):
    #     input = """
    #         func main() {
    #             for var i = 1; i < 10; i *= 3.0 {
    #                 putStringLn("Hello")
    #             }
    #         }
    #     """
    #     expect = f"Type Mismatch: {str(Assign(Id('i'), BinaryOp('*', Id('i'), FloatLiteral(3.0))))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 458))

    # def test357(self):
    #     """Testing complex multi-dimensional array access"""
    #     input = """
    #     func processMatrix(matrix [5][5]int) {
    #         sum := 0
    #         for i := 0; i < 5; i += 1 {
    #             for j := 0; j < 5; j += 1 {
    #                 if (i == j) {
    #                     sum += matrix[i][j]
    #                 }
    #             }
    #         }
    #         return sum
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(Return(Id('sum')))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 459))

    # def test358(self):
    #     """Testing struct with struct field initialization"""
    #     input = """
    #     type Person struct {
    #         name string
    #         age int
    #         address Address
    #     }
        
    #     type Address struct {
    #         street string
    #         city string
    #         zip string
    #     }

    #     func main() {
    #         person := Person{
    #             name: "John",
    #             age: 30,
    #             address: Address{
    #                 street: "123 Main St",
    #                 city: "Anytown",
    #                 zip: "12345"}}
    #     }

    #     func al() { return; }

    #     var al = 1.20;
    #     """
    #     expect = f"Redeclared Variable: al\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 460))

    # def test359(self):
    #     """Testing array of structs initialization"""
    #     input = """
    #     type Employee struct {
    #         id int
    #         name string
    #         dept string
    #     }
        
    #     func main() {
    #         employees := [3]Employee{
    #             Employee{id: 1, name: "Alice", dept: "HR"},
    #             Employee{id: 2, name: "Bob", dept: "Engineering"},
    #             Employee{id: 3, name: "Charlie", dept: "Marketing"}}

    #         var str string = employees[2].name + employees[2].dept
    #         putInt(str)
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('putInt', [Id('str')]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 461))

    # def test359(self):
    #     """Testing array of structs initialization"""
    #     input = """
    #     type Employee struct {
    #         name string
    #         dept string
    #     }
        
    #     func main() {
    #         employees := [3]Employee{
    #             Employee{id: 1, name: "Alice", dept: "HR"},
    #             Employee{id: 2, name: "Bob", dept: "Engineering"},
    #             Employee{id: 3, name: "Charlie", dept: "Marketing"}}

    #         var str string = employees[2].name + employees[2].dept
    #         putStringLnt(str)
    #     }
    #     """
    #     expect = f"Undeclared Field: id\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 462))

    # def test360(self):
    #     """Testing complex interface with multiple method prototypes"""
    #     input = """
    #     var i = 1
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 463))

    # def test361(self):
    #     """Testing method with complex parameter types"""
    #     input = """
    #         type Employee struct {
    #             id int
    #             name string
    #             dept string
    #         }
            
    #         func main() {
    #             employees := [3]Employee{
    #                 Employee{id: 1, name: "Alice", dept: "HR"},
    #                 Employee{id: 2, name: "Bob", dept: "Engineering"},
    #                 Employee{id: 3, name: "Charlie", dept: "Marketing"}}

    #             var str string = employees[2].name + employees[2].dept
    #             putStringLn(str)
    #         }

    #         const Employee = 2
    #     """
    #     expect = f"Redeclared Constant: Employee\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 464))

    # def test362(self):
    #     """Testing struct with array of structs field"""
    #     input = """
    #         const Employee = 2
            
    #         type Employee struct {
    #             id int
    #             name string
    #             dept string
    #         }
            
    #         func main() {
    #             employees := [3]Employee{
    #                 Employee{id: 1, name: "Alice", dept: "HR"},
    #                 Employee{id: 2, name: "Bob", dept: "Engineering"},
    #                 Employee{id: 3, name: "Charlie", dept: "Marketing"}}

    #             var str string = employees[2].name + employees[2].dept
    #             putStringLn(str)
    #         }
    #     """
    #     expect = "Redeclared Type: Employee\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 465))

    # def test363(self):
    #     """Testing nested array literals"""
    #     input = """
    #     func createMatrix() {
    #         matrix := [3][3]int{
    #             {1, 2, 3},
    #             {4, 5, 6},
    #             {7, 8}}
            
    #         cube := [2][2][2]float{
    #             {{1, 2}, {3, 4}},
    #             {{5, 6}, {7, 8}}}
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 466))

    # def test364(self):
    #     """Testing complex method chain"""
    #     input = """
    #     var ex = i + 1
    #     """
    #     expect = f"Undeclared Identifier: i\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 467))

    # def test365(self):
    #     """Testing complex expression with mixed operators"""
    #     input = """
    #     func evaluateExpression(a int, b int, c int, d int) boolean {
    #         return (a > b && c < d) || (a + b) == (c - d) || !(a * b > c * d)
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 468))

    # def test366(self):
    #     """Testing complex expression with mixed operators"""
    #     input = """
    #     func evaluateExpression(a int, b float, c int, d int) boolean {
    #         return (a > b && c < d) || (a + 1) == (c - d) || !(a * 1 > c * d)
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(BinaryOp('>', Id('a'), Id('b')))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 469))

    # def test367(self):
    #     """Testing function with multiple variable declarations"""
    #     input = """
    #         var count int = 0
    #         var total float = 0.0
    #         var name string = "Default"

    #         func initialize() {
    #             putStringLn("Hello")    
    #         }

    #         var active boolean = true
    #         var items [10]int
    #         var matrix [3][3]float

    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 470))

    # def test368(self):
    #     """Testing function with multiple constant declarations"""
    #     input = """
    #     const PI = 3.14159
    #     const MAX_USERS = 1000
    #     const SERVER_NAME = "Main Server"
    #     const DEBUG_MODE = false
    #     const TIMEOUT_MS = 30000
        
    #     type Config struct {
    #         pi float
    #         maxUsers int
    #         serverName string
    #         debugMode boolean
    #         timeoutMs int
    #     }

    #     func getConfig() Config {
    #         return Config{
    #             pi: PI,
    #             maxUsers: MAX_USERS,
    #             serverName: SERVER_NAME,
    #             debugMode: DEBUG_MODE,
    #             timeoutMs: TIMEOUT_MS}
    #     }

    #     var Config = -123
    #     """
    #     expect = "Redeclared Variable: Config\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 471))

    # def test369(self):
    #     """Testing combined struct and interface definition"""
    #     input = """
    #     type Canvas struct {
    #         a int
    #     }

    #     func (c Canvas) setColor(a string) {
    #         return;
    #     }

    #     func (c Canvas) drawShape(s Shape) {
    #         return;
    #     }
        
    #     type Shape struct {
    #         x int;
    #         y int;
    #         color string;
    #     }
        
    #     type Rectangle struct {
    #         x int
    #         y int
    #         width float
    #         height float
    #     }

    #     func (s Shape) getBounds() Rectangle {
    #         return Rectangle{x: s.x, y: s.y, width: 0, height: 0}
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(StructLiteral('Rectangle', [('x', FieldAccess(Id('s'), 'x')), ('y', FieldAccess(Id('s'), 'y')), ('width', IntLiteral(0)), ('height', IntLiteral(0))]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 472))

    # def test370(self):
    #     """Testing function with multiple function calls"""
    #     input = """
    #     func processImage(img int) int {
    #         img := applyFilter(img, "blur", 5.0)
    #         img := adjustBrightness(img, 1.2)
    #         img := adjustContrast(img, 0.8)
    #         img := cropToSquare(img)
    #         img := resize(img, 800, 800)
    #         return img
    #     }
    #     """
    #     expect = "Undeclared Function: applyFilter\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 473))

    # def test371(self):
    #     """Testing complex for each loop with nested structure"""
    #     input = """
    #     type Student struct {
    #         name string
    #         grades [3]float
    #         active boolean
    #     }

    #     func (s Student) getAverageGrade() float {
    #         return (s.grades[0] + s.grades[2] + s.grades[2]) * (1.0 / 3)
    #     }
        
    #     func analyzeStudents(students [50]Student) {
    #         totalGPA := 0.0
    #         numStudents := 0
            
    #         var student Student
    #         var idx int

    #         for idx, student := range students {
    #             if (student.active) {
    #                 var grade float
    #                 for idx, grade := range student.grades {
    #                     totalGPA += grade
    #                 }
    #                 numStudents += 1
                    
    #                 putString("Student: " + student.name + "\\nAverage: ")
    #                 putFloatLn(student.getAverageGrade())
    #             }
    #         }
            
    #         if (numStudents > 0) {
    #             return 1;
    #         }
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(Return(IntLiteral(1)))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 474))

    # def test372(self):
    #     input = """
    #         func main() int {
    #             x := 1
    #             y := 2
                
    #             // Testing different assignment operators
    #             x += y        // x = x + y
    #             x -= y        // x = x - y
    #             x *= y        // x = x * y
    #             x /= y        // x = x / y
    #             x %= y        // x = x % y

    #             for x < 10 {
    #                 if (x == 5) {
    #                     return 5.0
    #                 }
    #             }
    #         }
    #     """
    #     expect = f"Type Mismatch: {str(Return(FloatLiteral(5.0)))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 475))


    # def test373(self):
    #     """Testing multiple method declarations for same struct"""
    #     input = """
    #     type Circle struct {
    #         x float;
    #         y float;
    #         radius float;
    #     }
        
    #     func (c Circle) area() float {
    #         return 3.14 * c.radius * c.radius
    #     }
        
    #     func (c Circle) circumference() float {
    #         return 2.0 * 3.14 * c.radius
    #     }
        
    #     func (c Circle) contains(px float, py float) boolean {
    #         dx := px - c.x
    #         dy := py - c.y
    #         distanceSquared := dx*dx + dy*dy
    #         return distanceSquared <= c.radius*c.radius
    #     }

    #     func (c Circle) scale(factor float) Circle {
    #         c.radius *= factor
    #         return c
    #     }

    #     func (c Circle) s(factor float) Circle {
    #         c.radius *= factor
    #         return 12
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(Return(IntLiteral(12)))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 476))

    # def test374(self):
    #     """Testing nested struct instantiation with array fields"""
    #     input = """
    #     type User struct {
    #         username string
    #         profile Profile
    #         permissions [4]Permission
    #     }

    #     type Profile struct {
    #         fullName string
    #         email string
    #         phoneNumbers [3]string
    #     }

    #     type Permission struct {
    #         name string
    #         enabled boolean
    #     }
        
    #     func createUser() User {
    #         return User{
    #             username: "johndoe",
    #             profile: Profile{
    #                 fullName: "John Doe",
    #                 email: "john@example.com",
    #                 phoneNumbers: [3]string{"123-456-7890", "555-123-4567", ""}},
    #             permissions: [4]Permission{
    #                 Permission{name: "read", enabled: true},
    #                 Permission{name: "write", enabled: true},
    #                 Permission{name: "admin", enabled: false},
    #                 Permission{name: "delete", enabled: false}},
    #             id: 1001}
    #     }
    #     """
    #     expect = f"Undeclared Field: id\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 477))

    # def test375(self):
    #     """Testing empty function body"""
    #     input = """func emptyFunction() { return; };"""
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 478))

    # def test376(self):
    #     """Testing function with multiple return statements"""
    #     input = """
    #     func max(a int, b int) int {
    #         if (a > b) {
    #             return a
    #         }
    #         return b
    #         return "Hello"
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(Return(StringLiteral("Hello")))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 479))

    # def test377(self):
    #     """Testing function with multi-level return expression"""
    #     input = """
    #     func complexReturn(a int, b int, c int) int {
    #         return a + (b * (c - a)) / (b + c)
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 480))

    # def test378(self):
    #     """Testing function with multi-level return expression"""
    #     input = """
    #     func complexReturn(a int, b int, c int) int {
    #         return a + (b * (c - a)) / (b + c)
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 481))

    # def test379(self):
    #     """Testing complex nested if-else statements"""
    #     input = """
    #     func println(a int) {
    #         return ;
    #     }
        
    #     func nestedConditions(a int, b int, c int) {
    #         if (a > b) {
    #             if (a > c) {
    #                 println(a)
    #             } else {
    #                 if (b > c) {
    #                     println(b)
    #                 } else {
    #                     println(c)
    #                 }
    #             }
    #         } else if (b > c || 1) {
    #             println(b)
    #         } else {
    #             println(c)
    #         }
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(BinaryOp('||', BinaryOp('>', Id('b'), Id('c')), IntLiteral(1)))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 482))

    # def test380(self):
    #     """Testing complex for loop with break and continue"""
    #     input = """
    #     func processNumbers(arr [10]int) int {
    #         for i := 0; i < 10; i += 1 {
    #             if (arr[i] == 0) {
    #                 continue
    #             }
    #             if (arr[i] < 0) {
    #                 return arr[i]
    #                 break
    #             }
    #             putFloatLn(arr[i])
    #         }
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('putFloatLn', [ArrayCell(Id('arr'), [Id('i')])]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 483))

    # def test381(self):
    #     """Testing complex multi-dimensional array access"""
    #     input = """
    #     func processMatrix(matrix [5][5]int) {
    #         sum := 0
    #         for i := 0; i < 5; i += 1 {
    #             for j := 0; j < 5; j += 1 {
    #                 if (i == j) {
    #                     sum += matrix[i][j]
    #                 }
    #             }
    #         }
    #         return sum
    #     }
    #     """
    #     expect = f"Type Mismatch: {str(Return(Id('sum')))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 484))

    # def test385(self):
    #     input = """
    #     func main() {
    #         x := 5
            
    #         // Using expression in an array index
    #         arr := [5]int{10, 20, 30, 40, 50}
    #         value := arr[1 + 2 * (x - 3) / 4]
            
    #         // Using function call in an array index
    #         value2 := arr[getIndex()]
    #     }
    #     """
    #     expect = f"Undeclared Function: getIndex\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 485))

    # def test_486(self):
    #     input = """var a int; var b int; var a int; """
    #     expect = "Redeclared Variable: a\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,486))

    # def test_487(self):
    #     input = """var a int = 1.2;"""
    #     expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,487))

    # def test_488r(self):
    #     input = Program([VarDecl("a",IntType(),Id("b"))])
    #     expect = "Undeclared Identifier: b\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,488))
  
    # def test_489(self):
    #     """Simple program: void main() {} """
    #     input = """
    #         var arr = [2][2]int{{1, 2}, {3, 4}}
    #         func main () {
    #             a := 1
    #             var b boolean = true
    #         };
    #         var x int ;
    #         const c = 3
    #         var h = [c]int{1, 2.0}
            
    #     """
    #     expect = """Type Mismatch: ArrayLiteral([Id(c)],IntType,[IntLiteral(1),FloatLiteral(2.0)])\n"""
    #     self.assertTrue(TestCodeGen.test(input,expect,489))

    # def test_490(self):
    #     """More complex program"""
    #     input = """
    #         type Person struct {
    #             birth_year int
    #         }
            
    #         func foo () {
    #             x := (3*7 + 2 - (-1))/10 + 5 % 4;
    #             if (x < 10) {
    #                 putIntLn(x);
    #             } else if (x < 0) {
    #                 x += 1;
    #                 putInt(x);
    #             } else {
    #                 putIntLn(10)
    #             }
    #         }

    #         func (p Person) cal_age(current_year int) int {
    #             return p.birth_year - current_year;
    #         }

    #         var x int = "34" + "hello"
    #     """
    #     expect = f"Type Mismatch: {str(VarDecl('x', IntType(), BinaryOp('+', StringLiteral('34'), StringLiteral('hello'))))}\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,490))
    
    # def test_491(self):
    #     input = """
    #         var length = 0b101011
    #         var width = 0X145AF9C;
            
    #         func main () {
    #             area := length * width
    #             putString("Area: ")
    #             putIntLn(area)
    #         }

    #         const size = 10

    #         var arr = [2][2]int{{1, 2}, {3, 4}}

    #         var x string = 1*4 + arr[1][1]
    #     """
    #     expect = f"Type Mismatch: {str(VarDecl('x', StringType(), BinaryOp('+', BinaryOp('*', IntLiteral(1), IntLiteral(4)), ArrayCell(Id('arr'), [IntLiteral(1), IntLiteral(1)]))))}\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,491))

    # def test_492(self):
    #     input = """
    #         var GDP float = 1.425
    #         var population int = 0O145701

    #         func avGDP(GDP float, pop int) float {
    #             return GDP/pop;
    #         }

    #         func main() {
    #             putFloatLn(avGDP(GDP, population));
    #             putFloatln(avGDP(GDP, population));
    #         }
    #     """
    #     expect = f"Undeclared Function: putFloatln\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,492))

    # def test_493(self):
    #     input = """
    #         var arr [3]int = [3]int{1, 0X1AF, 0B11}

    #         type HumanAct interface {
    #             eat(food string);
    #         }

    #         type Person struct {
    #             name string
    #             age int
    #         }

    #         func main() {
    #             var idx int;
    #             var val int;

    #             for idx, val := range arr {
    #                 putIntLn(idx)
    #                 putIntLn(val)
    #             }

    #             var p = Person{name: "A", age: 10}
    #             p.eat("Fish")
    #         }
    #     """
    #     expect = f"Undeclared Method: eat\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,493))

    # def test_494(self):
    #     input = """
    #         type Shape interface {
    #             Circum(a int) int;
    #             Area() float;
    #         }

    #         type Rectangle struct {
    #             length int;
    #             width int;
    #         }

    #         func (r Rectangle) Circum(a int) int {
    #             return (r.length + r.width) * 2;
    #         }

    #         func (r Rectangle) Area() float {
    #             return r.length * r.width * 1.0
    #         }

    #         func main() {
    #             recs := [3]Rectangle{
    #                 Rectangle{length: 0B1010, width: 20},
    #                 Rectangle{length: 0b101, width: 0X1},
    #                 Rectangle{length: 4, width: 3}}

    #             var idx int;                    

    #             for idx, val := range recs {
    #                 putString("Check the rectangle ")
    #                 putIntLn(idx)
    #                 var cir = val.Circum(1)
    #                 if (cir > 5) {
    #                     putString("Area: ")
    #                     putFloatLn(val.Area())
    #                 } else {
    #                     putStringLn("It is so small!")
    #                 }
    #             }
    #         }
    #     """
    #     expect = f"Undeclared Identifier: val\n"
    #     # print(expect)
    #     self.assertTrue(TestCodeGen.test(input,expect, 494))

    # def test_495(self):
    #     input = """
    #         type Person struct {
    #             height float;
    #             weight float
    #         }
            
    #         var arr = [3][2]Person{
    #             {Person{height: 17.0e-1, weight: 7.0E1}, Person{height: 148.0E-2, weight: 0.42e2}},
    #             {Person{height: 16.1E-1, weight: 6700.0e-2}, Person{height: 1765.0E-3, weight: 90.0}},
    #             {Person{}, Person{}}}
            
    #         func BMI(height, weight float) float {
    #             return weight / (height * height)
    #         }

    #         func main() {
    #             for i := 0; i <= 2; i += 1 {
    #                 for var j = 0; j <= 2; j += 1 {
    #                     bmi := BMI(arr[i][j].height, arr[i][j].weight);
    #                     if (bmi < 18.5) {
    #                         putStringLn("Underweight")
    #                     } else if (18.5 <= bmi && bmi < 25.0) {
    #                         putStringLn("Normal")
    #                     } else if (25.0 <= bmi && bmi < 29.0) {
    #                         putStringLn("Pre-obese")
    #                     } else {
    #                         putStringLn(1)
    #                     }
    #                 }
    #             }
    #         }
    #     """
    #     expect = f"Type Mismatch: {str(FuncCall('putStringLn', [IntLiteral(1)]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 495))

#     def test_496(self):
#         """Test wrong variable declarations with arrays"""
#         input = """
#             func One() int {
#                 return 1;
#             }
            
#             const b = 1 == 4
#             const t = 1
#             const d = 3 + t - -1*2 - 3
#             var arr = [2][d]int{{7, 2, 3}, {4, 5, 6}}
            
#             func main() {
#                 var i int = 0;
#                 var j int = 0;
#                 var flag boolean = false;

#                 const k = [2]int{1 + 1, 3}
#                 const l = k[0]
#                 var subArr = [l]int{5, 5}

#                 for i < 2 {
#                     for j < 2 {
#                         if (arr[i][j] > 5) {
#                             flag := true
#                             j += 1
#                             continue
#                         }
#                         putInt(i)
#                         putString(" ")
#                         putInt(j)
#                         putLn()
#                         j += 1
#                     }
#                     i += 1;
#                     j := 0;
#                 }

#                 return
#             }
#         """
#         expect = """0 1
# 1 0
# 1 1
# """
#         self.assertTrue(TestCodeGen.test(input, expect, 597))

    # def test_497(self):
    #     """Test variable declarations with structs"""
    #     input = """
    #         type Circle struct {
    #             radius float
    #         }
            
    #         var c Circle = Circle{radius: 5.12}

    #         const Pi = 3.14;

    #         func (c Circle) CirArea() float {
    #             return c.radius * c.radius * Pi;
    #         }

    #         func main() {
    #             putFloatLn(Pi);

    #             putFloatLn(c.CirArea())
    #         }

    #         var c = 1
    #     """
    #     expect = f"Redeclared Variable: c\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 497))

    # def test_498(self):
    #     """Test wrong variable declarations with structs"""
    #     input = """
    #         var i = 1 + 1 + 1
    #         var j int = 2 * (-(-1))
    #         var arr = [3][i][j]boolean{
    #                     {{true, false}, {true, true}, {false, true}},
    #                     {{false, false}, {true, false}, {true, true}},
    #                     {{true, true}, {false, true}, {false, false}}}
    #     """
    #     expect = f"Type Mismatch: {str(ArrayLiteral([IntLiteral(3), Id('i'), Id('j')], BoolType(), [[[BooleanLiteral(True), BooleanLiteral(False)], [BooleanLiteral(True), BooleanLiteral(True)], [BooleanLiteral(False), BooleanLiteral(True)]], [[BooleanLiteral(False), BooleanLiteral(False)], [BooleanLiteral(True), BooleanLiteral(False)], [BooleanLiteral(True), BooleanLiteral(True)]], [[BooleanLiteral(True), BooleanLiteral(True)], [BooleanLiteral(False), BooleanLiteral(True)], [BooleanLiteral(False), BooleanLiteral(False)]]]))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 498))

    # def test_499(self):
    #     """Test variable declarations with strings"""
    #     input = """
    #         var last_name = "Khiem";

    #         var first_name string = "Nguyen Phuc Gia";

    #         func main() {
    #             putStringLn(last_name + " " + first_name);
    #         }

    #         var x = (1 + 1.0)*"e";
    #     """
    #     expect = f"Type Mismatch: {str(BinaryOp('*', BinaryOp('+', IntLiteral(1), FloatLiteral(1.0)), StringLiteral('e')))}\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 499))

    # def test_500(self):
    #     """Complex program with multiple features"""
    #     input = """
    #     type BankAccount struct {
    #         owner string
    #         balance float
    #         transactions [100]Transaction
    #         transactionCount int
    #     }
        
    #     type Transaction struct {
    #         date string
    #         amount float
    #         description string
    #     }
        
    #     func getCurrentDate() string {
    #         return "01/01/2025"
    #     }

    #     func (account BankAccount) deposit(amount float) boolean {
    #         if (amount <= 0.0) {
    #             return false
    #         }
            
    #         account.balance += amount
    #         account.transactions[account.transactionCount] := Transaction{
    #             date: getCurrentDate(),
    #             amount: amount,
    #             description: "Deposit"}
    #         account.transactionCount += 1
            
    #         return true
    #     }
        
    #     func (account BankAccount) withdraw(amount float) boolean {
    #         if (amount <= 0.0 || amount > account.balance) {
    #             return false
    #         }
            
    #         account.balance -= amount
    #         account.transactions[account.transactionCount] := Transaction{
    #             date: getCurrentDate(),
    #             amount: -amount,
    #             description: "Withdrawal"}
    #         account.transactionCount += 1
            
    #         return true
    #     }
        
    #     func main() {
    #         myAccount := BankAccount{
    #             owner: "John Doe",
    #             balance: 1000.0,
    #             transactionCount: 0}
            
    #         a := myAccount.deposit(500.0)
    #         b := myAccount.withdraw(200.0)
            
    #         println("Current balance:", myAccount.balance)
    #     }
    #     """
    #     expect = f"Undeclared Function: println\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 452))