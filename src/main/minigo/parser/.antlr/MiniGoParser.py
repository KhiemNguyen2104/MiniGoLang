# Generated from d:/Educational_program/242/CO3005-Principles of Programming Languages/Project/CO3005-Principles of Programming Languages/Assignment-4/assignment4/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,64,795,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,78,7,78,
        2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,84,2,85,
        7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,91,7,91,
        2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,97,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,204,8,1,1,2,1,2,1,2,1,2,1,2,3,2,211,
        8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,3,5,224,8,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,236,8,7,1,8,1,8,1,8,3,8,
        241,8,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,251,8,10,1,11,
        1,11,1,11,1,11,3,11,257,8,11,1,12,1,12,1,12,1,12,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,3,16,
        278,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,3,18,
        290,8,18,1,19,1,19,1,19,1,19,3,19,296,8,19,1,20,1,20,1,20,1,20,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,3,22,312,8,22,1,
        23,1,23,1,23,1,23,3,23,318,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,333,8,24,1,25,1,25,3,25,337,
        8,25,1,26,1,26,1,26,1,26,1,26,3,26,344,8,26,1,27,1,27,1,27,1,28,
        1,28,1,28,1,28,3,28,353,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,3,29,376,8,29,1,30,1,30,3,30,380,8,30,1,31,1,31,1,31,1,31,1,
        31,3,31,387,8,31,1,32,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,
        35,1,35,3,35,400,8,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,3,36,425,8,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,
        38,1,38,1,38,5,38,438,8,38,10,38,12,38,441,9,38,1,39,1,39,1,39,1,
        39,1,39,1,39,5,39,449,8,39,10,39,12,39,452,9,39,1,40,1,40,1,40,1,
        40,1,40,1,40,1,40,5,40,461,8,40,10,40,12,40,464,9,40,1,41,1,41,1,
        42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,5,42,477,8,42,10,42,12,
        42,480,9,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,
        43,1,43,5,43,494,8,43,10,43,12,43,497,9,43,1,44,1,44,1,44,1,44,1,
        44,3,44,504,8,44,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,
        45,1,45,5,45,517,8,45,10,45,12,45,520,9,45,1,46,1,46,1,46,1,46,1,
        46,1,46,1,46,1,46,1,46,3,46,531,8,46,1,47,1,47,3,47,535,8,47,1,48,
        1,48,1,48,1,48,1,48,1,49,1,49,3,49,544,8,49,1,50,1,50,1,50,1,50,
        1,50,3,50,551,8,50,1,51,1,51,1,52,1,52,1,52,1,52,1,52,3,52,560,8,
        52,1,53,1,53,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,
        55,3,55,575,8,55,1,56,1,56,1,56,1,56,1,56,1,57,1,57,1,57,3,57,585,
        8,57,1,58,1,58,1,58,1,58,1,58,5,58,592,8,58,10,58,12,58,595,9,58,
        1,59,1,59,3,59,599,8,59,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,62,
        1,62,1,63,1,63,1,63,3,63,613,8,63,1,64,1,64,3,64,617,8,64,1,65,1,
        65,1,65,1,65,1,65,1,66,1,66,1,66,1,66,1,67,1,67,3,67,630,8,67,1,
        68,1,68,1,68,1,68,1,68,3,68,637,8,68,1,69,1,69,1,69,3,69,642,8,69,
        1,70,1,70,1,70,1,70,1,70,1,71,1,71,3,71,651,8,71,1,72,1,72,1,72,
        1,72,1,72,3,72,658,8,72,1,73,1,73,1,73,1,73,1,74,1,74,3,74,666,8,
        74,1,75,1,75,1,75,1,75,1,75,1,75,1,75,1,75,1,75,1,76,1,76,1,76,1,
        76,1,76,1,76,1,76,1,76,1,76,1,77,1,77,1,78,1,78,1,79,1,79,1,79,1,
        79,1,79,1,79,1,79,1,79,3,79,698,8,79,1,80,1,80,1,81,1,81,1,81,3,
        81,705,8,81,1,82,1,82,1,82,1,82,1,82,1,82,1,82,1,83,1,83,1,83,1,
        83,1,83,1,83,1,83,1,83,1,83,1,83,1,83,1,84,1,84,1,84,1,84,1,84,1,
        84,1,84,1,84,1,84,1,84,1,84,1,84,1,84,3,84,738,8,84,1,85,1,85,1,
        85,1,85,1,86,1,86,1,86,1,86,1,86,1,86,1,86,1,86,1,86,1,86,1,86,1,
        86,1,87,1,87,1,87,3,87,759,8,87,1,88,1,88,1,89,1,89,1,90,1,90,1,
        91,1,91,1,91,1,92,1,92,1,92,1,93,1,93,3,93,775,8,93,1,94,1,94,1,
        94,1,95,1,95,1,95,1,96,1,96,1,96,1,96,1,97,1,97,1,97,1,97,1,97,1,
        97,3,97,793,8,97,1,97,0,7,76,78,80,84,86,90,116,98,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,
        100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,
        132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,
        164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,
        0,7,2,0,42,42,59,59,1,0,1,4,2,0,52,55,58,58,1,0,23,28,1,0,52,55,
        1,0,50,51,1,0,33,38,777,0,196,1,0,0,0,2,203,1,0,0,0,4,210,1,0,0,
        0,6,212,1,0,0,0,8,218,1,0,0,0,10,223,1,0,0,0,12,225,1,0,0,0,14,235,
        1,0,0,0,16,240,1,0,0,0,18,242,1,0,0,0,20,250,1,0,0,0,22,256,1,0,
        0,0,24,258,1,0,0,0,26,262,1,0,0,0,28,264,1,0,0,0,30,270,1,0,0,0,
        32,277,1,0,0,0,34,279,1,0,0,0,36,289,1,0,0,0,38,295,1,0,0,0,40,297,
        1,0,0,0,42,301,1,0,0,0,44,311,1,0,0,0,46,317,1,0,0,0,48,332,1,0,
        0,0,50,336,1,0,0,0,52,343,1,0,0,0,54,345,1,0,0,0,56,352,1,0,0,0,
        58,375,1,0,0,0,60,379,1,0,0,0,62,386,1,0,0,0,64,388,1,0,0,0,66,391,
        1,0,0,0,68,393,1,0,0,0,70,399,1,0,0,0,72,424,1,0,0,0,74,426,1,0,
        0,0,76,431,1,0,0,0,78,442,1,0,0,0,80,453,1,0,0,0,82,465,1,0,0,0,
        84,467,1,0,0,0,86,481,1,0,0,0,88,503,1,0,0,0,90,505,1,0,0,0,92,530,
        1,0,0,0,94,534,1,0,0,0,96,536,1,0,0,0,98,543,1,0,0,0,100,550,1,0,
        0,0,102,552,1,0,0,0,104,559,1,0,0,0,106,561,1,0,0,0,108,563,1,0,
        0,0,110,574,1,0,0,0,112,576,1,0,0,0,114,584,1,0,0,0,116,586,1,0,
        0,0,118,598,1,0,0,0,120,600,1,0,0,0,122,604,1,0,0,0,124,607,1,0,
        0,0,126,612,1,0,0,0,128,616,1,0,0,0,130,618,1,0,0,0,132,623,1,0,
        0,0,134,629,1,0,0,0,136,636,1,0,0,0,138,641,1,0,0,0,140,643,1,0,
        0,0,142,650,1,0,0,0,144,657,1,0,0,0,146,659,1,0,0,0,148,665,1,0,
        0,0,150,667,1,0,0,0,152,676,1,0,0,0,154,685,1,0,0,0,156,687,1,0,
        0,0,158,697,1,0,0,0,160,699,1,0,0,0,162,704,1,0,0,0,164,706,1,0,
        0,0,166,713,1,0,0,0,168,737,1,0,0,0,170,739,1,0,0,0,172,743,1,0,
        0,0,174,758,1,0,0,0,176,760,1,0,0,0,178,762,1,0,0,0,180,764,1,0,
        0,0,182,766,1,0,0,0,184,769,1,0,0,0,186,774,1,0,0,0,188,776,1,0,
        0,0,190,779,1,0,0,0,192,782,1,0,0,0,194,792,1,0,0,0,196,197,3,2,
        1,0,197,198,5,0,0,1,198,1,1,0,0,0,199,200,3,4,2,0,200,201,3,2,1,
        0,201,204,1,0,0,0,202,204,3,4,2,0,203,199,1,0,0,0,203,202,1,0,0,
        0,204,3,1,0,0,0,205,211,3,6,3,0,206,211,3,10,5,0,207,211,3,32,16,
        0,208,211,3,58,29,0,209,211,3,72,36,0,210,205,1,0,0,0,210,206,1,
        0,0,0,210,207,1,0,0,0,210,208,1,0,0,0,210,209,1,0,0,0,211,5,1,0,
        0,0,212,213,5,5,0,0,213,214,5,58,0,0,214,215,5,32,0,0,215,216,3,
        14,7,0,216,217,3,8,4,0,217,7,1,0,0,0,218,219,7,0,0,0,219,9,1,0,0,
        0,220,224,3,12,6,0,221,224,3,28,14,0,222,224,3,30,15,0,223,220,1,
        0,0,0,223,221,1,0,0,0,223,222,1,0,0,0,224,11,1,0,0,0,225,226,5,6,
        0,0,226,227,5,58,0,0,227,228,3,16,8,0,228,229,5,32,0,0,229,230,3,
        14,7,0,230,231,3,8,4,0,231,13,1,0,0,0,232,236,3,76,38,0,233,236,
        3,130,65,0,234,236,3,140,70,0,235,232,1,0,0,0,235,233,1,0,0,0,235,
        234,1,0,0,0,236,15,1,0,0,0,237,241,3,18,9,0,238,241,5,58,0,0,239,
        241,3,20,10,0,240,237,1,0,0,0,240,238,1,0,0,0,240,239,1,0,0,0,241,
        17,1,0,0,0,242,243,7,1,0,0,243,19,1,0,0,0,244,245,3,22,11,0,245,
        246,3,18,9,0,246,251,1,0,0,0,247,248,3,22,11,0,248,249,5,58,0,0,
        249,251,1,0,0,0,250,244,1,0,0,0,250,247,1,0,0,0,251,21,1,0,0,0,252,
        253,3,24,12,0,253,254,3,22,11,0,254,257,1,0,0,0,255,257,3,24,12,
        0,256,252,1,0,0,0,256,255,1,0,0,0,257,23,1,0,0,0,258,259,5,45,0,
        0,259,260,3,26,13,0,260,261,5,46,0,0,261,25,1,0,0,0,262,263,7,2,
        0,0,263,27,1,0,0,0,264,265,5,6,0,0,265,266,5,58,0,0,266,267,5,32,
        0,0,267,268,3,14,7,0,268,269,3,8,4,0,269,29,1,0,0,0,270,271,5,6,
        0,0,271,272,5,58,0,0,272,273,3,16,8,0,273,274,3,8,4,0,274,31,1,0,
        0,0,275,278,3,34,17,0,276,278,3,42,21,0,277,275,1,0,0,0,277,276,
        1,0,0,0,278,33,1,0,0,0,279,280,5,8,0,0,280,281,5,58,0,0,281,282,
        5,10,0,0,282,283,5,47,0,0,283,284,3,38,19,0,284,285,5,48,0,0,285,
        286,3,8,4,0,286,35,1,0,0,0,287,290,3,38,19,0,288,290,1,0,0,0,289,
        287,1,0,0,0,289,288,1,0,0,0,290,37,1,0,0,0,291,292,3,40,20,0,292,
        293,3,38,19,0,293,296,1,0,0,0,294,296,3,40,20,0,295,291,1,0,0,0,
        295,294,1,0,0,0,296,39,1,0,0,0,297,298,5,58,0,0,298,299,3,16,8,0,
        299,300,3,8,4,0,300,41,1,0,0,0,301,302,5,8,0,0,302,303,5,58,0,0,
        303,304,5,11,0,0,304,305,5,47,0,0,305,306,3,46,23,0,306,307,5,48,
        0,0,307,308,3,8,4,0,308,43,1,0,0,0,309,312,3,46,23,0,310,312,1,0,
        0,0,311,309,1,0,0,0,311,310,1,0,0,0,312,45,1,0,0,0,313,314,3,48,
        24,0,314,315,3,46,23,0,315,318,1,0,0,0,316,318,3,48,24,0,317,313,
        1,0,0,0,317,316,1,0,0,0,318,47,1,0,0,0,319,320,5,58,0,0,320,321,
        5,43,0,0,321,322,3,50,25,0,322,323,5,44,0,0,323,324,3,16,8,0,324,
        325,3,8,4,0,325,333,1,0,0,0,326,327,5,58,0,0,327,328,5,43,0,0,328,
        329,3,50,25,0,329,330,5,44,0,0,330,331,3,8,4,0,331,333,1,0,0,0,332,
        319,1,0,0,0,332,326,1,0,0,0,333,49,1,0,0,0,334,337,3,52,26,0,335,
        337,1,0,0,0,336,334,1,0,0,0,336,335,1,0,0,0,337,51,1,0,0,0,338,339,
        3,54,27,0,339,340,5,40,0,0,340,341,3,52,26,0,341,344,1,0,0,0,342,
        344,3,54,27,0,343,338,1,0,0,0,343,342,1,0,0,0,344,53,1,0,0,0,345,
        346,3,56,28,0,346,347,3,16,8,0,347,55,1,0,0,0,348,349,5,58,0,0,349,
        350,5,40,0,0,350,353,3,56,28,0,351,353,5,58,0,0,352,348,1,0,0,0,
        352,351,1,0,0,0,353,57,1,0,0,0,354,355,5,9,0,0,355,356,5,58,0,0,
        356,357,5,43,0,0,357,358,3,60,30,0,358,359,5,44,0,0,359,360,3,16,
        8,0,360,361,5,47,0,0,361,362,3,66,33,0,362,363,5,48,0,0,363,364,
        3,8,4,0,364,376,1,0,0,0,365,366,5,9,0,0,366,367,5,58,0,0,367,368,
        5,43,0,0,368,369,3,60,30,0,369,370,5,44,0,0,370,371,5,47,0,0,371,
        372,3,66,33,0,372,373,5,48,0,0,373,374,3,8,4,0,374,376,1,0,0,0,375,
        354,1,0,0,0,375,365,1,0,0,0,376,59,1,0,0,0,377,380,3,62,31,0,378,
        380,1,0,0,0,379,377,1,0,0,0,379,378,1,0,0,0,380,61,1,0,0,0,381,382,
        3,64,32,0,382,383,5,40,0,0,383,384,3,62,31,0,384,387,1,0,0,0,385,
        387,3,64,32,0,386,381,1,0,0,0,386,385,1,0,0,0,387,63,1,0,0,0,388,
        389,3,56,28,0,389,390,3,16,8,0,390,65,1,0,0,0,391,392,3,68,34,0,
        392,67,1,0,0,0,393,394,3,70,35,0,394,69,1,0,0,0,395,396,3,110,55,
        0,396,397,3,70,35,0,397,400,1,0,0,0,398,400,3,110,55,0,399,395,1,
        0,0,0,399,398,1,0,0,0,400,71,1,0,0,0,401,402,5,9,0,0,402,403,3,74,
        37,0,403,404,5,58,0,0,404,405,5,43,0,0,405,406,3,60,30,0,406,407,
        5,44,0,0,407,408,3,16,8,0,408,409,5,47,0,0,409,410,3,66,33,0,410,
        411,5,48,0,0,411,412,3,8,4,0,412,425,1,0,0,0,413,414,5,9,0,0,414,
        415,3,74,37,0,415,416,5,58,0,0,416,417,5,43,0,0,417,418,3,60,30,
        0,418,419,5,44,0,0,419,420,5,47,0,0,420,421,3,66,33,0,421,422,5,
        48,0,0,422,423,3,8,4,0,423,425,1,0,0,0,424,401,1,0,0,0,424,413,1,
        0,0,0,425,73,1,0,0,0,426,427,5,43,0,0,427,428,5,58,0,0,428,429,5,
        58,0,0,429,430,5,44,0,0,430,75,1,0,0,0,431,432,6,38,-1,0,432,433,
        3,78,39,0,433,439,1,0,0,0,434,435,10,2,0,0,435,436,5,30,0,0,436,
        438,3,78,39,0,437,434,1,0,0,0,438,441,1,0,0,0,439,437,1,0,0,0,439,
        440,1,0,0,0,440,77,1,0,0,0,441,439,1,0,0,0,442,443,6,39,-1,0,443,
        444,3,80,40,0,444,450,1,0,0,0,445,446,10,2,0,0,446,447,5,29,0,0,
        447,449,3,80,40,0,448,445,1,0,0,0,449,452,1,0,0,0,450,448,1,0,0,
        0,450,451,1,0,0,0,451,79,1,0,0,0,452,450,1,0,0,0,453,454,6,40,-1,
        0,454,455,3,84,42,0,455,462,1,0,0,0,456,457,10,2,0,0,457,458,3,82,
        41,0,458,459,3,84,42,0,459,461,1,0,0,0,460,456,1,0,0,0,461,464,1,
        0,0,0,462,460,1,0,0,0,462,463,1,0,0,0,463,81,1,0,0,0,464,462,1,0,
        0,0,465,466,7,3,0,0,466,83,1,0,0,0,467,468,6,42,-1,0,468,469,3,86,
        43,0,469,478,1,0,0,0,470,471,10,3,0,0,471,472,5,18,0,0,472,477,3,
        86,43,0,473,474,10,2,0,0,474,475,5,19,0,0,475,477,3,86,43,0,476,
        470,1,0,0,0,476,473,1,0,0,0,477,480,1,0,0,0,478,476,1,0,0,0,478,
        479,1,0,0,0,479,85,1,0,0,0,480,478,1,0,0,0,481,482,6,43,-1,0,482,
        483,3,88,44,0,483,495,1,0,0,0,484,485,10,4,0,0,485,486,5,20,0,0,
        486,494,3,88,44,0,487,488,10,3,0,0,488,489,5,21,0,0,489,494,3,88,
        44,0,490,491,10,2,0,0,491,492,5,22,0,0,492,494,3,88,44,0,493,484,
        1,0,0,0,493,487,1,0,0,0,493,490,1,0,0,0,494,497,1,0,0,0,495,493,
        1,0,0,0,495,496,1,0,0,0,496,87,1,0,0,0,497,495,1,0,0,0,498,499,5,
        31,0,0,499,504,3,88,44,0,500,501,5,19,0,0,501,504,3,88,44,0,502,
        504,3,90,45,0,503,498,1,0,0,0,503,500,1,0,0,0,503,502,1,0,0,0,504,
        89,1,0,0,0,505,506,6,45,-1,0,506,507,3,92,46,0,507,518,1,0,0,0,508,
        509,10,3,0,0,509,510,5,45,0,0,510,511,3,76,38,0,511,512,5,46,0,0,
        512,517,1,0,0,0,513,514,10,2,0,0,514,515,5,39,0,0,515,517,3,94,47,
        0,516,508,1,0,0,0,516,513,1,0,0,0,517,520,1,0,0,0,518,516,1,0,0,
        0,518,519,1,0,0,0,519,91,1,0,0,0,520,518,1,0,0,0,521,531,3,104,52,
        0,522,531,5,58,0,0,523,524,5,43,0,0,524,525,3,76,38,0,525,526,5,
        44,0,0,526,531,1,0,0,0,527,531,3,96,48,0,528,531,3,130,65,0,529,
        531,3,140,70,0,530,521,1,0,0,0,530,522,1,0,0,0,530,523,1,0,0,0,530,
        527,1,0,0,0,530,528,1,0,0,0,530,529,1,0,0,0,531,93,1,0,0,0,532,535,
        5,58,0,0,533,535,3,96,48,0,534,532,1,0,0,0,534,533,1,0,0,0,535,95,
        1,0,0,0,536,537,5,58,0,0,537,538,5,43,0,0,538,539,3,98,49,0,539,
        540,5,44,0,0,540,97,1,0,0,0,541,544,3,100,50,0,542,544,1,0,0,0,543,
        541,1,0,0,0,543,542,1,0,0,0,544,99,1,0,0,0,545,546,3,102,51,0,546,
        547,5,40,0,0,547,548,3,100,50,0,548,551,1,0,0,0,549,551,3,102,51,
        0,550,545,1,0,0,0,550,549,1,0,0,0,551,101,1,0,0,0,552,553,3,76,38,
        0,553,103,1,0,0,0,554,560,3,106,53,0,555,560,5,56,0,0,556,560,5,
        57,0,0,557,560,3,108,54,0,558,560,5,49,0,0,559,554,1,0,0,0,559,555,
        1,0,0,0,559,556,1,0,0,0,559,557,1,0,0,0,559,558,1,0,0,0,560,105,
        1,0,0,0,561,562,7,4,0,0,562,107,1,0,0,0,563,564,7,5,0,0,564,109,
        1,0,0,0,565,575,3,10,5,0,566,575,3,6,3,0,567,575,3,112,56,0,568,
        575,3,148,74,0,569,575,3,162,81,0,570,575,3,182,91,0,571,575,3,184,
        92,0,572,575,3,186,93,0,573,575,3,194,97,0,574,565,1,0,0,0,574,566,
        1,0,0,0,574,567,1,0,0,0,574,568,1,0,0,0,574,569,1,0,0,0,574,570,
        1,0,0,0,574,571,1,0,0,0,574,572,1,0,0,0,574,573,1,0,0,0,575,111,
        1,0,0,0,576,577,3,114,57,0,577,578,3,124,62,0,578,579,3,126,63,0,
        579,580,3,8,4,0,580,113,1,0,0,0,581,582,5,58,0,0,582,585,3,116,58,
        0,583,585,5,58,0,0,584,581,1,0,0,0,584,583,1,0,0,0,585,115,1,0,0,
        0,586,587,6,58,-1,0,587,588,3,118,59,0,588,593,1,0,0,0,589,590,10,
        2,0,0,590,592,3,118,59,0,591,589,1,0,0,0,592,595,1,0,0,0,593,591,
        1,0,0,0,593,594,1,0,0,0,594,117,1,0,0,0,595,593,1,0,0,0,596,599,
        3,120,60,0,597,599,3,122,61,0,598,596,1,0,0,0,598,597,1,0,0,0,599,
        119,1,0,0,0,600,601,5,45,0,0,601,602,3,76,38,0,602,603,5,46,0,0,
        603,121,1,0,0,0,604,605,5,39,0,0,605,606,5,58,0,0,606,123,1,0,0,
        0,607,608,7,6,0,0,608,125,1,0,0,0,609,613,3,76,38,0,610,613,3,130,
        65,0,611,613,3,140,70,0,612,609,1,0,0,0,612,610,1,0,0,0,612,611,
        1,0,0,0,613,127,1,0,0,0,614,617,3,130,65,0,615,617,3,132,66,0,616,
        614,1,0,0,0,616,615,1,0,0,0,617,129,1,0,0,0,618,619,3,20,10,0,619,
        620,5,47,0,0,620,621,3,134,67,0,621,622,5,48,0,0,622,131,1,0,0,0,
        623,624,5,47,0,0,624,625,3,134,67,0,625,626,5,48,0,0,626,133,1,0,
        0,0,627,630,3,136,68,0,628,630,1,0,0,0,629,627,1,0,0,0,629,628,1,
        0,0,0,630,135,1,0,0,0,631,632,3,138,69,0,632,633,5,40,0,0,633,634,
        3,136,68,0,634,637,1,0,0,0,635,637,3,138,69,0,636,631,1,0,0,0,636,
        635,1,0,0,0,637,137,1,0,0,0,638,642,3,76,38,0,639,642,3,128,64,0,
        640,642,3,140,70,0,641,638,1,0,0,0,641,639,1,0,0,0,641,640,1,0,0,
        0,642,139,1,0,0,0,643,644,5,58,0,0,644,645,5,47,0,0,645,646,3,142,
        71,0,646,647,5,48,0,0,647,141,1,0,0,0,648,651,3,144,72,0,649,651,
        1,0,0,0,650,648,1,0,0,0,650,649,1,0,0,0,651,143,1,0,0,0,652,653,
        3,146,73,0,653,654,5,40,0,0,654,655,3,144,72,0,655,658,1,0,0,0,656,
        658,3,146,73,0,657,652,1,0,0,0,657,656,1,0,0,0,658,145,1,0,0,0,659,
        660,5,58,0,0,660,661,5,41,0,0,661,662,3,76,38,0,662,147,1,0,0,0,
        663,666,3,150,75,0,664,666,3,152,76,0,665,663,1,0,0,0,665,664,1,
        0,0,0,666,149,1,0,0,0,667,668,5,12,0,0,668,669,5,43,0,0,669,670,
        3,154,77,0,670,671,5,44,0,0,671,672,5,47,0,0,672,673,3,156,78,0,
        673,674,5,48,0,0,674,675,3,8,4,0,675,151,1,0,0,0,676,677,5,12,0,
        0,677,678,5,43,0,0,678,679,3,154,77,0,679,680,5,44,0,0,680,681,5,
        47,0,0,681,682,3,156,78,0,682,683,5,48,0,0,683,684,3,158,79,0,684,
        153,1,0,0,0,685,686,3,76,38,0,686,155,1,0,0,0,687,688,3,68,34,0,
        688,157,1,0,0,0,689,690,5,13,0,0,690,698,3,148,74,0,691,692,5,13,
        0,0,692,693,5,47,0,0,693,694,3,160,80,0,694,695,5,48,0,0,695,696,
        3,8,4,0,696,698,1,0,0,0,697,689,1,0,0,0,697,691,1,0,0,0,698,159,
        1,0,0,0,699,700,3,68,34,0,700,161,1,0,0,0,701,705,3,164,82,0,702,
        705,3,166,83,0,703,705,3,172,86,0,704,701,1,0,0,0,704,702,1,0,0,
        0,704,703,1,0,0,0,705,163,1,0,0,0,706,707,5,14,0,0,707,708,3,154,
        77,0,708,709,5,47,0,0,709,710,3,180,90,0,710,711,5,48,0,0,711,712,
        3,8,4,0,712,165,1,0,0,0,713,714,5,14,0,0,714,715,3,168,84,0,715,
        716,5,42,0,0,716,717,3,154,77,0,717,718,5,42,0,0,718,719,3,170,85,
        0,719,720,5,47,0,0,720,721,3,180,90,0,721,722,5,48,0,0,722,723,3,
        8,4,0,723,167,1,0,0,0,724,725,5,58,0,0,725,726,5,33,0,0,726,738,
        3,76,38,0,727,728,5,6,0,0,728,729,5,58,0,0,729,730,3,16,8,0,730,
        731,5,32,0,0,731,732,3,76,38,0,732,738,1,0,0,0,733,734,5,6,0,0,734,
        735,5,58,0,0,735,736,5,32,0,0,736,738,3,76,38,0,737,724,1,0,0,0,
        737,727,1,0,0,0,737,733,1,0,0,0,738,169,1,0,0,0,739,740,5,58,0,0,
        740,741,3,124,62,0,741,742,3,76,38,0,742,171,1,0,0,0,743,744,5,14,
        0,0,744,745,3,176,88,0,745,746,5,40,0,0,746,747,3,178,89,0,747,748,
        5,33,0,0,748,749,5,17,0,0,749,750,3,174,87,0,750,751,5,47,0,0,751,
        752,3,180,90,0,752,753,5,48,0,0,753,754,3,8,4,0,754,173,1,0,0,0,
        755,759,5,58,0,0,756,759,3,130,65,0,757,759,3,76,38,0,758,755,1,
        0,0,0,758,756,1,0,0,0,758,757,1,0,0,0,759,175,1,0,0,0,760,761,5,
        58,0,0,761,177,1,0,0,0,762,763,5,58,0,0,763,179,1,0,0,0,764,765,
        3,68,34,0,765,181,1,0,0,0,766,767,5,16,0,0,767,768,3,8,4,0,768,183,
        1,0,0,0,769,770,5,15,0,0,770,771,3,8,4,0,771,185,1,0,0,0,772,775,
        3,188,94,0,773,775,3,190,95,0,774,772,1,0,0,0,774,773,1,0,0,0,775,
        187,1,0,0,0,776,777,3,96,48,0,777,778,3,8,4,0,778,189,1,0,0,0,779,
        780,3,192,96,0,780,781,3,8,4,0,781,191,1,0,0,0,782,783,3,76,38,0,
        783,784,5,39,0,0,784,785,3,96,48,0,785,193,1,0,0,0,786,787,5,7,0,
        0,787,793,3,8,4,0,788,789,5,7,0,0,789,790,3,76,38,0,790,791,3,8,
        4,0,791,793,1,0,0,0,792,786,1,0,0,0,792,788,1,0,0,0,793,195,1,0,
        0,0,54,203,210,223,235,240,250,256,277,289,295,311,317,332,336,343,
        352,375,379,386,399,424,439,450,462,476,478,493,495,503,516,518,
        530,534,543,550,559,574,584,593,598,612,616,629,636,641,650,657,
        665,697,704,737,758,774,792
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'string'", "'boolean'", 
                     "'const'", "'var'", "'return'", "'type'", "'func'", 
                     "'struct'", "'interface'", "'if'", "'else'", "'for'", 
                     "'continue'", "'break'", "'range'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'&&'", "'||'", "'!'", "'='", "':='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'.'", "','", "':'", 
                     "';'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'nil'", 
                     "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "Key_type_int", "Key_type_float", "Key_type_string", 
                      "Key_type_boolean", "Key_decl_const", "Key_decl_var", 
                      "Key_return", "Key_type", "Key_func", "Key_struct", 
                      "Key_interface", "Key_if", "Key_else", "Key_loop_for", 
                      "Key_loop_continue", "Key_loop_break", "Key_range", 
                      "Ope_plus", "Ope_minus", "Ope_multi", "Ope_div", "Ope_mod", 
                      "Ope_equal", "Ope_nequal", "Ope_let", "Ope_leq", "Ope_get", 
                      "Ope_geq", "Ope_and", "Ope_or", "Ope_not", "Ope_assign", 
                      "Ope_init", "Ope_assign_plus", "Ope_assign_minus", 
                      "Ope_assign_multi", "Ope_assign_div", "Ope_assign_mod", 
                      "Ope_select", "Comma", "Colon", "Semicolon", "Lparen", 
                      "Rparen", "Lsquare", "Rsquare", "Lcurly", "Rcurly", 
                      "Literal_nil", "Literal_true", "Literal_false", "Literal_dec", 
                      "Literal_bin", "Literal_oct", "Literal_hex", "Literal_float", 
                      "Literal_string", "Identifier", "NL", "WS", "SL_COMMENT", 
                      "ML_COMMENT", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_const_decl = 3
    RULE_end_stmt = 4
    RULE_var_decl = 5
    RULE_var_decl_expl = 6
    RULE_var_value = 7
    RULE_data_type = 8
    RULE_primitive_type = 9
    RULE_array_type = 10
    RULE_dimension_list = 11
    RULE_dimension = 12
    RULE_size = 13
    RULE_var_decl_infer = 14
    RULE_var_decl_nil = 15
    RULE_type_decl = 16
    RULE_struct_decl = 17
    RULE_field_set = 18
    RULE_field_list = 19
    RULE_field_decl = 20
    RULE_interface_decl = 21
    RULE_interface_method_set = 22
    RULE_interface_method_list = 23
    RULE_interface_method_decl = 24
    RULE_interface_method_param_set = 25
    RULE_interface_method_param_list = 26
    RULE_interface_method_param = 27
    RULE_id_list = 28
    RULE_func_decl = 29
    RULE_param_set = 30
    RULE_param_list = 31
    RULE_param = 32
    RULE_func_body = 33
    RULE_stmt_set = 34
    RULE_stmt_list = 35
    RULE_method_decl = 36
    RULE_receiver = 37
    RULE_expr = 38
    RULE_expr1 = 39
    RULE_expr2 = 40
    RULE_ope_relation = 41
    RULE_expr3 = 42
    RULE_expr4 = 43
    RULE_expr5 = 44
    RULE_expr6 = 45
    RULE_expr7 = 46
    RULE_expr8 = 47
    RULE_func_call = 48
    RULE_argument_set = 49
    RULE_argument_list = 50
    RULE_argument = 51
    RULE_prim_literal = 52
    RULE_literal_int = 53
    RULE_literal_bool = 54
    RULE_stmt = 55
    RULE_assign_stmt = 56
    RULE_lhs = 57
    RULE_access_list = 58
    RULE_access = 59
    RULE_array_access = 60
    RULE_struct_access = 61
    RULE_ope_assign = 62
    RULE_rhs = 63
    RULE_literal_array = 64
    RULE_full_array_literal = 65
    RULE_partial_array_literal = 66
    RULE_array_element_set = 67
    RULE_array_element_list = 68
    RULE_array_element = 69
    RULE_literal_struct = 70
    RULE_struct_element_set = 71
    RULE_struct_element_list = 72
    RULE_struct_element = 73
    RULE_if_stmt = 74
    RULE_matched = 75
    RULE_unmatched = 76
    RULE_condition = 77
    RULE_if_stmt_body = 78
    RULE_else_stmt_list = 79
    RULE_else_stmt_body = 80
    RULE_for_stmt = 81
    RULE_for_basic = 82
    RULE_for_icu = 83
    RULE_init = 84
    RULE_update = 85
    RULE_for_range = 86
    RULE_array_instance = 87
    RULE_index = 88
    RULE_value = 89
    RULE_for_body = 90
    RULE_break_stmt = 91
    RULE_continue_stmt = 92
    RULE_call_stmt = 93
    RULE_func_call_stmt = 94
    RULE_method_call_stmt = 95
    RULE_method_call = 96
    RULE_return_stmt = 97

    ruleNames =  [ "program", "decllist", "decl", "const_decl", "end_stmt", 
                   "var_decl", "var_decl_expl", "var_value", "data_type", 
                   "primitive_type", "array_type", "dimension_list", "dimension", 
                   "size", "var_decl_infer", "var_decl_nil", "type_decl", 
                   "struct_decl", "field_set", "field_list", "field_decl", 
                   "interface_decl", "interface_method_set", "interface_method_list", 
                   "interface_method_decl", "interface_method_param_set", 
                   "interface_method_param_list", "interface_method_param", 
                   "id_list", "func_decl", "param_set", "param_list", "param", 
                   "func_body", "stmt_set", "stmt_list", "method_decl", 
                   "receiver", "expr", "expr1", "expr2", "ope_relation", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "func_call", "argument_set", "argument_list", "argument", 
                   "prim_literal", "literal_int", "literal_bool", "stmt", 
                   "assign_stmt", "lhs", "access_list", "access", "array_access", 
                   "struct_access", "ope_assign", "rhs", "literal_array", 
                   "full_array_literal", "partial_array_literal", "array_element_set", 
                   "array_element_list", "array_element", "literal_struct", 
                   "struct_element_set", "struct_element_list", "struct_element", 
                   "if_stmt", "matched", "unmatched", "condition", "if_stmt_body", 
                   "else_stmt_list", "else_stmt_body", "for_stmt", "for_basic", 
                   "for_icu", "init", "update", "for_range", "array_instance", 
                   "index", "value", "for_body", "break_stmt", "continue_stmt", 
                   "call_stmt", "func_call_stmt", "method_call_stmt", "method_call", 
                   "return_stmt" ]

    EOF = Token.EOF
    Key_type_int=1
    Key_type_float=2
    Key_type_string=3
    Key_type_boolean=4
    Key_decl_const=5
    Key_decl_var=6
    Key_return=7
    Key_type=8
    Key_func=9
    Key_struct=10
    Key_interface=11
    Key_if=12
    Key_else=13
    Key_loop_for=14
    Key_loop_continue=15
    Key_loop_break=16
    Key_range=17
    Ope_plus=18
    Ope_minus=19
    Ope_multi=20
    Ope_div=21
    Ope_mod=22
    Ope_equal=23
    Ope_nequal=24
    Ope_let=25
    Ope_leq=26
    Ope_get=27
    Ope_geq=28
    Ope_and=29
    Ope_or=30
    Ope_not=31
    Ope_assign=32
    Ope_init=33
    Ope_assign_plus=34
    Ope_assign_minus=35
    Ope_assign_multi=36
    Ope_assign_div=37
    Ope_assign_mod=38
    Ope_select=39
    Comma=40
    Colon=41
    Semicolon=42
    Lparen=43
    Rparen=44
    Lsquare=45
    Rsquare=46
    Lcurly=47
    Rcurly=48
    Literal_nil=49
    Literal_true=50
    Literal_false=51
    Literal_dec=52
    Literal_bin=53
    Literal_oct=54
    Literal_hex=55
    Literal_float=56
    Literal_string=57
    Identifier=58
    NL=59
    WS=60
    SL_COMMENT=61
    ML_COMMENT=62
    UNCLOSE_STRING=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.decllist()
            self.state = 197
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decllist




    def decllist(self):

        localctx = MiniGoParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.decl()
                self.state = 200
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def type_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Type_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.const_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.type_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.func_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 209
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_decl_const(self):
            return self.getToken(MiniGoParser.Key_decl_const, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Ope_assign(self):
            return self.getToken(MiniGoParser.Ope_assign, 0)

        def var_value(self):
            return self.getTypedRuleContext(MiniGoParser.Var_valueContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MiniGoParser.Key_decl_const)
            self.state = 213
            self.match(MiniGoParser.Identifier)
            self.state = 214
            self.match(MiniGoParser.Ope_assign)
            self.state = 215
            self.var_value()
            self.state = 216
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def Semicolon(self):
            return self.getToken(MiniGoParser.Semicolon, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_stmt




    def end_stmt(self):

        localctx = MiniGoParser.End_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_end_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            _la = self._input.LA(1)
            if not(_la==42 or _la==59):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_expl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_explContext,0)


        def var_decl_infer(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_inferContext,0)


        def var_decl_nil(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_nilContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_decl)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.var_decl_expl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.var_decl_infer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.var_decl_nil()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_explContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_decl_var(self):
            return self.getToken(MiniGoParser.Key_decl_var, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def Ope_assign(self):
            return self.getToken(MiniGoParser.Ope_assign, 0)

        def var_value(self):
            return self.getTypedRuleContext(MiniGoParser.Var_valueContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_expl




    def var_decl_expl(self):

        localctx = MiniGoParser.Var_decl_explContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_decl_expl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MiniGoParser.Key_decl_var)
            self.state = 226
            self.match(MiniGoParser.Identifier)
            self.state = 227
            self.data_type()
            self.state = 228
            self.match(MiniGoParser.Ope_assign)
            self.state = 229
            self.var_value()
            self.state = 230
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def literal_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_value




    def var_value(self):

        localctx = MiniGoParser.Var_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_value)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.full_array_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.literal_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_data_type)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.primitive_type()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(MiniGoParser.Identifier)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_type_int(self):
            return self.getToken(MiniGoParser.Key_type_int, 0)

        def Key_type_float(self):
            return self.getToken(MiniGoParser.Key_type_float, 0)

        def Key_type_boolean(self):
            return self.getToken(MiniGoParser.Key_type_boolean, 0)

        def Key_type_string(self):
            return self.getToken(MiniGoParser.Key_type_string, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_type)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.dimension_list()
                self.state = 245
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.dimension_list()
                self.state = 248
                self.match(MiniGoParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionContext,0)


        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_list




    def dimension_list(self):

        localctx = MiniGoParser.Dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dimension_list)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.dimension()
                self.state = 253
                self.dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.dimension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lsquare(self):
            return self.getToken(MiniGoParser.Lsquare, 0)

        def size(self):
            return self.getTypedRuleContext(MiniGoParser.SizeContext,0)


        def Rsquare(self):
            return self.getToken(MiniGoParser.Rsquare, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension




    def dimension(self):

        localctx = MiniGoParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(MiniGoParser.Lsquare)
            self.state = 259
            self.size()
            self.state = 260
            self.match(MiniGoParser.Rsquare)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Literal_bin(self):
            return self.getToken(MiniGoParser.Literal_bin, 0)

        def Literal_hex(self):
            return self.getToken(MiniGoParser.Literal_hex, 0)

        def Literal_oct(self):
            return self.getToken(MiniGoParser.Literal_oct, 0)

        def Literal_dec(self):
            return self.getToken(MiniGoParser.Literal_dec, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_size




    def size(self):

        localctx = MiniGoParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 355784370562269184) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_inferContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_decl_var(self):
            return self.getToken(MiniGoParser.Key_decl_var, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Ope_assign(self):
            return self.getToken(MiniGoParser.Ope_assign, 0)

        def var_value(self):
            return self.getTypedRuleContext(MiniGoParser.Var_valueContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_infer




    def var_decl_infer(self):

        localctx = MiniGoParser.Var_decl_inferContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_decl_infer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(MiniGoParser.Key_decl_var)
            self.state = 265
            self.match(MiniGoParser.Identifier)
            self.state = 266
            self.match(MiniGoParser.Ope_assign)
            self.state = 267
            self.var_value()
            self.state = 268
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_nilContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_decl_var(self):
            return self.getToken(MiniGoParser.Key_decl_var, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_nil




    def var_decl_nil(self):

        localctx = MiniGoParser.Var_decl_nilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var_decl_nil)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(MiniGoParser.Key_decl_var)
            self.state = 271
            self.match(MiniGoParser.Identifier)
            self.state = 272
            self.data_type()
            self.state = 273
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_decl




    def type_decl(self):

        localctx = MiniGoParser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type_decl)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.struct_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.interface_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_type(self):
            return self.getToken(MiniGoParser.Key_type, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Key_struct(self):
            return self.getToken(MiniGoParser.Key_struct, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MiniGoParser.Key_type)
            self.state = 280
            self.match(MiniGoParser.Identifier)
            self.state = 281
            self.match(MiniGoParser.Key_struct)
            self.state = 282
            self.match(MiniGoParser.Lcurly)
            self.state = 283
            self.field_list()
            self.state = 284
            self.match(MiniGoParser.Rcurly)
            self.state = 285
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_set




    def field_set(self):

        localctx = MiniGoParser.Field_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_field_set)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.field_list()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Field_declContext,0)


        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_list




    def field_list(self):

        localctx = MiniGoParser.Field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_field_list)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.field_decl()
                self.state = 292
                self.field_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.field_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_decl




    def field_decl(self):

        localctx = MiniGoParser.Field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MiniGoParser.Identifier)
            self.state = 298
            self.data_type()
            self.state = 299
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_type(self):
            return self.getToken(MiniGoParser.Key_type, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Key_interface(self):
            return self.getToken(MiniGoParser.Key_interface, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(MiniGoParser.Key_type)
            self.state = 302
            self.match(MiniGoParser.Identifier)
            self.state = 303
            self.match(MiniGoParser.Key_interface)
            self.state = 304
            self.match(MiniGoParser.Lcurly)
            self.state = 305
            self.interface_method_list()
            self.state = 306
            self.match(MiniGoParser.Rcurly)
            self.state = 307
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_set




    def interface_method_set(self):

        localctx = MiniGoParser.Interface_method_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_interface_method_set)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.interface_method_list()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_declContext,0)


        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_list




    def interface_method_list(self):

        localctx = MiniGoParser.Interface_method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_interface_method_list)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.interface_method_decl()
                self.state = 314
                self.interface_method_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.interface_method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def interface_method_param_set(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_param_setContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_decl




    def interface_method_decl(self):

        localctx = MiniGoParser.Interface_method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_interface_method_decl)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(MiniGoParser.Identifier)
                self.state = 320
                self.match(MiniGoParser.Lparen)
                self.state = 321
                self.interface_method_param_set()
                self.state = 322
                self.match(MiniGoParser.Rparen)
                self.state = 323
                self.data_type()
                self.state = 324
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.match(MiniGoParser.Identifier)
                self.state = 327
                self.match(MiniGoParser.Lparen)
                self.state = 328
                self.interface_method_param_set()
                self.state = 329
                self.match(MiniGoParser.Rparen)
                self.state = 330
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_param_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_param_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_param_set




    def interface_method_param_set(self):

        localctx = MiniGoParser.Interface_method_param_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_interface_method_param_set)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.interface_method_param_list()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_param(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_paramContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def interface_method_param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_param_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_param_list




    def interface_method_param_list(self):

        localctx = MiniGoParser.Interface_method_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_interface_method_param_list)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.interface_method_param()
                self.state = 339
                self.match(MiniGoParser.Comma)
                self.state = 340
                self.interface_method_param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.interface_method_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_param




    def interface_method_param(self):

        localctx = MiniGoParser.Interface_method_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_interface_method_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.id_list()
            self.state = 346
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_list




    def id_list(self):

        localctx = MiniGoParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_id_list)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(MiniGoParser.Identifier)
                self.state = 349
                self.match(MiniGoParser.Comma)
                self.state = 350
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(MiniGoParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_func(self):
            return self.getToken(MiniGoParser.Key_func, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def param_set(self):
            return self.getTypedRuleContext(MiniGoParser.Param_setContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def func_body(self):
            return self.getTypedRuleContext(MiniGoParser.Func_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_decl)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(MiniGoParser.Key_func)
                self.state = 355
                self.match(MiniGoParser.Identifier)
                self.state = 356
                self.match(MiniGoParser.Lparen)
                self.state = 357
                self.param_set()
                self.state = 358
                self.match(MiniGoParser.Rparen)
                self.state = 359
                self.data_type()
                self.state = 360
                self.match(MiniGoParser.Lcurly)
                self.state = 361
                self.func_body()
                self.state = 362
                self.match(MiniGoParser.Rcurly)
                self.state = 363
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.match(MiniGoParser.Key_func)
                self.state = 366
                self.match(MiniGoParser.Identifier)
                self.state = 367
                self.match(MiniGoParser.Lparen)
                self.state = 368
                self.param_set()
                self.state = 369
                self.match(MiniGoParser.Rparen)
                self.state = 370
                self.match(MiniGoParser.Lcurly)
                self.state = 371
                self.func_body()
                self.state = 372
                self.match(MiniGoParser.Rcurly)
                self.state = 373
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_set




    def param_set(self):

        localctx = MiniGoParser.Param_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_param_set)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.param_list()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_list




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_param_list)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.param()
                self.state = 382
                self.match(MiniGoParser.Comma)
                self.state = 383
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.id_list()
            self.state = 389
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_set(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_setContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_body




    def func_body(self):

        localctx = MiniGoParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.stmt_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_set




    def stmt_set(self):

        localctx = MiniGoParser.Stmt_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stmt_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_list




    def stmt_list(self):

        localctx = MiniGoParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_stmt_list)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.stmt()
                self.state = 396
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_func(self):
            return self.getToken(MiniGoParser.Key_func, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def param_set(self):
            return self.getTypedRuleContext(MiniGoParser.Param_setContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def func_body(self):
            return self.getTypedRuleContext(MiniGoParser.Func_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_decl)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(MiniGoParser.Key_func)
                self.state = 402
                self.receiver()
                self.state = 403
                self.match(MiniGoParser.Identifier)
                self.state = 404
                self.match(MiniGoParser.Lparen)
                self.state = 405
                self.param_set()
                self.state = 406
                self.match(MiniGoParser.Rparen)
                self.state = 407
                self.data_type()
                self.state = 408
                self.match(MiniGoParser.Lcurly)
                self.state = 409
                self.func_body()
                self.state = 410
                self.match(MiniGoParser.Rcurly)
                self.state = 411
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.match(MiniGoParser.Key_func)
                self.state = 414
                self.receiver()
                self.state = 415
                self.match(MiniGoParser.Identifier)
                self.state = 416
                self.match(MiniGoParser.Lparen)
                self.state = 417
                self.param_set()
                self.state = 418
                self.match(MiniGoParser.Rparen)
                self.state = 419
                self.match(MiniGoParser.Lcurly)
                self.state = 420
                self.func_body()
                self.state = 421
                self.match(MiniGoParser.Rcurly)
                self.state = 422
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.Identifier)
            else:
                return self.getToken(MiniGoParser.Identifier, i)

        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.Lparen)
            self.state = 427
            self.match(MiniGoParser.Identifier)
            self.state = 428
            self.match(MiniGoParser.Identifier)
            self.state = 429
            self.match(MiniGoParser.Rparen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Ope_or(self):
            return self.getToken(MiniGoParser.Ope_or, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 434
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 435
                    self.match(MiniGoParser.Ope_or)
                    self.state = 436
                    self.expr1(0) 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def Ope_and(self):
            return self.getToken(MiniGoParser.Ope_and, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 445
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 446
                    self.match(MiniGoParser.Ope_and)
                    self.state = 447
                    self.expr2(0) 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def ope_relation(self):
            return self.getTypedRuleContext(MiniGoParser.Ope_relationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 456
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 457
                    self.ope_relation()
                    self.state = 458
                    self.expr3(0) 
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Ope_relationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ope_equal(self):
            return self.getToken(MiniGoParser.Ope_equal, 0)

        def Ope_nequal(self):
            return self.getToken(MiniGoParser.Ope_nequal, 0)

        def Ope_let(self):
            return self.getToken(MiniGoParser.Ope_let, 0)

        def Ope_leq(self):
            return self.getToken(MiniGoParser.Ope_leq, 0)

        def Ope_get(self):
            return self.getToken(MiniGoParser.Ope_get, 0)

        def Ope_geq(self):
            return self.getToken(MiniGoParser.Ope_geq, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ope_relation




    def ope_relation(self):

        localctx = MiniGoParser.Ope_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_ope_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def Ope_plus(self):
            return self.getToken(MiniGoParser.Ope_plus, 0)

        def Ope_minus(self):
            return self.getToken(MiniGoParser.Ope_minus, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 478
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 476
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 470
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 471
                        self.match(MiniGoParser.Ope_plus)
                        self.state = 472
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 473
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 474
                        self.match(MiniGoParser.Ope_minus)
                        self.state = 475
                        self.expr4(0)
                        pass

             
                self.state = 480
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def Ope_multi(self):
            return self.getToken(MiniGoParser.Ope_multi, 0)

        def Ope_div(self):
            return self.getToken(MiniGoParser.Ope_div, 0)

        def Ope_mod(self):
            return self.getToken(MiniGoParser.Ope_mod, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 495
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 493
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 484
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 485
                        self.match(MiniGoParser.Ope_multi)
                        self.state = 486
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 487
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 488
                        self.match(MiniGoParser.Ope_div)
                        self.state = 489
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 490
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 491
                        self.match(MiniGoParser.Ope_mod)
                        self.state = 492
                        self.expr5()
                        pass

             
                self.state = 497
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ope_not(self):
            return self.getToken(MiniGoParser.Ope_not, 0)

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def Ope_minus(self):
            return self.getToken(MiniGoParser.Ope_minus, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr5)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(MiniGoParser.Ope_not)
                self.state = 499
                self.expr5()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.match(MiniGoParser.Ope_minus)
                self.state = 501
                self.expr5()
                pass
            elif token in [43, 45, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]:
                self.enterOuterAlt(localctx, 3)
                self.state = 502
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def Lsquare(self):
            return self.getToken(MiniGoParser.Lsquare, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Rsquare(self):
            return self.getToken(MiniGoParser.Rsquare, 0)

        def Ope_select(self):
            return self.getToken(MiniGoParser.Ope_select, 0)

        def expr8(self):
            return self.getTypedRuleContext(MiniGoParser.Expr8Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 516
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 508
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 509
                        self.match(MiniGoParser.Lsquare)
                        self.state = 510
                        self.expr(0)
                        self.state = 511
                        self.match(MiniGoParser.Rsquare)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 513
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 514
                        self.match(MiniGoParser.Ope_select)
                        self.state = 515
                        self.expr8()
                        pass

             
                self.state = 520
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Prim_literalContext,0)


        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def literal_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr7)
        try:
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.prim_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(MiniGoParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.match(MiniGoParser.Lparen)
                self.state = 524
                self.expr(0)
                self.state = 525
                self.match(MiniGoParser.Rparen)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 527
                self.func_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 528
                self.full_array_literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 529
                self.literal_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr8




    def expr8(self):

        localctx = MiniGoParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr8)
        try:
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(MiniGoParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def argument_set(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_setContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(MiniGoParser.Identifier)
            self.state = 537
            self.match(MiniGoParser.Lparen)
            self.state = 538
            self.argument_set()
            self.state = 539
            self.match(MiniGoParser.Rparen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument_list(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_set




    def argument_set(self):

        localctx = MiniGoParser.Argument_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_argument_set)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 31, 43, 45, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.argument_list()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_list




    def argument_list(self):

        localctx = MiniGoParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_argument_list)
        try:
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.argument()
                self.state = 546
                self.match(MiniGoParser.Comma)
                self.state = 547
                self.argument_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument




    def argument(self):

        localctx = MiniGoParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_int(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_intContext,0)


        def Literal_float(self):
            return self.getToken(MiniGoParser.Literal_float, 0)

        def Literal_string(self):
            return self.getToken(MiniGoParser.Literal_string, 0)

        def literal_bool(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_boolContext,0)


        def Literal_nil(self):
            return self.getToken(MiniGoParser.Literal_nil, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_prim_literal




    def prim_literal(self):

        localctx = MiniGoParser.Prim_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_prim_literal)
        try:
            self.state = 559
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52, 53, 54, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.literal_int()
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
                self.match(MiniGoParser.Literal_float)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.match(MiniGoParser.Literal_string)
                pass
            elif token in [50, 51]:
                self.enterOuterAlt(localctx, 4)
                self.state = 557
                self.literal_bool()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 5)
                self.state = 558
                self.match(MiniGoParser.Literal_nil)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Literal_dec(self):
            return self.getToken(MiniGoParser.Literal_dec, 0)

        def Literal_bin(self):
            return self.getToken(MiniGoParser.Literal_bin, 0)

        def Literal_hex(self):
            return self.getToken(MiniGoParser.Literal_hex, 0)

        def Literal_oct(self):
            return self.getToken(MiniGoParser.Literal_oct, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_int




    def literal_int(self):

        localctx = MiniGoParser.Literal_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_literal_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67553994410557440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Literal_false(self):
            return self.getToken(MiniGoParser.Literal_false, 0)

        def Literal_true(self):
            return self.getToken(MiniGoParser.Literal_true, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_bool




    def literal_bool(self):

        localctx = MiniGoParser.Literal_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_literal_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            _la = self._input.LA(1)
            if not(_la==50 or _la==51):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_stmt)
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 567
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 568
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 569
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 570
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 571
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 572
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 573
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def ope_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Ope_assignContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MiniGoParser.RhsContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.lhs()
            self.state = 577
            self.ope_assign()
            self.state = 578
            self.rhs()
            self.state = 579
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def access_list(self):
            return self.getTypedRuleContext(MiniGoParser.Access_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_lhs)
        try:
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.match(MiniGoParser.Identifier)
                self.state = 582
                self.access_list(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 583
                self.match(MiniGoParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def access(self):
            return self.getTypedRuleContext(MiniGoParser.AccessContext,0)


        def access_list(self):
            return self.getTypedRuleContext(MiniGoParser.Access_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_access_list



    def access_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Access_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_access_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.access()
            self._ctx.stop = self._input.LT(-1)
            self.state = 593
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Access_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_access_list)
                    self.state = 589
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 590
                    self.access() 
                self.state = 595
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_access




    def access(self):

        localctx = MiniGoParser.AccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_access)
        try:
            self.state = 598
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 596
                self.array_access()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
                self.struct_access()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lsquare(self):
            return self.getToken(MiniGoParser.Lsquare, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Rsquare(self):
            return self.getToken(MiniGoParser.Rsquare, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(MiniGoParser.Lsquare)
            self.state = 601
            self.expr(0)
            self.state = 602
            self.match(MiniGoParser.Rsquare)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ope_select(self):
            return self.getToken(MiniGoParser.Ope_select, 0)

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.Ope_select)
            self.state = 605
            self.match(MiniGoParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ope_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ope_init(self):
            return self.getToken(MiniGoParser.Ope_init, 0)

        def Ope_assign_div(self):
            return self.getToken(MiniGoParser.Ope_assign_div, 0)

        def Ope_assign_minus(self):
            return self.getToken(MiniGoParser.Ope_assign_minus, 0)

        def Ope_assign_mod(self):
            return self.getToken(MiniGoParser.Ope_assign_mod, 0)

        def Ope_assign_multi(self):
            return self.getToken(MiniGoParser.Ope_assign_multi, 0)

        def Ope_assign_plus(self):
            return self.getToken(MiniGoParser.Ope_assign_plus, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ope_assign




    def ope_assign(self):

        localctx = MiniGoParser.Ope_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_ope_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 541165879296) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def literal_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rhs




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_rhs)
        try:
            self.state = 612
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 609
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
                self.full_array_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 611
                self.literal_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def partial_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Partial_array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_array




    def literal_array(self):

        localctx = MiniGoParser.Literal_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_literal_array)
        try:
            self.state = 616
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self.full_array_literal()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 615
                self.partial_array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Full_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def array_element_set(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_setContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_full_array_literal




    def full_array_literal(self):

        localctx = MiniGoParser.Full_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_full_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.array_type()
            self.state = 619
            self.match(MiniGoParser.Lcurly)
            self.state = 620
            self.array_element_set()
            self.state = 621
            self.match(MiniGoParser.Rcurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Partial_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def array_element_set(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_setContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_partial_array_literal




    def partial_array_literal(self):

        localctx = MiniGoParser.Partial_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_partial_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.match(MiniGoParser.Lcurly)
            self.state = 624
            self.array_element_set()
            self.state = 625
            self.match(MiniGoParser.Rcurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element_set




    def array_element_set(self):

        localctx = MiniGoParser.Array_element_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_array_element_set)
        try:
            self.state = 629
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 31, 43, 45, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 627
                self.array_element_list()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element_list




    def array_element_list(self):

        localctx = MiniGoParser.Array_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_array_element_list)
        try:
            self.state = 636
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 631
                self.array_element()
                self.state = 632
                self.match(MiniGoParser.Comma)
                self.state = 633
                self.array_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 635
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def literal_array(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_arrayContext,0)


        def literal_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_array_element)
        try:
            self.state = 641
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 638
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 639
                self.literal_array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 640
                self.literal_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def struct_element_set(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_element_setContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_struct




    def literal_struct(self):

        localctx = MiniGoParser.Literal_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_literal_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.match(MiniGoParser.Identifier)
            self.state = 644
            self.match(MiniGoParser.Lcurly)
            self.state = 645
            self.struct_element_set()
            self.state = 646
            self.match(MiniGoParser.Rcurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_element_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element_set




    def struct_element_set(self):

        localctx = MiniGoParser.Struct_element_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_struct_element_set)
        try:
            self.state = 650
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 648
                self.struct_element_list()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def struct_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element_list




    def struct_element_list(self):

        localctx = MiniGoParser.Struct_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_struct_element_list)
        try:
            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 652
                self.struct_element()
                self.state = 653
                self.match(MiniGoParser.Comma)
                self.state = 654
                self.struct_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 656
                self.struct_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Colon(self):
            return self.getToken(MiniGoParser.Colon, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element




    def struct_element(self):

        localctx = MiniGoParser.Struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_struct_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 659
            self.match(MiniGoParser.Identifier)
            self.state = 660
            self.match(MiniGoParser.Colon)
            self.state = 661
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matched(self):
            return self.getTypedRuleContext(MiniGoParser.MatchedContext,0)


        def unmatched(self):
            return self.getTypedRuleContext(MiniGoParser.UnmatchedContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_if_stmt)
        try:
            self.state = 665
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.matched()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 664
                self.unmatched()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_if(self):
            return self.getToken(MiniGoParser.Key_if, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def if_stmt_body(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_matched




    def matched(self):

        localctx = MiniGoParser.MatchedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_matched)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.match(MiniGoParser.Key_if)
            self.state = 668
            self.match(MiniGoParser.Lparen)
            self.state = 669
            self.condition()
            self.state = 670
            self.match(MiniGoParser.Rparen)
            self.state = 671
            self.match(MiniGoParser.Lcurly)
            self.state = 672
            self.if_stmt_body()
            self.state = 673
            self.match(MiniGoParser.Rcurly)
            self.state = 674
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnmatchedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_if(self):
            return self.getToken(MiniGoParser.Key_if, 0)

        def Lparen(self):
            return self.getToken(MiniGoParser.Lparen, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def Rparen(self):
            return self.getToken(MiniGoParser.Rparen, 0)

        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def if_stmt_body(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def else_stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unmatched




    def unmatched(self):

        localctx = MiniGoParser.UnmatchedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_unmatched)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
            self.match(MiniGoParser.Key_if)
            self.state = 677
            self.match(MiniGoParser.Lparen)
            self.state = 678
            self.condition()
            self.state = 679
            self.match(MiniGoParser.Rparen)
            self.state = 680
            self.match(MiniGoParser.Lcurly)
            self.state = 681
            self.if_stmt_body()
            self.state = 682
            self.match(MiniGoParser.Rcurly)
            self.state = 683
            self.else_stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condition




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmt_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_set(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_setContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt_body




    def if_stmt_body(self):

        localctx = MiniGoParser.If_stmt_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_if_stmt_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self.stmt_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_else(self):
            return self.getToken(MiniGoParser.Key_else, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def else_stmt_body(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmt_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt_list




    def else_stmt_list(self):

        localctx = MiniGoParser.Else_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_else_stmt_list)
        try:
            self.state = 697
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 689
                self.match(MiniGoParser.Key_else)
                self.state = 690
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 691
                self.match(MiniGoParser.Key_else)
                self.state = 692
                self.match(MiniGoParser.Lcurly)
                self.state = 693
                self.else_stmt_body()
                self.state = 694
                self.match(MiniGoParser.Rcurly)
                self.state = 695
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmt_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_set(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_setContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt_body




    def else_stmt_body(self):

        localctx = MiniGoParser.Else_stmt_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_else_stmt_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            self.stmt_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_basic(self):
            return self.getTypedRuleContext(MiniGoParser.For_basicContext,0)


        def for_icu(self):
            return self.getTypedRuleContext(MiniGoParser.For_icuContext,0)


        def for_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_for_stmt)
        try:
            self.state = 704
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 701
                self.for_basic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 702
                self.for_icu()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 703
                self.for_range()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_basicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_for(self):
            return self.getToken(MiniGoParser.Key_loop_for, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def for_body(self):
            return self.getTypedRuleContext(MiniGoParser.For_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_basic




    def for_basic(self):

        localctx = MiniGoParser.For_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_for_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(MiniGoParser.Key_loop_for)
            self.state = 707
            self.condition()
            self.state = 708
            self.match(MiniGoParser.Lcurly)
            self.state = 709
            self.for_body()
            self.state = 710
            self.match(MiniGoParser.Rcurly)
            self.state = 711
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_icuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_for(self):
            return self.getToken(MiniGoParser.Key_loop_for, 0)

        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.Semicolon)
            else:
                return self.getToken(MiniGoParser.Semicolon, i)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def for_body(self):
            return self.getTypedRuleContext(MiniGoParser.For_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_icu




    def for_icu(self):

        localctx = MiniGoParser.For_icuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_for_icu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 713
            self.match(MiniGoParser.Key_loop_for)
            self.state = 714
            self.init()
            self.state = 715
            self.match(MiniGoParser.Semicolon)
            self.state = 716
            self.condition()
            self.state = 717
            self.match(MiniGoParser.Semicolon)
            self.state = 718
            self.update()
            self.state = 719
            self.match(MiniGoParser.Lcurly)
            self.state = 720
            self.for_body()
            self.state = 721
            self.match(MiniGoParser.Rcurly)
            self.state = 722
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def Ope_init(self):
            return self.getToken(MiniGoParser.Ope_init, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Key_decl_var(self):
            return self.getToken(MiniGoParser.Key_decl_var, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def Ope_assign(self):
            return self.getToken(MiniGoParser.Ope_assign, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_init




    def init(self):

        localctx = MiniGoParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_init)
        try:
            self.state = 737
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 724
                self.match(MiniGoParser.Identifier)
                self.state = 725
                self.match(MiniGoParser.Ope_init)
                self.state = 726
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 727
                self.match(MiniGoParser.Key_decl_var)
                self.state = 728
                self.match(MiniGoParser.Identifier)
                self.state = 729
                self.data_type()
                self.state = 730
                self.match(MiniGoParser.Ope_assign)
                self.state = 731
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 733
                self.match(MiniGoParser.Key_decl_var)
                self.state = 734
                self.match(MiniGoParser.Identifier)
                self.state = 735
                self.match(MiniGoParser.Ope_assign)
                self.state = 736
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def ope_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Ope_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
            self.match(MiniGoParser.Identifier)
            self.state = 740
            self.ope_assign()
            self.state = 741
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_for(self):
            return self.getToken(MiniGoParser.Key_loop_for, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def Comma(self):
            return self.getToken(MiniGoParser.Comma, 0)

        def value(self):
            return self.getTypedRuleContext(MiniGoParser.ValueContext,0)


        def Ope_init(self):
            return self.getToken(MiniGoParser.Ope_init, 0)

        def Key_range(self):
            return self.getToken(MiniGoParser.Key_range, 0)

        def array_instance(self):
            return self.getTypedRuleContext(MiniGoParser.Array_instanceContext,0)


        def Lcurly(self):
            return self.getToken(MiniGoParser.Lcurly, 0)

        def for_body(self):
            return self.getTypedRuleContext(MiniGoParser.For_bodyContext,0)


        def Rcurly(self):
            return self.getToken(MiniGoParser.Rcurly, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_range




    def for_range(self):

        localctx = MiniGoParser.For_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_for_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
            self.match(MiniGoParser.Key_loop_for)
            self.state = 744
            self.index()
            self.state = 745
            self.match(MiniGoParser.Comma)
            self.state = 746
            self.value()
            self.state = 747
            self.match(MiniGoParser.Ope_init)
            self.state = 748
            self.match(MiniGoParser.Key_range)
            self.state = 749
            self.array_instance()
            self.state = 750
            self.match(MiniGoParser.Lcurly)
            self.state = 751
            self.for_body()
            self.state = 752
            self.match(MiniGoParser.Rcurly)
            self.state = 753
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def full_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Full_array_literalContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_instance




    def array_instance(self):

        localctx = MiniGoParser.Array_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_array_instance)
        try:
            self.state = 758
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 755
                self.match(MiniGoParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 756
                self.full_array_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 757
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_index




    def index(self):

        localctx = MiniGoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 760
            self.match(MiniGoParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MiniGoParser.Identifier, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_value




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 762
            self.match(MiniGoParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_set(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_setContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_body




    def for_body(self):

        localctx = MiniGoParser.For_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_for_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 764
            self.stmt_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_break(self):
            return self.getToken(MiniGoParser.Key_loop_break, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 766
            self.match(MiniGoParser.Key_loop_break)
            self.state = 767
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_loop_continue(self):
            return self.getToken(MiniGoParser.Key_loop_continue, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 769
            self.match(MiniGoParser.Key_loop_continue)
            self.state = 770
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_stmtContext,0)


        def method_call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Method_call_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_call_stmt)
        try:
            self.state = 774
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 772
                self.func_call_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 773
                self.method_call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call_stmt




    def func_call_stmt(self):

        localctx = MiniGoParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776
            self.func_call()
            self.state = 777
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call_stmt




    def method_call_stmt(self):

        localctx = MiniGoParser.Method_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_method_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 779
            self.method_call()
            self.state = 780
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def Ope_select(self):
            return self.getToken(MiniGoParser.Ope_select, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 782
            self.expr(0)
            self.state = 783
            self.match(MiniGoParser.Ope_select)
            self.state = 784
            self.func_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Key_return(self):
            return self.getToken(MiniGoParser.Key_return, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_return_stmt)
        try:
            self.state = 792
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 786
                self.match(MiniGoParser.Key_return)
                self.state = 787
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 788
                self.match(MiniGoParser.Key_return)
                self.state = 789
                self.expr(0)
                self.state = 790
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[38] = self.expr_sempred
        self._predicates[39] = self.expr1_sempred
        self._predicates[40] = self.expr2_sempred
        self._predicates[42] = self.expr3_sempred
        self._predicates[43] = self.expr4_sempred
        self._predicates[45] = self.expr6_sempred
        self._predicates[58] = self.access_list_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def access_list_sempred(self, localctx:Access_listContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




