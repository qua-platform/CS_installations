
# Single QUA script generated at 2025-01-01 12:08:47.646602
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, value=4000)
    v2 = declare(int, value=4000)
    v3 = declare(int, )
    v4 = declare(int, )
    v5 = declare(int, )
    v6 = declare(fixed, )
    v7 = declare(fixed, )
    v8 = declare(bool, )
    v9 = declare(int, )
    v10 = declare(int, value=0)
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
    with for_(v4,0,(v4<3),(v4+1)):
        with for_(v5,0,(v5<2),(v5+1)):
            with strict_timing_():
                with for_(v9,0,(v9<5),(v9+1)):
                    with for_(v17,0,(v17<3999),(v17+1)):
                        assign(v15, call_library_function('random', 'rand_int', [v18,24]))
                        assign(v10, a1[((v10*24)+v15)])
                        assign(a3[v17], v15)
                    assign(v16, a2[v10])
                    assign(a3[3999], v16)
                    assign(v20, 0)
                    with for_(v19,0,(v19<=v1),(v19+1)):
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
                    with for_(v21,0,(v21<=v1),(v21+1)):
                        with if_((a3[v21]==0), unsafe=True):
                            wait(13, "qubit5")
                        with elif_((a3[v21]==1)):
                            play("x180_square", "qubit5")
                        with elif_((a3[v21]==2)):
                            play("y180_square", "qubit5")
                        with elif_((a3[v21]==3)):
                            play("y180_square", "qubit5")
                            play("x180_square", "qubit5")
                        with elif_((a3[v21]==4)):
                            play("x90_square", "qubit5")
                            play("y90_square", "qubit5")
                        with elif_((a3[v21]==5)):
                            play("x90_square", "qubit5")
                            play("-y90_square", "qubit5")
                        with elif_((a3[v21]==6)):
                            play("-x90_square", "qubit5")
                            play("y90_square", "qubit5")
                        with elif_((a3[v21]==7)):
                            play("-x90_square", "qubit5")
                            play("-y90_square", "qubit5")
                        with elif_((a3[v21]==8)):
                            play("y90_square", "qubit5")
                            play("x90_square", "qubit5")
                        with elif_((a3[v21]==9)):
                            play("y90_square", "qubit5")
                            play("-x90_square", "qubit5")
                        with elif_((a3[v21]==10)):
                            play("-y90_square", "qubit5")
                            play("x90_square", "qubit5")
                        with elif_((a3[v21]==11)):
                            play("-y90_square", "qubit5")
                            play("-x90_square", "qubit5")
                        with elif_((a3[v21]==12)):
                            play("x90_square", "qubit5")
                        with elif_((a3[v21]==13)):
                            play("-x90_square", "qubit5")
                        with elif_((a3[v21]==14)):
                            play("y90_square", "qubit5")
                        with elif_((a3[v21]==15)):
                            play("-y90_square", "qubit5")
                        with elif_((a3[v21]==16)):
                            play("-x90_square", "qubit5")
                            play("y90_square", "qubit5")
                            play("x90_square", "qubit5")
                        with elif_((a3[v21]==17)):
                            play("-x90_square", "qubit5")
                            play("-y90_square", "qubit5")
                            play("x90_square", "qubit5")
                        with elif_((a3[v21]==18)):
                            play("x180_square", "qubit5")
                            play("y90_square", "qubit5")
                        with elif_((a3[v21]==19)):
                            play("x180_square", "qubit5")
                            play("-y90_square", "qubit5")
                        with elif_((a3[v21]==20)):
                            play("y180_square", "qubit5")
                            play("x90_square", "qubit5")
                        with elif_((a3[v21]==21)):
                            play("y180_square", "qubit5")
                            play("-x90_square", "qubit5")
                        with elif_((a3[v21]==22)):
                            play("x90_square", "qubit5")
                            play("y90_square", "qubit5")
                            play("x90_square", "qubit5")
                        with elif_((a3[v21]==23)):
                            play("-x90_square", "qubit5")
                            play("y90_square", "qubit5")
                            play("-x90_square", "qubit5")
                with for_(v9,0,(v9<5),(v9+1)):
                    with for_(v24,0,(v24<3999),(v24+1)):
                        assign(v22, call_library_function('random', 'rand_int', [v25,24]))
                        assign(v10, a4[((v10*24)+v22)])
                        assign(a6[v24], v22)
                    assign(v23, a5[v10])
                    assign(a6[3999], v23)
                    assign(v27, 0)
                    with for_(v26,0,(v26<=v2),(v26+1)):
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
                    with for_(v28,0,(v28<=v2),(v28+1)):
                        with if_((a6[v28]==0), unsafe=True):
                            wait(13, "qubit5_trio1")
                        with elif_((a6[v28]==1)):
                            play("x180_square", "qubit5_trio1")
                        with elif_((a6[v28]==2)):
                            play("y180_square", "qubit5_trio1")
                        with elif_((a6[v28]==3)):
                            play("y180_square", "qubit5_trio1")
                            play("x180_square", "qubit5_trio1")
                        with elif_((a6[v28]==4)):
                            play("x90_square", "qubit5_trio1")
                            play("y90_square", "qubit5_trio1")
                        with elif_((a6[v28]==5)):
                            play("x90_square", "qubit5_trio1")
                            play("-y90_square", "qubit5_trio1")
                        with elif_((a6[v28]==6)):
                            play("-x90_square", "qubit5_trio1")
                            play("y90_square", "qubit5_trio1")
                        with elif_((a6[v28]==7)):
                            play("-x90_square", "qubit5_trio1")
                            play("-y90_square", "qubit5_trio1")
                        with elif_((a6[v28]==8)):
                            play("y90_square", "qubit5_trio1")
                            play("x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==9)):
                            play("y90_square", "qubit5_trio1")
                            play("-x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==10)):
                            play("-y90_square", "qubit5_trio1")
                            play("x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==11)):
                            play("-y90_square", "qubit5_trio1")
                            play("-x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==12)):
                            play("x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==13)):
                            play("-x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==14)):
                            play("y90_square", "qubit5_trio1")
                        with elif_((a6[v28]==15)):
                            play("-y90_square", "qubit5_trio1")
                        with elif_((a6[v28]==16)):
                            play("-x90_square", "qubit5_trio1")
                            play("y90_square", "qubit5_trio1")
                            play("x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==17)):
                            play("-x90_square", "qubit5_trio1")
                            play("-y90_square", "qubit5_trio1")
                            play("x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==18)):
                            play("x180_square", "qubit5_trio1")
                            play("y90_square", "qubit5_trio1")
                        with elif_((a6[v28]==19)):
                            play("x180_square", "qubit5_trio1")
                            play("-y90_square", "qubit5_trio1")
                        with elif_((a6[v28]==20)):
                            play("y180_square", "qubit5_trio1")
                            play("x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==21)):
                            play("y180_square", "qubit5_trio1")
                            play("-x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==22)):
                            play("x90_square", "qubit5_trio1")
                            play("y90_square", "qubit5_trio1")
                            play("x90_square", "qubit5_trio1")
                        with elif_((a6[v28]==23)):
                            play("-x90_square", "qubit5_trio1")
                            play("y90_square", "qubit5_trio1")
                            play("-x90_square", "qubit5_trio1")
            wait(25000, )
        r1 = declare_stream()
        save(v4, r1)


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "5": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                    },
                    "digital_outputs": {
                        "1": {},
                        "3": {},
                        "5": {},
                    },
                    "analog_inputs": {
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": 1000000000,
                        },
                    },
                },
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {},
                },
            },
        },
    },
    "elements": {
        "P1": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2": {
            "singleInput": {
                "port": ('con1', 3, 2),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P3": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "operations": {
                "step": "P3_step_pulse",
            },
        },
        "P4": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "operations": {
                "step": "P4_step_pulse",
            },
        },
        "P5": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "operations": {
                "step": "P5_step_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": ('con1', 3, 2),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P3_sticky": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P3_step_pulse",
            },
        },
        "P4_sticky": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P4_step_pulse",
            },
        },
        "P5_sticky": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P5_step_pulse",
            },
        },
        "B1": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "operations": {
                "step": "B1_step_pulse",
            },
        },
        "B2": {
            "singleInput": {
                "port": ('con1', 3, 5),
            },
            "operations": {
                "step": "B2_step_pulse",
            },
        },
        "B3": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "operations": {
                "step": "B3_step_pulse",
            },
        },
        "B4": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "operations": {
                "step": "B4_step_pulse",
            },
        },
        "B1_sticky": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "B1_step_pulse",
            },
        },
        "B2_sticky": {
            "singleInput": {
                "port": ('con1', 3, 5),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "B2_step_pulse",
            },
        },
        "B3_sticky": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "B3_step_pulse",
            },
        },
        "B4_sticky": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "B4_step_pulse",
            },
        },
        "Psd1": {
            "singleInput": {
                "port": ('con1', 3, 7),
            },
            "operations": {
                "step": "Psd1_step_pulse",
            },
        },
        "Psd2": {
            "singleInput": {
                "port": ('con1', 3, 8),
            },
            "operations": {
                "step": "Psd2_step_pulse",
            },
        },
        "Psd1_sticky": {
            "singleInput": {
                "port": ('con1', 3, 7),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "Psd1_step_pulse",
            },
        },
        "Psd2_sticky": {
            "singleInput": {
                "port": ('con1', 3, 8),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "Psd2_step_pulse",
            },
        },
        "qubit1": {
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit1",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit2": {
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit2",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 200000000,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit3": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit3",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit4": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit4",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit5": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit5",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 5),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit1_trio1": {
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit1",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
                "x180_square": "square_x180_pulse_trio1",
                "x90_square": "square_x90_pulse_trio1",
                "-x90_square": "square_minus_x90_pulse_trio1",
                "y180_square": "square_y180_pulse_trio1",
                "y90_square": "square_y90_pulse_trio1",
                "-y90_square": "square_minus_y90_pulse_trio1",
            },
        },
        "qubit2_trio1": {
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit2",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 200000000,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
                "x180_square": "square_x180_pulse_trio1",
                "x90_square": "square_x90_pulse_trio1",
                "-x90_square": "square_minus_x90_pulse_trio1",
                "y180_square": "square_y180_pulse_trio1",
                "y90_square": "square_y90_pulse_trio1",
                "-y90_square": "square_minus_y90_pulse_trio1",
            },
        },
        "qubit3_trio1": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit3",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
                "x180_square": "square_x180_pulse_trio1",
                "x90_square": "square_x90_pulse_trio1",
                "-x90_square": "square_minus_x90_pulse_trio1",
                "y180_square": "square_y180_pulse_trio1",
                "y90_square": "square_y90_pulse_trio1",
                "-y90_square": "square_minus_y90_pulse_trio1",
            },
        },
        "qubit4_trio1": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit4",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
                "x180_square": "square_x180_pulse_trio1",
                "x90_square": "square_x90_pulse_trio1",
                "-x90_square": "square_minus_x90_pulse_trio1",
                "y180_square": "square_y180_pulse_trio1",
                "y90_square": "square_y90_pulse_trio1",
                "-y90_square": "square_minus_y90_pulse_trio1",
            },
        },
        "qubit5_trio1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit5",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 5),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
                "x180_square": "square_x180_pulse_trio1",
                "x90_square": "square_x90_pulse_trio1",
                "-x90_square": "square_minus_x90_pulse_trio1",
                "y180_square": "square_y180_pulse_trio1",
                "y90_square": "square_y90_pulse_trio1",
                "-y90_square": "square_minus_y90_pulse_trio1",
            },
        },
        "qubit1_trio2": {
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit1",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit2_trio2": {
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit2",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 200000000,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit3_trio2": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit3",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit4_trio2": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit4",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit5_trio2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit5",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 5),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qp_control_c3t2": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qp_control_c3t2",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qp_control_c3t2",
                "x90_kaiser": "x90_kaiser_pulse_qp_control_c3t2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qp_control_c3t2",
                "y180_kaiser": "y180_kaiser_pulse_qp_control_c3t2",
                "y90_kaiser": "y90_kaiser_pulse_qp_control_c3t2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qp_control_c3t2",
                "x180_gauss": "x180_gaussian_pulse_qp_control_c3t2",
                "x90_gauss": "x90_gaussian_pulse_qp_control_c3t2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qp_control_c3t2",
                "y180_gauss": "y180_gaussian_pulse_qp_control_c3t2",
                "y90_gauss": "y90_gaussian_pulse_qp_control_c3t2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qp_control_c3t2",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit1_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit2_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit3_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 3),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit4_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 3),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit5_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 5),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "tank_circuit1": {
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "intermediate_frequency": 150000000,
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit1",
            },
            "outputs": {
                "out1": ('con1', 5, 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        "tank_circuit2": {
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "intermediate_frequency": 200000000,
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit2",
            },
            "outputs": {
                "out1": ('con1', 5, 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
    },
    "pulses": {
        "P1_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P1_step_wf",
            },
        },
        "P2_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P2_step_wf",
            },
        },
        "P3_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P3_step_wf",
            },
        },
        "P4_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P4_step_wf",
            },
        },
        "P5_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P5_step_wf",
            },
        },
        "B1_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "B1_step_wf",
            },
        },
        "B2_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "B2_step_wf",
            },
        },
        "B3_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "B3_step_wf",
            },
        },
        "B4_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "B4_step_wf",
            },
        },
        "Psd1_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "Psd1_step_wf",
            },
        },
        "Psd2_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "Psd2_step_wf",
            },
        },
        "x180_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit1",
                "Q": "x180_gaussian_Q_wf_qubit1",
            },
        },
        "x180_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit2",
                "Q": "x180_gaussian_Q_wf_qubit2",
            },
        },
        "x180_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit3",
                "Q": "x180_gaussian_Q_wf_qubit3",
            },
        },
        "x180_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit4",
                "Q": "x180_gaussian_Q_wf_qubit4",
            },
        },
        "x180_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit5",
                "Q": "x180_gaussian_Q_wf_qubit5",
            },
        },
        "x90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit1",
                "Q": "x90_gaussian_Q_wf_qubit1",
            },
        },
        "x90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit2",
                "Q": "x90_gaussian_Q_wf_qubit2",
            },
        },
        "x90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit3",
                "Q": "x90_gaussian_Q_wf_qubit3",
            },
        },
        "x90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit4",
                "Q": "x90_gaussian_Q_wf_qubit4",
            },
        },
        "x90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit5",
                "Q": "x90_gaussian_Q_wf_qubit5",
            },
        },
        "minus_x90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit1",
                "Q": "minus_x90_gaussian_Q_wf_qubit1",
            },
        },
        "minus_x90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit2",
                "Q": "minus_x90_gaussian_Q_wf_qubit2",
            },
        },
        "minus_x90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit3",
                "Q": "minus_x90_gaussian_Q_wf_qubit3",
            },
        },
        "minus_x90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit4",
                "Q": "minus_x90_gaussian_Q_wf_qubit4",
            },
        },
        "minus_x90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit5",
                "Q": "minus_x90_gaussian_Q_wf_qubit5",
            },
        },
        "y180_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit1",
                "Q": "y180_gaussian_Q_wf_qubit1",
            },
        },
        "y180_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit2",
                "Q": "y180_gaussian_Q_wf_qubit2",
            },
        },
        "y180_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit3",
                "Q": "y180_gaussian_Q_wf_qubit3",
            },
        },
        "y180_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit4",
                "Q": "y180_gaussian_Q_wf_qubit4",
            },
        },
        "y180_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit5",
                "Q": "y180_gaussian_Q_wf_qubit5",
            },
        },
        "y90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit1",
                "Q": "y90_gaussian_Q_wf_qubit1",
            },
        },
        "y90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit2",
                "Q": "y90_gaussian_Q_wf_qubit2",
            },
        },
        "y90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit3",
                "Q": "y90_gaussian_Q_wf_qubit3",
            },
        },
        "y90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit4",
                "Q": "y90_gaussian_Q_wf_qubit4",
            },
        },
        "y90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit5",
                "Q": "y90_gaussian_Q_wf_qubit5",
            },
        },
        "minus_y90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit1",
                "Q": "minus_y90_gaussian_Q_wf_qubit1",
            },
        },
        "minus_y90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit2",
                "Q": "minus_y90_gaussian_Q_wf_qubit2",
            },
        },
        "minus_y90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit3",
                "Q": "minus_y90_gaussian_Q_wf_qubit3",
            },
        },
        "minus_y90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit4",
                "Q": "minus_y90_gaussian_Q_wf_qubit4",
            },
        },
        "minus_y90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit5",
                "Q": "minus_y90_gaussian_Q_wf_qubit5",
            },
        },
        "x180_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit1",
                "Q": "x180_kaiser_Q_wf_qubit1",
            },
        },
        "x180_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit2",
                "Q": "x180_kaiser_Q_wf_qubit2",
            },
        },
        "x180_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit3",
                "Q": "x180_kaiser_Q_wf_qubit3",
            },
        },
        "x180_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit4",
                "Q": "x180_kaiser_Q_wf_qubit4",
            },
        },
        "x180_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit5",
                "Q": "x180_kaiser_Q_wf_qubit5",
            },
        },
        "x90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit1",
                "Q": "x90_kaiser_Q_wf_qubit1",
            },
        },
        "x90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit2",
                "Q": "x90_kaiser_Q_wf_qubit2",
            },
        },
        "x90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit3",
                "Q": "x90_kaiser_Q_wf_qubit3",
            },
        },
        "x90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit4",
                "Q": "x90_kaiser_Q_wf_qubit4",
            },
        },
        "x90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit5",
                "Q": "x90_kaiser_Q_wf_qubit5",
            },
        },
        "minus_x90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit1",
                "Q": "minus_x90_kaiser_Q_wf_qubit1",
            },
        },
        "minus_x90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit2",
                "Q": "minus_x90_kaiser_Q_wf_qubit2",
            },
        },
        "minus_x90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit3",
                "Q": "minus_x90_kaiser_Q_wf_qubit3",
            },
        },
        "minus_x90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit4",
                "Q": "minus_x90_kaiser_Q_wf_qubit4",
            },
        },
        "minus_x90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit5",
                "Q": "minus_x90_kaiser_Q_wf_qubit5",
            },
        },
        "y180_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit1",
                "Q": "y180_kaiser_Q_wf_qubit1",
            },
        },
        "y180_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit2",
                "Q": "y180_kaiser_Q_wf_qubit2",
            },
        },
        "y180_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit3",
                "Q": "y180_kaiser_Q_wf_qubit3",
            },
        },
        "y180_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit4",
                "Q": "y180_kaiser_Q_wf_qubit4",
            },
        },
        "y180_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit5",
                "Q": "y180_kaiser_Q_wf_qubit5",
            },
        },
        "y90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit1",
                "Q": "y90_kaiser_Q_wf_qubit1",
            },
        },
        "y90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit2",
                "Q": "y90_kaiser_Q_wf_qubit2",
            },
        },
        "y90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit3",
                "Q": "y90_kaiser_Q_wf_qubit3",
            },
        },
        "y90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit4",
                "Q": "y90_kaiser_Q_wf_qubit4",
            },
        },
        "y90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit5",
                "Q": "y90_kaiser_Q_wf_qubit5",
            },
        },
        "minus_y90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit1",
                "Q": "minus_y90_kaiser_Q_wf_qubit1",
            },
        },
        "minus_y90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit2",
                "Q": "minus_y90_kaiser_Q_wf_qubit2",
            },
        },
        "minus_y90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit3",
                "Q": "minus_y90_kaiser_Q_wf_qubit3",
            },
        },
        "minus_y90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit4",
                "Q": "minus_y90_kaiser_Q_wf_qubit4",
            },
        },
        "minus_y90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit5",
                "Q": "minus_y90_kaiser_Q_wf_qubit5",
            },
        },
        "x180_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qp_control_c3t2",
                "Q": "x180_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "x90_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qp_control_c3t2",
                "Q": "x90_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "minus_x90_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qp_control_c3t2",
                "Q": "minus_x90_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "y180_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qp_control_c3t2",
                "Q": "y180_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "y90_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qp_control_c3t2",
                "Q": "y90_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "minus_y90_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qp_control_c3t2",
                "Q": "minus_y90_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "x180_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qp_control_c3t2",
                "Q": "x180_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "x90_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qp_control_c3t2",
                "Q": "x90_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "minus_x90_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qp_control_c3t2",
                "Q": "minus_x90_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "y180_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qp_control_c3t2",
                "Q": "y180_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "y90_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qp_control_c3t2",
                "Q": "y90_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "minus_y90_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qp_control_c3t2",
                "Q": "minus_y90_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "reflectometry_readout_pulse_tank_circuit1": {
            "operation": "measurement",
            "length": 400,
            "waveforms": {
                "single": "reflectometry_readout_wf_tank_circuit1",
            },
            "integration_weights": {
                "cos": "cosine_weights_tank_circuit1",
                "sin": "sine_weights_tank_circuit1",
            },
            "digital_marker": "ON",
        },
        "reflectometry_readout_pulse_tank_circuit2": {
            "operation": "measurement",
            "length": 400,
            "waveforms": {
                "single": "reflectometry_readout_wf_tank_circuit2",
            },
            "integration_weights": {
                "cos": "cosine_weights_tank_circuit2",
                "sin": "sine_weights_tank_circuit2",
            },
            "digital_marker": "ON",
        },
        "const_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_y180_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_y90_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_minus_y90_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse_trio1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf_trio1",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_trio1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf_trio1",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_trio1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf_trio1",
                "Q": "zero_wf",
            },
        },
        "square_y180_pulse_trio1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf_trio1",
                "Q": "zero_wf",
            },
        },
        "square_y90_pulse_trio1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf_trio1",
                "Q": "zero_wf",
            },
        },
        "square_minus_y90_pulse_trio1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf_trio1",
                "Q": "zero_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
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
            "sample": 0.1,
        },
        "square_x180_I_wf": {
            "type": "constant",
            "sample": 0.45,
        },
        "square_x90_I_wf": {
            "type": "constant",
            "sample": 0.4,
        },
        "square_minus_x90_I_wf": {
            "type": "constant",
            "sample": -0.4,
        },
        "square_y180_I_wf": {
            "type": "constant",
            "sample": 0.35,
        },
        "square_y90_I_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "square_minus_y90_I_wf": {
            "type": "constant",
            "sample": -0.3,
        },
        "square_x180_I_wf_trio1": {
            "type": "constant",
            "sample": 0.225,
        },
        "square_x90_I_wf_trio1": {
            "type": "constant",
            "sample": 0.2,
        },
        "square_minus_x90_I_wf_trio1": {
            "type": "constant",
            "sample": -0.2,
        },
        "square_y180_I_wf_trio1": {
            "type": "constant",
            "sample": 0.175,
        },
        "square_y90_I_wf_trio1": {
            "type": "constant",
            "sample": 0.15,
        },
        "square_minus_y90_I_wf_trio1": {
            "type": "constant",
            "sample": -0.15,
        },
        "reflectometry_readout_wf_tank_circuit1": {
            "type": "constant",
            "sample": 0.1,
        },
        "reflectometry_readout_wf_tank_circuit2": {
            "type": "constant",
            "sample": 0.1,
        },
        "P1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P3_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P4_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P5_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B3_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B4_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "Psd1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "Psd2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "x180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.000623059395668357, 0.0013134158229892211, 0.00207600456516317, 0.0029157968026681785, 0.003837749297415329, 0.004846747956223626, 0.0059475454464649755, 0.007144693172446949, 0.008442468066474543, 0.00984479480112677, 0.01135516418617893, 0.012976548671420715, 0.014711316031583668, 0.016561142457583073, 0.01852692641493371, 0.020608704751007553, 0.02280557263323139, 0.02511560897595016, 0.027535809060335543, 0.03006202606562717, 0.03268892320793267, 0.035409938122250045, 0.038217261022609625, 0.04110182803350147, 0.04405333090334345, 0.04706024408905373, 0.05010986994237358, 0.05318840243716088, 0.05628100955729227, 0.059371934122988815, 0.06244461247619, 0.06548181008073263, 0.06846577272886803, 0.07137839169082312, 0.07420138080762224, 0.07691646321812151, 0.07950556513773178, 0.08195101387660032, 0.08423573710622746, 0.08634346026167618, 0.08825889890645858, 0.08996794289214834, 0.09145782921645602, 0.09271730062188518, 0.09373674718038912, 0.09450832837415593, 0.09502607350358355] + [0.09528595862392984] * 2 + [0.09502607350358355, 0.09450832837415593, 0.09373674718038912, 0.09271730062188518, 0.09145782921645602, 0.08996794289214834, 0.08825889890645858, 0.08634346026167618, 0.08423573710622746, 0.08195101387660032, 0.07950556513773178, 0.07691646321812151, 0.07420138080762224, 0.07137839169082312, 0.06846577272886803, 0.06548181008073263, 0.06244461247619, 0.059371934122988815, 0.05628100955729227, 0.05318840243716088, 0.05010986994237358, 0.04706024408905373, 0.04405333090334345, 0.04110182803350147, 0.038217261022609625, 0.035409938122250045, 0.03268892320793267, 0.03006202606562717, 0.027535809060335543, 0.02511560897595016, 0.02280557263323139, 0.020608704751007553, 0.01852692641493371, 0.016561142457583073, 0.014711316031583668, 0.012976548671420715, 0.01135516418617893, 0.00984479480112677, 0.008442468066474543, 0.007144693172446949, 0.0059475454464649755, 0.004846747956223626, 0.003837749297415329, 0.0029157968026681785, 0.00207600456516317, 0.0013134158229892211, 0.000623059395668357] + [0.0] * 3,
        },
        "x180_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
        },
        "x90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003115296978341785, 0.0006567079114946106, 0.001038002282581585, 0.0014578984013340892, 0.0019188746487076645, 0.002423373978111813, 0.0029737727232324877, 0.0035723465862234744, 0.004221234033237271, 0.004922397400563385, 0.005677582093089465, 0.0064882743357103576, 0.007355658015791834, 0.008280571228791537, 0.009263463207466856, 0.010304352375503777, 0.011402786316615695, 0.01255780448797508, 0.013767904530167772, 0.015031013032813585, 0.016344461603966336, 0.017704969061125023, 0.019108630511304812, 0.020550914016750736, 0.022026665451671725, 0.023530122044526865, 0.02505493497118679, 0.02659420121858044, 0.028140504778646134, 0.029685967061494407, 0.031222306238095, 0.032740905040366315, 0.034232886364434015, 0.03568919584541156, 0.03710069040381112, 0.038458231609060756, 0.03975278256886589, 0.04097550693830016, 0.04211786855311373, 0.04317173013083809, 0.04412944945322929, 0.04498397144607417, 0.04572891460822801, 0.04635865031094259, 0.04686837359019456, 0.047254164187077966, 0.047513036751791776] + [0.04764297931196492] * 2 + [0.047513036751791776, 0.047254164187077966, 0.04686837359019456, 0.04635865031094259, 0.04572891460822801, 0.04498397144607417, 0.04412944945322929, 0.04317173013083809, 0.04211786855311373, 0.04097550693830016, 0.03975278256886589, 0.038458231609060756, 0.03710069040381112, 0.03568919584541156, 0.034232886364434015, 0.032740905040366315, 0.031222306238095, 0.029685967061494407, 0.028140504778646134, 0.02659420121858044, 0.02505493497118679, 0.023530122044526865, 0.022026665451671725, 0.020550914016750736, 0.019108630511304812, 0.017704969061125023, 0.016344461603966336, 0.015031013032813585, 0.013767904530167772, 0.01255780448797508, 0.011402786316615695, 0.010304352375503777, 0.009263463207466856, 0.008280571228791537, 0.007355658015791834, 0.0064882743357103576, 0.005677582093089465, 0.004922397400563385, 0.004221234033237271, 0.0035723465862234744, 0.0029737727232324877, 0.002423373978111813, 0.0019188746487076645, 0.0014578984013340892, 0.001038002282581585, 0.0006567079114946106, 0.0003115296978341785] + [0.0] * 3,
        },
        "x90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
        },
        "minus_x90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003115296978341785, -0.0006567079114946106, -0.001038002282581585, -0.0014578984013340892, -0.0019188746487076645, -0.002423373978111813, -0.0029737727232324877, -0.0035723465862234744, -0.004221234033237271, -0.004922397400563385, -0.005677582093089465, -0.0064882743357103576, -0.007355658015791834, -0.008280571228791537, -0.009263463207466856, -0.010304352375503777, -0.011402786316615695, -0.01255780448797508, -0.013767904530167772, -0.015031013032813585, -0.016344461603966336, -0.017704969061125023, -0.019108630511304812, -0.020550914016750736, -0.022026665451671725, -0.023530122044526865, -0.02505493497118679, -0.02659420121858044, -0.028140504778646134, -0.029685967061494407, -0.031222306238095, -0.032740905040366315, -0.034232886364434015, -0.03568919584541156, -0.03710069040381112, -0.038458231609060756, -0.03975278256886589, -0.04097550693830016, -0.04211786855311373, -0.04317173013083809, -0.04412944945322929, -0.04498397144607417, -0.04572891460822801, -0.04635865031094259, -0.04686837359019456, -0.047254164187077966, -0.047513036751791776] + [-0.04764297931196492] * 2 + [-0.047513036751791776, -0.047254164187077966, -0.04686837359019456, -0.04635865031094259, -0.04572891460822801, -0.04498397144607417, -0.04412944945322929, -0.04317173013083809, -0.04211786855311373, -0.04097550693830016, -0.03975278256886589, -0.038458231609060756, -0.03710069040381112, -0.03568919584541156, -0.034232886364434015, -0.032740905040366315, -0.031222306238095, -0.029685967061494407, -0.028140504778646134, -0.02659420121858044, -0.02505493497118679, -0.023530122044526865, -0.022026665451671725, -0.020550914016750736, -0.019108630511304812, -0.017704969061125023, -0.016344461603966336, -0.015031013032813585, -0.013767904530167772, -0.01255780448797508, -0.011402786316615695, -0.010304352375503777, -0.009263463207466856, -0.008280571228791537, -0.007355658015791834, -0.0064882743357103576, -0.005677582093089465, -0.004922397400563385, -0.004221234033237271, -0.0035723465862234744, -0.0029737727232324877, -0.002423373978111813, -0.0019188746487076645, -0.0014578984013340892, -0.001038002282581585, -0.0006567079114946106, -0.0003115296978341785] + [0.0] * 3,
        },
        "minus_x90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
        },
        "y180_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
        },
        "y180_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.000623059395668357, 0.0013134158229892211, 0.00207600456516317, 0.0029157968026681785, 0.003837749297415329, 0.004846747956223626, 0.0059475454464649755, 0.007144693172446949, 0.008442468066474543, 0.00984479480112677, 0.01135516418617893, 0.012976548671420715, 0.014711316031583668, 0.016561142457583073, 0.01852692641493371, 0.020608704751007553, 0.02280557263323139, 0.02511560897595016, 0.027535809060335543, 0.03006202606562717, 0.03268892320793267, 0.035409938122250045, 0.038217261022609625, 0.04110182803350147, 0.04405333090334345, 0.04706024408905373, 0.05010986994237358, 0.05318840243716088, 0.05628100955729227, 0.059371934122988815, 0.06244461247619, 0.06548181008073263, 0.06846577272886803, 0.07137839169082312, 0.07420138080762224, 0.07691646321812151, 0.07950556513773178, 0.08195101387660032, 0.08423573710622746, 0.08634346026167618, 0.08825889890645858, 0.08996794289214834, 0.09145782921645602, 0.09271730062188518, 0.09373674718038912, 0.09450832837415593, 0.09502607350358355] + [0.09528595862392984] * 2 + [0.09502607350358355, 0.09450832837415593, 0.09373674718038912, 0.09271730062188518, 0.09145782921645602, 0.08996794289214834, 0.08825889890645858, 0.08634346026167618, 0.08423573710622746, 0.08195101387660032, 0.07950556513773178, 0.07691646321812151, 0.07420138080762224, 0.07137839169082312, 0.06846577272886803, 0.06548181008073263, 0.06244461247619, 0.059371934122988815, 0.05628100955729227, 0.05318840243716088, 0.05010986994237358, 0.04706024408905373, 0.04405333090334345, 0.04110182803350147, 0.038217261022609625, 0.035409938122250045, 0.03268892320793267, 0.03006202606562717, 0.027535809060335543, 0.02511560897595016, 0.02280557263323139, 0.020608704751007553, 0.01852692641493371, 0.016561142457583073, 0.014711316031583668, 0.012976548671420715, 0.01135516418617893, 0.00984479480112677, 0.008442468066474543, 0.007144693172446949, 0.0059475454464649755, 0.004846747956223626, 0.003837749297415329, 0.0029157968026681785, 0.00207600456516317, 0.0013134158229892211, 0.000623059395668357] + [0.0] * 3,
        },
        "y90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
        },
        "y90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003115296978341785, 0.0006567079114946106, 0.001038002282581585, 0.0014578984013340892, 0.0019188746487076645, 0.002423373978111813, 0.0029737727232324877, 0.0035723465862234744, 0.004221234033237271, 0.004922397400563385, 0.005677582093089465, 0.0064882743357103576, 0.007355658015791834, 0.008280571228791537, 0.009263463207466856, 0.010304352375503777, 0.011402786316615695, 0.01255780448797508, 0.013767904530167772, 0.015031013032813585, 0.016344461603966336, 0.017704969061125023, 0.019108630511304812, 0.020550914016750736, 0.022026665451671725, 0.023530122044526865, 0.02505493497118679, 0.02659420121858044, 0.028140504778646134, 0.029685967061494407, 0.031222306238095, 0.032740905040366315, 0.034232886364434015, 0.03568919584541156, 0.03710069040381112, 0.038458231609060756, 0.03975278256886589, 0.04097550693830016, 0.04211786855311373, 0.04317173013083809, 0.04412944945322929, 0.04498397144607417, 0.04572891460822801, 0.04635865031094259, 0.04686837359019456, 0.047254164187077966, 0.047513036751791776] + [0.04764297931196492] * 2 + [0.047513036751791776, 0.047254164187077966, 0.04686837359019456, 0.04635865031094259, 0.04572891460822801, 0.04498397144607417, 0.04412944945322929, 0.04317173013083809, 0.04211786855311373, 0.04097550693830016, 0.03975278256886589, 0.038458231609060756, 0.03710069040381112, 0.03568919584541156, 0.034232886364434015, 0.032740905040366315, 0.031222306238095, 0.029685967061494407, 0.028140504778646134, 0.02659420121858044, 0.02505493497118679, 0.023530122044526865, 0.022026665451671725, 0.020550914016750736, 0.019108630511304812, 0.017704969061125023, 0.016344461603966336, 0.015031013032813585, 0.013767904530167772, 0.01255780448797508, 0.011402786316615695, 0.010304352375503777, 0.009263463207466856, 0.008280571228791537, 0.007355658015791834, 0.0064882743357103576, 0.005677582093089465, 0.004922397400563385, 0.004221234033237271, 0.0035723465862234744, 0.0029737727232324877, 0.002423373978111813, 0.0019188746487076645, 0.0014578984013340892, 0.001038002282581585, 0.0006567079114946106, 0.0003115296978341785] + [0.0] * 3,
        },
        "minus_y90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
        },
        "minus_y90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003115296978341785, -0.0006567079114946106, -0.001038002282581585, -0.0014578984013340892, -0.0019188746487076645, -0.002423373978111813, -0.0029737727232324877, -0.0035723465862234744, -0.004221234033237271, -0.004922397400563385, -0.005677582093089465, -0.0064882743357103576, -0.007355658015791834, -0.008280571228791537, -0.009263463207466856, -0.010304352375503777, -0.011402786316615695, -0.01255780448797508, -0.013767904530167772, -0.015031013032813585, -0.016344461603966336, -0.017704969061125023, -0.019108630511304812, -0.020550914016750736, -0.022026665451671725, -0.023530122044526865, -0.02505493497118679, -0.02659420121858044, -0.028140504778646134, -0.029685967061494407, -0.031222306238095, -0.032740905040366315, -0.034232886364434015, -0.03568919584541156, -0.03710069040381112, -0.038458231609060756, -0.03975278256886589, -0.04097550693830016, -0.04211786855311373, -0.04317173013083809, -0.04412944945322929, -0.04498397144607417, -0.04572891460822801, -0.04635865031094259, -0.04686837359019456, -0.047254164187077966, -0.047513036751791776] + [-0.04764297931196492] * 2 + [-0.047513036751791776, -0.047254164187077966, -0.04686837359019456, -0.04635865031094259, -0.04572891460822801, -0.04498397144607417, -0.04412944945322929, -0.04317173013083809, -0.04211786855311373, -0.04097550693830016, -0.03975278256886589, -0.038458231609060756, -0.03710069040381112, -0.03568919584541156, -0.034232886364434015, -0.032740905040366315, -0.031222306238095, -0.029685967061494407, -0.028140504778646134, -0.02659420121858044, -0.02505493497118679, -0.023530122044526865, -0.022026665451671725, -0.020550914016750736, -0.019108630511304812, -0.017704969061125023, -0.016344461603966336, -0.015031013032813585, -0.013767904530167772, -0.01255780448797508, -0.011402786316615695, -0.010304352375503777, -0.009263463207466856, -0.008280571228791537, -0.007355658015791834, -0.0064882743357103576, -0.005677582093089465, -0.004922397400563385, -0.004221234033237271, -0.0035723465862234744, -0.0029737727232324877, -0.002423373978111813, -0.0019188746487076645, -0.0014578984013340892, -0.001038002282581585, -0.0006567079114946106, -0.0003115296978341785] + [0.0] * 3,
        },
        "x180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0001306438144712879, 0.00023132187674409848, 0.0003707991780740096, 0.0005574391218594114, 0.0008003941708179544, 0.0011095399428924942, 0.0014953855867247238, 0.0019689601966731024, 0.0025416755920456883, 0.003225166380287162, 0.0040311088354394045, 0.0049710207362835285, 0.006056044907394079, 0.007296719774748082, 0.008702740769447388, 0.010282716872948027, 0.012043926980302464, 0.01399208105104621, 0.016131091209017425, 0.018462858033262076, 0.020987077245404648, 0.023701071840357107, 0.026599654425844745, 0.02967502413386515, 0.03291670194889541, 0.03631150767153205, 0.03984358101334329, 0.04349444851284272, 0.04724313708992553, 0.051066334135211805, 0.054938593081588605, 0.05883258244909391, 0.06271937541311469, 0.06656877604179862, 0.0703496775033089, 0.07403044677783581, 0.07757932974235295, 0.08096486994518408, 0.08415633396728084, 0.08712413598952014, 0.089840254058968, 0.09227863057700843, 0.09441554972003091, 0.09622998484670547, 0.09770390943881668, 0.09882256575559714, 0.09957468614155682] + [0.09995266279888454] * 2 + [0.09957468614155682, 0.09882256575559714, 0.09770390943881668, 0.09622998484670547, 0.09441554972003091, 0.09227863057700843, 0.089840254058968, 0.08712413598952014, 0.08415633396728084, 0.0809648699451842, 0.07757932974235295, 0.07403044677783581, 0.0703496775033089, 0.06656877604179862, 0.06271937541311469, 0.05883258244909391, 0.054938593081588605, 0.051066334135211805, 0.04724313708992561, 0.04349444851284272, 0.03984358101334329, 0.036311507671532114, 0.03291670194889541, 0.02967502413386515, 0.026599654425844745, 0.023701071840357107, 0.020987077245404648, 0.018462858033262076, 0.016131091209017425, 0.01399208105104621, 0.012043926980302464, 0.010282716872948027, 0.008702740769447388, 0.007296719774748089, 0.006056044907394079, 0.0049710207362835285, 0.004031108835439411, 0.003225166380287162, 0.0025416755920456883, 0.001968960196673105, 0.0014953855867247238, 0.0011095399428924942, 0.0008003941708179558, 0.00055743912185941, 0.0003707991780740096, 0.00023132187674409872, 0.00013064381447128748, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 6.532190723564394e-05, 0.00011566093837204924, 0.0001853995890370048, 0.0002787195609297057, 0.0004001970854089772, 0.0005547699714462471, 0.0007476927933623619, 0.0009844800983365512, 0.0012708377960228441, 0.001612583190143581, 0.0020155544177197023, 0.0024855103681417643, 0.0030280224536970396, 0.003648359887374041, 0.004351370384723694, 0.005141358436474014, 0.006021963490151232, 0.006996040525523105, 0.008065545604508713, 0.009231429016631038, 0.010493538622702324, 0.011850535920178554, 0.013299827212922373, 0.014837512066932575, 0.016458350974447707, 0.018155753835766026, 0.019921790506671644, 0.02174722425642136, 0.023621568544962765, 0.025533167067605902, 0.027469296540794302, 0.029416291224546955, 0.031359687706557345, 0.03328438802089931, 0.03517483875165445, 0.037015223388917905, 0.03878966487117647, 0.04048243497259204, 0.04207816698364042, 0.04356206799476007, 0.044920127029484, 0.046139315288504214, 0.047207774860015456, 0.04811499242335274, 0.04885195471940834, 0.04941128287779857, 0.04978734307077841] + [0.04997633139944227] * 2 + [0.04978734307077841, 0.04941128287779857, 0.04885195471940834, 0.04811499242335274, 0.047207774860015456, 0.046139315288504214, 0.044920127029484, 0.04356206799476007, 0.04207816698364042, 0.0404824349725921, 0.03878966487117647, 0.037015223388917905, 0.03517483875165445, 0.03328438802089931, 0.031359687706557345, 0.029416291224546955, 0.027469296540794302, 0.025533167067605902, 0.023621568544962807, 0.02174722425642136, 0.019921790506671644, 0.018155753835766057, 0.016458350974447707, 0.014837512066932575, 0.013299827212922373, 0.011850535920178554, 0.010493538622702324, 0.009231429016631038, 0.008065545604508713, 0.006996040525523105, 0.006021963490151232, 0.005141358436474014, 0.004351370384723694, 0.0036483598873740444, 0.0030280224536970396, 0.0024855103681417643, 0.0020155544177197053, 0.001612583190143581, 0.0012708377960228441, 0.0009844800983365525, 0.0007476927933623619, 0.0005547699714462471, 0.0004001970854089779, 0.000278719560929705, 0.0001853995890370048, 0.00011566093837204936, 6.532190723564374e-05, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "minus_x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -6.532190723564394e-05, -0.00011566093837204924, -0.0001853995890370048, -0.0002787195609297057, -0.0004001970854089772, -0.0005547699714462471, -0.0007476927933623619, -0.0009844800983365512, -0.0012708377960228441, -0.001612583190143581, -0.0020155544177197023, -0.0024855103681417643, -0.0030280224536970396, -0.003648359887374041, -0.004351370384723694, -0.005141358436474014, -0.006021963490151232, -0.006996040525523105, -0.008065545604508713, -0.009231429016631038, -0.010493538622702324, -0.011850535920178554, -0.013299827212922373, -0.014837512066932575, -0.016458350974447707, -0.018155753835766026, -0.019921790506671644, -0.02174722425642136, -0.023621568544962765, -0.025533167067605902, -0.027469296540794302, -0.029416291224546955, -0.031359687706557345, -0.03328438802089931, -0.03517483875165445, -0.037015223388917905, -0.03878966487117647, -0.04048243497259204, -0.04207816698364042, -0.04356206799476007, -0.044920127029484, -0.046139315288504214, -0.047207774860015456, -0.04811499242335274, -0.04885195471940834, -0.04941128287779857, -0.04978734307077841] + [-0.04997633139944227] * 2 + [-0.04978734307077841, -0.04941128287779857, -0.04885195471940834, -0.04811499242335274, -0.047207774860015456, -0.046139315288504214, -0.044920127029484, -0.04356206799476007, -0.04207816698364042, -0.0404824349725921, -0.03878966487117647, -0.037015223388917905, -0.03517483875165445, -0.03328438802089931, -0.031359687706557345, -0.029416291224546955, -0.027469296540794302, -0.025533167067605902, -0.023621568544962807, -0.02174722425642136, -0.019921790506671644, -0.018155753835766057, -0.016458350974447707, -0.014837512066932575, -0.013299827212922373, -0.011850535920178554, -0.010493538622702324, -0.009231429016631038, -0.008065545604508713, -0.006996040525523105, -0.006021963490151232, -0.005141358436474014, -0.004351370384723694, -0.0036483598873740444, -0.0030280224536970396, -0.0024855103681417643, -0.0020155544177197053, -0.001612583190143581, -0.0012708377960228441, -0.0009844800983365525, -0.0007476927933623619, -0.0005547699714462471, -0.0004001970854089779, -0.000278719560929705, -0.0001853995890370048, -0.00011566093837204936, -6.532190723564374e-05, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "y180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "y180_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0001306438144712879, 0.00023132187674409848, 0.0003707991780740096, 0.0005574391218594114, 0.0008003941708179544, 0.0011095399428924942, 0.0014953855867247238, 0.0019689601966731024, 0.0025416755920456883, 0.003225166380287162, 0.0040311088354394045, 0.0049710207362835285, 0.006056044907394079, 0.007296719774748082, 0.008702740769447388, 0.010282716872948027, 0.012043926980302464, 0.01399208105104621, 0.016131091209017425, 0.018462858033262076, 0.020987077245404648, 0.023701071840357107, 0.026599654425844745, 0.02967502413386515, 0.03291670194889541, 0.03631150767153205, 0.03984358101334329, 0.04349444851284272, 0.04724313708992553, 0.051066334135211805, 0.054938593081588605, 0.05883258244909391, 0.06271937541311469, 0.06656877604179862, 0.0703496775033089, 0.07403044677783581, 0.07757932974235295, 0.08096486994518408, 0.08415633396728084, 0.08712413598952014, 0.089840254058968, 0.09227863057700843, 0.09441554972003091, 0.09622998484670547, 0.09770390943881668, 0.09882256575559714, 0.09957468614155682] + [0.09995266279888454] * 2 + [0.09957468614155682, 0.09882256575559714, 0.09770390943881668, 0.09622998484670547, 0.09441554972003091, 0.09227863057700843, 0.089840254058968, 0.08712413598952014, 0.08415633396728084, 0.0809648699451842, 0.07757932974235295, 0.07403044677783581, 0.0703496775033089, 0.06656877604179862, 0.06271937541311469, 0.05883258244909391, 0.054938593081588605, 0.051066334135211805, 0.04724313708992561, 0.04349444851284272, 0.03984358101334329, 0.036311507671532114, 0.03291670194889541, 0.02967502413386515, 0.026599654425844745, 0.023701071840357107, 0.020987077245404648, 0.018462858033262076, 0.016131091209017425, 0.01399208105104621, 0.012043926980302464, 0.010282716872948027, 0.008702740769447388, 0.007296719774748089, 0.006056044907394079, 0.0049710207362835285, 0.004031108835439411, 0.003225166380287162, 0.0025416755920456883, 0.001968960196673105, 0.0014953855867247238, 0.0011095399428924942, 0.0008003941708179558, 0.00055743912185941, 0.0003707991780740096, 0.00023132187674409872, 0.00013064381447128748, 6.123359277961564e-05] + [0] * 2,
        },
        "y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 6.532190723564394e-05, 0.00011566093837204924, 0.0001853995890370048, 0.0002787195609297057, 0.0004001970854089772, 0.0005547699714462471, 0.0007476927933623619, 0.0009844800983365512, 0.0012708377960228441, 0.001612583190143581, 0.0020155544177197023, 0.0024855103681417643, 0.0030280224536970396, 0.003648359887374041, 0.004351370384723694, 0.005141358436474014, 0.006021963490151232, 0.006996040525523105, 0.008065545604508713, 0.009231429016631038, 0.010493538622702324, 0.011850535920178554, 0.013299827212922373, 0.014837512066932575, 0.016458350974447707, 0.018155753835766026, 0.019921790506671644, 0.02174722425642136, 0.023621568544962765, 0.025533167067605902, 0.027469296540794302, 0.029416291224546955, 0.031359687706557345, 0.03328438802089931, 0.03517483875165445, 0.037015223388917905, 0.03878966487117647, 0.04048243497259204, 0.04207816698364042, 0.04356206799476007, 0.044920127029484, 0.046139315288504214, 0.047207774860015456, 0.04811499242335274, 0.04885195471940834, 0.04941128287779857, 0.04978734307077841] + [0.04997633139944227] * 2 + [0.04978734307077841, 0.04941128287779857, 0.04885195471940834, 0.04811499242335274, 0.047207774860015456, 0.046139315288504214, 0.044920127029484, 0.04356206799476007, 0.04207816698364042, 0.0404824349725921, 0.03878966487117647, 0.037015223388917905, 0.03517483875165445, 0.03328438802089931, 0.031359687706557345, 0.029416291224546955, 0.027469296540794302, 0.025533167067605902, 0.023621568544962807, 0.02174722425642136, 0.019921790506671644, 0.018155753835766057, 0.016458350974447707, 0.014837512066932575, 0.013299827212922373, 0.011850535920178554, 0.010493538622702324, 0.009231429016631038, 0.008065545604508713, 0.006996040525523105, 0.006021963490151232, 0.005141358436474014, 0.004351370384723694, 0.0036483598873740444, 0.0030280224536970396, 0.0024855103681417643, 0.0020155544177197053, 0.001612583190143581, 0.0012708377960228441, 0.0009844800983365525, 0.0007476927933623619, 0.0005547699714462471, 0.0004001970854089779, 0.000278719560929705, 0.0001853995890370048, 0.00011566093837204936, 6.532190723564374e-05, 3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "minus_y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -6.532190723564394e-05, -0.00011566093837204924, -0.0001853995890370048, -0.0002787195609297057, -0.0004001970854089772, -0.0005547699714462471, -0.0007476927933623619, -0.0009844800983365512, -0.0012708377960228441, -0.001612583190143581, -0.0020155544177197023, -0.0024855103681417643, -0.0030280224536970396, -0.003648359887374041, -0.004351370384723694, -0.005141358436474014, -0.006021963490151232, -0.006996040525523105, -0.008065545604508713, -0.009231429016631038, -0.010493538622702324, -0.011850535920178554, -0.013299827212922373, -0.014837512066932575, -0.016458350974447707, -0.018155753835766026, -0.019921790506671644, -0.02174722425642136, -0.023621568544962765, -0.025533167067605902, -0.027469296540794302, -0.029416291224546955, -0.031359687706557345, -0.03328438802089931, -0.03517483875165445, -0.037015223388917905, -0.03878966487117647, -0.04048243497259204, -0.04207816698364042, -0.04356206799476007, -0.044920127029484, -0.046139315288504214, -0.047207774860015456, -0.04811499242335274, -0.04885195471940834, -0.04941128287779857, -0.04978734307077841] + [-0.04997633139944227] * 2 + [-0.04978734307077841, -0.04941128287779857, -0.04885195471940834, -0.04811499242335274, -0.047207774860015456, -0.046139315288504214, -0.044920127029484, -0.04356206799476007, -0.04207816698364042, -0.0404824349725921, -0.03878966487117647, -0.037015223388917905, -0.03517483875165445, -0.03328438802089931, -0.031359687706557345, -0.029416291224546955, -0.027469296540794302, -0.025533167067605902, -0.023621568544962807, -0.02174722425642136, -0.019921790506671644, -0.018155753835766057, -0.016458350974447707, -0.014837512066932575, -0.013299827212922373, -0.011850535920178554, -0.010493538622702324, -0.009231429016631038, -0.008065545604508713, -0.006996040525523105, -0.006021963490151232, -0.005141358436474014, -0.004351370384723694, -0.0036483598873740444, -0.0030280224536970396, -0.0024855103681417643, -0.0020155544177197053, -0.001612583190143581, -0.0012708377960228441, -0.0009844800983365525, -0.0007476927933623619, -0.0005547699714462471, -0.0004001970854089779, -0.000278719560929705, -0.0001853995890370048, -0.00011566093837204936, -6.532190723564374e-05, -3.061679638980782e-05] + [0] * 2,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_tank_circuit1": {
            "cosine": [(1.0, 400)],
            "sine": [(0.0, 400)],
        },
        "cosine_weights_tank_circuit2": {
            "cosine": [(1.0, 400)],
            "sine": [(0.0, 400)],
        },
        "sine_weights_tank_circuit1": {
            "cosine": [(0.0, 400)],
            "sine": [(1.0, 400)],
        },
        "sine_weights_tank_circuit2": {
            "cosine": [(0.0, 400)],
            "sine": [(1.0, 400)],
        },
    },
    "mixers": {
        "mixer_qubit1": [{'intermediate_frequency': 50000000, 'lo_frequency': 16000000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qubit2": [{'intermediate_frequency': 200000000, 'lo_frequency': 16000000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qubit3": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qubit4": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qubit5": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qp_control_c3t2": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
    },
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "5": {
                    "type": "LF",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                    },
                    "analog_inputs": {
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                        },
                    },
                    "digital_outputs": {
                        "1": {
                            "shareable": False,
                            "inverted": False,
                            "level": "LVTTL",
                        },
                        "3": {
                            "shareable": False,
                            "inverted": False,
                            "level": "LVTTL",
                        },
                        "5": {
                            "shareable": False,
                            "inverted": False,
                            "level": "LVTTL",
                        },
                    },
                },
                "3": {
                    "type": "LF",
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
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
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
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
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
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "P1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P1_step_pulse",
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
                "port": ('con1', 3, 1),
            },
        },
        "P2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P2_step_pulse",
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
                "port": ('con1', 3, 2),
            },
        },
        "P3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P3_step_pulse",
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
                "port": ('con1', 3, 3),
            },
        },
        "P4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P4_step_pulse",
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
                "port": ('con1', 3, 4),
            },
        },
        "P5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P5_step_pulse",
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
                "port": ('con1', 3, 6),
            },
        },
        "P1_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P1_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 1),
            },
        },
        "P2_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P2_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 2),
            },
        },
        "P3_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P3_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 3),
            },
        },
        "P4_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P4_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 4),
            },
        },
        "P5_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P5_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 6),
            },
        },
        "B1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B1_step_pulse",
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
                "port": ('con1', 3, 4),
            },
        },
        "B2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B2_step_pulse",
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
                "port": ('con1', 3, 5),
            },
        },
        "B3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B3_step_pulse",
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
                "port": ('con1', 3, 6),
            },
        },
        "B4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B4_step_pulse",
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
                "port": ('con1', 3, 6),
            },
        },
        "B1_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B1_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 4),
            },
        },
        "B2_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B2_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 5),
            },
        },
        "B3_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B3_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 6),
            },
        },
        "B4_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B4_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 6),
            },
        },
        "Psd1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "Psd1_step_pulse",
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
                "port": ('con1', 3, 7),
            },
        },
        "Psd2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "Psd2_step_pulse",
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
                "port": ('con1', 3, 8),
            },
        },
        "Psd1_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "Psd1_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 7),
            },
        },
        "Psd2_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "Psd2_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 8),
            },
        },
        "qubit1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
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
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "mixer": "mixer_qubit1",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
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
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "mixer": "mixer_qubit2",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 200000000.0,
        },
        "qubit3": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
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
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "mixer": "mixer_qubit3",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit4": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
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
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "mixer": "mixer_qubit4",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit5": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
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
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit5",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit1_trio1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
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
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "mixer": "mixer_qubit1",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit2_trio1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
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
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "mixer": "mixer_qubit2",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 200000000.0,
        },
        "qubit3_trio1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
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
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "mixer": "mixer_qubit3",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit4_trio1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
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
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "mixer": "mixer_qubit4",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit5_trio1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
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
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit5",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit1_trio2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
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
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "mixer": "mixer_qubit1",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit2_trio2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
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
            "mixInputs": {
                "I": ('con1', 5, 1),
                "Q": ('con1', 5, 2),
                "mixer": "mixer_qubit2",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 200000000.0,
        },
        "qubit3_trio2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
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
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "mixer": "mixer_qubit3",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit4_trio2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
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
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "mixer": "mixer_qubit4",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit5_trio2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
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
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit5",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qp_control_c3t2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qp_control_c3t2",
                "x90_kaiser": "x90_kaiser_pulse_qp_control_c3t2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qp_control_c3t2",
                "y180_kaiser": "y180_kaiser_pulse_qp_control_c3t2",
                "y90_kaiser": "y90_kaiser_pulse_qp_control_c3t2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qp_control_c3t2",
                "x180_gauss": "x180_gaussian_pulse_qp_control_c3t2",
                "x90_gauss": "x90_gaussian_pulse_qp_control_c3t2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qp_control_c3t2",
                "y180_gauss": "y180_gaussian_pulse_qp_control_c3t2",
                "y90_gauss": "y90_gaussian_pulse_qp_control_c3t2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qp_control_c3t2",
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
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "mixer": "mixer_qp_control_c3t2",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit1_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "qubit2_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "qubit3_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "qubit4_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "qubit5_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "tank_circuit1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 2),
            },
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit1",
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
                "port": ('con1', 5, 8),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 150000000.0,
        },
        "tank_circuit2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 2),
            },
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit2",
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
                "port": ('con1', 5, 8),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 200000000.0,
        },
    },
    "pulses": {
        "P1_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P1_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P2_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P2_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P3_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P3_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P4_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P4_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P5_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P5_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "B1_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "B1_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "B2_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "B2_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "B3_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "B3_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "B4_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "B4_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "Psd1_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "Psd1_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "Psd2_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "Psd2_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit1",
                "Q": "x180_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit2",
                "Q": "x180_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit3",
                "Q": "x180_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit4",
                "Q": "x180_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit5",
                "Q": "x180_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit1",
                "Q": "x90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit2",
                "Q": "x90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit3",
                "Q": "x90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit4",
                "Q": "x90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit5",
                "Q": "x90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit1",
                "Q": "minus_x90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit2",
                "Q": "minus_x90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit3",
                "Q": "minus_x90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit4",
                "Q": "minus_x90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit5",
                "Q": "minus_x90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit1",
                "Q": "y180_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit2",
                "Q": "y180_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit3",
                "Q": "y180_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit4",
                "Q": "y180_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit5",
                "Q": "y180_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit1",
                "Q": "y90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit2",
                "Q": "y90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit3",
                "Q": "y90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit4",
                "Q": "y90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit5",
                "Q": "y90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit1",
                "Q": "minus_y90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit2",
                "Q": "minus_y90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit3",
                "Q": "minus_y90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit4",
                "Q": "minus_y90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit5",
                "Q": "minus_y90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit1",
                "Q": "x180_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit2",
                "Q": "x180_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit3",
                "Q": "x180_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit4",
                "Q": "x180_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit5",
                "Q": "x180_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit1",
                "Q": "x90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit2",
                "Q": "x90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit3",
                "Q": "x90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit4",
                "Q": "x90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit5",
                "Q": "x90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit1",
                "Q": "minus_x90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit2",
                "Q": "minus_x90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit3",
                "Q": "minus_x90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit4",
                "Q": "minus_x90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit5",
                "Q": "minus_x90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit1",
                "Q": "y180_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit2",
                "Q": "y180_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit3",
                "Q": "y180_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit4",
                "Q": "y180_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit5",
                "Q": "y180_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit1",
                "Q": "y90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit2",
                "Q": "y90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit3",
                "Q": "y90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit4",
                "Q": "y90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit5",
                "Q": "y90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit1",
                "Q": "minus_y90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit2",
                "Q": "minus_y90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit3",
                "Q": "minus_y90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit4",
                "Q": "minus_y90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit5",
                "Q": "minus_y90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qp_control_c3t2",
                "Q": "x180_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qp_control_c3t2",
                "Q": "x90_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qp_control_c3t2",
                "Q": "minus_x90_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qp_control_c3t2",
                "Q": "y180_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qp_control_c3t2",
                "Q": "y90_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qp_control_c3t2",
                "Q": "minus_y90_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qp_control_c3t2",
                "Q": "x180_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qp_control_c3t2",
                "Q": "x90_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qp_control_c3t2",
                "Q": "minus_x90_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qp_control_c3t2",
                "Q": "y180_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qp_control_c3t2",
                "Q": "y90_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qp_control_c3t2",
                "Q": "minus_y90_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "reflectometry_readout_pulse_tank_circuit1": {
            "length": 400,
            "waveforms": {
                "single": "reflectometry_readout_wf_tank_circuit1",
            },
            "integration_weights": {
                "cos": "cosine_weights_tank_circuit1",
                "sin": "sine_weights_tank_circuit1",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "reflectometry_readout_pulse_tank_circuit2": {
            "length": 400,
            "waveforms": {
                "single": "reflectometry_readout_wf_tank_circuit2",
            },
            "integration_weights": {
                "cos": "cosine_weights_tank_circuit2",
                "sin": "sine_weights_tank_circuit2",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "const_pulse": {
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_trio1": {
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf_trio1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_trio1": {
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf_trio1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_trio1": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf_trio1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_trio1": {
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf_trio1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_trio1": {
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf_trio1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_trio1": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf_trio1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "trigger_pulse": {
            "length": 1000,
            "waveforms": {},
            "integration_weights": {},
            "operation": "control",
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
            "sample": 0.1,
        },
        "square_x180_I_wf": {
            "type": "constant",
            "sample": 0.45,
        },
        "square_x90_I_wf": {
            "type": "constant",
            "sample": 0.4,
        },
        "square_minus_x90_I_wf": {
            "type": "constant",
            "sample": -0.4,
        },
        "square_y180_I_wf": {
            "type": "constant",
            "sample": 0.35,
        },
        "square_y90_I_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "square_minus_y90_I_wf": {
            "type": "constant",
            "sample": -0.3,
        },
        "square_x180_I_wf_trio1": {
            "type": "constant",
            "sample": 0.225,
        },
        "square_x90_I_wf_trio1": {
            "type": "constant",
            "sample": 0.2,
        },
        "square_minus_x90_I_wf_trio1": {
            "type": "constant",
            "sample": -0.2,
        },
        "square_y180_I_wf_trio1": {
            "type": "constant",
            "sample": 0.175,
        },
        "square_y90_I_wf_trio1": {
            "type": "constant",
            "sample": 0.15,
        },
        "square_minus_y90_I_wf_trio1": {
            "type": "constant",
            "sample": -0.15,
        },
        "reflectometry_readout_wf_tank_circuit1": {
            "type": "constant",
            "sample": 0.1,
        },
        "reflectometry_readout_wf_tank_circuit2": {
            "type": "constant",
            "sample": 0.1,
        },
        "P1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P3_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P4_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P5_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B3_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B4_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "Psd1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "Psd2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "x180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.000623059395668357, 0.0013134158229892211, 0.00207600456516317, 0.0029157968026681785, 0.003837749297415329, 0.004846747956223626, 0.0059475454464649755, 0.007144693172446949, 0.008442468066474543, 0.00984479480112677, 0.01135516418617893, 0.012976548671420715, 0.014711316031583668, 0.016561142457583073, 0.01852692641493371, 0.020608704751007553, 0.02280557263323139, 0.02511560897595016, 0.027535809060335543, 0.03006202606562717, 0.03268892320793267, 0.035409938122250045, 0.038217261022609625, 0.04110182803350147, 0.04405333090334345, 0.04706024408905373, 0.05010986994237358, 0.05318840243716088, 0.05628100955729227, 0.059371934122988815, 0.06244461247619, 0.06548181008073263, 0.06846577272886803, 0.07137839169082312, 0.07420138080762224, 0.07691646321812151, 0.07950556513773178, 0.08195101387660032, 0.08423573710622746, 0.08634346026167618, 0.08825889890645858, 0.08996794289214834, 0.09145782921645602, 0.09271730062188518, 0.09373674718038912, 0.09450832837415593, 0.09502607350358355] + [0.09528595862392984] * 2 + [0.09502607350358355, 0.09450832837415593, 0.09373674718038912, 0.09271730062188518, 0.09145782921645602, 0.08996794289214834, 0.08825889890645858, 0.08634346026167618, 0.08423573710622746, 0.08195101387660032, 0.07950556513773178, 0.07691646321812151, 0.07420138080762224, 0.07137839169082312, 0.06846577272886803, 0.06548181008073263, 0.06244461247619, 0.059371934122988815, 0.05628100955729227, 0.05318840243716088, 0.05010986994237358, 0.04706024408905373, 0.04405333090334345, 0.04110182803350147, 0.038217261022609625, 0.035409938122250045, 0.03268892320793267, 0.03006202606562717, 0.027535809060335543, 0.02511560897595016, 0.02280557263323139, 0.020608704751007553, 0.01852692641493371, 0.016561142457583073, 0.014711316031583668, 0.012976548671420715, 0.01135516418617893, 0.00984479480112677, 0.008442468066474543, 0.007144693172446949, 0.0059475454464649755, 0.004846747956223626, 0.003837749297415329, 0.0029157968026681785, 0.00207600456516317, 0.0013134158229892211, 0.000623059395668357] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003115296978341785, 0.0006567079114946106, 0.001038002282581585, 0.0014578984013340892, 0.0019188746487076645, 0.002423373978111813, 0.0029737727232324877, 0.0035723465862234744, 0.004221234033237271, 0.004922397400563385, 0.005677582093089465, 0.0064882743357103576, 0.007355658015791834, 0.008280571228791537, 0.009263463207466856, 0.010304352375503777, 0.011402786316615695, 0.01255780448797508, 0.013767904530167772, 0.015031013032813585, 0.016344461603966336, 0.017704969061125023, 0.019108630511304812, 0.020550914016750736, 0.022026665451671725, 0.023530122044526865, 0.02505493497118679, 0.02659420121858044, 0.028140504778646134, 0.029685967061494407, 0.031222306238095, 0.032740905040366315, 0.034232886364434015, 0.03568919584541156, 0.03710069040381112, 0.038458231609060756, 0.03975278256886589, 0.04097550693830016, 0.04211786855311373, 0.04317173013083809, 0.04412944945322929, 0.04498397144607417, 0.04572891460822801, 0.04635865031094259, 0.04686837359019456, 0.047254164187077966, 0.047513036751791776] + [0.04764297931196492] * 2 + [0.047513036751791776, 0.047254164187077966, 0.04686837359019456, 0.04635865031094259, 0.04572891460822801, 0.04498397144607417, 0.04412944945322929, 0.04317173013083809, 0.04211786855311373, 0.04097550693830016, 0.03975278256886589, 0.038458231609060756, 0.03710069040381112, 0.03568919584541156, 0.034232886364434015, 0.032740905040366315, 0.031222306238095, 0.029685967061494407, 0.028140504778646134, 0.02659420121858044, 0.02505493497118679, 0.023530122044526865, 0.022026665451671725, 0.020550914016750736, 0.019108630511304812, 0.017704969061125023, 0.016344461603966336, 0.015031013032813585, 0.013767904530167772, 0.01255780448797508, 0.011402786316615695, 0.010304352375503777, 0.009263463207466856, 0.008280571228791537, 0.007355658015791834, 0.0064882743357103576, 0.005677582093089465, 0.004922397400563385, 0.004221234033237271, 0.0035723465862234744, 0.0029737727232324877, 0.002423373978111813, 0.0019188746487076645, 0.0014578984013340892, 0.001038002282581585, 0.0006567079114946106, 0.0003115296978341785] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003115296978341785, -0.0006567079114946106, -0.001038002282581585, -0.0014578984013340892, -0.0019188746487076645, -0.002423373978111813, -0.0029737727232324877, -0.0035723465862234744, -0.004221234033237271, -0.004922397400563385, -0.005677582093089465, -0.0064882743357103576, -0.007355658015791834, -0.008280571228791537, -0.009263463207466856, -0.010304352375503777, -0.011402786316615695, -0.01255780448797508, -0.013767904530167772, -0.015031013032813585, -0.016344461603966336, -0.017704969061125023, -0.019108630511304812, -0.020550914016750736, -0.022026665451671725, -0.023530122044526865, -0.02505493497118679, -0.02659420121858044, -0.028140504778646134, -0.029685967061494407, -0.031222306238095, -0.032740905040366315, -0.034232886364434015, -0.03568919584541156, -0.03710069040381112, -0.038458231609060756, -0.03975278256886589, -0.04097550693830016, -0.04211786855311373, -0.04317173013083809, -0.04412944945322929, -0.04498397144607417, -0.04572891460822801, -0.04635865031094259, -0.04686837359019456, -0.047254164187077966, -0.047513036751791776] + [-0.04764297931196492] * 2 + [-0.047513036751791776, -0.047254164187077966, -0.04686837359019456, -0.04635865031094259, -0.04572891460822801, -0.04498397144607417, -0.04412944945322929, -0.04317173013083809, -0.04211786855311373, -0.04097550693830016, -0.03975278256886589, -0.038458231609060756, -0.03710069040381112, -0.03568919584541156, -0.034232886364434015, -0.032740905040366315, -0.031222306238095, -0.029685967061494407, -0.028140504778646134, -0.02659420121858044, -0.02505493497118679, -0.023530122044526865, -0.022026665451671725, -0.020550914016750736, -0.019108630511304812, -0.017704969061125023, -0.016344461603966336, -0.015031013032813585, -0.013767904530167772, -0.01255780448797508, -0.011402786316615695, -0.010304352375503777, -0.009263463207466856, -0.008280571228791537, -0.007355658015791834, -0.0064882743357103576, -0.005677582093089465, -0.004922397400563385, -0.004221234033237271, -0.0035723465862234744, -0.0029737727232324877, -0.002423373978111813, -0.0019188746487076645, -0.0014578984013340892, -0.001038002282581585, -0.0006567079114946106, -0.0003115296978341785] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.000623059395668357, 0.0013134158229892211, 0.00207600456516317, 0.0029157968026681785, 0.003837749297415329, 0.004846747956223626, 0.0059475454464649755, 0.007144693172446949, 0.008442468066474543, 0.00984479480112677, 0.01135516418617893, 0.012976548671420715, 0.014711316031583668, 0.016561142457583073, 0.01852692641493371, 0.020608704751007553, 0.02280557263323139, 0.02511560897595016, 0.027535809060335543, 0.03006202606562717, 0.03268892320793267, 0.035409938122250045, 0.038217261022609625, 0.04110182803350147, 0.04405333090334345, 0.04706024408905373, 0.05010986994237358, 0.05318840243716088, 0.05628100955729227, 0.059371934122988815, 0.06244461247619, 0.06548181008073263, 0.06846577272886803, 0.07137839169082312, 0.07420138080762224, 0.07691646321812151, 0.07950556513773178, 0.08195101387660032, 0.08423573710622746, 0.08634346026167618, 0.08825889890645858, 0.08996794289214834, 0.09145782921645602, 0.09271730062188518, 0.09373674718038912, 0.09450832837415593, 0.09502607350358355] + [0.09528595862392984] * 2 + [0.09502607350358355, 0.09450832837415593, 0.09373674718038912, 0.09271730062188518, 0.09145782921645602, 0.08996794289214834, 0.08825889890645858, 0.08634346026167618, 0.08423573710622746, 0.08195101387660032, 0.07950556513773178, 0.07691646321812151, 0.07420138080762224, 0.07137839169082312, 0.06846577272886803, 0.06548181008073263, 0.06244461247619, 0.059371934122988815, 0.05628100955729227, 0.05318840243716088, 0.05010986994237358, 0.04706024408905373, 0.04405333090334345, 0.04110182803350147, 0.038217261022609625, 0.035409938122250045, 0.03268892320793267, 0.03006202606562717, 0.027535809060335543, 0.02511560897595016, 0.02280557263323139, 0.020608704751007553, 0.01852692641493371, 0.016561142457583073, 0.014711316031583668, 0.012976548671420715, 0.01135516418617893, 0.00984479480112677, 0.008442468066474543, 0.007144693172446949, 0.0059475454464649755, 0.004846747956223626, 0.003837749297415329, 0.0029157968026681785, 0.00207600456516317, 0.0013134158229892211, 0.000623059395668357] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003115296978341785, 0.0006567079114946106, 0.001038002282581585, 0.0014578984013340892, 0.0019188746487076645, 0.002423373978111813, 0.0029737727232324877, 0.0035723465862234744, 0.004221234033237271, 0.004922397400563385, 0.005677582093089465, 0.0064882743357103576, 0.007355658015791834, 0.008280571228791537, 0.009263463207466856, 0.010304352375503777, 0.011402786316615695, 0.01255780448797508, 0.013767904530167772, 0.015031013032813585, 0.016344461603966336, 0.017704969061125023, 0.019108630511304812, 0.020550914016750736, 0.022026665451671725, 0.023530122044526865, 0.02505493497118679, 0.02659420121858044, 0.028140504778646134, 0.029685967061494407, 0.031222306238095, 0.032740905040366315, 0.034232886364434015, 0.03568919584541156, 0.03710069040381112, 0.038458231609060756, 0.03975278256886589, 0.04097550693830016, 0.04211786855311373, 0.04317173013083809, 0.04412944945322929, 0.04498397144607417, 0.04572891460822801, 0.04635865031094259, 0.04686837359019456, 0.047254164187077966, 0.047513036751791776] + [0.04764297931196492] * 2 + [0.047513036751791776, 0.047254164187077966, 0.04686837359019456, 0.04635865031094259, 0.04572891460822801, 0.04498397144607417, 0.04412944945322929, 0.04317173013083809, 0.04211786855311373, 0.04097550693830016, 0.03975278256886589, 0.038458231609060756, 0.03710069040381112, 0.03568919584541156, 0.034232886364434015, 0.032740905040366315, 0.031222306238095, 0.029685967061494407, 0.028140504778646134, 0.02659420121858044, 0.02505493497118679, 0.023530122044526865, 0.022026665451671725, 0.020550914016750736, 0.019108630511304812, 0.017704969061125023, 0.016344461603966336, 0.015031013032813585, 0.013767904530167772, 0.01255780448797508, 0.011402786316615695, 0.010304352375503777, 0.009263463207466856, 0.008280571228791537, 0.007355658015791834, 0.0064882743357103576, 0.005677582093089465, 0.004922397400563385, 0.004221234033237271, 0.0035723465862234744, 0.0029737727232324877, 0.002423373978111813, 0.0019188746487076645, 0.0014578984013340892, 0.001038002282581585, 0.0006567079114946106, 0.0003115296978341785] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003115296978341785, -0.0006567079114946106, -0.001038002282581585, -0.0014578984013340892, -0.0019188746487076645, -0.002423373978111813, -0.0029737727232324877, -0.0035723465862234744, -0.004221234033237271, -0.004922397400563385, -0.005677582093089465, -0.0064882743357103576, -0.007355658015791834, -0.008280571228791537, -0.009263463207466856, -0.010304352375503777, -0.011402786316615695, -0.01255780448797508, -0.013767904530167772, -0.015031013032813585, -0.016344461603966336, -0.017704969061125023, -0.019108630511304812, -0.020550914016750736, -0.022026665451671725, -0.023530122044526865, -0.02505493497118679, -0.02659420121858044, -0.028140504778646134, -0.029685967061494407, -0.031222306238095, -0.032740905040366315, -0.034232886364434015, -0.03568919584541156, -0.03710069040381112, -0.038458231609060756, -0.03975278256886589, -0.04097550693830016, -0.04211786855311373, -0.04317173013083809, -0.04412944945322929, -0.04498397144607417, -0.04572891460822801, -0.04635865031094259, -0.04686837359019456, -0.047254164187077966, -0.047513036751791776] + [-0.04764297931196492] * 2 + [-0.047513036751791776, -0.047254164187077966, -0.04686837359019456, -0.04635865031094259, -0.04572891460822801, -0.04498397144607417, -0.04412944945322929, -0.04317173013083809, -0.04211786855311373, -0.04097550693830016, -0.03975278256886589, -0.038458231609060756, -0.03710069040381112, -0.03568919584541156, -0.034232886364434015, -0.032740905040366315, -0.031222306238095, -0.029685967061494407, -0.028140504778646134, -0.02659420121858044, -0.02505493497118679, -0.023530122044526865, -0.022026665451671725, -0.020550914016750736, -0.019108630511304812, -0.017704969061125023, -0.016344461603966336, -0.015031013032813585, -0.013767904530167772, -0.01255780448797508, -0.011402786316615695, -0.010304352375503777, -0.009263463207466856, -0.008280571228791537, -0.007355658015791834, -0.0064882743357103576, -0.005677582093089465, -0.004922397400563385, -0.004221234033237271, -0.0035723465862234744, -0.0029737727232324877, -0.002423373978111813, -0.0019188746487076645, -0.0014578984013340892, -0.001038002282581585, -0.0006567079114946106, -0.0003115296978341785] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0001306438144712879, 0.00023132187674409848, 0.0003707991780740096, 0.0005574391218594114, 0.0008003941708179544, 0.0011095399428924942, 0.0014953855867247238, 0.0019689601966731024, 0.0025416755920456883, 0.003225166380287162, 0.0040311088354394045, 0.0049710207362835285, 0.006056044907394079, 0.007296719774748082, 0.008702740769447388, 0.010282716872948027, 0.012043926980302464, 0.01399208105104621, 0.016131091209017425, 0.018462858033262076, 0.020987077245404648, 0.023701071840357107, 0.026599654425844745, 0.02967502413386515, 0.03291670194889541, 0.03631150767153205, 0.03984358101334329, 0.04349444851284272, 0.04724313708992553, 0.051066334135211805, 0.054938593081588605, 0.05883258244909391, 0.06271937541311469, 0.06656877604179862, 0.0703496775033089, 0.07403044677783581, 0.07757932974235295, 0.08096486994518408, 0.08415633396728084, 0.08712413598952014, 0.089840254058968, 0.09227863057700843, 0.09441554972003091, 0.09622998484670547, 0.09770390943881668, 0.09882256575559714, 0.09957468614155682] + [0.09995266279888454] * 2 + [0.09957468614155682, 0.09882256575559714, 0.09770390943881668, 0.09622998484670547, 0.09441554972003091, 0.09227863057700843, 0.089840254058968, 0.08712413598952014, 0.08415633396728084, 0.0809648699451842, 0.07757932974235295, 0.07403044677783581, 0.0703496775033089, 0.06656877604179862, 0.06271937541311469, 0.05883258244909391, 0.054938593081588605, 0.051066334135211805, 0.04724313708992561, 0.04349444851284272, 0.03984358101334329, 0.036311507671532114, 0.03291670194889541, 0.02967502413386515, 0.026599654425844745, 0.023701071840357107, 0.020987077245404648, 0.018462858033262076, 0.016131091209017425, 0.01399208105104621, 0.012043926980302464, 0.010282716872948027, 0.008702740769447388, 0.007296719774748089, 0.006056044907394079, 0.0049710207362835285, 0.004031108835439411, 0.003225166380287162, 0.0025416755920456883, 0.001968960196673105, 0.0014953855867247238, 0.0011095399428924942, 0.0008003941708179558, 0.00055743912185941, 0.0003707991780740096, 0.00023132187674409872, 0.00013064381447128748, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 6.532190723564394e-05, 0.00011566093837204924, 0.0001853995890370048, 0.0002787195609297057, 0.0004001970854089772, 0.0005547699714462471, 0.0007476927933623619, 0.0009844800983365512, 0.0012708377960228441, 0.001612583190143581, 0.0020155544177197023, 0.0024855103681417643, 0.0030280224536970396, 0.003648359887374041, 0.004351370384723694, 0.005141358436474014, 0.006021963490151232, 0.006996040525523105, 0.008065545604508713, 0.009231429016631038, 0.010493538622702324, 0.011850535920178554, 0.013299827212922373, 0.014837512066932575, 0.016458350974447707, 0.018155753835766026, 0.019921790506671644, 0.02174722425642136, 0.023621568544962765, 0.025533167067605902, 0.027469296540794302, 0.029416291224546955, 0.031359687706557345, 0.03328438802089931, 0.03517483875165445, 0.037015223388917905, 0.03878966487117647, 0.04048243497259204, 0.04207816698364042, 0.04356206799476007, 0.044920127029484, 0.046139315288504214, 0.047207774860015456, 0.04811499242335274, 0.04885195471940834, 0.04941128287779857, 0.04978734307077841] + [0.04997633139944227] * 2 + [0.04978734307077841, 0.04941128287779857, 0.04885195471940834, 0.04811499242335274, 0.047207774860015456, 0.046139315288504214, 0.044920127029484, 0.04356206799476007, 0.04207816698364042, 0.0404824349725921, 0.03878966487117647, 0.037015223388917905, 0.03517483875165445, 0.03328438802089931, 0.031359687706557345, 0.029416291224546955, 0.027469296540794302, 0.025533167067605902, 0.023621568544962807, 0.02174722425642136, 0.019921790506671644, 0.018155753835766057, 0.016458350974447707, 0.014837512066932575, 0.013299827212922373, 0.011850535920178554, 0.010493538622702324, 0.009231429016631038, 0.008065545604508713, 0.006996040525523105, 0.006021963490151232, 0.005141358436474014, 0.004351370384723694, 0.0036483598873740444, 0.0030280224536970396, 0.0024855103681417643, 0.0020155544177197053, 0.001612583190143581, 0.0012708377960228441, 0.0009844800983365525, 0.0007476927933623619, 0.0005547699714462471, 0.0004001970854089779, 0.000278719560929705, 0.0001853995890370048, 0.00011566093837204936, 6.532190723564374e-05, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -6.532190723564394e-05, -0.00011566093837204924, -0.0001853995890370048, -0.0002787195609297057, -0.0004001970854089772, -0.0005547699714462471, -0.0007476927933623619, -0.0009844800983365512, -0.0012708377960228441, -0.001612583190143581, -0.0020155544177197023, -0.0024855103681417643, -0.0030280224536970396, -0.003648359887374041, -0.004351370384723694, -0.005141358436474014, -0.006021963490151232, -0.006996040525523105, -0.008065545604508713, -0.009231429016631038, -0.010493538622702324, -0.011850535920178554, -0.013299827212922373, -0.014837512066932575, -0.016458350974447707, -0.018155753835766026, -0.019921790506671644, -0.02174722425642136, -0.023621568544962765, -0.025533167067605902, -0.027469296540794302, -0.029416291224546955, -0.031359687706557345, -0.03328438802089931, -0.03517483875165445, -0.037015223388917905, -0.03878966487117647, -0.04048243497259204, -0.04207816698364042, -0.04356206799476007, -0.044920127029484, -0.046139315288504214, -0.047207774860015456, -0.04811499242335274, -0.04885195471940834, -0.04941128287779857, -0.04978734307077841] + [-0.04997633139944227] * 2 + [-0.04978734307077841, -0.04941128287779857, -0.04885195471940834, -0.04811499242335274, -0.047207774860015456, -0.046139315288504214, -0.044920127029484, -0.04356206799476007, -0.04207816698364042, -0.0404824349725921, -0.03878966487117647, -0.037015223388917905, -0.03517483875165445, -0.03328438802089931, -0.031359687706557345, -0.029416291224546955, -0.027469296540794302, -0.025533167067605902, -0.023621568544962807, -0.02174722425642136, -0.019921790506671644, -0.018155753835766057, -0.016458350974447707, -0.014837512066932575, -0.013299827212922373, -0.011850535920178554, -0.010493538622702324, -0.009231429016631038, -0.008065545604508713, -0.006996040525523105, -0.006021963490151232, -0.005141358436474014, -0.004351370384723694, -0.0036483598873740444, -0.0030280224536970396, -0.0024855103681417643, -0.0020155544177197053, -0.001612583190143581, -0.0012708377960228441, -0.0009844800983365525, -0.0007476927933623619, -0.0005547699714462471, -0.0004001970854089779, -0.000278719560929705, -0.0001853995890370048, -0.00011566093837204936, -6.532190723564374e-05, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0001306438144712879, 0.00023132187674409848, 0.0003707991780740096, 0.0005574391218594114, 0.0008003941708179544, 0.0011095399428924942, 0.0014953855867247238, 0.0019689601966731024, 0.0025416755920456883, 0.003225166380287162, 0.0040311088354394045, 0.0049710207362835285, 0.006056044907394079, 0.007296719774748082, 0.008702740769447388, 0.010282716872948027, 0.012043926980302464, 0.01399208105104621, 0.016131091209017425, 0.018462858033262076, 0.020987077245404648, 0.023701071840357107, 0.026599654425844745, 0.02967502413386515, 0.03291670194889541, 0.03631150767153205, 0.03984358101334329, 0.04349444851284272, 0.04724313708992553, 0.051066334135211805, 0.054938593081588605, 0.05883258244909391, 0.06271937541311469, 0.06656877604179862, 0.0703496775033089, 0.07403044677783581, 0.07757932974235295, 0.08096486994518408, 0.08415633396728084, 0.08712413598952014, 0.089840254058968, 0.09227863057700843, 0.09441554972003091, 0.09622998484670547, 0.09770390943881668, 0.09882256575559714, 0.09957468614155682] + [0.09995266279888454] * 2 + [0.09957468614155682, 0.09882256575559714, 0.09770390943881668, 0.09622998484670547, 0.09441554972003091, 0.09227863057700843, 0.089840254058968, 0.08712413598952014, 0.08415633396728084, 0.0809648699451842, 0.07757932974235295, 0.07403044677783581, 0.0703496775033089, 0.06656877604179862, 0.06271937541311469, 0.05883258244909391, 0.054938593081588605, 0.051066334135211805, 0.04724313708992561, 0.04349444851284272, 0.03984358101334329, 0.036311507671532114, 0.03291670194889541, 0.02967502413386515, 0.026599654425844745, 0.023701071840357107, 0.020987077245404648, 0.018462858033262076, 0.016131091209017425, 0.01399208105104621, 0.012043926980302464, 0.010282716872948027, 0.008702740769447388, 0.007296719774748089, 0.006056044907394079, 0.0049710207362835285, 0.004031108835439411, 0.003225166380287162, 0.0025416755920456883, 0.001968960196673105, 0.0014953855867247238, 0.0011095399428924942, 0.0008003941708179558, 0.00055743912185941, 0.0003707991780740096, 0.00023132187674409872, 0.00013064381447128748, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 6.532190723564394e-05, 0.00011566093837204924, 0.0001853995890370048, 0.0002787195609297057, 0.0004001970854089772, 0.0005547699714462471, 0.0007476927933623619, 0.0009844800983365512, 0.0012708377960228441, 0.001612583190143581, 0.0020155544177197023, 0.0024855103681417643, 0.0030280224536970396, 0.003648359887374041, 0.004351370384723694, 0.005141358436474014, 0.006021963490151232, 0.006996040525523105, 0.008065545604508713, 0.009231429016631038, 0.010493538622702324, 0.011850535920178554, 0.013299827212922373, 0.014837512066932575, 0.016458350974447707, 0.018155753835766026, 0.019921790506671644, 0.02174722425642136, 0.023621568544962765, 0.025533167067605902, 0.027469296540794302, 0.029416291224546955, 0.031359687706557345, 0.03328438802089931, 0.03517483875165445, 0.037015223388917905, 0.03878966487117647, 0.04048243497259204, 0.04207816698364042, 0.04356206799476007, 0.044920127029484, 0.046139315288504214, 0.047207774860015456, 0.04811499242335274, 0.04885195471940834, 0.04941128287779857, 0.04978734307077841] + [0.04997633139944227] * 2 + [0.04978734307077841, 0.04941128287779857, 0.04885195471940834, 0.04811499242335274, 0.047207774860015456, 0.046139315288504214, 0.044920127029484, 0.04356206799476007, 0.04207816698364042, 0.0404824349725921, 0.03878966487117647, 0.037015223388917905, 0.03517483875165445, 0.03328438802089931, 0.031359687706557345, 0.029416291224546955, 0.027469296540794302, 0.025533167067605902, 0.023621568544962807, 0.02174722425642136, 0.019921790506671644, 0.018155753835766057, 0.016458350974447707, 0.014837512066932575, 0.013299827212922373, 0.011850535920178554, 0.010493538622702324, 0.009231429016631038, 0.008065545604508713, 0.006996040525523105, 0.006021963490151232, 0.005141358436474014, 0.004351370384723694, 0.0036483598873740444, 0.0030280224536970396, 0.0024855103681417643, 0.0020155544177197053, 0.001612583190143581, 0.0012708377960228441, 0.0009844800983365525, 0.0007476927933623619, 0.0005547699714462471, 0.0004001970854089779, 0.000278719560929705, 0.0001853995890370048, 0.00011566093837204936, 6.532190723564374e-05, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -6.532190723564394e-05, -0.00011566093837204924, -0.0001853995890370048, -0.0002787195609297057, -0.0004001970854089772, -0.0005547699714462471, -0.0007476927933623619, -0.0009844800983365512, -0.0012708377960228441, -0.001612583190143581, -0.0020155544177197023, -0.0024855103681417643, -0.0030280224536970396, -0.003648359887374041, -0.004351370384723694, -0.005141358436474014, -0.006021963490151232, -0.006996040525523105, -0.008065545604508713, -0.009231429016631038, -0.010493538622702324, -0.011850535920178554, -0.013299827212922373, -0.014837512066932575, -0.016458350974447707, -0.018155753835766026, -0.019921790506671644, -0.02174722425642136, -0.023621568544962765, -0.025533167067605902, -0.027469296540794302, -0.029416291224546955, -0.031359687706557345, -0.03328438802089931, -0.03517483875165445, -0.037015223388917905, -0.03878966487117647, -0.04048243497259204, -0.04207816698364042, -0.04356206799476007, -0.044920127029484, -0.046139315288504214, -0.047207774860015456, -0.04811499242335274, -0.04885195471940834, -0.04941128287779857, -0.04978734307077841] + [-0.04997633139944227] * 2 + [-0.04978734307077841, -0.04941128287779857, -0.04885195471940834, -0.04811499242335274, -0.047207774860015456, -0.046139315288504214, -0.044920127029484, -0.04356206799476007, -0.04207816698364042, -0.0404824349725921, -0.03878966487117647, -0.037015223388917905, -0.03517483875165445, -0.03328438802089931, -0.031359687706557345, -0.029416291224546955, -0.027469296540794302, -0.025533167067605902, -0.023621568544962807, -0.02174722425642136, -0.019921790506671644, -0.018155753835766057, -0.016458350974447707, -0.014837512066932575, -0.013299827212922373, -0.011850535920178554, -0.010493538622702324, -0.009231429016631038, -0.008065545604508713, -0.006996040525523105, -0.006021963490151232, -0.005141358436474014, -0.004351370384723694, -0.0036483598873740444, -0.0030280224536970396, -0.0024855103681417643, -0.0020155544177197053, -0.001612583190143581, -0.0012708377960228441, -0.0009844800983365525, -0.0007476927933623619, -0.0005547699714462471, -0.0004001970854089779, -0.000278719560929705, -0.0001853995890370048, -0.00011566093837204936, -6.532190723564374e-05, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_tank_circuit1": {
            "cosine": [(1.0, 400)],
            "sine": [(0.0, 400)],
        },
        "cosine_weights_tank_circuit2": {
            "cosine": [(1.0, 400)],
            "sine": [(0.0, 400)],
        },
        "sine_weights_tank_circuit1": {
            "cosine": [(0.0, 400)],
            "sine": [(1.0, 400)],
        },
        "sine_weights_tank_circuit2": {
            "cosine": [(0.0, 400)],
            "sine": [(1.0, 400)],
        },
    },
    "mixers": {
        "mixer_qubit1": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 16000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit2": [{'intermediate_frequency': 200000000.0, 'lo_frequency': 16000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit3": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit4": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit5": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qp_control_c3t2": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
    },
}


