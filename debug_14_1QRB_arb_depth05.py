
# Single QUA script generated at 2025-01-01 12:38:14.180497
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    v3 = declare(int, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(bool, )
    v7 = declare(int, )
    v8 = declare(int, value=0)
    v9 = declare(int, value=4000)
    v10 = declare(int, value=4000)
    v11 = declare(int, value=0)
    v12 = declare(int, value=0)
    v13 = declare(int, value=0)
    v14 = declare(int, value=0)
    a1 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 0, 3, 2, 6, 7, 4, 5, 11, 10, 9, 8, 13, 12, 18, 19, 22, 23, 14, 15, 21, 20, 16, 17, 2, 3, 0, 1, 7, 6, 5, 4, 10, 11, 8, 9, 20, 21, 15, 14, 23, 22, 19, 18, 12, 13, 17, 16, 3, 2, 1, 0, 5, 4, 7, 6, 9, 8, 11, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 23, 22, 4, 7, 5, 6, 11, 8, 9, 10, 2, 3, 1, 0, 22, 17, 21, 12, 14, 18, 13, 20, 23, 16, 15, 19, 5, 6, 4, 7, 10, 9, 8, 11, 1, 0, 2, 3, 23, 16, 12, 21, 19, 15, 20, 13, 22, 17, 18, 14, 6, 5, 7, 4, 8, 11, 10, 9, 3, 2, 0, 1, 16, 23, 20, 13, 18, 14, 12, 21, 17, 22, 19, 15, 7, 4, 6, 5, 9, 10, 11, 8, 0, 1, 3, 2, 17, 22, 13, 20, 15, 19, 21, 12, 16, 23, 14, 18, 8, 9, 11, 10, 1, 3, 2, 0, 7, 4, 5, 6, 19, 14, 22, 16, 20, 12, 23, 17, 15, 18, 13, 21, 9, 8, 10, 11, 2, 0, 1, 3, 6, 5, 4, 7, 14, 19, 23, 17, 13, 21, 22, 16, 18, 15, 20, 12, 10, 11, 9, 8, 3, 1, 0, 2, 4, 7, 6, 5, 18, 15, 17, 23, 12, 20, 16, 22, 14, 19, 21, 13, 11, 10, 8, 9, 0, 2, 3, 1, 5, 6, 7, 4, 15, 18, 16, 22, 21, 13, 17, 23, 19, 14, 12, 20, 12, 13, 21, 20, 18, 19, 14, 15, 22, 17, 23, 16, 1, 0, 4, 5, 8, 10, 6, 7, 2, 3, 11, 9, 13, 12, 20, 21, 14, 15, 18, 19, 16, 23, 17, 22, 0, 1, 6, 7, 11, 9, 4, 5, 3, 2, 8, 10, 14, 19, 15, 18, 22, 16, 23, 17, 20, 21, 12, 13, 8, 9, 2, 0, 6, 4, 1, 3, 10, 11, 7, 5, 15, 18, 14, 19, 17, 23, 16, 22, 12, 13, 20, 21, 10, 11, 0, 2, 5, 7, 3, 1, 8, 9, 4, 6, 16, 23, 22, 17, 12, 21, 20, 13, 19, 14, 15, 18, 5, 6, 8, 11, 3, 0, 10, 9, 7, 4, 1, 2, 17, 22, 23, 16, 21, 12, 13, 20, 14, 19, 18, 15, 4, 7, 9, 10, 0, 3, 11, 8, 6, 5, 2, 1, 18, 15, 19, 14, 16, 22, 17, 23, 21, 20, 13, 12, 11, 10, 3, 1, 4, 6, 0, 2, 9, 8, 5, 7, 19, 14, 18, 15, 23, 17, 22, 16, 13, 12, 21, 20, 9, 8, 1, 3, 7, 5, 2, 0, 11, 10, 6, 4, 20, 21, 13, 12, 19, 18, 15, 14, 17, 22, 16, 23, 3, 2, 7, 6, 10, 8, 5, 4, 0, 1, 9, 11, 21, 20, 12, 13, 15, 14, 19, 18, 23, 16, 22, 17, 2, 3, 5, 4, 9, 11, 7, 6, 1, 0, 10, 8, 22, 17, 16, 23, 13, 20, 21, 12, 15, 18, 19, 14, 7, 4, 11, 8, 2, 1, 9, 10, 5, 6, 0, 3, 23, 16, 17, 22, 20, 13, 12, 21, 18, 15, 14, 19, 6, 5, 10, 9, 1, 2, 8, 11, 4, 7, 3, 0])
    a2 = declare(int, value=[0, 1, 2, 3, 11, 9, 10, 8, 7, 5, 6, 4, 13, 12, 15, 14, 17, 16, 18, 19, 20, 21, 22, 23])
    v15 = declare(int, )
    a3 = declare(int, size=4000)
    v16 = declare(int, )
    v17 = declare(int, )
    v18 = declare(int, value=34553)
    v19 = declare(int, )
    v20 = declare(int, )
    v21 = declare(int, )
    a4 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 0, 3, 2, 6, 7, 4, 5, 11, 10, 9, 8, 13, 12, 18, 19, 22, 23, 14, 15, 21, 20, 16, 17, 2, 3, 0, 1, 7, 6, 5, 4, 10, 11, 8, 9, 20, 21, 15, 14, 23, 22, 19, 18, 12, 13, 17, 16, 3, 2, 1, 0, 5, 4, 7, 6, 9, 8, 11, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 23, 22, 4, 7, 5, 6, 11, 8, 9, 10, 2, 3, 1, 0, 22, 17, 21, 12, 14, 18, 13, 20, 23, 16, 15, 19, 5, 6, 4, 7, 10, 9, 8, 11, 1, 0, 2, 3, 23, 16, 12, 21, 19, 15, 20, 13, 22, 17, 18, 14, 6, 5, 7, 4, 8, 11, 10, 9, 3, 2, 0, 1, 16, 23, 20, 13, 18, 14, 12, 21, 17, 22, 19, 15, 7, 4, 6, 5, 9, 10, 11, 8, 0, 1, 3, 2, 17, 22, 13, 20, 15, 19, 21, 12, 16, 23, 14, 18, 8, 9, 11, 10, 1, 3, 2, 0, 7, 4, 5, 6, 19, 14, 22, 16, 20, 12, 23, 17, 15, 18, 13, 21, 9, 8, 10, 11, 2, 0, 1, 3, 6, 5, 4, 7, 14, 19, 23, 17, 13, 21, 22, 16, 18, 15, 20, 12, 10, 11, 9, 8, 3, 1, 0, 2, 4, 7, 6, 5, 18, 15, 17, 23, 12, 20, 16, 22, 14, 19, 21, 13, 11, 10, 8, 9, 0, 2, 3, 1, 5, 6, 7, 4, 15, 18, 16, 22, 21, 13, 17, 23, 19, 14, 12, 20, 12, 13, 21, 20, 18, 19, 14, 15, 22, 17, 23, 16, 1, 0, 4, 5, 8, 10, 6, 7, 2, 3, 11, 9, 13, 12, 20, 21, 14, 15, 18, 19, 16, 23, 17, 22, 0, 1, 6, 7, 11, 9, 4, 5, 3, 2, 8, 10, 14, 19, 15, 18, 22, 16, 23, 17, 20, 21, 12, 13, 8, 9, 2, 0, 6, 4, 1, 3, 10, 11, 7, 5, 15, 18, 14, 19, 17, 23, 16, 22, 12, 13, 20, 21, 10, 11, 0, 2, 5, 7, 3, 1, 8, 9, 4, 6, 16, 23, 22, 17, 12, 21, 20, 13, 19, 14, 15, 18, 5, 6, 8, 11, 3, 0, 10, 9, 7, 4, 1, 2, 17, 22, 23, 16, 21, 12, 13, 20, 14, 19, 18, 15, 4, 7, 9, 10, 0, 3, 11, 8, 6, 5, 2, 1, 18, 15, 19, 14, 16, 22, 17, 23, 21, 20, 13, 12, 11, 10, 3, 1, 4, 6, 0, 2, 9, 8, 5, 7, 19, 14, 18, 15, 23, 17, 22, 16, 13, 12, 21, 20, 9, 8, 1, 3, 7, 5, 2, 0, 11, 10, 6, 4, 20, 21, 13, 12, 19, 18, 15, 14, 17, 22, 16, 23, 3, 2, 7, 6, 10, 8, 5, 4, 0, 1, 9, 11, 21, 20, 12, 13, 15, 14, 19, 18, 23, 16, 22, 17, 2, 3, 5, 4, 9, 11, 7, 6, 1, 0, 10, 8, 22, 17, 16, 23, 13, 20, 21, 12, 15, 18, 19, 14, 7, 4, 11, 8, 2, 1, 9, 10, 5, 6, 0, 3, 23, 16, 17, 22, 20, 13, 12, 21, 18, 15, 14, 19, 6, 5, 10, 9, 1, 2, 8, 11, 4, 7, 3, 0])
    a5 = declare(int, value=[0, 1, 2, 3, 11, 9, 10, 8, 7, 5, 6, 4, 13, 12, 15, 14, 17, 16, 18, 19, 20, 21, 22, 23])
    v22 = declare(int, )
    a6 = declare(int, size=4000)
    v23 = declare(int, )
    v24 = declare(int, )
    v25 = declare(int, value=34553)
    v26 = declare(int, )
    v27 = declare(int, )
    v28 = declare(int, )
    with for_(v2,0,(v2<3),(v2+1)):
        with for_(v3,0,(v3<2),(v3+1)):
            with strict_timing_():
                with for_(v7,0,(v7<5),(v7+1)):
                    with for_(v17,0,(v17<3999),(v17+1)):
                        assign(v15, call_library_function('random', 'rand_int', [v18,24]))
                        assign(v8, a1[((v8*24)+v15)])
                        assign(a3[v17], v15)
                    assign(v16, a2[v8])
                    assign(a3[3999], v16)
                    assign(v20, 0)
                    with for_(v19,0,(v19<=v9),(v19+1)):
                        with if_((a3[v19]==0), unsafe=True):
                            assign(v20, (v20+52))
                        with elif_((a3[v19]==1)):
                            assign(v20, (v20+52))
                        with elif_((a3[v19]==2)):
                            assign(v20, (v20+52))
                        with elif_((a3[v19]==3)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==4)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==5)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==6)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==7)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==8)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==9)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==10)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==11)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==12)):
                            assign(v20, (v20+52))
                        with elif_((a3[v19]==13)):
                            assign(v20, (v20+52))
                        with elif_((a3[v19]==14)):
                            assign(v20, (v20+52))
                        with elif_((a3[v19]==15)):
                            assign(v20, (v20+52))
                        with elif_((a3[v19]==16)):
                            assign(v20, (((v20+52)+52)+52))
                        with elif_((a3[v19]==17)):
                            assign(v20, (((v20+52)+52)+52))
                        with elif_((a3[v19]==18)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==19)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==20)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==21)):
                            assign(v20, ((v20+52)+52))
                        with elif_((a3[v19]==22)):
                            assign(v20, (((v20+52)+52)+52))
                        with elif_((a3[v19]==23)):
                            assign(v20, (((v20+52)+52)+52))
                    assign(v13, v20)
                    with for_(v21,0,(v21<=v9),(v21+1)):
                        with if_((a3[v21]==0), unsafe=True):
                            wait(13, "qubit1")
                        with elif_((a3[v21]==1)):
                            play("x180_square", "qubit1")
                        with elif_((a3[v21]==2)):
                            play("y180_square", "qubit1")
                        with elif_((a3[v21]==3)):
                            play("y180_square", "qubit1")
                            play("x180_square", "qubit1")
                        with elif_((a3[v21]==4)):
                            play("x90_square", "qubit1")
                            play("y90_square", "qubit1")
                        with elif_((a3[v21]==5)):
                            play("x90_square", "qubit1")
                            play("-y90_square", "qubit1")
                        with elif_((a3[v21]==6)):
                            play("-x90_square", "qubit1")
                            play("y90_square", "qubit1")
                        with elif_((a3[v21]==7)):
                            play("-x90_square", "qubit1")
                            play("-y90_square", "qubit1")
                        with elif_((a3[v21]==8)):
                            play("y90_square", "qubit1")
                            play("x90_square", "qubit1")
                        with elif_((a3[v21]==9)):
                            play("y90_square", "qubit1")
                            play("-x90_square", "qubit1")
                        with elif_((a3[v21]==10)):
                            play("-y90_square", "qubit1")
                            play("x90_square", "qubit1")
                        with elif_((a3[v21]==11)):
                            play("-y90_square", "qubit1")
                            play("-x90_square", "qubit1")
                        with elif_((a3[v21]==12)):
                            play("x90_square", "qubit1")
                        with elif_((a3[v21]==13)):
                            play("-x90_square", "qubit1")
                        with elif_((a3[v21]==14)):
                            play("y90_square", "qubit1")
                        with elif_((a3[v21]==15)):
                            play("-y90_square", "qubit1")
                        with elif_((a3[v21]==16)):
                            play("-x90_square", "qubit1")
                            play("y90_square", "qubit1")
                            play("x90_square", "qubit1")
                        with elif_((a3[v21]==17)):
                            play("-x90_square", "qubit1")
                            play("-y90_square", "qubit1")
                            play("x90_square", "qubit1")
                        with elif_((a3[v21]==18)):
                            play("x180_square", "qubit1")
                            play("y90_square", "qubit1")
                        with elif_((a3[v21]==19)):
                            play("x180_square", "qubit1")
                            play("-y90_square", "qubit1")
                        with elif_((a3[v21]==20)):
                            play("y180_square", "qubit1")
                            play("x90_square", "qubit1")
                        with elif_((a3[v21]==21)):
                            play("y180_square", "qubit1")
                            play("-x90_square", "qubit1")
                        with elif_((a3[v21]==22)):
                            play("x90_square", "qubit1")
                            play("y90_square", "qubit1")
                            play("x90_square", "qubit1")
                        with elif_((a3[v21]==23)):
                            play("-x90_square", "qubit1")
                            play("y90_square", "qubit1")
                            play("-x90_square", "qubit1")
                with for_(v7,0,(v7<5),(v7+1)):
                    with for_(v24,0,(v24<3999),(v24+1)):
                        assign(v22, call_library_function('random', 'rand_int', [v25,24]))
                        assign(v8, a4[((v8*24)+v22)])
                        assign(a6[v24], v22)
                    assign(v23, a5[v8])
                    assign(a6[3999], v23)
                    assign(v27, 0)
                    with for_(v26,0,(v26<=v10),(v26+1)):
                        with if_((a6[v26]==0), unsafe=True):
                            assign(v27, (v27+52))
                        with elif_((a6[v26]==1)):
                            assign(v27, (v27+52))
                        with elif_((a6[v26]==2)):
                            assign(v27, (v27+52))
                        with elif_((a6[v26]==3)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==4)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==5)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==6)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==7)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==8)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==9)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==10)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==11)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==12)):
                            assign(v27, (v27+52))
                        with elif_((a6[v26]==13)):
                            assign(v27, (v27+52))
                        with elif_((a6[v26]==14)):
                            assign(v27, (v27+52))
                        with elif_((a6[v26]==15)):
                            assign(v27, (v27+52))
                        with elif_((a6[v26]==16)):
                            assign(v27, (((v27+52)+52)+52))
                        with elif_((a6[v26]==17)):
                            assign(v27, (((v27+52)+52)+52))
                        with elif_((a6[v26]==18)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==19)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==20)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==21)):
                            assign(v27, ((v27+52)+52))
                        with elif_((a6[v26]==22)):
                            assign(v27, (((v27+52)+52)+52))
                        with elif_((a6[v26]==23)):
                            assign(v27, (((v27+52)+52)+52))
                    assign(v14, v27)
                    with for_(v28,0,(v28<=v10),(v28+1)):
                        with if_((a6[v28]==0), unsafe=True):
                            wait(13, "qubit1_trio1")
                        with elif_((a6[v28]==1)):
                            play("x180_square", "qubit1_trio1")
                        with elif_((a6[v28]==2)):
                            play("y180_square", "qubit1_trio1")
                        with elif_((a6[v28]==3)):
                            play("y180_square", "qubit1_trio1")
                            play("x180_square", "qubit1_trio1")
                        with elif_((a6[v28]==4)):
                            play("x90_square", "qubit1_trio1")
                            play("y90_square", "qubit1_trio1")
                        with elif_((a6[v28]==5)):
                            play("x90_square", "qubit1_trio1")
                            play("-y90_square", "qubit1_trio1")
                        with elif_((a6[v28]==6)):
                            play("-x90_square", "qubit1_trio1")
                            play("y90_square", "qubit1_trio1")
                        with elif_((a6[v28]==7)):
                            play("-x90_square", "qubit1_trio1")
                            play("-y90_square", "qubit1_trio1")
                        with elif_((a6[v28]==8)):
                            play("y90_square", "qubit1_trio1")
                            play("x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==9)):
                            play("y90_square", "qubit1_trio1")
                            play("-x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==10)):
                            play("-y90_square", "qubit1_trio1")
                            play("x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==11)):
                            play("-y90_square", "qubit1_trio1")
                            play("-x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==12)):
                            play("x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==13)):
                            play("-x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==14)):
                            play("y90_square", "qubit1_trio1")
                        with elif_((a6[v28]==15)):
                            play("-y90_square", "qubit1_trio1")
                        with elif_((a6[v28]==16)):
                            play("-x90_square", "qubit1_trio1")
                            play("y90_square", "qubit1_trio1")
                            play("x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==17)):
                            play("-x90_square", "qubit1_trio1")
                            play("-y90_square", "qubit1_trio1")
                            play("x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==18)):
                            play("x180_square", "qubit1_trio1")
                            play("y90_square", "qubit1_trio1")
                        with elif_((a6[v28]==19)):
                            play("x180_square", "qubit1_trio1")
                            play("-y90_square", "qubit1_trio1")
                        with elif_((a6[v28]==20)):
                            play("y180_square", "qubit1_trio1")
                            play("x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==21)):
                            play("y180_square", "qubit1_trio1")
                            play("-x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==22)):
                            play("x90_square", "qubit1_trio1")
                            play("y90_square", "qubit1_trio1")
                            play("x90_square", "qubit1_trio1")
                        with elif_((a6[v28]==23)):
                            play("-x90_square", "qubit1_trio1")
                            play("y90_square", "qubit1_trio1")
                            play("-x90_square", "qubit1_trio1")
            wait(250000, )
        r1 = declare_stream()
        save(v2, r1)


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                },
                "2": {
                    "offset": 0.0,
                },
                "3": {
                    "offset": 0.0,
                },
            },
            "digital_outputs": {},
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                },
            },
        },
    },
    "elements": {
        "qubit1": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit1_trio1": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_square": "square_x180_pulse_trio1",
                "x90_square": "square_x90_pulse_trio1",
                "-x90_square": "square_minus_x90_pulse_trio1",
                "y180_square": "square_y180_pulse_trio1",
                "y90_square": "square_y90_pulse_trio1",
                "-y90_square": "square_minus_y90_pulse_trio1",
            },
        },
        "qubit1_trio2": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_square": "square_x180_pulse_trio2",
                "x90_square": "square_x90_pulse_trio2",
                "-x90_square": "square_minus_x90_pulse_trio2",
                "y180_square": "square_y180_pulse_trio2",
                "y90_square": "square_y90_pulse_trio2",
                "-y90_square": "square_minus_y90_pulse_trio2",
            },
        },
        "tank_circuit1": {
            "singleInput": {
                "port": ('con1', 3),
            },
            "intermediate_frequency": 150000000,
            "operations": {
                "readout": "reflectometry_readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 28,
            "smearing": 0,
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "square_x180_pulse": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "x180_wf",
            },
        },
        "square_y180_pulse": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "y180_wf",
            },
        },
        "square_x90_pulse": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "x90_wf",
            },
        },
        "square_y90_pulse": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "y90_wf",
            },
        },
        "square_minus_x90_pulse": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "minus_x90_wf",
            },
        },
        "square_minus_y90_pulse": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "minus_y90_wf",
            },
        },
        "square_x180_pulse_trio1": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "x180_wf_trio1",
            },
        },
        "square_y180_pulse_trio1": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "y180_wf_trio1",
            },
        },
        "square_x90_pulse_trio1": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "x90_wf_trio1",
            },
        },
        "square_y90_pulse_trio1": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "y90_wf_trio1",
            },
        },
        "square_minus_x90_pulse_trio1": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "minus_x90_wf_trio1",
            },
        },
        "square_minus_y90_pulse_trio1": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "minus_y90_wf_trio1",
            },
        },
        "square_x180_pulse_trio2": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "x180_wf_trio2",
            },
        },
        "square_y180_pulse_trio2": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "y180_wf_trio2",
            },
        },
        "square_x90_pulse_trio2": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "x90_wf_trio2",
            },
        },
        "square_y90_pulse_trio2": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "y90_wf_trio2",
            },
        },
        "square_minus_x90_pulse_trio2": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "minus_x90_wf_trio2",
            },
        },
        "square_minus_y90_pulse_trio2": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "minus_y90_wf_trio2",
            },
        },
        "reflectometry_readout_pulse": {
            "operation": "measurement",
            "length": 1000,
            "waveforms": {
                "single": "readout_pulse_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.4,
        },
        "x180_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "y180_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "x90_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "y90_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "minus_x90_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "minus_y90_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "x180_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "y180_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "x90_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "y90_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "minus_x90_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "minus_y90_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "x180_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "y180_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "x90_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "y90_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "minus_x90_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "minus_y90_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "readout_pulse_wf": {
            "type": "constant",
            "sample": 0.03,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "constant_weights": {
            "cosine": [(1, 1000)],
            "sine": [(0.0, 1000)],
        },
        "cosine_weights": {
            "cosine": [(1.0, 1000)],
            "sine": [(0.0, 1000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
    },
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {},
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "qubit1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit1_trio1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_square": "square_x180_pulse_trio1",
                "x90_square": "square_x90_pulse_trio1",
                "-x90_square": "square_minus_x90_pulse_trio1",
                "y180_square": "square_y180_pulse_trio1",
                "y90_square": "square_y90_pulse_trio1",
                "-y90_square": "square_minus_y90_pulse_trio1",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "intermediate_frequency": 0,
        },
        "qubit1_trio2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_square": "square_x180_pulse_trio2",
                "x90_square": "square_x90_pulse_trio2",
                "-x90_square": "square_minus_x90_pulse_trio2",
                "y180_square": "square_y180_pulse_trio2",
                "y90_square": "square_y90_pulse_trio2",
                "-y90_square": "square_minus_y90_pulse_trio2",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "intermediate_frequency": 0,
        },
        "tank_circuit1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
            "operations": {
                "readout": "reflectometry_readout_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 1, 3),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 150000000.0,
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 60,
            "waveforms": {
                "single": "const_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse": {
            "length": 60,
            "waveforms": {
                "single": "x180_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse": {
            "length": 60,
            "waveforms": {
                "single": "y180_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse": {
            "length": 60,
            "waveforms": {
                "single": "x90_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse": {
            "length": 60,
            "waveforms": {
                "single": "y90_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse": {
            "length": 60,
            "waveforms": {
                "single": "minus_x90_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse": {
            "length": 60,
            "waveforms": {
                "single": "minus_y90_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_trio1": {
            "length": 60,
            "waveforms": {
                "single": "x180_wf_trio1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_trio1": {
            "length": 60,
            "waveforms": {
                "single": "y180_wf_trio1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_trio1": {
            "length": 60,
            "waveforms": {
                "single": "x90_wf_trio1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_trio1": {
            "length": 60,
            "waveforms": {
                "single": "y90_wf_trio1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_trio1": {
            "length": 60,
            "waveforms": {
                "single": "minus_x90_wf_trio1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_trio1": {
            "length": 60,
            "waveforms": {
                "single": "minus_y90_wf_trio1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_trio2": {
            "length": 60,
            "waveforms": {
                "single": "x180_wf_trio2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_trio2": {
            "length": 60,
            "waveforms": {
                "single": "y180_wf_trio2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_trio2": {
            "length": 60,
            "waveforms": {
                "single": "x90_wf_trio2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_trio2": {
            "length": 60,
            "waveforms": {
                "single": "y90_wf_trio2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_trio2": {
            "length": 60,
            "waveforms": {
                "single": "minus_x90_wf_trio2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_trio2": {
            "length": 60,
            "waveforms": {
                "single": "minus_y90_wf_trio2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "reflectometry_readout_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "readout_pulse_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.4,
        },
        "x180_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "y180_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "x90_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "y90_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "minus_x90_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "minus_y90_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "x180_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "y180_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "x90_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "y90_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "minus_x90_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "minus_y90_wf_trio1": {
            "type": "constant",
            "sample": 0.18,
        },
        "x180_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "y180_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "x90_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "y90_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "minus_x90_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "minus_y90_wf_trio2": {
            "type": "constant",
            "sample": 0.09,
        },
        "readout_pulse_wf": {
            "type": "constant",
            "sample": 0.03,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "constant_weights": {
            "cosine": [(1.0, 1000)],
            "sine": [(0.0, 1000)],
        },
        "cosine_weights": {
            "cosine": [(1.0, 1000)],
            "sine": [(0.0, 1000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
    },
    "mixers": {},
}


