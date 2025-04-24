
# Single QUA script generated at 2025-04-23 20:32:07.885580
# QUA library version: 1.2.2

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    v3 = declare(int, )
    v4 = declare(int, )
    v5 = declare(int, )
    v6 = declare(fixed, )
    v7 = declare(fixed, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
    v10 = declare(int, )
    v11 = declare(int, )
    a1 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 0, 3, 2, 6, 7, 4, 5, 11, 10, 9, 8, 13, 12, 18, 19, 22, 23, 14, 15, 21, 20, 16, 17, 2, 3, 0, 1, 7, 6, 5, 4, 10, 11, 8, 9, 20, 21, 15, 14, 23, 22, 19, 18, 12, 13, 17, 16, 3, 2, 1, 0, 5, 4, 7, 6, 9, 8, 11, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 23, 22, 4, 7, 5, 6, 11, 8, 9, 10, 2, 3, 1, 0, 22, 17, 21, 12, 14, 18, 13, 20, 23, 16, 15, 19, 5, 6, 4, 7, 10, 9, 8, 11, 1, 0, 2, 3, 23, 16, 12, 21, 19, 15, 20, 13, 22, 17, 18, 14, 6, 5, 7, 4, 8, 11, 10, 9, 3, 2, 0, 1, 16, 23, 20, 13, 18, 14, 12, 21, 17, 22, 19, 15, 7, 4, 6, 5, 9, 10, 11, 8, 0, 1, 3, 2, 17, 22, 13, 20, 15, 19, 21, 12, 16, 23, 14, 18, 8, 9, 11, 10, 1, 3, 2, 0, 7, 4, 5, 6, 19, 14, 22, 16, 20, 12, 23, 17, 15, 18, 13, 21, 9, 8, 10, 11, 2, 0, 1, 3, 6, 5, 4, 7, 14, 19, 23, 17, 13, 21, 22, 16, 18, 15, 20, 12, 10, 11, 9, 8, 3, 1, 0, 2, 4, 7, 6, 5, 18, 15, 17, 23, 12, 20, 16, 22, 14, 19, 21, 13, 11, 10, 8, 9, 0, 2, 3, 1, 5, 6, 7, 4, 15, 18, 16, 22, 21, 13, 17, 23, 19, 14, 12, 20, 12, 13, 21, 20, 18, 19, 14, 15, 22, 17, 23, 16, 1, 0, 4, 5, 8, 10, 6, 7, 2, 3, 11, 9, 13, 12, 20, 21, 14, 15, 18, 19, 16, 23, 17, 22, 0, 1, 6, 7, 11, 9, 4, 5, 3, 2, 8, 10, 14, 19, 15, 18, 22, 16, 23, 17, 20, 21, 12, 13, 8, 9, 2, 0, 6, 4, 1, 3, 10, 11, 7, 5, 15, 18, 14, 19, 17, 23, 16, 22, 12, 13, 20, 21, 10, 11, 0, 2, 5, 7, 3, 1, 8, 9, 4, 6, 16, 23, 22, 17, 12, 21, 20, 13, 19, 14, 15, 18, 5, 6, 8, 11, 3, 0, 10, 9, 7, 4, 1, 2, 17, 22, 23, 16, 21, 12, 13, 20, 14, 19, 18, 15, 4, 7, 9, 10, 0, 3, 11, 8, 6, 5, 2, 1, 18, 15, 19, 14, 16, 22, 17, 23, 21, 20, 13, 12, 11, 10, 3, 1, 4, 6, 0, 2, 9, 8, 5, 7, 19, 14, 18, 15, 23, 17, 22, 16, 13, 12, 21, 20, 9, 8, 1, 3, 7, 5, 2, 0, 11, 10, 6, 4, 20, 21, 13, 12, 19, 18, 15, 14, 17, 22, 16, 23, 3, 2, 7, 6, 10, 8, 5, 4, 0, 1, 9, 11, 21, 20, 12, 13, 15, 14, 19, 18, 23, 16, 22, 17, 2, 3, 5, 4, 9, 11, 7, 6, 1, 0, 10, 8, 22, 17, 16, 23, 13, 20, 21, 12, 15, 18, 19, 14, 7, 4, 11, 8, 2, 1, 9, 10, 5, 6, 0, 3, 23, 16, 17, 22, 20, 13, 12, 21, 18, 15, 14, 19, 6, 5, 10, 9, 1, 2, 8, 11, 4, 7, 3, 0])
    a2 = declare(int, value=[0, 1, 2, 3, 11, 9, 10, 8, 7, 5, 6, 4, 13, 12, 15, 14, 17, 16, 18, 19, 20, 21, 22, 23])
    v12 = declare(int, )
    v13 = declare(int, )
    a3 = declare(int, size=6001)
    a4 = declare(int, size=6001)
    v14 = declare(int, )
    v15 = declare(int, value=345324)
    v16 = declare(int, )
    v17 = declare(int, )
    v18 = declare(fixed, )
    v19 = declare(fixed, )
    v20 = declare(fixed, )
    v21 = declare(fixed, )
    set_dc_offset("q1.z", "single", 0.0)
    set_dc_offset("q2.z", "single", 0.0)
    set_dc_offset("c12.z", "single", 0)
    align("q1.I", "q1.Q", "q1.resonator", "q1.z")
    set_dc_offset("q1.z", "single", 0.0)
    set_dc_offset("q2.z", "single", 0.0)
    set_dc_offset("c12.z", "single", 0)
    align("q2.I", "q2.Q", "q2.resonator", "q2.z")
    with for_(v4,0,(v4<10),(v4+1)):
        assign(v12, 0)
        with for_(v14,0,(v14<6000),(v14+1)):
            assign(v13, Random(v15).rand_int(24))
            assign(v12, a1[((v12*24)+v13)])
            assign(a3[v14], v13)
            assign(a4[v14], a2[v12])
        assign(v2, 1)
        with for_(v1,1,(v1<=6000),(v1+1)):
            assign(v3, a3[v1])
            assign(a3[v1], a4[(v1-1)])
            with if_((v1==v2)):
                with for_(v5,0,(v5<1),(v5+1)):
                    wait(18750, "q1.resonator")
                    wait(18750, "q2.resonator")
                    align()
                    with for_(v16,0,(v16<=v1),(v16+1)):
                        with if_((a3[v16]==0), unsafe=True):
                            wait(10, "q1.I", "q1.Q")
                        with elif_((a3[v16]==1)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x180_Cosine", "q1.I")
                            play("x180_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==2)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x180_Cosine", "q1.I")
                            play("x180_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==3)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x180_Cosine", "q1.I")
                            play("x180_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x180_Cosine", "q1.I")
                            play("x180_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==4)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==5)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==6)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==7)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==8)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==9)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==10)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==11)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==12)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==13)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==14)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==15)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==16)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==17)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==18)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x180_Cosine", "q1.I")
                            play("x180_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==19)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x180_Cosine", "q1.I")
                            play("x180_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==20)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x180_Cosine", "q1.I")
                            play("x180_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==21)):
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x180_Cosine", "q1.I")
                            play("x180_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==22)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                        with elif_((a3[v16]==23)):
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.I")
                            frame_rotation_2pi(0.25, "q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("x90_Cosine", "q1.I")
                            play("x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                            reset_frame("q1.I")
                            reset_frame("q1.Q")
                            frame_rotation_2pi(0.25, "q1.Q")
                            align("q1.I", "q1.Q")
                            play("-x90_Cosine", "q1.I")
                            play("-x90_Cosine", "q1.Q")
                            reset_frame("q1.Q")
                    with for_(v17,0,(v17<=v1),(v17+1)):
                        with if_((a3[v17]==0), unsafe=True):
                            wait(10, "q2.I", "q2.Q")
                        with elif_((a3[v17]==1)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x180_Cosine", "q2.I")
                            play("x180_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==2)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x180_Cosine", "q2.I")
                            play("x180_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==3)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x180_Cosine", "q2.I")
                            play("x180_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x180_Cosine", "q2.I")
                            play("x180_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==4)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==5)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==6)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==7)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==8)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==9)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==10)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==11)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==12)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==13)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==14)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==15)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==16)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==17)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==18)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x180_Cosine", "q2.I")
                            play("x180_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==19)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x180_Cosine", "q2.I")
                            play("x180_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==20)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x180_Cosine", "q2.I")
                            play("x180_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==21)):
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x180_Cosine", "q2.I")
                            play("x180_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==22)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                        with elif_((a3[v17]==23)):
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.I")
                            frame_rotation_2pi(0.25, "q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("x90_Cosine", "q2.I")
                            play("x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                            reset_frame("q2.I")
                            reset_frame("q2.Q")
                            frame_rotation_2pi(0.25, "q2.Q")
                            align("q2.I", "q2.Q")
                            play("-x90_Cosine", "q2.I")
                            play("-x90_Cosine", "q2.Q")
                            reset_frame("q2.Q")
                    align()
                    measure("readout", "q1.resonator", dual_demod.full("iw1", "iw2", v18), dual_demod.full("iw3", "iw1", v19))
                    assign(v10, Cast.to_int((v18>0.0)))
                    wait(250, "q1.resonator")
                    r7 = declare_stream()
                    save(v10, r7)
                    measure("readout", "q2.resonator", dual_demod.full("iw1", "iw2", v20), dual_demod.full("iw3", "iw1", v21))
                    assign(v11, Cast.to_int((v20>0.0)))
                    wait(250, "q2.resonator")
                    r8 = declare_stream()
                    save(v11, r8)
                assign(v2, (v2+20))
            assign(a3[v1], v3)
        r6 = declare_stream()
        save(v4, r6)
    with stream_processing():
        r6.save("iteration")
        r7.buffer(1).map(FUNCTIONS.average()).buffer(300).buffer(10).save("state1")
        r8.buffer(1).map(FUNCTIONS.average()).buffer(300).buffer(10).save("state2")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "fems": {
                "5": {
                    "type": "LF",
                    "analog_outputs": {
                        "5": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "1": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "2": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "3": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "4": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                    },
                },
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "upconverter_frequency": 4200000000,
                        },
                        "1": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "upconverter_frequency": 7300000000,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 2,
                            "downconverter_frequency": 7300000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "c12.xy": {
            "operations": {
                "x180_DragCosine": "c12.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "c12.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "c12.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "c12.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "c12.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "c12.xy.-y90_DragCosine.pulse",
                "x180_Square": "c12.xy.x180_Square.pulse",
                "x90_Square": "c12.xy.x90_Square.pulse",
                "-x90_Square": "c12.xy.-x90_Square.pulse",
                "y180_Square": "c12.xy.y180_Square.pulse",
                "y90_Square": "c12.xy.y90_Square.pulse",
                "-y90_Square": "c12.xy.-y90_Square.pulse",
                "x180": "c12.xy.x180_DragCosine.pulse",
                "x90": "c12.xy.x90_DragCosine.pulse",
                "-x90": "c12.xy.-x90_DragCosine.pulse",
                "y180": "c12.xy.y180_DragCosine.pulse",
                "y90": "c12.xy.y90_DragCosine.pulse",
                "-y90": "c12.xy.-y90_DragCosine.pulse",
                "saturation": "c12.xy.saturation.pulse",
            },
            "intermediate_frequency": -200000000.0,
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "c12.z": {
            "operations": {
                "const": "c12.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 5, 5),
            },
        },
        "q1.I": {
            "operations": {
                "x180_Cosine": "q1.I.x180_Cosine.pulse",
                "x90_Cosine": "q1.I.x90_Cosine.pulse",
                "-x90_Cosine": "q1.I.-x90_Cosine.pulse",
                "x180_DragCosine": "q1.I.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.I.x90_DragCosine.pulse",
                "x180_Square": "q1.I.x180_Square.pulse",
                "x90_Square": "q1.I.x90_Square.pulse",
                "saturation": "q1.I.saturation.pulse",
            },
            "intermediate_frequency": 100000000.0,
            "singleInput": {
                "port": ('con1', 5, 1),
            },
        },
        "q1.Q": {
            "operations": {
                "x180_Cosine": "q1.Q.x180_Cosine.pulse",
                "x90_Cosine": "q1.Q.x90_Cosine.pulse",
                "-x90_Cosine": "q1.Q.-x90_Cosine.pulse",
                "x180_DragCosine": "q1.Q.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.Q.x90_DragCosine.pulse",
                "x180_Square": "q1.Q.x180_Square.pulse",
                "x90_Square": "q1.Q.x90_Square.pulse",
                "saturation": "q1.Q.saturation.pulse",
            },
            "intermediate_frequency": 100000000.0,
            "singleInput": {
                "port": ('con1', 5, 1),
            },
        },
        "q1.z": {
            "operations": {
                "const": "q1.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 5, 2),
            },
        },
        "q1.resonator": {
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "intermediate_frequency": -297307575.0,
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
        "q2.I": {
            "operations": {
                "x180_Cosine": "q2.I.x180_Cosine.pulse",
                "x90_Cosine": "q2.I.x90_Cosine.pulse",
                "-x90_Cosine": "q2.I.-x90_Cosine.pulse",
                "x180_DragCosine": "q2.I.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.I.x90_DragCosine.pulse",
                "x180_Square": "q2.I.x180_Square.pulse",
                "x90_Square": "q2.I.x90_Square.pulse",
                "saturation": "q2.I.saturation.pulse",
            },
            "intermediate_frequency": 200000000.0,
            "singleInput": {
                "port": ('con1', 5, 3),
            },
        },
        "q2.Q": {
            "operations": {
                "x180_Cosine": "q2.Q.x180_Cosine.pulse",
                "x90_Cosine": "q2.Q.x90_Cosine.pulse",
                "-x90_Cosine": "q2.Q.-x90_Cosine.pulse",
                "x180_DragCosine": "q2.Q.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.Q.x90_DragCosine.pulse",
                "x180_Square": "q2.Q.x180_Square.pulse",
                "x90_Square": "q2.Q.x90_Square.pulse",
                "saturation": "q2.Q.saturation.pulse",
            },
            "intermediate_frequency": 200000000.0,
            "singleInput": {
                "port": ('con1', 5, 3),
            },
        },
        "q2.z": {
            "operations": {
                "const": "q2.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 5, 4),
            },
        },
        "q2.resonator": {
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "intermediate_frequency": -183964642.0,
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "c12.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.x180_DragCosine.wf.I",
                "Q": "c12.xy.x180_DragCosine.wf.Q",
            },
        },
        "c12.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.x90_DragCosine.wf.I",
                "Q": "c12.xy.x90_DragCosine.wf.Q",
            },
        },
        "c12.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.-x90_DragCosine.wf.I",
                "Q": "c12.xy.-x90_DragCosine.wf.Q",
            },
        },
        "c12.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.y180_DragCosine.wf.I",
                "Q": "c12.xy.y180_DragCosine.wf.Q",
            },
        },
        "c12.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.y90_DragCosine.wf.I",
                "Q": "c12.xy.y90_DragCosine.wf.Q",
            },
        },
        "c12.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.-y90_DragCosine.wf.I",
                "Q": "c12.xy.-y90_DragCosine.wf.Q",
            },
        },
        "c12.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.x180_Square.wf.I",
                "Q": "c12.xy.x180_Square.wf.Q",
            },
        },
        "c12.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.x90_Square.wf.I",
                "Q": "c12.xy.x90_Square.wf.Q",
            },
        },
        "c12.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.-x90_Square.wf.I",
                "Q": "c12.xy.-x90_Square.wf.Q",
            },
        },
        "c12.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.y180_Square.wf.I",
                "Q": "c12.xy.y180_Square.wf.Q",
            },
        },
        "c12.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.y90_Square.wf.I",
                "Q": "c12.xy.y90_Square.wf.Q",
            },
        },
        "c12.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.-y90_Square.wf.I",
                "Q": "c12.xy.-y90_Square.wf.Q",
            },
        },
        "c12.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.saturation.wf.I",
                "Q": "c12.xy.saturation.wf.Q",
            },
        },
        "c12.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "c12.z.const.wf",
            },
        },
        "q1.I.x180_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x180_Cosine.wf",
            },
        },
        "q1.I.x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x90_Cosine.wf",
            },
        },
        "q1.I.-x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.-x90_Cosine.wf",
            },
        },
        "q1.I.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x180_DragCosine.wf",
            },
        },
        "q1.I.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x90_DragCosine.wf",
            },
        },
        "q1.I.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x180_Square.wf",
            },
        },
        "q1.I.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x90_Square.wf",
            },
        },
        "q1.I.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.saturation.wf",
            },
        },
        "q1.Q.x180_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x180_Cosine.wf",
            },
        },
        "q1.Q.x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x90_Cosine.wf",
            },
        },
        "q1.Q.-x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.-x90_Cosine.wf",
            },
        },
        "q1.Q.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x180_DragCosine.wf",
            },
        },
        "q1.Q.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x90_DragCosine.wf",
            },
        },
        "q1.Q.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x180_Square.wf",
            },
        },
        "q1.Q.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x90_Square.wf",
            },
        },
        "q1.Q.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.saturation.wf",
            },
        },
        "q1.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q1.z.const.wf",
            },
        },
        "q1.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2500,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
        },
        "q1.resonator.const.pulse": {
            "operation": "control",
            "length": 2500,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
        },
        "q2.I.x180_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x180_Cosine.wf",
            },
        },
        "q2.I.x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x90_Cosine.wf",
            },
        },
        "q2.I.-x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.-x90_Cosine.wf",
            },
        },
        "q2.I.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x180_DragCosine.wf",
            },
        },
        "q2.I.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x90_DragCosine.wf",
            },
        },
        "q2.I.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x180_Square.wf",
            },
        },
        "q2.I.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x90_Square.wf",
            },
        },
        "q2.I.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.saturation.wf",
            },
        },
        "q2.Q.x180_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x180_Cosine.wf",
            },
        },
        "q2.Q.x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x90_Cosine.wf",
            },
        },
        "q2.Q.-x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.-x90_Cosine.wf",
            },
        },
        "q2.Q.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x180_DragCosine.wf",
            },
        },
        "q2.Q.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x90_DragCosine.wf",
            },
        },
        "q2.Q.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x180_Square.wf",
            },
        },
        "q2.Q.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x90_Square.wf",
            },
        },
        "q2.Q.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.saturation.wf",
            },
        },
        "q2.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q2.z.const.wf",
            },
        },
        "q2.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2500,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
        },
        "q2.resonator.const.pulse": {
            "operation": "control",
            "length": 2500,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
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
        "c12.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010235029373752758, 0.00405210941898847, 0.008961827939636185, 0.015551654046215668, 0.02355179948365188, 0.032634737357758986, 0.04242861112477117, 0.05253245844193564, 0.06253262661293602, 0.07201970757788172, 0.08060529912738312, 0.08793790613463955, 0.0937173308072291, 0.09770696282000245] + [0.09974346616959476] * 2 + [0.09770696282000245, 0.0937173308072291, 0.08793790613463956, 0.08060529912738314, 0.07201970757788172, 0.06253262661293606, 0.05253245844193569, 0.04242861112477117, 0.032634737357758986, 0.02355179948365188, 0.015551654046215675, 0.008961827939636185, 0.00405210941898847, 0.001023502937375287, 0.0],
        },
        "c12.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 32,
        },
        "c12.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005117514686876379, 0.002026054709494235, 0.004480913969818093, 0.007775827023107834, 0.01177589974182594, 0.016317368678879493, 0.021214305562385585, 0.02626622922096782, 0.03126631330646801, 0.03600985378894086, 0.04030264956369156, 0.04396895306731977, 0.04685866540361455, 0.048853481410001225] + [0.04987173308479738] * 2 + [0.048853481410001225, 0.04685866540361455, 0.04396895306731978, 0.04030264956369157, 0.03600985378894086, 0.03126631330646803, 0.026266229220967843, 0.021214305562385585, 0.016317368678879493, 0.01177589974182594, 0.007775827023107838, 0.004480913969818093, 0.002026054709494235, 0.0005117514686876435, 0.0],
        },
        "c12.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 32,
        },
        "c12.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005117514686876379, -0.002026054709494235, -0.004480913969818093, -0.007775827023107834, -0.01177589974182594, -0.016317368678879493, -0.021214305562385585, -0.02626622922096782, -0.03126631330646801, -0.03600985378894086, -0.04030264956369156, -0.04396895306731977, -0.04685866540361455, -0.048853481410001225] + [-0.04987173308479738] * 2 + [-0.048853481410001225, -0.04685866540361455, -0.04396895306731978, -0.04030264956369157, -0.03600985378894086, -0.03126631330646803, -0.026266229220967843, -0.021214305562385585, -0.016317368678879493, -0.01177589974182594, -0.007775827023107838, -0.004480913969818093, -0.002026054709494235, -0.0005117514686876435, 0.0],
        },
        "c12.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.267147980872727e-20, 2.481201414879535e-19, 5.487536950392387e-19, 9.522641674572502e-19, 1.442131792590728e-18, 1.9983013323097046e-18, 2.59800314031094e-18, 3.2166853541128915e-18, 3.829019051190435e-18, 4.409935218039061e-18, 4.935651078533234e-18, 5.384643763575336e-18, 5.738531459885338e-18, 5.982825963596272e-18] + [6.107525829022826e-18] * 2 + [5.982825963596272e-18, 5.738531459885338e-18, 5.384643763575337e-18, 4.9356510785332354e-18, 4.409935218039061e-18, 3.829019051190437e-18, 3.2166853541128946e-18, 2.59800314031094e-18, 1.9983013323097046e-18, 1.442131792590728e-18, 9.522641674572505e-19, 5.487536950392387e-19, 2.481201414879535e-19, 6.267147980872795e-20, 0.0],
        },
        "c12.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.267147980872727e-20, 2.481201414879535e-19, 5.487536950392387e-19, 9.522641674572502e-19, 1.442131792590728e-18, 1.9983013323097046e-18, 2.59800314031094e-18, 3.2166853541128915e-18, 3.829019051190435e-18, 4.409935218039061e-18, 4.935651078533234e-18, 5.384643763575336e-18, 5.738531459885338e-18, 5.982825963596272e-18] + [6.107525829022826e-18] * 2 + [5.982825963596272e-18, 5.738531459885338e-18, 5.384643763575337e-18, 4.9356510785332354e-18, 4.409935218039061e-18, 3.829019051190437e-18, 3.2166853541128946e-18, 2.59800314031094e-18, 1.9983013323097046e-18, 1.442131792590728e-18, 9.522641674572505e-19, 5.487536950392387e-19, 2.481201414879535e-19, 6.267147980872795e-20, 0.0],
        },
        "c12.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010235029373752758, 0.00405210941898847, 0.008961827939636185, 0.015551654046215668, 0.02355179948365188, 0.032634737357758986, 0.04242861112477117, 0.05253245844193564, 0.06253262661293602, 0.07201970757788172, 0.08060529912738312, 0.08793790613463955, 0.0937173308072291, 0.09770696282000245] + [0.09974346616959476] * 2 + [0.09770696282000245, 0.0937173308072291, 0.08793790613463956, 0.08060529912738314, 0.07201970757788172, 0.06253262661293606, 0.05253245844193569, 0.04242861112477117, 0.032634737357758986, 0.02355179948365188, 0.015551654046215675, 0.008961827939636185, 0.00405210941898847, 0.001023502937375287, 0.0],
        },
        "c12.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1335739904363637e-20, 1.2406007074397676e-19, 2.7437684751961936e-19, 4.761320837286251e-19, 7.21065896295364e-19, 9.991506661548523e-19, 1.29900157015547e-18, 1.6083426770564457e-18, 1.9145095255952173e-18, 2.2049676090195304e-18, 2.467825539266617e-18, 2.692321881787668e-18, 2.869265729942669e-18, 2.991412981798136e-18] + [3.053762914511413e-18] * 2 + [2.991412981798136e-18, 2.869265729942669e-18, 2.6923218817876684e-18, 2.4678255392666177e-18, 2.2049676090195304e-18, 1.9145095255952185e-18, 1.6083426770564473e-18, 1.29900157015547e-18, 9.991506661548523e-19, 7.21065896295364e-19, 4.761320837286253e-19, 2.7437684751961936e-19, 1.2406007074397676e-19, 3.1335739904363974e-20, 0.0],
        },
        "c12.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005117514686876379, 0.002026054709494235, 0.004480913969818093, 0.007775827023107834, 0.01177589974182594, 0.016317368678879493, 0.021214305562385585, 0.02626622922096782, 0.03126631330646801, 0.03600985378894086, 0.04030264956369156, 0.04396895306731977, 0.04685866540361455, 0.048853481410001225] + [0.04987173308479738] * 2 + [0.048853481410001225, 0.04685866540361455, 0.04396895306731978, 0.04030264956369157, 0.03600985378894086, 0.03126631330646803, 0.026266229220967843, 0.021214305562385585, 0.016317368678879493, 0.01177589974182594, 0.007775827023107838, 0.004480913969818093, 0.002026054709494235, 0.0005117514686876435, 0.0],
        },
        "c12.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1335739904363637e-20, 1.2406007074397676e-19, 2.7437684751961936e-19, 4.761320837286251e-19, 7.21065896295364e-19, 9.991506661548523e-19, 1.29900157015547e-18, 1.6083426770564457e-18, 1.9145095255952173e-18, 2.2049676090195304e-18, 2.467825539266617e-18, 2.692321881787668e-18, 2.869265729942669e-18, 2.991412981798136e-18] + [3.053762914511413e-18] * 2 + [2.991412981798136e-18, 2.869265729942669e-18, 2.6923218817876684e-18, 2.4678255392666177e-18, 2.2049676090195304e-18, 1.9145095255952185e-18, 1.6083426770564473e-18, 1.29900157015547e-18, 9.991506661548523e-19, 7.21065896295364e-19, 4.761320837286253e-19, 2.7437684751961936e-19, 1.2406007074397676e-19, 3.1335739904363974e-20, 0.0],
        },
        "c12.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005117514686876379, -0.002026054709494235, -0.004480913969818093, -0.007775827023107834, -0.01177589974182594, -0.016317368678879493, -0.021214305562385585, -0.02626622922096782, -0.03126631330646801, -0.03600985378894086, -0.04030264956369156, -0.04396895306731977, -0.04685866540361455, -0.048853481410001225] + [-0.04987173308479738] * 2 + [-0.048853481410001225, -0.04685866540361455, -0.04396895306731978, -0.04030264956369157, -0.03600985378894086, -0.03126631330646803, -0.026266229220967843, -0.021214305562385585, -0.016317368678879493, -0.01177589974182594, -0.007775827023107838, -0.004480913969818093, -0.002026054709494235, -0.0005117514686876435, 0.0],
        },
        "c12.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "c12.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "c12.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "c12.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "c12.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "c12.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "c12.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "c12.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "c12.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "c12.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "c12.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.I.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00010743860459705856, 0.0004269718149640719, 0.0009503238887956046, 0.0016639402822836136, 0.0025493387056822, 0.0035835878049037266, 0.004739901071544409, 0.0059883305993816555, 0.007296542719414335, 0.008630655424905802, 0.009956115897560977, 0.011238595407370443, 0.012444878408685616, 0.013543722805403726, 0.014506669104846175, 0.01530877750366982, 0.01592927381567328, 0.01635208751230737] + [0.016566267940923092] * 2 + [0.01635208751230737, 0.015929273815673283, 0.015308777503669824, 0.014506669104846178, 0.013543722805403726, 0.012444878408685611, 0.011238595407370449, 0.00995611589756098, 0.008630655424905802, 0.007296542719414342, 0.005988330599381661, 0.004739901071544412, 0.0035835878049037297, 0.002549338705682201, 0.0016639402822836136, 0.0009503238887956036, 0.000426971814964071, 0.00010743860459705856, 0.0],
        },
        "q1.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 5.371930229852928e-05, 0.00021348590748203596, 0.0004751619443978023, 0.0008319701411418068, 0.0012746693528411, 0.0017917939024518633, 0.0023699505357722044, 0.0029941652996908277, 0.0036482713597071675, 0.004315327712452901, 0.004978057948780488, 0.005619297703685222, 0.006222439204342808, 0.006771861402701863, 0.0072533345524230875, 0.00765438875183491, 0.00796463690783664, 0.008176043756153686] + [0.008283133970461546] * 2 + [0.008176043756153686, 0.007964636907836642, 0.007654388751834912, 0.007253334552423089, 0.006771861402701863, 0.0062224392043428054, 0.005619297703685224, 0.00497805794878049, 0.004315327712452901, 0.003648271359707171, 0.0029941652996908303, 0.002369950535772206, 0.0017917939024518648, 0.0012746693528411005, 0.0008319701411418068, 0.0004751619443978018, 0.0002134859074820355, 5.371930229852928e-05, 0.0],
        },
        "q1.I.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006474868681043578, -0.002573177902642726, -0.005727198717339505, -0.010027861829824942, -0.015363782324520032, -0.021596762663442206, -0.02856537192984729, -0.03608912680417736, -0.04397316598723385, -0.05201329700547076, -0.060001284688802205, -0.06773024435212678, -0.07500000000000001, -0.08162226877976886, -0.08742553740855505, -0.09225950427718974, -0.09599897218294122, -0.0985470908713026, -0.0998378654067105, -0.09983786540671051, -0.0985470908713026, -0.09599897218294123, -0.09225950427718976, -0.08742553740855508, -0.08162226877976886, -0.07499999999999998, -0.06773024435212681, -0.060001284688802226, -0.05201329700547076, -0.043973165987233886, -0.0360891268041774, -0.028565371929847313, -0.021596762663442223, -0.015363782324520037, -0.010027861829824942, -0.0057271987173395, -0.0025731779026427204, -0.0006474868681043578, 0.0],
        },
        "q1.I.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012949737362087156, 0.005146355805285452, 0.01145439743467901, 0.020055723659649884, 0.030727564649040064, 0.04319352532688441, 0.05713074385969458, 0.07217825360835473, 0.0879463319744677, 0.10402659401094153, 0.12000256937760441, 0.13546048870425356, 0.15000000000000002, 0.16324453755953772, 0.1748510748171101, 0.18451900855437947, 0.19199794436588244, 0.1970941817426052, 0.199675730813421, 0.19967573081342102, 0.1970941817426052, 0.19199794436588247, 0.18451900855437953, 0.17485107481711015, 0.16324453755953772, 0.14999999999999997, 0.13546048870425362, 0.12000256937760445, 0.10402659401094153, 0.08794633197446777, 0.0721782536083548, 0.057130743859694626, 0.04319352532688445, 0.030727564649040074, 0.020055723659649884, 0.011454397434679, 0.005146355805285441, 0.0012949737362087156, 0.0],
        },
        "q1.I.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006474865235251675, 0.0025731765421745604, 0.00572719572252497, 0.010027856668006575, 0.015363774578439817, 0.02159675205631711, 0.028565358344901863, 0.036089110297807266, 0.04397314679519682, 0.05201327554174647, 0.06000126153702194, 0.06773022024973922, 0.07499997581560172, 0.0816222454842792, 0.08742551604114582, 0.09225948590708327, 0.0959989578683585, 0.0985470816169707, 0.09983786212142061, 0.09983786886245094, 0.0985471016654741, 0.09599899070509398, 0.09225953068160411, 0.08742557159382541, 0.08162231037634414, 0.07500004836639468, 0.06773029858024633, 0.060001343618537185, 0.0520133592484133, 0.04397322995906577, 0.036089190764983514, 0.028565434031329072, 0.021596821001752402, 0.015363834997222079, 0.010027906995303338, 0.005727234654859972, 0.0025732030711865103, 0.0006474999620832822, 2.051915953781308e-23],
        },
        "q1.I.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.I.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.I.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.Q.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.Q.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.Q.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.Q.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.002742073177055731, 0.005413128099170471, 0.007943985846902028, 0.010269098533982546, 0.012328246963142131, 0.014068100271686437, 0.015443597172827051, 0.0164191130193397, 0.016969382463214604, 0.01708015381489863, 0.016748558154568684, 0.015983183635648122, 0.014803853056144253, 0.013241110458592388, 0.011335430055398216, 0.009136167967996604, 0.0067002839292320555, 0.004090866056197569, 0.0013754969011406171, -0.001375496901140613, -0.004090866056197572, -0.006700283929232043, -0.009136167967996597, -0.011335430055398207, -0.013241110458592392, -0.014803853056144256, -0.01598318363564812, -0.016748558154568684, -0.01708015381489863, -0.016969382463214604, -0.016419113019339703, -0.015443597172827055, -0.01406810027168644, -0.012328246963142131, -0.010269098533982548, -0.007943985846902027, -0.005413128099170466, -0.002742073177055738, -4.186826663751637e-18],
        },
        "q1.Q.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013710371168688756, 0.0027065660647557863, 0.00397199830085438, 0.005134560717308439, 0.006164144432031172, 0.007034084578733267, 0.007721850900375471, 0.008209631260363719, 0.008484792959128686, 0.0085402099084502, 0.008374447190037784, 0.007991798218483993, 0.007402173546107199, 0.0066208441895274405, 0.005668046125561179, 0.0045684561995969234, 0.0033505530199023133, 0.002045879390062873, 0.0006882253818169591, -0.000687246794114037, -0.0020449134542271726, -0.003349612060124502, -0.00456755189320125, -0.005667189200569045, -0.006620044146807444, -0.007401438413307741, -0.007991134342121528, -0.00837385907112546, -0.008539700085924046, -0.008484361944090534, -0.008209277522843944, -0.007721570908958379, -0.007033872892018857, -0.006163993839564462, -0.005134462426326372, -0.0039719421640136325, -0.0027065408429435014, -0.0013710307702896325, -2.09341389001896e-18],
        },
        "q1.Q.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.Q.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.Q.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.I.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003977503386995841, 0.001580699829954654, 0.003518210703316471, 0.006160102444892592, 0.009437951446298063, 0.013266863140171314, 0.017547670724875793, 0.02216950353257238, 0.02701265852127879, 0.03195170052077975, 0.03685871093764755, 0.041606600779619286, 0.04607240219373963, 0.05014045326916037, 0.05370539361987702, 0.05667489316338301, 0.05897204342130786, 0.0605373494086088, 0.061330270522432125, 0.06133027052243213, 0.0605373494086088, 0.058972043421307865, 0.056674893163383026, 0.053705393619877036, 0.05014045326916037, 0.046072402193739606, 0.0416066007796193, 0.03685871093764756, 0.03195170052077975, 0.027012658521278814, 0.0221695035325724, 0.017547670724875807, 0.013266863140171324, 0.009437951446298066, 0.006160102444892592, 0.003518210703316468, 0.0015806998299546504, 0.0003977503386995841, 0.0],
        },
        "q2.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00019887516934979205, 0.000790349914977327, 0.0017591053516582355, 0.003080051222446296, 0.004718975723149031, 0.006633431570085657, 0.008773835362437896, 0.01108475176628619, 0.013506329260639395, 0.015975850260389876, 0.018429355468823776, 0.020803300389809643, 0.023036201096869813, 0.025070226634580185, 0.02685269680993851, 0.028337446581691506, 0.02948602171065393, 0.0302686747043044, 0.030665135261216062, 0.030665135261216066, 0.0302686747043044, 0.029486021710653933, 0.028337446581691513, 0.026852696809938518, 0.025070226634580185, 0.023036201096869803, 0.02080330038980965, 0.01842935546882378, 0.015975850260389876, 0.013506329260639407, 0.0110847517662862, 0.008773835362437903, 0.006633431570085662, 0.004718975723149033, 0.003080051222446296, 0.001759105351658234, 0.0007903499149773252, 0.00019887516934979205, 0.0],
        },
        "q2.I.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006474868681043578, -0.002573177902642726, -0.005727198717339505, -0.010027861829824942, -0.015363782324520032, -0.021596762663442206, -0.02856537192984729, -0.03608912680417736, -0.04397316598723385, -0.05201329700547076, -0.060001284688802205, -0.06773024435212678, -0.07500000000000001, -0.08162226877976886, -0.08742553740855505, -0.09225950427718974, -0.09599897218294122, -0.0985470908713026, -0.0998378654067105, -0.09983786540671051, -0.0985470908713026, -0.09599897218294123, -0.09225950427718976, -0.08742553740855508, -0.08162226877976886, -0.07499999999999998, -0.06773024435212681, -0.060001284688802226, -0.05201329700547076, -0.043973165987233886, -0.0360891268041774, -0.028565371929847313, -0.021596762663442223, -0.015363782324520037, -0.010027861829824942, -0.0057271987173395, -0.0025731779026427204, -0.0006474868681043578, 0.0],
        },
        "q2.I.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012949737362087156, 0.005146355805285452, 0.01145439743467901, 0.020055723659649884, 0.030727564649040064, 0.04319352532688441, 0.05713074385969458, 0.07217825360835473, 0.0879463319744677, 0.10402659401094153, 0.12000256937760441, 0.13546048870425356, 0.15000000000000002, 0.16324453755953772, 0.1748510748171101, 0.18451900855437947, 0.19199794436588244, 0.1970941817426052, 0.199675730813421, 0.19967573081342102, 0.1970941817426052, 0.19199794436588247, 0.18451900855437953, 0.17485107481711015, 0.16324453755953772, 0.14999999999999997, 0.13546048870425362, 0.12000256937760445, 0.10402659401094153, 0.08794633197446777, 0.0721782536083548, 0.057130743859694626, 0.04319352532688445, 0.030727564649040074, 0.020055723659649884, 0.011454397434679, 0.005146355805285441, 0.0012949737362087156, 0.0],
        },
        "q2.I.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006474865235251675, 0.0025731765421745604, 0.00572719572252497, 0.010027856668006575, 0.015363774578439817, 0.02159675205631711, 0.028565358344901863, 0.036089110297807266, 0.04397314679519682, 0.05201327554174647, 0.06000126153702194, 0.06773022024973922, 0.07499997581560172, 0.0816222454842792, 0.08742551604114582, 0.09225948590708327, 0.0959989578683585, 0.0985470816169707, 0.09983786212142061, 0.09983786886245094, 0.0985471016654741, 0.09599899070509398, 0.09225953068160411, 0.08742557159382541, 0.08162231037634414, 0.07500004836639468, 0.06773029858024633, 0.060001343618537185, 0.0520133592484133, 0.04397322995906577, 0.036089190764983514, 0.028565434031329072, 0.021596821001752402, 0.015363834997222079, 0.010027906995303338, 0.005727234654859972, 0.0025732030711865103, 0.0006474999620832822, 2.051915953781308e-23],
        },
        "q2.I.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.I.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.I.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.Q.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.Q.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.Q.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.Q.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.002742073177055731, 0.005413128099170471, 0.007943985846902028, 0.010269098533982546, 0.012328246963142131, 0.014068100271686437, 0.015443597172827051, 0.0164191130193397, 0.016969382463214604, 0.01708015381489863, 0.016748558154568684, 0.015983183635648122, 0.014803853056144253, 0.013241110458592388, 0.011335430055398216, 0.009136167967996604, 0.0067002839292320555, 0.004090866056197569, 0.0013754969011406171, -0.001375496901140613, -0.004090866056197572, -0.006700283929232043, -0.009136167967996597, -0.011335430055398207, -0.013241110458592392, -0.014803853056144256, -0.01598318363564812, -0.016748558154568684, -0.01708015381489863, -0.016969382463214604, -0.016419113019339703, -0.015443597172827055, -0.01406810027168644, -0.012328246963142131, -0.010269098533982548, -0.007943985846902027, -0.005413128099170466, -0.002742073177055738, -4.186826663751637e-18],
        },
        "q2.Q.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013710371168688756, 0.0027065660647557863, 0.00397199830085438, 0.005134560717308439, 0.006164144432031172, 0.007034084578733267, 0.007721850900375471, 0.008209631260363719, 0.008484792959128686, 0.0085402099084502, 0.008374447190037784, 0.007991798218483993, 0.007402173546107199, 0.0066208441895274405, 0.005668046125561179, 0.0045684561995969234, 0.0033505530199023133, 0.002045879390062873, 0.0006882253818169591, -0.000687246794114037, -0.0020449134542271726, -0.003349612060124502, -0.00456755189320125, -0.005667189200569045, -0.006620044146807444, -0.007401438413307741, -0.007991134342121528, -0.00837385907112546, -0.008539700085924046, -0.008484361944090534, -0.008209277522843944, -0.007721570908958379, -0.007033872892018857, -0.006163993839564462, -0.005134462426326372, -0.0039719421640136325, -0.0027065408429435014, -0.0013710307702896325, -2.09341389001896e-18],
        },
        "q2.Q.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.Q.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.Q.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [[1, 0]],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(1.0, 2500)],
            "sine": [(-0.0, 2500)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.0, 2500)],
            "sine": [(1.0, 2500)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.0, 2500)],
            "sine": [(-1.0, 2500)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(1.0, 2500)],
            "sine": [(-0.0, 2500)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.0, 2500)],
            "sine": [(1.0, 2500)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.0, 2500)],
            "sine": [(-1.0, 2500)],
        },
    },
    "mixers": {},
    "oscillators": {},
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
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
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
                                "exponential": [],
                                "high_pass": None,
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                },
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4200000000.0,
                                },
                            },
                        },
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7300000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 2,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7300000000.0,
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "c12.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "c12.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "c12.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "c12.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "c12.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "c12.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "c12.xy.-y90_DragCosine.pulse",
                "x180_Square": "c12.xy.x180_Square.pulse",
                "x90_Square": "c12.xy.x90_Square.pulse",
                "-x90_Square": "c12.xy.-x90_Square.pulse",
                "y180_Square": "c12.xy.y180_Square.pulse",
                "y90_Square": "c12.xy.y90_Square.pulse",
                "-y90_Square": "c12.xy.-y90_Square.pulse",
                "x180": "c12.xy.x180_DragCosine.pulse",
                "x90": "c12.xy.x90_DragCosine.pulse",
                "-x90": "c12.xy.-x90_DragCosine.pulse",
                "y180": "c12.xy.y180_DragCosine.pulse",
                "y90": "c12.xy.y90_DragCosine.pulse",
                "-y90": "c12.xy.-y90_DragCosine.pulse",
                "saturation": "c12.xy.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": -200000000.0,
        },
        "c12.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "c12.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 5),
            },
        },
        "q1.I": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_Cosine": "q1.I.x180_Cosine.pulse",
                "x90_Cosine": "q1.I.x90_Cosine.pulse",
                "-x90_Cosine": "q1.I.-x90_Cosine.pulse",
                "x180_DragCosine": "q1.I.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.I.x90_DragCosine.pulse",
                "x180_Square": "q1.I.x180_Square.pulse",
                "x90_Square": "q1.I.x90_Square.pulse",
                "saturation": "q1.I.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 1),
            },
            "intermediate_frequency": 100000000.0,
        },
        "q1.Q": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_Cosine": "q1.Q.x180_Cosine.pulse",
                "x90_Cosine": "q1.Q.x90_Cosine.pulse",
                "-x90_Cosine": "q1.Q.-x90_Cosine.pulse",
                "x180_DragCosine": "q1.Q.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.Q.x90_DragCosine.pulse",
                "x180_Square": "q1.Q.x180_Square.pulse",
                "x90_Square": "q1.Q.x90_Square.pulse",
                "saturation": "q1.Q.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 1),
            },
            "intermediate_frequency": 100000000.0,
        },
        "q1.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q1.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 2),
            },
        },
        "q1.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -297307575.0,
        },
        "q2.I": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_Cosine": "q2.I.x180_Cosine.pulse",
                "x90_Cosine": "q2.I.x90_Cosine.pulse",
                "-x90_Cosine": "q2.I.-x90_Cosine.pulse",
                "x180_DragCosine": "q2.I.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.I.x90_DragCosine.pulse",
                "x180_Square": "q2.I.x180_Square.pulse",
                "x90_Square": "q2.I.x90_Square.pulse",
                "saturation": "q2.I.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 3),
            },
            "intermediate_frequency": 200000000.0,
        },
        "q2.Q": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_Cosine": "q2.Q.x180_Cosine.pulse",
                "x90_Cosine": "q2.Q.x90_Cosine.pulse",
                "-x90_Cosine": "q2.Q.-x90_Cosine.pulse",
                "x180_DragCosine": "q2.Q.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.Q.x90_DragCosine.pulse",
                "x180_Square": "q2.Q.x180_Square.pulse",
                "x90_Square": "q2.Q.x90_Square.pulse",
                "saturation": "q2.Q.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 3),
            },
            "intermediate_frequency": 200000000.0,
        },
        "q2.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q2.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 4),
            },
        },
        "q2.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -183964642.0,
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "c12.xy.x180_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.x180_DragCosine.wf.I",
                "Q": "c12.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.x90_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.x90_DragCosine.wf.I",
                "Q": "c12.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.-x90_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.-x90_DragCosine.wf.I",
                "Q": "c12.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.y180_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.y180_DragCosine.wf.I",
                "Q": "c12.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.y90_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.y90_DragCosine.wf.I",
                "Q": "c12.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.-y90_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.-y90_DragCosine.wf.I",
                "Q": "c12.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.x180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.x180_Square.wf.I",
                "Q": "c12.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.x90_Square.wf.I",
                "Q": "c12.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.-x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.-x90_Square.wf.I",
                "Q": "c12.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.y180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.y180_Square.wf.I",
                "Q": "c12.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.y90_Square.wf.I",
                "Q": "c12.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.-y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.-y90_Square.wf.I",
                "Q": "c12.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "c12.xy.saturation.wf.I",
                "Q": "c12.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "c12.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.I.x180_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x180_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.-x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.-x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x180_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x90_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x180_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x90_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "single": "q1.I.saturation.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x180_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x180_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.-x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.-x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x180_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x90_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x180_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x90_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "single": "q1.Q.saturation.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q1.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.resonator.readout.pulse": {
            "length": 2500,
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q1.resonator.const.pulse": {
            "length": 2500,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.I.x180_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x180_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.-x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.-x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x180_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x90_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x180_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x90_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "single": "q2.I.saturation.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x180_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x180_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.-x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.-x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x180_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x90_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x180_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x90_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "single": "q2.Q.saturation.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q2.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.resonator.readout.pulse": {
            "length": 2500,
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q2.resonator.const.pulse": {
            "length": 2500,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
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
        "c12.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010235029373752758, 0.00405210941898847, 0.008961827939636185, 0.015551654046215668, 0.02355179948365188, 0.032634737357758986, 0.04242861112477117, 0.05253245844193564, 0.06253262661293602, 0.07201970757788172, 0.08060529912738312, 0.08793790613463955, 0.0937173308072291, 0.09770696282000245] + [0.09974346616959476] * 2 + [0.09770696282000245, 0.0937173308072291, 0.08793790613463956, 0.08060529912738314, 0.07201970757788172, 0.06253262661293606, 0.05253245844193569, 0.04242861112477117, 0.032634737357758986, 0.02355179948365188, 0.015551654046215675, 0.008961827939636185, 0.00405210941898847, 0.001023502937375287, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 32,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005117514686876379, 0.002026054709494235, 0.004480913969818093, 0.007775827023107834, 0.01177589974182594, 0.016317368678879493, 0.021214305562385585, 0.02626622922096782, 0.03126631330646801, 0.03600985378894086, 0.04030264956369156, 0.04396895306731977, 0.04685866540361455, 0.048853481410001225] + [0.04987173308479738] * 2 + [0.048853481410001225, 0.04685866540361455, 0.04396895306731978, 0.04030264956369157, 0.03600985378894086, 0.03126631330646803, 0.026266229220967843, 0.021214305562385585, 0.016317368678879493, 0.01177589974182594, 0.007775827023107838, 0.004480913969818093, 0.002026054709494235, 0.0005117514686876435, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 32,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005117514686876379, -0.002026054709494235, -0.004480913969818093, -0.007775827023107834, -0.01177589974182594, -0.016317368678879493, -0.021214305562385585, -0.02626622922096782, -0.03126631330646801, -0.03600985378894086, -0.04030264956369156, -0.04396895306731977, -0.04685866540361455, -0.048853481410001225] + [-0.04987173308479738] * 2 + [-0.048853481410001225, -0.04685866540361455, -0.04396895306731978, -0.04030264956369157, -0.03600985378894086, -0.03126631330646803, -0.026266229220967843, -0.021214305562385585, -0.016317368678879493, -0.01177589974182594, -0.007775827023107838, -0.004480913969818093, -0.002026054709494235, -0.0005117514686876435, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.267147980872727e-20, 2.481201414879535e-19, 5.487536950392387e-19, 9.522641674572502e-19, 1.442131792590728e-18, 1.9983013323097046e-18, 2.59800314031094e-18, 3.2166853541128915e-18, 3.829019051190435e-18, 4.409935218039061e-18, 4.935651078533234e-18, 5.384643763575336e-18, 5.738531459885338e-18, 5.982825963596272e-18] + [6.107525829022826e-18] * 2 + [5.982825963596272e-18, 5.738531459885338e-18, 5.384643763575337e-18, 4.9356510785332354e-18, 4.409935218039061e-18, 3.829019051190437e-18, 3.2166853541128946e-18, 2.59800314031094e-18, 1.9983013323097046e-18, 1.442131792590728e-18, 9.522641674572505e-19, 5.487536950392387e-19, 2.481201414879535e-19, 6.267147980872795e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.267147980872727e-20, 2.481201414879535e-19, 5.487536950392387e-19, 9.522641674572502e-19, 1.442131792590728e-18, 1.9983013323097046e-18, 2.59800314031094e-18, 3.2166853541128915e-18, 3.829019051190435e-18, 4.409935218039061e-18, 4.935651078533234e-18, 5.384643763575336e-18, 5.738531459885338e-18, 5.982825963596272e-18] + [6.107525829022826e-18] * 2 + [5.982825963596272e-18, 5.738531459885338e-18, 5.384643763575337e-18, 4.9356510785332354e-18, 4.409935218039061e-18, 3.829019051190437e-18, 3.2166853541128946e-18, 2.59800314031094e-18, 1.9983013323097046e-18, 1.442131792590728e-18, 9.522641674572505e-19, 5.487536950392387e-19, 2.481201414879535e-19, 6.267147980872795e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010235029373752758, 0.00405210941898847, 0.008961827939636185, 0.015551654046215668, 0.02355179948365188, 0.032634737357758986, 0.04242861112477117, 0.05253245844193564, 0.06253262661293602, 0.07201970757788172, 0.08060529912738312, 0.08793790613463955, 0.0937173308072291, 0.09770696282000245] + [0.09974346616959476] * 2 + [0.09770696282000245, 0.0937173308072291, 0.08793790613463956, 0.08060529912738314, 0.07201970757788172, 0.06253262661293606, 0.05253245844193569, 0.04242861112477117, 0.032634737357758986, 0.02355179948365188, 0.015551654046215675, 0.008961827939636185, 0.00405210941898847, 0.001023502937375287, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1335739904363637e-20, 1.2406007074397676e-19, 2.7437684751961936e-19, 4.761320837286251e-19, 7.21065896295364e-19, 9.991506661548523e-19, 1.29900157015547e-18, 1.6083426770564457e-18, 1.9145095255952173e-18, 2.2049676090195304e-18, 2.467825539266617e-18, 2.692321881787668e-18, 2.869265729942669e-18, 2.991412981798136e-18] + [3.053762914511413e-18] * 2 + [2.991412981798136e-18, 2.869265729942669e-18, 2.6923218817876684e-18, 2.4678255392666177e-18, 2.2049676090195304e-18, 1.9145095255952185e-18, 1.6083426770564473e-18, 1.29900157015547e-18, 9.991506661548523e-19, 7.21065896295364e-19, 4.761320837286253e-19, 2.7437684751961936e-19, 1.2406007074397676e-19, 3.1335739904363974e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005117514686876379, 0.002026054709494235, 0.004480913969818093, 0.007775827023107834, 0.01177589974182594, 0.016317368678879493, 0.021214305562385585, 0.02626622922096782, 0.03126631330646801, 0.03600985378894086, 0.04030264956369156, 0.04396895306731977, 0.04685866540361455, 0.048853481410001225] + [0.04987173308479738] * 2 + [0.048853481410001225, 0.04685866540361455, 0.04396895306731978, 0.04030264956369157, 0.03600985378894086, 0.03126631330646803, 0.026266229220967843, 0.021214305562385585, 0.016317368678879493, 0.01177589974182594, 0.007775827023107838, 0.004480913969818093, 0.002026054709494235, 0.0005117514686876435, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1335739904363637e-20, 1.2406007074397676e-19, 2.7437684751961936e-19, 4.761320837286251e-19, 7.21065896295364e-19, 9.991506661548523e-19, 1.29900157015547e-18, 1.6083426770564457e-18, 1.9145095255952173e-18, 2.2049676090195304e-18, 2.467825539266617e-18, 2.692321881787668e-18, 2.869265729942669e-18, 2.991412981798136e-18] + [3.053762914511413e-18] * 2 + [2.991412981798136e-18, 2.869265729942669e-18, 2.6923218817876684e-18, 2.4678255392666177e-18, 2.2049676090195304e-18, 1.9145095255952185e-18, 1.6083426770564473e-18, 1.29900157015547e-18, 9.991506661548523e-19, 7.21065896295364e-19, 4.761320837286253e-19, 2.7437684751961936e-19, 1.2406007074397676e-19, 3.1335739904363974e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005117514686876379, -0.002026054709494235, -0.004480913969818093, -0.007775827023107834, -0.01177589974182594, -0.016317368678879493, -0.021214305562385585, -0.02626622922096782, -0.03126631330646801, -0.03600985378894086, -0.04030264956369156, -0.04396895306731977, -0.04685866540361455, -0.048853481410001225] + [-0.04987173308479738] * 2 + [-0.048853481410001225, -0.04685866540361455, -0.04396895306731978, -0.04030264956369157, -0.03600985378894086, -0.03126631330646803, -0.026266229220967843, -0.021214305562385585, -0.016317368678879493, -0.01177589974182594, -0.007775827023107838, -0.004480913969818093, -0.002026054709494235, -0.0005117514686876435, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "c12.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "c12.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "c12.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "c12.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "c12.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "c12.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "c12.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "c12.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "c12.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "c12.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.I.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00010743860459705856, 0.0004269718149640719, 0.0009503238887956046, 0.0016639402822836136, 0.0025493387056822, 0.0035835878049037266, 0.004739901071544409, 0.0059883305993816555, 0.007296542719414335, 0.008630655424905802, 0.009956115897560977, 0.011238595407370443, 0.012444878408685616, 0.013543722805403726, 0.014506669104846175, 0.01530877750366982, 0.01592927381567328, 0.01635208751230737] + [0.016566267940923092] * 2 + [0.01635208751230737, 0.015929273815673283, 0.015308777503669824, 0.014506669104846178, 0.013543722805403726, 0.012444878408685611, 0.011238595407370449, 0.00995611589756098, 0.008630655424905802, 0.007296542719414342, 0.005988330599381661, 0.004739901071544412, 0.0035835878049037297, 0.002549338705682201, 0.0016639402822836136, 0.0009503238887956036, 0.000426971814964071, 0.00010743860459705856, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 5.371930229852928e-05, 0.00021348590748203596, 0.0004751619443978023, 0.0008319701411418068, 0.0012746693528411, 0.0017917939024518633, 0.0023699505357722044, 0.0029941652996908277, 0.0036482713597071675, 0.004315327712452901, 0.004978057948780488, 0.005619297703685222, 0.006222439204342808, 0.006771861402701863, 0.0072533345524230875, 0.00765438875183491, 0.00796463690783664, 0.008176043756153686] + [0.008283133970461546] * 2 + [0.008176043756153686, 0.007964636907836642, 0.007654388751834912, 0.007253334552423089, 0.006771861402701863, 0.0062224392043428054, 0.005619297703685224, 0.00497805794878049, 0.004315327712452901, 0.003648271359707171, 0.0029941652996908303, 0.002369950535772206, 0.0017917939024518648, 0.0012746693528411005, 0.0008319701411418068, 0.0004751619443978018, 0.0002134859074820355, 5.371930229852928e-05, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006474868681043578, -0.002573177902642726, -0.005727198717339505, -0.010027861829824942, -0.015363782324520032, -0.021596762663442206, -0.02856537192984729, -0.03608912680417736, -0.04397316598723385, -0.05201329700547076, -0.060001284688802205, -0.06773024435212678, -0.07500000000000001, -0.08162226877976886, -0.08742553740855505, -0.09225950427718974, -0.09599897218294122, -0.0985470908713026, -0.0998378654067105, -0.09983786540671051, -0.0985470908713026, -0.09599897218294123, -0.09225950427718976, -0.08742553740855508, -0.08162226877976886, -0.07499999999999998, -0.06773024435212681, -0.060001284688802226, -0.05201329700547076, -0.043973165987233886, -0.0360891268041774, -0.028565371929847313, -0.021596762663442223, -0.015363782324520037, -0.010027861829824942, -0.0057271987173395, -0.0025731779026427204, -0.0006474868681043578, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012949737362087156, 0.005146355805285452, 0.01145439743467901, 0.020055723659649884, 0.030727564649040064, 0.04319352532688441, 0.05713074385969458, 0.07217825360835473, 0.0879463319744677, 0.10402659401094153, 0.12000256937760441, 0.13546048870425356, 0.15000000000000002, 0.16324453755953772, 0.1748510748171101, 0.18451900855437947, 0.19199794436588244, 0.1970941817426052, 0.199675730813421, 0.19967573081342102, 0.1970941817426052, 0.19199794436588247, 0.18451900855437953, 0.17485107481711015, 0.16324453755953772, 0.14999999999999997, 0.13546048870425362, 0.12000256937760445, 0.10402659401094153, 0.08794633197446777, 0.0721782536083548, 0.057130743859694626, 0.04319352532688445, 0.030727564649040074, 0.020055723659649884, 0.011454397434679, 0.005146355805285441, 0.0012949737362087156, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006474865235251675, 0.0025731765421745604, 0.00572719572252497, 0.010027856668006575, 0.015363774578439817, 0.02159675205631711, 0.028565358344901863, 0.036089110297807266, 0.04397314679519682, 0.05201327554174647, 0.06000126153702194, 0.06773022024973922, 0.07499997581560172, 0.0816222454842792, 0.08742551604114582, 0.09225948590708327, 0.0959989578683585, 0.0985470816169707, 0.09983786212142061, 0.09983786886245094, 0.0985471016654741, 0.09599899070509398, 0.09225953068160411, 0.08742557159382541, 0.08162231037634414, 0.07500004836639468, 0.06773029858024633, 0.060001343618537185, 0.0520133592484133, 0.04397322995906577, 0.036089190764983514, 0.028565434031329072, 0.021596821001752402, 0.015363834997222079, 0.010027906995303338, 0.005727234654859972, 0.0025732030711865103, 0.0006474999620832822, 2.051915953781308e-23],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.I.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.I.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.Q.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.002742073177055731, 0.005413128099170471, 0.007943985846902028, 0.010269098533982546, 0.012328246963142131, 0.014068100271686437, 0.015443597172827051, 0.0164191130193397, 0.016969382463214604, 0.01708015381489863, 0.016748558154568684, 0.015983183635648122, 0.014803853056144253, 0.013241110458592388, 0.011335430055398216, 0.009136167967996604, 0.0067002839292320555, 0.004090866056197569, 0.0013754969011406171, -0.001375496901140613, -0.004090866056197572, -0.006700283929232043, -0.009136167967996597, -0.011335430055398207, -0.013241110458592392, -0.014803853056144256, -0.01598318363564812, -0.016748558154568684, -0.01708015381489863, -0.016969382463214604, -0.016419113019339703, -0.015443597172827055, -0.01406810027168644, -0.012328246963142131, -0.010269098533982548, -0.007943985846902027, -0.005413128099170466, -0.002742073177055738, -4.186826663751637e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013710371168688756, 0.0027065660647557863, 0.00397199830085438, 0.005134560717308439, 0.006164144432031172, 0.007034084578733267, 0.007721850900375471, 0.008209631260363719, 0.008484792959128686, 0.0085402099084502, 0.008374447190037784, 0.007991798218483993, 0.007402173546107199, 0.0066208441895274405, 0.005668046125561179, 0.0045684561995969234, 0.0033505530199023133, 0.002045879390062873, 0.0006882253818169591, -0.000687246794114037, -0.0020449134542271726, -0.003349612060124502, -0.00456755189320125, -0.005667189200569045, -0.006620044146807444, -0.007401438413307741, -0.007991134342121528, -0.00837385907112546, -0.008539700085924046, -0.008484361944090534, -0.008209277522843944, -0.007721570908958379, -0.007033872892018857, -0.006163993839564462, -0.005134462426326372, -0.0039719421640136325, -0.0027065408429435014, -0.0013710307702896325, -2.09341389001896e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.Q.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.Q.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.I.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003977503386995841, 0.001580699829954654, 0.003518210703316471, 0.006160102444892592, 0.009437951446298063, 0.013266863140171314, 0.017547670724875793, 0.02216950353257238, 0.02701265852127879, 0.03195170052077975, 0.03685871093764755, 0.041606600779619286, 0.04607240219373963, 0.05014045326916037, 0.05370539361987702, 0.05667489316338301, 0.05897204342130786, 0.0605373494086088, 0.061330270522432125, 0.06133027052243213, 0.0605373494086088, 0.058972043421307865, 0.056674893163383026, 0.053705393619877036, 0.05014045326916037, 0.046072402193739606, 0.0416066007796193, 0.03685871093764756, 0.03195170052077975, 0.027012658521278814, 0.0221695035325724, 0.017547670724875807, 0.013266863140171324, 0.009437951446298066, 0.006160102444892592, 0.003518210703316468, 0.0015806998299546504, 0.0003977503386995841, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00019887516934979205, 0.000790349914977327, 0.0017591053516582355, 0.003080051222446296, 0.004718975723149031, 0.006633431570085657, 0.008773835362437896, 0.01108475176628619, 0.013506329260639395, 0.015975850260389876, 0.018429355468823776, 0.020803300389809643, 0.023036201096869813, 0.025070226634580185, 0.02685269680993851, 0.028337446581691506, 0.02948602171065393, 0.0302686747043044, 0.030665135261216062, 0.030665135261216066, 0.0302686747043044, 0.029486021710653933, 0.028337446581691513, 0.026852696809938518, 0.025070226634580185, 0.023036201096869803, 0.02080330038980965, 0.01842935546882378, 0.015975850260389876, 0.013506329260639407, 0.0110847517662862, 0.008773835362437903, 0.006633431570085662, 0.004718975723149033, 0.003080051222446296, 0.001759105351658234, 0.0007903499149773252, 0.00019887516934979205, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006474868681043578, -0.002573177902642726, -0.005727198717339505, -0.010027861829824942, -0.015363782324520032, -0.021596762663442206, -0.02856537192984729, -0.03608912680417736, -0.04397316598723385, -0.05201329700547076, -0.060001284688802205, -0.06773024435212678, -0.07500000000000001, -0.08162226877976886, -0.08742553740855505, -0.09225950427718974, -0.09599897218294122, -0.0985470908713026, -0.0998378654067105, -0.09983786540671051, -0.0985470908713026, -0.09599897218294123, -0.09225950427718976, -0.08742553740855508, -0.08162226877976886, -0.07499999999999998, -0.06773024435212681, -0.060001284688802226, -0.05201329700547076, -0.043973165987233886, -0.0360891268041774, -0.028565371929847313, -0.021596762663442223, -0.015363782324520037, -0.010027861829824942, -0.0057271987173395, -0.0025731779026427204, -0.0006474868681043578, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012949737362087156, 0.005146355805285452, 0.01145439743467901, 0.020055723659649884, 0.030727564649040064, 0.04319352532688441, 0.05713074385969458, 0.07217825360835473, 0.0879463319744677, 0.10402659401094153, 0.12000256937760441, 0.13546048870425356, 0.15000000000000002, 0.16324453755953772, 0.1748510748171101, 0.18451900855437947, 0.19199794436588244, 0.1970941817426052, 0.199675730813421, 0.19967573081342102, 0.1970941817426052, 0.19199794436588247, 0.18451900855437953, 0.17485107481711015, 0.16324453755953772, 0.14999999999999997, 0.13546048870425362, 0.12000256937760445, 0.10402659401094153, 0.08794633197446777, 0.0721782536083548, 0.057130743859694626, 0.04319352532688445, 0.030727564649040074, 0.020055723659649884, 0.011454397434679, 0.005146355805285441, 0.0012949737362087156, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006474865235251675, 0.0025731765421745604, 0.00572719572252497, 0.010027856668006575, 0.015363774578439817, 0.02159675205631711, 0.028565358344901863, 0.036089110297807266, 0.04397314679519682, 0.05201327554174647, 0.06000126153702194, 0.06773022024973922, 0.07499997581560172, 0.0816222454842792, 0.08742551604114582, 0.09225948590708327, 0.0959989578683585, 0.0985470816169707, 0.09983786212142061, 0.09983786886245094, 0.0985471016654741, 0.09599899070509398, 0.09225953068160411, 0.08742557159382541, 0.08162231037634414, 0.07500004836639468, 0.06773029858024633, 0.060001343618537185, 0.0520133592484133, 0.04397322995906577, 0.036089190764983514, 0.028565434031329072, 0.021596821001752402, 0.015363834997222079, 0.010027906995303338, 0.005727234654859972, 0.0025732030711865103, 0.0006474999620832822, 2.051915953781308e-23],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.I.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.I.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.Q.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.002742073177055731, 0.005413128099170471, 0.007943985846902028, 0.010269098533982546, 0.012328246963142131, 0.014068100271686437, 0.015443597172827051, 0.0164191130193397, 0.016969382463214604, 0.01708015381489863, 0.016748558154568684, 0.015983183635648122, 0.014803853056144253, 0.013241110458592388, 0.011335430055398216, 0.009136167967996604, 0.0067002839292320555, 0.004090866056197569, 0.0013754969011406171, -0.001375496901140613, -0.004090866056197572, -0.006700283929232043, -0.009136167967996597, -0.011335430055398207, -0.013241110458592392, -0.014803853056144256, -0.01598318363564812, -0.016748558154568684, -0.01708015381489863, -0.016969382463214604, -0.016419113019339703, -0.015443597172827055, -0.01406810027168644, -0.012328246963142131, -0.010269098533982548, -0.007943985846902027, -0.005413128099170466, -0.002742073177055738, -4.186826663751637e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013710371168688756, 0.0027065660647557863, 0.00397199830085438, 0.005134560717308439, 0.006164144432031172, 0.007034084578733267, 0.007721850900375471, 0.008209631260363719, 0.008484792959128686, 0.0085402099084502, 0.008374447190037784, 0.007991798218483993, 0.007402173546107199, 0.0066208441895274405, 0.005668046125561179, 0.0045684561995969234, 0.0033505530199023133, 0.002045879390062873, 0.0006882253818169591, -0.000687246794114037, -0.0020449134542271726, -0.003349612060124502, -0.00456755189320125, -0.005667189200569045, -0.006620044146807444, -0.007401438413307741, -0.007991134342121528, -0.00837385907112546, -0.008539700085924046, -0.008484361944090534, -0.008209277522843944, -0.007721570908958379, -0.007033872892018857, -0.006163993839564462, -0.005134462426326372, -0.0039719421640136325, -0.0027065408429435014, -0.0013710307702896325, -2.09341389001896e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.Q.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.Q.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(1.0, 2500)],
            "sine": [(-0.0, 2500)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.0, 2500)],
            "sine": [(1.0, 2500)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.0, 2500)],
            "sine": [(-1.0, 2500)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(1.0, 2500)],
            "sine": [(-0.0, 2500)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.0, 2500)],
            "sine": [(1.0, 2500)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.0, 2500)],
            "sine": [(-1.0, 2500)],
        },
    },
    "mixers": {},
}


