
# Single QUA script generated at 2025-01-16 00:44:01.131241
# QUA library version: 1.2.1

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
    v8 = declare(bool, )
    v9 = declare(bool, )
    v10 = declare(bool, )
    v11 = declare(int, value=1)
    v12 = declare(int, value=1)
    v13 = declare(int, )
    v14 = declare(int, )
    v15 = declare(int, )
    a1 = declare(fixed, value=[0.0, 0.0])
    a2 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 0, 3, 2, 6, 7, 4, 5, 11, 10, 9, 8, 13, 12, 18, 19, 22, 23, 14, 15, 21, 20, 16, 17, 2, 3, 0, 1, 7, 6, 5, 4, 10, 11, 8, 9, 20, 21, 15, 14, 23, 22, 19, 18, 12, 13, 17, 16, 3, 2, 1, 0, 5, 4, 7, 6, 9, 8, 11, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 23, 22, 4, 7, 5, 6, 11, 8, 9, 10, 2, 3, 1, 0, 22, 17, 21, 12, 14, 18, 13, 20, 23, 16, 15, 19, 5, 6, 4, 7, 10, 9, 8, 11, 1, 0, 2, 3, 23, 16, 12, 21, 19, 15, 20, 13, 22, 17, 18, 14, 6, 5, 7, 4, 8, 11, 10, 9, 3, 2, 0, 1, 16, 23, 20, 13, 18, 14, 12, 21, 17, 22, 19, 15, 7, 4, 6, 5, 9, 10, 11, 8, 0, 1, 3, 2, 17, 22, 13, 20, 15, 19, 21, 12, 16, 23, 14, 18, 8, 9, 11, 10, 1, 3, 2, 0, 7, 4, 5, 6, 19, 14, 22, 16, 20, 12, 23, 17, 15, 18, 13, 21, 9, 8, 10, 11, 2, 0, 1, 3, 6, 5, 4, 7, 14, 19, 23, 17, 13, 21, 22, 16, 18, 15, 20, 12, 10, 11, 9, 8, 3, 1, 0, 2, 4, 7, 6, 5, 18, 15, 17, 23, 12, 20, 16, 22, 14, 19, 21, 13, 11, 10, 8, 9, 0, 2, 3, 1, 5, 6, 7, 4, 15, 18, 16, 22, 21, 13, 17, 23, 19, 14, 12, 20, 12, 13, 21, 20, 18, 19, 14, 15, 22, 17, 23, 16, 1, 0, 4, 5, 8, 10, 6, 7, 2, 3, 11, 9, 13, 12, 20, 21, 14, 15, 18, 19, 16, 23, 17, 22, 0, 1, 6, 7, 11, 9, 4, 5, 3, 2, 8, 10, 14, 19, 15, 18, 22, 16, 23, 17, 20, 21, 12, 13, 8, 9, 2, 0, 6, 4, 1, 3, 10, 11, 7, 5, 15, 18, 14, 19, 17, 23, 16, 22, 12, 13, 20, 21, 10, 11, 0, 2, 5, 7, 3, 1, 8, 9, 4, 6, 16, 23, 22, 17, 12, 21, 20, 13, 19, 14, 15, 18, 5, 6, 8, 11, 3, 0, 10, 9, 7, 4, 1, 2, 17, 22, 23, 16, 21, 12, 13, 20, 14, 19, 18, 15, 4, 7, 9, 10, 0, 3, 11, 8, 6, 5, 2, 1, 18, 15, 19, 14, 16, 22, 17, 23, 21, 20, 13, 12, 11, 10, 3, 1, 4, 6, 0, 2, 9, 8, 5, 7, 19, 14, 18, 15, 23, 17, 22, 16, 13, 12, 21, 20, 9, 8, 1, 3, 7, 5, 2, 0, 11, 10, 6, 4, 20, 21, 13, 12, 19, 18, 15, 14, 17, 22, 16, 23, 3, 2, 7, 6, 10, 8, 5, 4, 0, 1, 9, 11, 21, 20, 12, 13, 15, 14, 19, 18, 23, 16, 22, 17, 2, 3, 5, 4, 9, 11, 7, 6, 1, 0, 10, 8, 22, 17, 16, 23, 13, 20, 21, 12, 15, 18, 19, 14, 7, 4, 11, 8, 2, 1, 9, 10, 5, 6, 0, 3, 23, 16, 17, 22, 20, 13, 12, 21, 18, 15, 14, 19, 6, 5, 10, 9, 1, 2, 8, 11, 4, 7, 3, 0])
    a3 = declare(int, value=[62, 62, 62, 124, 124, 124, 124, 124, 124, 124, 124, 124, 62, 62, 62, 62, 186, 186, 124, 124, 124, 124, 186, 186])
    a4 = declare(int, value=[0, 1, 2, 3, 11, 9, 10, 8, 7, 5, 6, 4, 13, 12, 15, 14, 17, 16, 18, 19, 20, 21, 22, 23])
    v16 = declare(int, )
    v17 = declare(int, )
    a5 = declare(int, size=15001)
    v18 = declare(int, )
    v19 = declare(int, )
    v20 = declare(int, )
    v21 = declare(int, )
    a6 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 0, 3, 2, 6, 7, 4, 5, 11, 10, 9, 8, 13, 12, 18, 19, 22, 23, 14, 15, 21, 20, 16, 17, 2, 3, 0, 1, 7, 6, 5, 4, 10, 11, 8, 9, 20, 21, 15, 14, 23, 22, 19, 18, 12, 13, 17, 16, 3, 2, 1, 0, 5, 4, 7, 6, 9, 8, 11, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 23, 22, 4, 7, 5, 6, 11, 8, 9, 10, 2, 3, 1, 0, 22, 17, 21, 12, 14, 18, 13, 20, 23, 16, 15, 19, 5, 6, 4, 7, 10, 9, 8, 11, 1, 0, 2, 3, 23, 16, 12, 21, 19, 15, 20, 13, 22, 17, 18, 14, 6, 5, 7, 4, 8, 11, 10, 9, 3, 2, 0, 1, 16, 23, 20, 13, 18, 14, 12, 21, 17, 22, 19, 15, 7, 4, 6, 5, 9, 10, 11, 8, 0, 1, 3, 2, 17, 22, 13, 20, 15, 19, 21, 12, 16, 23, 14, 18, 8, 9, 11, 10, 1, 3, 2, 0, 7, 4, 5, 6, 19, 14, 22, 16, 20, 12, 23, 17, 15, 18, 13, 21, 9, 8, 10, 11, 2, 0, 1, 3, 6, 5, 4, 7, 14, 19, 23, 17, 13, 21, 22, 16, 18, 15, 20, 12, 10, 11, 9, 8, 3, 1, 0, 2, 4, 7, 6, 5, 18, 15, 17, 23, 12, 20, 16, 22, 14, 19, 21, 13, 11, 10, 8, 9, 0, 2, 3, 1, 5, 6, 7, 4, 15, 18, 16, 22, 21, 13, 17, 23, 19, 14, 12, 20, 12, 13, 21, 20, 18, 19, 14, 15, 22, 17, 23, 16, 1, 0, 4, 5, 8, 10, 6, 7, 2, 3, 11, 9, 13, 12, 20, 21, 14, 15, 18, 19, 16, 23, 17, 22, 0, 1, 6, 7, 11, 9, 4, 5, 3, 2, 8, 10, 14, 19, 15, 18, 22, 16, 23, 17, 20, 21, 12, 13, 8, 9, 2, 0, 6, 4, 1, 3, 10, 11, 7, 5, 15, 18, 14, 19, 17, 23, 16, 22, 12, 13, 20, 21, 10, 11, 0, 2, 5, 7, 3, 1, 8, 9, 4, 6, 16, 23, 22, 17, 12, 21, 20, 13, 19, 14, 15, 18, 5, 6, 8, 11, 3, 0, 10, 9, 7, 4, 1, 2, 17, 22, 23, 16, 21, 12, 13, 20, 14, 19, 18, 15, 4, 7, 9, 10, 0, 3, 11, 8, 6, 5, 2, 1, 18, 15, 19, 14, 16, 22, 17, 23, 21, 20, 13, 12, 11, 10, 3, 1, 4, 6, 0, 2, 9, 8, 5, 7, 19, 14, 18, 15, 23, 17, 22, 16, 13, 12, 21, 20, 9, 8, 1, 3, 7, 5, 2, 0, 11, 10, 6, 4, 20, 21, 13, 12, 19, 18, 15, 14, 17, 22, 16, 23, 3, 2, 7, 6, 10, 8, 5, 4, 0, 1, 9, 11, 21, 20, 12, 13, 15, 14, 19, 18, 23, 16, 22, 17, 2, 3, 5, 4, 9, 11, 7, 6, 1, 0, 10, 8, 22, 17, 16, 23, 13, 20, 21, 12, 15, 18, 19, 14, 7, 4, 11, 8, 2, 1, 9, 10, 5, 6, 0, 3, 23, 16, 17, 22, 20, 13, 12, 21, 18, 15, 14, 19, 6, 5, 10, 9, 1, 2, 8, 11, 4, 7, 3, 0])
    a7 = declare(int, value=[62, 62, 62, 124, 124, 124, 124, 124, 124, 124, 124, 124, 62, 62, 62, 62, 186, 186, 124, 124, 124, 124, 186, 186])
    a8 = declare(int, value=[0, 1, 2, 3, 11, 9, 10, 8, 7, 5, 6, 4, 13, 12, 15, 14, 17, 16, 18, 19, 20, 21, 22, 23])
    v22 = declare(int, )
    v23 = declare(int, )
    a9 = declare(int, size=15001)
    v24 = declare(int, )
    v25 = declare(int, )
    v26 = declare(int, )
    v27 = declare(int, )
    a10 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 0, 3, 2, 6, 7, 4, 5, 11, 10, 9, 8, 13, 12, 18, 19, 22, 23, 14, 15, 21, 20, 16, 17, 2, 3, 0, 1, 7, 6, 5, 4, 10, 11, 8, 9, 20, 21, 15, 14, 23, 22, 19, 18, 12, 13, 17, 16, 3, 2, 1, 0, 5, 4, 7, 6, 9, 8, 11, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 23, 22, 4, 7, 5, 6, 11, 8, 9, 10, 2, 3, 1, 0, 22, 17, 21, 12, 14, 18, 13, 20, 23, 16, 15, 19, 5, 6, 4, 7, 10, 9, 8, 11, 1, 0, 2, 3, 23, 16, 12, 21, 19, 15, 20, 13, 22, 17, 18, 14, 6, 5, 7, 4, 8, 11, 10, 9, 3, 2, 0, 1, 16, 23, 20, 13, 18, 14, 12, 21, 17, 22, 19, 15, 7, 4, 6, 5, 9, 10, 11, 8, 0, 1, 3, 2, 17, 22, 13, 20, 15, 19, 21, 12, 16, 23, 14, 18, 8, 9, 11, 10, 1, 3, 2, 0, 7, 4, 5, 6, 19, 14, 22, 16, 20, 12, 23, 17, 15, 18, 13, 21, 9, 8, 10, 11, 2, 0, 1, 3, 6, 5, 4, 7, 14, 19, 23, 17, 13, 21, 22, 16, 18, 15, 20, 12, 10, 11, 9, 8, 3, 1, 0, 2, 4, 7, 6, 5, 18, 15, 17, 23, 12, 20, 16, 22, 14, 19, 21, 13, 11, 10, 8, 9, 0, 2, 3, 1, 5, 6, 7, 4, 15, 18, 16, 22, 21, 13, 17, 23, 19, 14, 12, 20, 12, 13, 21, 20, 18, 19, 14, 15, 22, 17, 23, 16, 1, 0, 4, 5, 8, 10, 6, 7, 2, 3, 11, 9, 13, 12, 20, 21, 14, 15, 18, 19, 16, 23, 17, 22, 0, 1, 6, 7, 11, 9, 4, 5, 3, 2, 8, 10, 14, 19, 15, 18, 22, 16, 23, 17, 20, 21, 12, 13, 8, 9, 2, 0, 6, 4, 1, 3, 10, 11, 7, 5, 15, 18, 14, 19, 17, 23, 16, 22, 12, 13, 20, 21, 10, 11, 0, 2, 5, 7, 3, 1, 8, 9, 4, 6, 16, 23, 22, 17, 12, 21, 20, 13, 19, 14, 15, 18, 5, 6, 8, 11, 3, 0, 10, 9, 7, 4, 1, 2, 17, 22, 23, 16, 21, 12, 13, 20, 14, 19, 18, 15, 4, 7, 9, 10, 0, 3, 11, 8, 6, 5, 2, 1, 18, 15, 19, 14, 16, 22, 17, 23, 21, 20, 13, 12, 11, 10, 3, 1, 4, 6, 0, 2, 9, 8, 5, 7, 19, 14, 18, 15, 23, 17, 22, 16, 13, 12, 21, 20, 9, 8, 1, 3, 7, 5, 2, 0, 11, 10, 6, 4, 20, 21, 13, 12, 19, 18, 15, 14, 17, 22, 16, 23, 3, 2, 7, 6, 10, 8, 5, 4, 0, 1, 9, 11, 21, 20, 12, 13, 15, 14, 19, 18, 23, 16, 22, 17, 2, 3, 5, 4, 9, 11, 7, 6, 1, 0, 10, 8, 22, 17, 16, 23, 13, 20, 21, 12, 15, 18, 19, 14, 7, 4, 11, 8, 2, 1, 9, 10, 5, 6, 0, 3, 23, 16, 17, 22, 20, 13, 12, 21, 18, 15, 14, 19, 6, 5, 10, 9, 1, 2, 8, 11, 4, 7, 3, 0])
    a11 = declare(int, value=[62, 62, 62, 124, 124, 124, 124, 124, 124, 124, 124, 124, 62, 62, 62, 62, 186, 186, 124, 124, 124, 124, 186, 186])
    a12 = declare(int, value=[0, 1, 2, 3, 11, 9, 10, 8, 7, 5, 6, 4, 13, 12, 15, 14, 17, 16, 18, 19, 20, 21, 22, 23])
    v28 = declare(int, )
    v29 = declare(int, )
    a13 = declare(int, size=15001)
    v30 = declare(int, )
    v31 = declare(int, )
    v32 = declare(int, )
    v33 = declare(int, )
    a14 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 0, 3, 2, 6, 7, 4, 5, 11, 10, 9, 8, 13, 12, 18, 19, 22, 23, 14, 15, 21, 20, 16, 17, 2, 3, 0, 1, 7, 6, 5, 4, 10, 11, 8, 9, 20, 21, 15, 14, 23, 22, 19, 18, 12, 13, 17, 16, 3, 2, 1, 0, 5, 4, 7, 6, 9, 8, 11, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 23, 22, 4, 7, 5, 6, 11, 8, 9, 10, 2, 3, 1, 0, 22, 17, 21, 12, 14, 18, 13, 20, 23, 16, 15, 19, 5, 6, 4, 7, 10, 9, 8, 11, 1, 0, 2, 3, 23, 16, 12, 21, 19, 15, 20, 13, 22, 17, 18, 14, 6, 5, 7, 4, 8, 11, 10, 9, 3, 2, 0, 1, 16, 23, 20, 13, 18, 14, 12, 21, 17, 22, 19, 15, 7, 4, 6, 5, 9, 10, 11, 8, 0, 1, 3, 2, 17, 22, 13, 20, 15, 19, 21, 12, 16, 23, 14, 18, 8, 9, 11, 10, 1, 3, 2, 0, 7, 4, 5, 6, 19, 14, 22, 16, 20, 12, 23, 17, 15, 18, 13, 21, 9, 8, 10, 11, 2, 0, 1, 3, 6, 5, 4, 7, 14, 19, 23, 17, 13, 21, 22, 16, 18, 15, 20, 12, 10, 11, 9, 8, 3, 1, 0, 2, 4, 7, 6, 5, 18, 15, 17, 23, 12, 20, 16, 22, 14, 19, 21, 13, 11, 10, 8, 9, 0, 2, 3, 1, 5, 6, 7, 4, 15, 18, 16, 22, 21, 13, 17, 23, 19, 14, 12, 20, 12, 13, 21, 20, 18, 19, 14, 15, 22, 17, 23, 16, 1, 0, 4, 5, 8, 10, 6, 7, 2, 3, 11, 9, 13, 12, 20, 21, 14, 15, 18, 19, 16, 23, 17, 22, 0, 1, 6, 7, 11, 9, 4, 5, 3, 2, 8, 10, 14, 19, 15, 18, 22, 16, 23, 17, 20, 21, 12, 13, 8, 9, 2, 0, 6, 4, 1, 3, 10, 11, 7, 5, 15, 18, 14, 19, 17, 23, 16, 22, 12, 13, 20, 21, 10, 11, 0, 2, 5, 7, 3, 1, 8, 9, 4, 6, 16, 23, 22, 17, 12, 21, 20, 13, 19, 14, 15, 18, 5, 6, 8, 11, 3, 0, 10, 9, 7, 4, 1, 2, 17, 22, 23, 16, 21, 12, 13, 20, 14, 19, 18, 15, 4, 7, 9, 10, 0, 3, 11, 8, 6, 5, 2, 1, 18, 15, 19, 14, 16, 22, 17, 23, 21, 20, 13, 12, 11, 10, 3, 1, 4, 6, 0, 2, 9, 8, 5, 7, 19, 14, 18, 15, 23, 17, 22, 16, 13, 12, 21, 20, 9, 8, 1, 3, 7, 5, 2, 0, 11, 10, 6, 4, 20, 21, 13, 12, 19, 18, 15, 14, 17, 22, 16, 23, 3, 2, 7, 6, 10, 8, 5, 4, 0, 1, 9, 11, 21, 20, 12, 13, 15, 14, 19, 18, 23, 16, 22, 17, 2, 3, 5, 4, 9, 11, 7, 6, 1, 0, 10, 8, 22, 17, 16, 23, 13, 20, 21, 12, 15, 18, 19, 14, 7, 4, 11, 8, 2, 1, 9, 10, 5, 6, 0, 3, 23, 16, 17, 22, 20, 13, 12, 21, 18, 15, 14, 19, 6, 5, 10, 9, 1, 2, 8, 11, 4, 7, 3, 0])
    a15 = declare(int, value=[62, 62, 62, 124, 124, 124, 124, 124, 124, 124, 124, 124, 62, 62, 62, 62, 186, 186, 124, 124, 124, 124, 186, 186])
    a16 = declare(int, value=[0, 1, 2, 3, 11, 9, 10, 8, 7, 5, 6, 4, 13, 12, 15, 14, 17, 16, 18, 19, 20, 21, 22, 23])
    v34 = declare(int, )
    v35 = declare(int, )
    a17 = declare(int, size=15001)
    v36 = declare(int, )
    v37 = declare(int, )
    v38 = declare(int, )
    v39 = declare(int, )
    wait((4+(0*((((Cast.to_int(v6)+Cast.to_int(v7))+Cast.to_int(v8))+Cast.to_int(v9))+Cast.to_int(v10)))), "tank_circuit1")
    set_dc_offset("P0_sticky", "single", -0.094)
    set_dc_offset("P1_sticky", "single", 0.094)
    with for_(v4,0,(v4<3),(v4+1)):
        play("x180_square", "qubit1")
        align()
        assign(v16, 0)
        assign(v18, 0)
        with for_(v20,0,(v20<15000),(v20+1)):
            assign(v17, call_library_function('random', 'rand_int', [v11,24]))
            assign(v16, a2[((v16*24)+v17)])
            assign(a5[(v20-0)], v17)
        with for_(v20,15000,(v20<30000),(v20+1)):
            assign(v17, call_library_function('random', 'rand_int', [v11,24]))
            assign(v16, a2[((v16*24)+v17)])
            assign(v19, (v19+a3[v17]))
        assign(a5[15000], a4[v16])
        assign(v19, (v19+a3[a4[v16]]))
        wait((241015+v18), "qubit1")
        with for_(v21,0,(v21<=14999),(v21+1)):
            with if_((a5[v21]==0), unsafe=True):
                play("x180_square", "qubit1")
            with elif_((a5[v21]==1)):
                play("x180_square", "qubit1")
            with elif_((a5[v21]==2)):
                play("x180_square", "qubit1")
            with elif_((a5[v21]==3)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==4)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==5)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==6)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==7)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==8)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==9)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==10)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==11)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==12)):
                play("x180_square", "qubit1")
            with elif_((a5[v21]==13)):
                play("x180_square", "qubit1")
            with elif_((a5[v21]==14)):
                play("x180_square", "qubit1")
            with elif_((a5[v21]==15)):
                play("x180_square", "qubit1")
            with elif_((a5[v21]==16)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==17)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==18)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==19)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==20)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==21)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==22)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
            with elif_((a5[v21]==23)):
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
                play("x180_square", "qubit1")
        assign(v22, 0)
        assign(v24, 0)
        with for_(v26,0,(v26<15000),(v26+1)):
            assign(v23, call_library_function('random', 'rand_int', [v11,24]))
            assign(v22, a6[((v22*24)+v23)])
            assign(v24, (v24+a7[v23]))
        with for_(v26,15000,(v26<30000),(v26+1)):
            assign(v23, call_library_function('random', 'rand_int', [v11,24]))
            assign(v22, a6[((v22*24)+v23)])
            assign(a9[(v26-15000)], v23)
        assign(a9[15000], a8[v22])
        wait((1016+v24), "qubit1_dup1")
        with for_(v27,0,(v27<=15000),(v27+1)):
            with if_((a9[v27]==0), unsafe=True):
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==1)):
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==2)):
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==3)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==4)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==5)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==6)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==7)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==8)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==9)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==10)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==11)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==12)):
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==13)):
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==14)):
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==15)):
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==16)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==17)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==18)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==19)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==20)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==21)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==22)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
            with elif_((a9[v27]==23)):
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
                play("x180_square", "qubit1_dup1")
        assign(v28, 0)
        assign(v30, 0)
        with for_(v32,0,(v32<15000),(v32+1)):
            assign(v29, call_library_function('random', 'rand_int', [v12,24]))
            assign(v28, a10[((v28*24)+v29)])
            assign(a13[(v32-0)], v29)
        with for_(v32,15000,(v32<30000),(v32+1)):
            assign(v29, call_library_function('random', 'rand_int', [v12,24]))
            assign(v28, a10[((v28*24)+v29)])
            assign(v31, (v31+a11[v29]))
        assign(a13[15000], a12[v28])
        assign(v31, (v31+a11[a12[v28]]))
        wait((1000+v30), "qubit2_dup1")
        with for_(v33,0,(v33<=14999),(v33+1)):
            with if_((a13[v33]==0), unsafe=True):
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==1)):
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==2)):
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==3)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==4)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==5)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==6)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==7)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==8)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==9)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==10)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==11)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==12)):
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==13)):
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==14)):
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==15)):
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==16)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==17)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==18)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==19)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==20)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==21)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==22)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
            with elif_((a13[v33]==23)):
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
                play("x180_square", "qubit2_dup1")
        assign(v34, 0)
        assign(v36, 0)
        with for_(v38,0,(v38<15000),(v38+1)):
            assign(v35, call_library_function('random', 'rand_int', [v12,24]))
            assign(v34, a14[((v34*24)+v35)])
            assign(v36, (v36+a15[v35]))
        with for_(v38,15000,(v38<30000),(v38+1)):
            assign(v35, call_library_function('random', 'rand_int', [v12,24]))
            assign(v34, a14[((v34*24)+v35)])
            assign(a17[(v38-15000)], v35)
        assign(a17[15000], a16[v34])
        wait((-238999+v36), "qubit2_dup2")
        with for_(v39,0,(v39<=15000),(v39+1)):
            with if_((a17[v39]==0), unsafe=True):
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==1)):
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==2)):
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==3)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==4)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==5)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==6)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==7)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==8)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==9)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==10)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==11)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==12)):
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==13)):
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==14)):
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==15)):
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==16)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==17)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==18)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==19)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==20)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==21)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==22)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
            with elif_((a17[v39]==23)):
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")
                play("x180_square", "qubit2_dup2")


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
                        "7": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {
                        "1": {},
                    },
                    "analog_inputs": {},
                },
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        "2": {
                            "offset": -0.007773877929687499,
                            "gain_db": 0,
                            "sampling_rate": 1000000000,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "P0": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "operations": {
                "step": "P0_step_pulse",
            },
        },
        "P1": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2": {
            "singleInput": {
                "port": ('con1', 3, 5),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P3": {
            "singleInput": {
                "port": ('con1', 3, 7),
            },
            "operations": {
                "step": "P3_step_pulse",
            },
        },
        "P4": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "operations": {
                "step": "P4_step_pulse",
            },
        },
        "P0_sticky": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P0_step_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": ('con1', 3, 3),
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
                "port": ('con1', 3, 5),
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
                "port": ('con1', 3, 7),
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
                "port": ('con1', 3, 1),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P4_step_pulse",
            },
        },
        "B1": {
            "singleInput": {
                "port": ('con1', 3, 2),
            },
            "operations": {
                "step": "B1_step_pulse",
            },
        },
        "B2": {
            "singleInput": {
                "port": ('con1', 3, 4),
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
                "port": ('con1', 3, 8),
            },
            "operations": {
                "step": "B4_step_pulse",
            },
        },
        "B1_sticky": {
            "singleInput": {
                "port": ('con1', 3, 2),
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
                "port": ('con1', 3, 4),
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
                "port": ('con1', 3, 8),
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
                "port": ('con1', 3, 2),
            },
            "operations": {
                "step": "Psd1_step_pulse",
            },
        },
        "Psd2": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "operations": {
                "step": "Psd2_step_pulse",
            },
        },
        "Psd1_sticky": {
            "singleInput": {
                "port": ('con1', 3, 2),
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
                "port": ('con1', 3, 3),
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit1",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit1",
                "x90_square": "square_x90_pulse_qubit1",
                "-x90_square": "square_minus_x90_pulse_qubit1",
                "y180_square": "square_y180_pulse_qubit1",
                "y90_square": "square_y90_pulse_qubit1",
                "-y90_square": "square_minus_y90_pulse_qubit1",
            },
        },
        "qubit2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit2",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit2",
                "x90_square": "square_x90_pulse_qubit2",
                "-x90_square": "square_minus_x90_pulse_qubit2",
                "y180_square": "square_y180_pulse_qubit2",
                "y90_square": "square_y90_pulse_qubit2",
                "-y90_square": "square_minus_y90_pulse_qubit2",
            },
        },
        "qubit3": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit3",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit3",
                "x90_square": "square_x90_pulse_qubit3",
                "-x90_square": "square_minus_x90_pulse_qubit3",
                "y180_square": "square_y180_pulse_qubit3",
                "y90_square": "square_y90_pulse_qubit3",
                "-y90_square": "square_minus_y90_pulse_qubit3",
            },
        },
        "qubit4": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit4",
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit4",
                "x90_square": "square_x90_pulse_qubit4",
                "-x90_square": "square_minus_x90_pulse_qubit4",
                "y180_square": "square_y180_pulse_qubit4",
                "y90_square": "square_y90_pulse_qubit4",
                "-y90_square": "square_minus_y90_pulse_qubit4",
            },
        },
        "qubit5": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit5",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit5",
                "x90_square": "square_x90_pulse_qubit5",
                "-x90_square": "square_minus_x90_pulse_qubit5",
                "y180_square": "square_y180_pulse_qubit5",
                "y90_square": "square_y90_pulse_qubit5",
                "-y90_square": "square_minus_y90_pulse_qubit5",
            },
        },
        "qubit1_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit1",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit2_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit2",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit3_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit3",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit4_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit4",
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit5_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit5",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit1_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit1",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qubit2_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit2",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qubit3_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit3",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qubit4_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit4",
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qubit5_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit5",
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qp_control_c3t2": {
            "mixInputs": {
                "I": ('con1', 5, 3),
                "Q": ('con1', 5, 4),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qp_control_c3t2",
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
        "rf_switch": {
            "singleInput": {
                "port": ('con1', 5, 1),
            },
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
        "tank_circuit1": {
            "singleInput": {
                "port": ('con1', 3, 8),
            },
            "intermediate_frequency": 181020000,
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit1",
            },
            "outputs": {
                "out1": ('con1', 3, 2),
            },
            "time_of_flight": 204,
            "smearing": 0,
        },
        "tank_circuit2": {
            "singleInput": {
                "port": ('con1', 3, 8),
            },
            "intermediate_frequency": 139534000,
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit2",
            },
            "outputs": {
                "out1": ('con1', 3, 2),
            },
            "time_of_flight": 204,
            "smearing": 0,
        },
    },
    "pulses": {
        "P0_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P0_step_wf",
            },
        },
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
            "length": 280,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit1",
                "Q": "x180_gaussian_Q_wf_qubit1",
            },
        },
        "x180_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit2",
                "Q": "x180_gaussian_Q_wf_qubit2",
            },
        },
        "x180_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit3",
                "Q": "x180_gaussian_Q_wf_qubit3",
            },
        },
        "x180_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit4",
                "Q": "x180_gaussian_Q_wf_qubit4",
            },
        },
        "x180_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit5",
                "Q": "x180_gaussian_Q_wf_qubit5",
            },
        },
        "x90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit1",
                "Q": "x90_gaussian_Q_wf_qubit1",
            },
        },
        "x90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit2",
                "Q": "x90_gaussian_Q_wf_qubit2",
            },
        },
        "x90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit3",
                "Q": "x90_gaussian_Q_wf_qubit3",
            },
        },
        "x90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit4",
                "Q": "x90_gaussian_Q_wf_qubit4",
            },
        },
        "x90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit5",
                "Q": "x90_gaussian_Q_wf_qubit5",
            },
        },
        "minus_x90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit1",
                "Q": "minus_x90_gaussian_Q_wf_qubit1",
            },
        },
        "minus_x90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit2",
                "Q": "minus_x90_gaussian_Q_wf_qubit2",
            },
        },
        "minus_x90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit3",
                "Q": "minus_x90_gaussian_Q_wf_qubit3",
            },
        },
        "minus_x90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit4",
                "Q": "minus_x90_gaussian_Q_wf_qubit4",
            },
        },
        "minus_x90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit5",
                "Q": "minus_x90_gaussian_Q_wf_qubit5",
            },
        },
        "y180_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit1",
                "Q": "y180_gaussian_Q_wf_qubit1",
            },
        },
        "y180_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit2",
                "Q": "y180_gaussian_Q_wf_qubit2",
            },
        },
        "y180_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit3",
                "Q": "y180_gaussian_Q_wf_qubit3",
            },
        },
        "y180_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit4",
                "Q": "y180_gaussian_Q_wf_qubit4",
            },
        },
        "y180_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit5",
                "Q": "y180_gaussian_Q_wf_qubit5",
            },
        },
        "y90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit1",
                "Q": "y90_gaussian_Q_wf_qubit1",
            },
        },
        "y90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit2",
                "Q": "y90_gaussian_Q_wf_qubit2",
            },
        },
        "y90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit3",
                "Q": "y90_gaussian_Q_wf_qubit3",
            },
        },
        "y90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit4",
                "Q": "y90_gaussian_Q_wf_qubit4",
            },
        },
        "y90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit5",
                "Q": "y90_gaussian_Q_wf_qubit5",
            },
        },
        "minus_y90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit1",
                "Q": "minus_y90_gaussian_Q_wf_qubit1",
            },
        },
        "minus_y90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit2",
                "Q": "minus_y90_gaussian_Q_wf_qubit2",
            },
        },
        "minus_y90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit3",
                "Q": "minus_y90_gaussian_Q_wf_qubit3",
            },
        },
        "minus_y90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit4",
                "Q": "minus_y90_gaussian_Q_wf_qubit4",
            },
        },
        "minus_y90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit5",
                "Q": "minus_y90_gaussian_Q_wf_qubit5",
            },
        },
        "x180_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit1",
                "Q": "x180_kaiser_Q_wf_qubit1",
            },
        },
        "x180_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit2",
                "Q": "x180_kaiser_Q_wf_qubit2",
            },
        },
        "x180_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit3",
                "Q": "x180_kaiser_Q_wf_qubit3",
            },
        },
        "x180_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit4",
                "Q": "x180_kaiser_Q_wf_qubit4",
            },
        },
        "x180_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit5",
                "Q": "x180_kaiser_Q_wf_qubit5",
            },
        },
        "x90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit1",
                "Q": "x90_kaiser_Q_wf_qubit1",
            },
        },
        "x90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit2",
                "Q": "x90_kaiser_Q_wf_qubit2",
            },
        },
        "x90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit3",
                "Q": "x90_kaiser_Q_wf_qubit3",
            },
        },
        "x90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit4",
                "Q": "x90_kaiser_Q_wf_qubit4",
            },
        },
        "x90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit5",
                "Q": "x90_kaiser_Q_wf_qubit5",
            },
        },
        "minus_x90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit1",
                "Q": "minus_x90_kaiser_Q_wf_qubit1",
            },
        },
        "minus_x90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit2",
                "Q": "minus_x90_kaiser_Q_wf_qubit2",
            },
        },
        "minus_x90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit3",
                "Q": "minus_x90_kaiser_Q_wf_qubit3",
            },
        },
        "minus_x90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit4",
                "Q": "minus_x90_kaiser_Q_wf_qubit4",
            },
        },
        "minus_x90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit5",
                "Q": "minus_x90_kaiser_Q_wf_qubit5",
            },
        },
        "y180_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit1",
                "Q": "y180_kaiser_Q_wf_qubit1",
            },
        },
        "y180_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit2",
                "Q": "y180_kaiser_Q_wf_qubit2",
            },
        },
        "y180_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit3",
                "Q": "y180_kaiser_Q_wf_qubit3",
            },
        },
        "y180_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit4",
                "Q": "y180_kaiser_Q_wf_qubit4",
            },
        },
        "y180_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit5",
                "Q": "y180_kaiser_Q_wf_qubit5",
            },
        },
        "y90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit1",
                "Q": "y90_kaiser_Q_wf_qubit1",
            },
        },
        "y90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit2",
                "Q": "y90_kaiser_Q_wf_qubit2",
            },
        },
        "y90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit3",
                "Q": "y90_kaiser_Q_wf_qubit3",
            },
        },
        "y90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit4",
                "Q": "y90_kaiser_Q_wf_qubit4",
            },
        },
        "y90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit5",
                "Q": "y90_kaiser_Q_wf_qubit5",
            },
        },
        "minus_y90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 280,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit1",
                "Q": "minus_y90_kaiser_Q_wf_qubit1",
            },
        },
        "minus_y90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit2",
                "Q": "minus_y90_kaiser_Q_wf_qubit2",
            },
        },
        "minus_y90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit3",
                "Q": "minus_y90_kaiser_Q_wf_qubit3",
            },
        },
        "minus_y90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit4",
                "Q": "minus_y90_kaiser_Q_wf_qubit4",
            },
        },
        "minus_y90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 160,
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
            "length": 20000,
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
            "length": 20000,
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
            "length": 320,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse": {
            "operation": "control",
            "length": 10000,
            "waveforms": {
                "I": "saturation_wf",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse_qubit1": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "square_x180_I_wf_qubit1",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse_qubit2": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "square_x180_I_wf_qubit2",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "square_x180_I_wf_qubit3",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "square_x180_I_wf_qubit4",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "square_x180_I_wf_qubit5",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_qubit1": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "square_x90_I_wf_qubit1",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_qubit2": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "square_x90_I_wf_qubit2",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "square_x90_I_wf_qubit3",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "square_x90_I_wf_qubit4",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "square_x90_I_wf_qubit5",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_qubit1": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit1",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_qubit2": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit2",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit3",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit4",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit5",
                "Q": "zero_wf",
            },
        },
        "square_y180_pulse_qubit1": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit1",
            },
        },
        "square_y180_pulse_qubit2": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit2",
            },
        },
        "square_y180_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit3",
            },
        },
        "square_y180_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit4",
            },
        },
        "square_y180_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit5",
            },
        },
        "square_y90_pulse_qubit1": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit1",
            },
        },
        "square_y90_pulse_qubit2": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit2",
            },
        },
        "square_y90_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit3",
            },
        },
        "square_y90_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit4",
            },
        },
        "square_y90_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit5",
            },
        },
        "square_minus_y90_pulse_qubit1": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit1",
            },
        },
        "square_minus_y90_pulse_qubit2": {
            "operation": "control",
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit2",
            },
        },
        "square_minus_y90_pulse_qubit3": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit3",
            },
        },
        "square_minus_y90_pulse_qubit4": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit4",
            },
        },
        "square_minus_y90_pulse_qubit5": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit5",
            },
        },
        "square_x180_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_x180_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_minus_x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_y180_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf",
            },
        },
        "square_y90_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf",
            },
        },
        "square_minus_y90_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf",
            },
        },
        "square_x180_pulse_dup1": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_x180_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_dup1": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_x90_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_dup1": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_minus_x90_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_y180_pulse_dup1": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_y180_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_y90_pulse_dup1": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_y90_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_minus_y90_pulse_dup1": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_minus_y90_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse_dup2": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_x180_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_dup2": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_x90_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_dup2": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_minus_x90_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_y180_pulse_dup2": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_y180_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_y90_pulse_dup2": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_y90_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_minus_y90_pulse_dup2": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "square_minus_y90_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "zero_wf",
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
            "sample": 0.3,
        },
        "saturation_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_x180_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.30671] * 246 + [0] * 2,
        },
        "square_x180_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.1579536] * 246 + [0] * 2,
        },
        "square_x180_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0] * 2,
        },
        "square_x180_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0] * 2,
        },
        "square_x180_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0] * 2,
        },
        "square_x90_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.153355] * 246 + [0] * 2,
        },
        "square_x90_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0789768] * 246 + [0] * 2,
        },
        "square_x90_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0] * 2,
        },
        "square_x90_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0] * 2,
        },
        "square_x90_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0] * 2,
        },
        "square_minus_x90_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.153355] * 246 + [0] * 2,
        },
        "square_minus_x90_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0789768] * 246 + [0] * 2,
        },
        "square_minus_x90_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0] * 2,
        },
        "square_minus_x90_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0] * 2,
        },
        "square_minus_x90_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0] * 2,
        },
        "square_y180_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.30671] * 246 + [0] * 2,
        },
        "square_y180_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.1579536] * 246 + [0] * 2,
        },
        "square_y180_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0] * 2,
        },
        "square_y180_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0] * 2,
        },
        "square_y180_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0] * 2,
        },
        "square_y90_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.153355] * 246 + [0] * 2,
        },
        "square_y90_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0789768] * 246 + [0] * 2,
        },
        "square_y90_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0] * 2,
        },
        "square_y90_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0] * 2,
        },
        "square_y90_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0] * 2,
        },
        "square_minus_y90_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.153355] * 246 + [0] * 2,
        },
        "square_minus_y90_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0789768] * 246 + [0] * 2,
        },
        "square_minus_y90_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0] * 2,
        },
        "square_minus_y90_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0] * 2,
        },
        "square_minus_y90_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0] * 2,
        },
        "square_x180_I_wf": {
            "type": "constant",
            "sample": 0.4,
        },
        "square_x90_I_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "square_minus_x90_I_wf": {
            "type": "constant",
            "sample": -0.2,
        },
        "square_y180_I_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "square_y90_I_wf": {
            "type": "constant",
            "sample": 0.15,
        },
        "square_minus_y90_I_wf": {
            "type": "constant",
            "sample": -0.15,
        },
        "square_x180_I_wf_dup1": {
            "type": "constant",
            "sample": 0.26666666666666666,
        },
        "square_x90_I_wf_dup1": {
            "type": "constant",
            "sample": 0.13333333333333333,
        },
        "square_minus_x90_I_wf_dup1": {
            "type": "constant",
            "sample": -0.13333333333333333,
        },
        "square_y180_I_wf_dup1": {
            "type": "constant",
            "sample": 0.19999999999999998,
        },
        "square_y90_I_wf_dup1": {
            "type": "constant",
            "sample": 0.09999999999999999,
        },
        "square_minus_y90_I_wf_dup1": {
            "type": "constant",
            "sample": -0.09999999999999999,
        },
        "square_x180_I_wf_dup2": {
            "type": "constant",
            "sample": 0.13333333333333333,
        },
        "square_x90_I_wf_dup2": {
            "type": "constant",
            "sample": 0.06666666666666667,
        },
        "square_minus_x90_I_wf_dup2": {
            "type": "constant",
            "sample": -0.06666666666666667,
        },
        "square_y180_I_wf_dup2": {
            "type": "constant",
            "sample": 0.09999999999999999,
        },
        "square_y90_I_wf_dup2": {
            "type": "constant",
            "sample": 0.049999999999999996,
        },
        "square_minus_y90_I_wf_dup2": {
            "type": "constant",
            "sample": -0.049999999999999996,
        },
        "reflectometry_readout_wf_tank_circuit1": {
            "type": "constant",
            "sample": 0.15,
        },
        "reflectometry_readout_wf_tank_circuit2": {
            "type": "constant",
            "sample": 0.15,
        },
        "P0_step_wf": {
            "type": "constant",
            "sample": 0.25,
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
            "samples": [0.0, 0.0009148923399437993, 0.0018644642330929335, 0.00284965898284922, 0.0038714271362863782, 0.0049307255528147804, 0.006028516420688381, 0.007165766220976314, 0.008343444638726875, 0.009562523421161033, 0.010823975182848718, 0.01212877215794101, 0.013477884899657545, 0.01487228092735833, 0.016312923321664778, 0.017800769268233846, 0.019336768550933622, 0.020921861995316114, 0.02255697986343462, 0.024243040201208592, 0.02598094713969632, 0.027771589151797407, 0.02961583726607, 0.03151454323951276, 0.03346853769132978, 0.03547862819986278, 0.037545597365046326, 0.03967020083890829, 0.041853165326808814, 0.04409518656227807, 0.046396927258479985, 0.04875901503949465, 0.051182040354774354, 0.05366655438028805, 0.05621306691002526, 0.05882204424168241, 0.06149390706050232, 0.06422902832537891, 0.06702773116147609, 0.06989028676373935, 0.07281691231580012, 0.07580776892888938, 0.07886295960548184, 0.08198252723249075, 0.0851664526089207, 0.08841465251296415, 0.09172697781359468, 0.09510321163176602, 0.09854306755637063, 0.10204618792014453, 0.10561214214072318, 0.10924042513206186, 0.11293045579142641, 0.11668157556713862, 0.1204930471122275, 0.12436405302908665, 0.12829369471017485, 0.13228099127971685, 0.1363248786412681, 0.14042420863589627, 0.14457774831560755, 0.14878417933650587, 0.15304209747601527, 0.15735001227832562, 0.1617063468320342, 0.16610943768375308, 0.17055753489123626, 0.17504880221934724, 0.17958131748194273, 0.18415307303248715, 0.18876197640593897, 0.19340585111416314, 0.19808243759682406, 0.20278939432940254, 0.20752429908965656, 0.21228465038351318, 0.2170678690310354, 0.22187129991275403, 0.22669221387629673, 0.23152780980287496, 0.23637521683281865, 0.24123149674896527, 0.2460936465163277, 0.2509586009760774, 0.2558232356914874, 0.2606843699430909, 0.26553876986991826, 0.2703831517532839, 0.27521418543920934, 0.2800284978951797, 0.28482267689655494, 0.2895932748375783, 0.29433681266156153, 0.29904978390446163, 0.303728658845719, 0.3083698887598838, 0.3129699102622307, 0.31752514974124635, 0.3220320278705748, 0.32648696419271617, 0.33088638176650803, 0.33522671187016195, 0.3395043987513959, 0.34371590441598443, 0.34785771344585487, 0.35192633783767974, 0.35591832185276323, 0.35983024686888715, 0.3636587362246724, 0.3674004600469257, 0.37105214005138065, 0.374610554307203, 0.3780725419556184, 0.38143500787303103, 0.3846949272690411, 0.38784935020982825, 0.3908954060574589, 0.393830307815786, 0.39665135637374793, 0.399355944637039, 0.40194156153930644, 0.40440579592424686, 0.40674634029020573, 0.40896099438914535, 0.411047668672128, 0.4130043875737647, 0.41482929262840457, 0.4165206454111864, 0.41807683029743753, 0.4194963570342907, 0.4207778631187886, 0.4219201159771637, 0.42292201494041654, 0.42378259301175647, 0.42450101842193527, 0.4250765959689697, 0.425508768139233, 0.42579711600738496] + [0.4259413599131059] * 2 + [0.42579711600738496, 0.425508768139233, 0.4250765959689697, 0.42450101842193527, 0.42378259301175647, 0.42292201494041654, 0.4219201159771637, 0.4207778631187886, 0.4194963570342907, 0.41807683029743753, 0.4165206454111864, 0.41482929262840457, 0.4130043875737647, 0.411047668672128, 0.40896099438914535, 0.40674634029020573, 0.40440579592424686, 0.40194156153930644, 0.399355944637039, 0.39665135637374793, 0.393830307815786, 0.3908954060574589, 0.38784935020982825, 0.3846949272690411, 0.38143500787303103, 0.3780725419556184, 0.374610554307203, 0.37105214005138065, 0.3674004600469257, 0.3636587362246724, 0.35983024686888715, 0.35591832185276323, 0.35192633783767974, 0.34785771344585487, 0.34371590441598443, 0.3395043987513959, 0.33522671187016195, 0.33088638176650803, 0.32648696419271617, 0.3220320278705748, 0.31752514974124635, 0.3129699102622307, 0.3083698887598838, 0.303728658845719, 0.29904978390446163, 0.29433681266156153, 0.2895932748375783, 0.28482267689655494, 0.2800284978951797, 0.27521418543920934, 0.2703831517532839, 0.26553876986991826, 0.2606843699430909, 0.2558232356914874, 0.2509586009760774, 0.2460936465163277, 0.24123149674896527, 0.23637521683281865, 0.23152780980287496, 0.22669221387629673, 0.22187129991275403, 0.2170678690310354, 0.21228465038351318, 0.20752429908965656, 0.20278939432940254, 0.19808243759682406, 0.19340585111416314, 0.18876197640593897, 0.18415307303248715, 0.17958131748194273, 0.17504880221934724, 0.17055753489123626, 0.16610943768375308, 0.1617063468320342, 0.15735001227832562, 0.15304209747601527, 0.14878417933650587, 0.14457774831560755, 0.14042420863589627, 0.1363248786412681, 0.13228099127971685, 0.12829369471017485, 0.12436405302908665, 0.1204930471122275, 0.11668157556713862, 0.11293045579142641, 0.10924042513206186, 0.10561214214072318, 0.10204618792014453, 0.09854306755637063, 0.09510321163176602, 0.09172697781359468, 0.08841465251296415, 0.0851664526089207, 0.08198252723249075, 0.07886295960548184, 0.07580776892888938, 0.07281691231580012, 0.06989028676373935, 0.06702773116147609, 0.06422902832537891, 0.06149390706050232, 0.05882204424168241, 0.05621306691002526, 0.05366655438028805, 0.051182040354774354, 0.04875901503949465, 0.046396927258479985, 0.04409518656227807, 0.041853165326808814, 0.03967020083890829, 0.037545597365046326, 0.03547862819986278, 0.03346853769132978, 0.03151454323951276, 0.02961583726607, 0.027771589151797407, 0.02598094713969632, 0.024243040201208592, 0.02255697986343462, 0.020921861995316114, 0.019336768550933622, 0.017800769268233846, 0.016312923321664778, 0.01487228092735833, 0.013477884899657545, 0.01212877215794101, 0.010823975182848718, 0.009562523421161033, 0.008343444638726875, 0.007165766220976314, 0.006028516420688381, 0.0049307255528147804, 0.0038714271362863782, 0.00284965898284922, 0.0018644642330929335, 0.0009148923399437993] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
        },
        "x180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
        },
        "x180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "x180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "x180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "x180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.00045744616997189964, 0.0009322321165464668, 0.00142482949142461, 0.0019357135681431891, 0.0024653627764073902, 0.0030142582103441905, 0.003582883110488157, 0.004171722319363438, 0.0047812617105805165, 0.005411987591424359, 0.006064386078970505, 0.006738942449828773, 0.007436140463679165, 0.008156461660832389, 0.008900384634116923, 0.009668384275466811, 0.010460930997658057, 0.01127848993171731, 0.012121520100604296, 0.01299047356984816, 0.013885794575898704, 0.014807918633035, 0.01575727161975638, 0.01673426884566489, 0.01773931409993139, 0.018772798682523163, 0.019835100419454146, 0.020926582663404407, 0.022047593281139036, 0.023198463629239992, 0.024379507519747327, 0.025591020177387177, 0.026833277190144025, 0.02810653345501263, 0.029411022120841204, 0.03074695353025116, 0.032114514162689456, 0.033513865580738045, 0.03494514338186967, 0.03640845615790006, 0.03790388446444469, 0.03943147980274092, 0.040991263616245374, 0.04258322630446035, 0.04420732625648208, 0.04586348890679734, 0.04755160581588301, 0.049271533778185314, 0.05102309396007226, 0.05280607107036159, 0.05462021256603093, 0.056465227895713205, 0.05834078778356931, 0.06024652355611375, 0.062182026514543326, 0.06414684735508742, 0.06614049563985842, 0.06816243932063405, 0.07021210431794814, 0.07228887415780377, 0.07439208966825293, 0.07652104873800764, 0.07867500613916281, 0.0808531734160171, 0.08305471884187654, 0.08527876744561813, 0.08752440110967362, 0.08979065874097136, 0.09207653651624358, 0.09438098820296949, 0.09670292555708157, 0.09904121879841203, 0.10139469716470127, 0.10376214954482828, 0.10614232519175659, 0.1085339345155177, 0.11093564995637702, 0.11334610693814837, 0.11576390490143748, 0.11818760841640932, 0.12061574837448263, 0.12304682325816385, 0.1254793004880387, 0.1279116178457437, 0.13034218497154546, 0.13276938493495913, 0.13519157587664196, 0.13760709271960467, 0.14001424894758985, 0.14241133844827747, 0.14479663741878915, 0.14716840633078077, 0.14952489195223082, 0.1518643294228595, 0.1541849443799419, 0.15648495513111535, 0.15876257487062317, 0.1610160139352874, 0.16324348209635808, 0.16544319088325402, 0.16761335593508098, 0.16975219937569794, 0.17185795220799222, 0.17392885672292743, 0.17596316891883987, 0.17795916092638162, 0.17991512343444357, 0.1818293681123362, 0.18370023002346286, 0.18552607002569033, 0.1873052771536015, 0.1890362709778092, 0.19071750393651551, 0.19234746363452054, 0.19392467510491412, 0.19544770302872946, 0.196915153907893, 0.19832567818687397, 0.1996779723185195, 0.20097078076965322, 0.20220289796212343, 0.20337317014510287, 0.20448049719457267, 0.205523834336064, 0.20650219378688234, 0.20741464631420228, 0.2082603227055932, 0.20903841514871876, 0.20974817851714536, 0.2103889315593943, 0.21096005798858186, 0.21146100747020827, 0.21189129650587823, 0.21225050921096764, 0.21253829798448484, 0.2127543840696165, 0.21289855800369248] + [0.21297067995655294] * 2 + [0.21289855800369248, 0.2127543840696165, 0.21253829798448484, 0.21225050921096764, 0.21189129650587823, 0.21146100747020827, 0.21096005798858186, 0.2103889315593943, 0.20974817851714536, 0.20903841514871876, 0.2082603227055932, 0.20741464631420228, 0.20650219378688234, 0.205523834336064, 0.20448049719457267, 0.20337317014510287, 0.20220289796212343, 0.20097078076965322, 0.1996779723185195, 0.19832567818687397, 0.196915153907893, 0.19544770302872946, 0.19392467510491412, 0.19234746363452054, 0.19071750393651551, 0.1890362709778092, 0.1873052771536015, 0.18552607002569033, 0.18370023002346286, 0.1818293681123362, 0.17991512343444357, 0.17795916092638162, 0.17596316891883987, 0.17392885672292743, 0.17185795220799222, 0.16975219937569794, 0.16761335593508098, 0.16544319088325402, 0.16324348209635808, 0.1610160139352874, 0.15876257487062317, 0.15648495513111535, 0.1541849443799419, 0.1518643294228595, 0.14952489195223082, 0.14716840633078077, 0.14479663741878915, 0.14241133844827747, 0.14001424894758985, 0.13760709271960467, 0.13519157587664196, 0.13276938493495913, 0.13034218497154546, 0.1279116178457437, 0.1254793004880387, 0.12304682325816385, 0.12061574837448263, 0.11818760841640932, 0.11576390490143748, 0.11334610693814837, 0.11093564995637702, 0.1085339345155177, 0.10614232519175659, 0.10376214954482828, 0.10139469716470127, 0.09904121879841203, 0.09670292555708157, 0.09438098820296949, 0.09207653651624358, 0.08979065874097136, 0.08752440110967362, 0.08527876744561813, 0.08305471884187654, 0.0808531734160171, 0.07867500613916281, 0.07652104873800764, 0.07439208966825293, 0.07228887415780377, 0.07021210431794814, 0.06816243932063405, 0.06614049563985842, 0.06414684735508742, 0.062182026514543326, 0.06024652355611375, 0.05834078778356931, 0.056465227895713205, 0.05462021256603093, 0.05280607107036159, 0.05102309396007226, 0.049271533778185314, 0.04755160581588301, 0.04586348890679734, 0.04420732625648208, 0.04258322630446035, 0.040991263616245374, 0.03943147980274092, 0.03790388446444469, 0.03640845615790006, 0.03494514338186967, 0.033513865580738045, 0.032114514162689456, 0.03074695353025116, 0.029411022120841204, 0.02810653345501263, 0.026833277190144025, 0.025591020177387177, 0.024379507519747327, 0.023198463629239992, 0.022047593281139036, 0.020926582663404407, 0.019835100419454146, 0.018772798682523163, 0.01773931409993139, 0.01673426884566489, 0.01575727161975638, 0.014807918633035, 0.013885794575898704, 0.01299047356984816, 0.012121520100604296, 0.01127848993171731, 0.010460930997658057, 0.009668384275466811, 0.008900384634116923, 0.008156461660832389, 0.007436140463679165, 0.006738942449828773, 0.006064386078970505, 0.005411987591424359, 0.0047812617105805165, 0.004171722319363438, 0.003582883110488157, 0.0030142582103441905, 0.0024653627764073902, 0.0019357135681431891, 0.00142482949142461, 0.0009322321165464668, 0.00045744616997189964] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
        },
        "x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
        },
        "x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "minus_x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.00045744616997189964, -0.0009322321165464668, -0.00142482949142461, -0.0019357135681431891, -0.0024653627764073902, -0.0030142582103441905, -0.003582883110488157, -0.004171722319363438, -0.0047812617105805165, -0.005411987591424359, -0.006064386078970505, -0.006738942449828773, -0.007436140463679165, -0.008156461660832389, -0.008900384634116923, -0.009668384275466811, -0.010460930997658057, -0.01127848993171731, -0.012121520100604296, -0.01299047356984816, -0.013885794575898704, -0.014807918633035, -0.01575727161975638, -0.01673426884566489, -0.01773931409993139, -0.018772798682523163, -0.019835100419454146, -0.020926582663404407, -0.022047593281139036, -0.023198463629239992, -0.024379507519747327, -0.025591020177387177, -0.026833277190144025, -0.02810653345501263, -0.029411022120841204, -0.03074695353025116, -0.032114514162689456, -0.033513865580738045, -0.03494514338186967, -0.03640845615790006, -0.03790388446444469, -0.03943147980274092, -0.040991263616245374, -0.04258322630446035, -0.04420732625648208, -0.04586348890679734, -0.04755160581588301, -0.049271533778185314, -0.05102309396007226, -0.05280607107036159, -0.05462021256603093, -0.056465227895713205, -0.05834078778356931, -0.06024652355611375, -0.062182026514543326, -0.06414684735508742, -0.06614049563985842, -0.06816243932063405, -0.07021210431794814, -0.07228887415780377, -0.07439208966825293, -0.07652104873800764, -0.07867500613916281, -0.0808531734160171, -0.08305471884187654, -0.08527876744561813, -0.08752440110967362, -0.08979065874097136, -0.09207653651624358, -0.09438098820296949, -0.09670292555708157, -0.09904121879841203, -0.10139469716470127, -0.10376214954482828, -0.10614232519175659, -0.1085339345155177, -0.11093564995637702, -0.11334610693814837, -0.11576390490143748, -0.11818760841640932, -0.12061574837448263, -0.12304682325816385, -0.1254793004880387, -0.1279116178457437, -0.13034218497154546, -0.13276938493495913, -0.13519157587664196, -0.13760709271960467, -0.14001424894758985, -0.14241133844827747, -0.14479663741878915, -0.14716840633078077, -0.14952489195223082, -0.1518643294228595, -0.1541849443799419, -0.15648495513111535, -0.15876257487062317, -0.1610160139352874, -0.16324348209635808, -0.16544319088325402, -0.16761335593508098, -0.16975219937569794, -0.17185795220799222, -0.17392885672292743, -0.17596316891883987, -0.17795916092638162, -0.17991512343444357, -0.1818293681123362, -0.18370023002346286, -0.18552607002569033, -0.1873052771536015, -0.1890362709778092, -0.19071750393651551, -0.19234746363452054, -0.19392467510491412, -0.19544770302872946, -0.196915153907893, -0.19832567818687397, -0.1996779723185195, -0.20097078076965322, -0.20220289796212343, -0.20337317014510287, -0.20448049719457267, -0.205523834336064, -0.20650219378688234, -0.20741464631420228, -0.2082603227055932, -0.20903841514871876, -0.20974817851714536, -0.2103889315593943, -0.21096005798858186, -0.21146100747020827, -0.21189129650587823, -0.21225050921096764, -0.21253829798448484, -0.2127543840696165, -0.21289855800369248] + [-0.21297067995655294] * 2 + [-0.21289855800369248, -0.2127543840696165, -0.21253829798448484, -0.21225050921096764, -0.21189129650587823, -0.21146100747020827, -0.21096005798858186, -0.2103889315593943, -0.20974817851714536, -0.20903841514871876, -0.2082603227055932, -0.20741464631420228, -0.20650219378688234, -0.205523834336064, -0.20448049719457267, -0.20337317014510287, -0.20220289796212343, -0.20097078076965322, -0.1996779723185195, -0.19832567818687397, -0.196915153907893, -0.19544770302872946, -0.19392467510491412, -0.19234746363452054, -0.19071750393651551, -0.1890362709778092, -0.1873052771536015, -0.18552607002569033, -0.18370023002346286, -0.1818293681123362, -0.17991512343444357, -0.17795916092638162, -0.17596316891883987, -0.17392885672292743, -0.17185795220799222, -0.16975219937569794, -0.16761335593508098, -0.16544319088325402, -0.16324348209635808, -0.1610160139352874, -0.15876257487062317, -0.15648495513111535, -0.1541849443799419, -0.1518643294228595, -0.14952489195223082, -0.14716840633078077, -0.14479663741878915, -0.14241133844827747, -0.14001424894758985, -0.13760709271960467, -0.13519157587664196, -0.13276938493495913, -0.13034218497154546, -0.1279116178457437, -0.1254793004880387, -0.12304682325816385, -0.12061574837448263, -0.11818760841640932, -0.11576390490143748, -0.11334610693814837, -0.11093564995637702, -0.1085339345155177, -0.10614232519175659, -0.10376214954482828, -0.10139469716470127, -0.09904121879841203, -0.09670292555708157, -0.09438098820296949, -0.09207653651624358, -0.08979065874097136, -0.08752440110967362, -0.08527876744561813, -0.08305471884187654, -0.0808531734160171, -0.07867500613916281, -0.07652104873800764, -0.07439208966825293, -0.07228887415780377, -0.07021210431794814, -0.06816243932063405, -0.06614049563985842, -0.06414684735508742, -0.062182026514543326, -0.06024652355611375, -0.05834078778356931, -0.056465227895713205, -0.05462021256603093, -0.05280607107036159, -0.05102309396007226, -0.049271533778185314, -0.04755160581588301, -0.04586348890679734, -0.04420732625648208, -0.04258322630446035, -0.040991263616245374, -0.03943147980274092, -0.03790388446444469, -0.03640845615790006, -0.03494514338186967, -0.033513865580738045, -0.032114514162689456, -0.03074695353025116, -0.029411022120841204, -0.02810653345501263, -0.026833277190144025, -0.025591020177387177, -0.024379507519747327, -0.023198463629239992, -0.022047593281139036, -0.020926582663404407, -0.019835100419454146, -0.018772798682523163, -0.01773931409993139, -0.01673426884566489, -0.01575727161975638, -0.014807918633035, -0.013885794575898704, -0.01299047356984816, -0.012121520100604296, -0.01127848993171731, -0.010460930997658057, -0.009668384275466811, -0.008900384634116923, -0.008156461660832389, -0.007436140463679165, -0.006738942449828773, -0.006064386078970505, -0.005411987591424359, -0.0047812617105805165, -0.004171722319363438, -0.003582883110488157, -0.0030142582103441905, -0.0024653627764073902, -0.0019357135681431891, -0.00142482949142461, -0.0009322321165464668, -0.00045744616997189964] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
        },
        "minus_x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
        },
        "minus_x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "minus_x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "minus_x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "minus_x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
        },
        "y180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 280,
        },
        "y180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "y180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "y180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "y180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "y180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009148923399437993, 0.0018644642330929335, 0.00284965898284922, 0.0038714271362863782, 0.0049307255528147804, 0.006028516420688381, 0.007165766220976314, 0.008343444638726875, 0.009562523421161033, 0.010823975182848718, 0.01212877215794101, 0.013477884899657545, 0.01487228092735833, 0.016312923321664778, 0.017800769268233846, 0.019336768550933622, 0.020921861995316114, 0.02255697986343462, 0.024243040201208592, 0.02598094713969632, 0.027771589151797407, 0.02961583726607, 0.03151454323951276, 0.03346853769132978, 0.03547862819986278, 0.037545597365046326, 0.03967020083890829, 0.041853165326808814, 0.04409518656227807, 0.046396927258479985, 0.04875901503949465, 0.051182040354774354, 0.05366655438028805, 0.05621306691002526, 0.05882204424168241, 0.06149390706050232, 0.06422902832537891, 0.06702773116147609, 0.06989028676373935, 0.07281691231580012, 0.07580776892888938, 0.07886295960548184, 0.08198252723249075, 0.0851664526089207, 0.08841465251296415, 0.09172697781359468, 0.09510321163176602, 0.09854306755637063, 0.10204618792014453, 0.10561214214072318, 0.10924042513206186, 0.11293045579142641, 0.11668157556713862, 0.1204930471122275, 0.12436405302908665, 0.12829369471017485, 0.13228099127971685, 0.1363248786412681, 0.14042420863589627, 0.14457774831560755, 0.14878417933650587, 0.15304209747601527, 0.15735001227832562, 0.1617063468320342, 0.16610943768375308, 0.17055753489123626, 0.17504880221934724, 0.17958131748194273, 0.18415307303248715, 0.18876197640593897, 0.19340585111416314, 0.19808243759682406, 0.20278939432940254, 0.20752429908965656, 0.21228465038351318, 0.2170678690310354, 0.22187129991275403, 0.22669221387629673, 0.23152780980287496, 0.23637521683281865, 0.24123149674896527, 0.2460936465163277, 0.2509586009760774, 0.2558232356914874, 0.2606843699430909, 0.26553876986991826, 0.2703831517532839, 0.27521418543920934, 0.2800284978951797, 0.28482267689655494, 0.2895932748375783, 0.29433681266156153, 0.29904978390446163, 0.303728658845719, 0.3083698887598838, 0.3129699102622307, 0.31752514974124635, 0.3220320278705748, 0.32648696419271617, 0.33088638176650803, 0.33522671187016195, 0.3395043987513959, 0.34371590441598443, 0.34785771344585487, 0.35192633783767974, 0.35591832185276323, 0.35983024686888715, 0.3636587362246724, 0.3674004600469257, 0.37105214005138065, 0.374610554307203, 0.3780725419556184, 0.38143500787303103, 0.3846949272690411, 0.38784935020982825, 0.3908954060574589, 0.393830307815786, 0.39665135637374793, 0.399355944637039, 0.40194156153930644, 0.40440579592424686, 0.40674634029020573, 0.40896099438914535, 0.411047668672128, 0.4130043875737647, 0.41482929262840457, 0.4165206454111864, 0.41807683029743753, 0.4194963570342907, 0.4207778631187886, 0.4219201159771637, 0.42292201494041654, 0.42378259301175647, 0.42450101842193527, 0.4250765959689697, 0.425508768139233, 0.42579711600738496] + [0.4259413599131059] * 2 + [0.42579711600738496, 0.425508768139233, 0.4250765959689697, 0.42450101842193527, 0.42378259301175647, 0.42292201494041654, 0.4219201159771637, 0.4207778631187886, 0.4194963570342907, 0.41807683029743753, 0.4165206454111864, 0.41482929262840457, 0.4130043875737647, 0.411047668672128, 0.40896099438914535, 0.40674634029020573, 0.40440579592424686, 0.40194156153930644, 0.399355944637039, 0.39665135637374793, 0.393830307815786, 0.3908954060574589, 0.38784935020982825, 0.3846949272690411, 0.38143500787303103, 0.3780725419556184, 0.374610554307203, 0.37105214005138065, 0.3674004600469257, 0.3636587362246724, 0.35983024686888715, 0.35591832185276323, 0.35192633783767974, 0.34785771344585487, 0.34371590441598443, 0.3395043987513959, 0.33522671187016195, 0.33088638176650803, 0.32648696419271617, 0.3220320278705748, 0.31752514974124635, 0.3129699102622307, 0.3083698887598838, 0.303728658845719, 0.29904978390446163, 0.29433681266156153, 0.2895932748375783, 0.28482267689655494, 0.2800284978951797, 0.27521418543920934, 0.2703831517532839, 0.26553876986991826, 0.2606843699430909, 0.2558232356914874, 0.2509586009760774, 0.2460936465163277, 0.24123149674896527, 0.23637521683281865, 0.23152780980287496, 0.22669221387629673, 0.22187129991275403, 0.2170678690310354, 0.21228465038351318, 0.20752429908965656, 0.20278939432940254, 0.19808243759682406, 0.19340585111416314, 0.18876197640593897, 0.18415307303248715, 0.17958131748194273, 0.17504880221934724, 0.17055753489123626, 0.16610943768375308, 0.1617063468320342, 0.15735001227832562, 0.15304209747601527, 0.14878417933650587, 0.14457774831560755, 0.14042420863589627, 0.1363248786412681, 0.13228099127971685, 0.12829369471017485, 0.12436405302908665, 0.1204930471122275, 0.11668157556713862, 0.11293045579142641, 0.10924042513206186, 0.10561214214072318, 0.10204618792014453, 0.09854306755637063, 0.09510321163176602, 0.09172697781359468, 0.08841465251296415, 0.0851664526089207, 0.08198252723249075, 0.07886295960548184, 0.07580776892888938, 0.07281691231580012, 0.06989028676373935, 0.06702773116147609, 0.06422902832537891, 0.06149390706050232, 0.05882204424168241, 0.05621306691002526, 0.05366655438028805, 0.051182040354774354, 0.04875901503949465, 0.046396927258479985, 0.04409518656227807, 0.041853165326808814, 0.03967020083890829, 0.037545597365046326, 0.03547862819986278, 0.03346853769132978, 0.03151454323951276, 0.02961583726607, 0.027771589151797407, 0.02598094713969632, 0.024243040201208592, 0.02255697986343462, 0.020921861995316114, 0.019336768550933622, 0.017800769268233846, 0.016312923321664778, 0.01487228092735833, 0.013477884899657545, 0.01212877215794101, 0.010823975182848718, 0.009562523421161033, 0.008343444638726875, 0.007165766220976314, 0.006028516420688381, 0.0049307255528147804, 0.0038714271362863782, 0.00284965898284922, 0.0018644642330929335, 0.0009148923399437993] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
        },
        "y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 280,
        },
        "y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.00045744616997189964, 0.0009322321165464668, 0.00142482949142461, 0.0019357135681431891, 0.0024653627764073902, 0.0030142582103441905, 0.003582883110488157, 0.004171722319363438, 0.0047812617105805165, 0.005411987591424359, 0.006064386078970505, 0.006738942449828773, 0.007436140463679165, 0.008156461660832389, 0.008900384634116923, 0.009668384275466811, 0.010460930997658057, 0.01127848993171731, 0.012121520100604296, 0.01299047356984816, 0.013885794575898704, 0.014807918633035, 0.01575727161975638, 0.01673426884566489, 0.01773931409993139, 0.018772798682523163, 0.019835100419454146, 0.020926582663404407, 0.022047593281139036, 0.023198463629239992, 0.024379507519747327, 0.025591020177387177, 0.026833277190144025, 0.02810653345501263, 0.029411022120841204, 0.03074695353025116, 0.032114514162689456, 0.033513865580738045, 0.03494514338186967, 0.03640845615790006, 0.03790388446444469, 0.03943147980274092, 0.040991263616245374, 0.04258322630446035, 0.04420732625648208, 0.04586348890679734, 0.04755160581588301, 0.049271533778185314, 0.05102309396007226, 0.05280607107036159, 0.05462021256603093, 0.056465227895713205, 0.05834078778356931, 0.06024652355611375, 0.062182026514543326, 0.06414684735508742, 0.06614049563985842, 0.06816243932063405, 0.07021210431794814, 0.07228887415780377, 0.07439208966825293, 0.07652104873800764, 0.07867500613916281, 0.0808531734160171, 0.08305471884187654, 0.08527876744561813, 0.08752440110967362, 0.08979065874097136, 0.09207653651624358, 0.09438098820296949, 0.09670292555708157, 0.09904121879841203, 0.10139469716470127, 0.10376214954482828, 0.10614232519175659, 0.1085339345155177, 0.11093564995637702, 0.11334610693814837, 0.11576390490143748, 0.11818760841640932, 0.12061574837448263, 0.12304682325816385, 0.1254793004880387, 0.1279116178457437, 0.13034218497154546, 0.13276938493495913, 0.13519157587664196, 0.13760709271960467, 0.14001424894758985, 0.14241133844827747, 0.14479663741878915, 0.14716840633078077, 0.14952489195223082, 0.1518643294228595, 0.1541849443799419, 0.15648495513111535, 0.15876257487062317, 0.1610160139352874, 0.16324348209635808, 0.16544319088325402, 0.16761335593508098, 0.16975219937569794, 0.17185795220799222, 0.17392885672292743, 0.17596316891883987, 0.17795916092638162, 0.17991512343444357, 0.1818293681123362, 0.18370023002346286, 0.18552607002569033, 0.1873052771536015, 0.1890362709778092, 0.19071750393651551, 0.19234746363452054, 0.19392467510491412, 0.19544770302872946, 0.196915153907893, 0.19832567818687397, 0.1996779723185195, 0.20097078076965322, 0.20220289796212343, 0.20337317014510287, 0.20448049719457267, 0.205523834336064, 0.20650219378688234, 0.20741464631420228, 0.2082603227055932, 0.20903841514871876, 0.20974817851714536, 0.2103889315593943, 0.21096005798858186, 0.21146100747020827, 0.21189129650587823, 0.21225050921096764, 0.21253829798448484, 0.2127543840696165, 0.21289855800369248] + [0.21297067995655294] * 2 + [0.21289855800369248, 0.2127543840696165, 0.21253829798448484, 0.21225050921096764, 0.21189129650587823, 0.21146100747020827, 0.21096005798858186, 0.2103889315593943, 0.20974817851714536, 0.20903841514871876, 0.2082603227055932, 0.20741464631420228, 0.20650219378688234, 0.205523834336064, 0.20448049719457267, 0.20337317014510287, 0.20220289796212343, 0.20097078076965322, 0.1996779723185195, 0.19832567818687397, 0.196915153907893, 0.19544770302872946, 0.19392467510491412, 0.19234746363452054, 0.19071750393651551, 0.1890362709778092, 0.1873052771536015, 0.18552607002569033, 0.18370023002346286, 0.1818293681123362, 0.17991512343444357, 0.17795916092638162, 0.17596316891883987, 0.17392885672292743, 0.17185795220799222, 0.16975219937569794, 0.16761335593508098, 0.16544319088325402, 0.16324348209635808, 0.1610160139352874, 0.15876257487062317, 0.15648495513111535, 0.1541849443799419, 0.1518643294228595, 0.14952489195223082, 0.14716840633078077, 0.14479663741878915, 0.14241133844827747, 0.14001424894758985, 0.13760709271960467, 0.13519157587664196, 0.13276938493495913, 0.13034218497154546, 0.1279116178457437, 0.1254793004880387, 0.12304682325816385, 0.12061574837448263, 0.11818760841640932, 0.11576390490143748, 0.11334610693814837, 0.11093564995637702, 0.1085339345155177, 0.10614232519175659, 0.10376214954482828, 0.10139469716470127, 0.09904121879841203, 0.09670292555708157, 0.09438098820296949, 0.09207653651624358, 0.08979065874097136, 0.08752440110967362, 0.08527876744561813, 0.08305471884187654, 0.0808531734160171, 0.07867500613916281, 0.07652104873800764, 0.07439208966825293, 0.07228887415780377, 0.07021210431794814, 0.06816243932063405, 0.06614049563985842, 0.06414684735508742, 0.062182026514543326, 0.06024652355611375, 0.05834078778356931, 0.056465227895713205, 0.05462021256603093, 0.05280607107036159, 0.05102309396007226, 0.049271533778185314, 0.04755160581588301, 0.04586348890679734, 0.04420732625648208, 0.04258322630446035, 0.040991263616245374, 0.03943147980274092, 0.03790388446444469, 0.03640845615790006, 0.03494514338186967, 0.033513865580738045, 0.032114514162689456, 0.03074695353025116, 0.029411022120841204, 0.02810653345501263, 0.026833277190144025, 0.025591020177387177, 0.024379507519747327, 0.023198463629239992, 0.022047593281139036, 0.020926582663404407, 0.019835100419454146, 0.018772798682523163, 0.01773931409993139, 0.01673426884566489, 0.01575727161975638, 0.014807918633035, 0.013885794575898704, 0.01299047356984816, 0.012121520100604296, 0.01127848993171731, 0.010460930997658057, 0.009668384275466811, 0.008900384634116923, 0.008156461660832389, 0.007436140463679165, 0.006738942449828773, 0.006064386078970505, 0.005411987591424359, 0.0047812617105805165, 0.004171722319363438, 0.003582883110488157, 0.0030142582103441905, 0.0024653627764073902, 0.0019357135681431891, 0.00142482949142461, 0.0009322321165464668, 0.00045744616997189964] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
        },
        "minus_y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 280,
        },
        "minus_y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "minus_y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "minus_y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "minus_y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
        },
        "minus_y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.00045744616997189964, -0.0009322321165464668, -0.00142482949142461, -0.0019357135681431891, -0.0024653627764073902, -0.0030142582103441905, -0.003582883110488157, -0.004171722319363438, -0.0047812617105805165, -0.005411987591424359, -0.006064386078970505, -0.006738942449828773, -0.007436140463679165, -0.008156461660832389, -0.008900384634116923, -0.009668384275466811, -0.010460930997658057, -0.01127848993171731, -0.012121520100604296, -0.01299047356984816, -0.013885794575898704, -0.014807918633035, -0.01575727161975638, -0.01673426884566489, -0.01773931409993139, -0.018772798682523163, -0.019835100419454146, -0.020926582663404407, -0.022047593281139036, -0.023198463629239992, -0.024379507519747327, -0.025591020177387177, -0.026833277190144025, -0.02810653345501263, -0.029411022120841204, -0.03074695353025116, -0.032114514162689456, -0.033513865580738045, -0.03494514338186967, -0.03640845615790006, -0.03790388446444469, -0.03943147980274092, -0.040991263616245374, -0.04258322630446035, -0.04420732625648208, -0.04586348890679734, -0.04755160581588301, -0.049271533778185314, -0.05102309396007226, -0.05280607107036159, -0.05462021256603093, -0.056465227895713205, -0.05834078778356931, -0.06024652355611375, -0.062182026514543326, -0.06414684735508742, -0.06614049563985842, -0.06816243932063405, -0.07021210431794814, -0.07228887415780377, -0.07439208966825293, -0.07652104873800764, -0.07867500613916281, -0.0808531734160171, -0.08305471884187654, -0.08527876744561813, -0.08752440110967362, -0.08979065874097136, -0.09207653651624358, -0.09438098820296949, -0.09670292555708157, -0.09904121879841203, -0.10139469716470127, -0.10376214954482828, -0.10614232519175659, -0.1085339345155177, -0.11093564995637702, -0.11334610693814837, -0.11576390490143748, -0.11818760841640932, -0.12061574837448263, -0.12304682325816385, -0.1254793004880387, -0.1279116178457437, -0.13034218497154546, -0.13276938493495913, -0.13519157587664196, -0.13760709271960467, -0.14001424894758985, -0.14241133844827747, -0.14479663741878915, -0.14716840633078077, -0.14952489195223082, -0.1518643294228595, -0.1541849443799419, -0.15648495513111535, -0.15876257487062317, -0.1610160139352874, -0.16324348209635808, -0.16544319088325402, -0.16761335593508098, -0.16975219937569794, -0.17185795220799222, -0.17392885672292743, -0.17596316891883987, -0.17795916092638162, -0.17991512343444357, -0.1818293681123362, -0.18370023002346286, -0.18552607002569033, -0.1873052771536015, -0.1890362709778092, -0.19071750393651551, -0.19234746363452054, -0.19392467510491412, -0.19544770302872946, -0.196915153907893, -0.19832567818687397, -0.1996779723185195, -0.20097078076965322, -0.20220289796212343, -0.20337317014510287, -0.20448049719457267, -0.205523834336064, -0.20650219378688234, -0.20741464631420228, -0.2082603227055932, -0.20903841514871876, -0.20974817851714536, -0.2103889315593943, -0.21096005798858186, -0.21146100747020827, -0.21189129650587823, -0.21225050921096764, -0.21253829798448484, -0.2127543840696165, -0.21289855800369248] + [-0.21297067995655294] * 2 + [-0.21289855800369248, -0.2127543840696165, -0.21253829798448484, -0.21225050921096764, -0.21189129650587823, -0.21146100747020827, -0.21096005798858186, -0.2103889315593943, -0.20974817851714536, -0.20903841514871876, -0.2082603227055932, -0.20741464631420228, -0.20650219378688234, -0.205523834336064, -0.20448049719457267, -0.20337317014510287, -0.20220289796212343, -0.20097078076965322, -0.1996779723185195, -0.19832567818687397, -0.196915153907893, -0.19544770302872946, -0.19392467510491412, -0.19234746363452054, -0.19071750393651551, -0.1890362709778092, -0.1873052771536015, -0.18552607002569033, -0.18370023002346286, -0.1818293681123362, -0.17991512343444357, -0.17795916092638162, -0.17596316891883987, -0.17392885672292743, -0.17185795220799222, -0.16975219937569794, -0.16761335593508098, -0.16544319088325402, -0.16324348209635808, -0.1610160139352874, -0.15876257487062317, -0.15648495513111535, -0.1541849443799419, -0.1518643294228595, -0.14952489195223082, -0.14716840633078077, -0.14479663741878915, -0.14241133844827747, -0.14001424894758985, -0.13760709271960467, -0.13519157587664196, -0.13276938493495913, -0.13034218497154546, -0.1279116178457437, -0.1254793004880387, -0.12304682325816385, -0.12061574837448263, -0.11818760841640932, -0.11576390490143748, -0.11334610693814837, -0.11093564995637702, -0.1085339345155177, -0.10614232519175659, -0.10376214954482828, -0.10139469716470127, -0.09904121879841203, -0.09670292555708157, -0.09438098820296949, -0.09207653651624358, -0.08979065874097136, -0.08752440110967362, -0.08527876744561813, -0.08305471884187654, -0.0808531734160171, -0.07867500613916281, -0.07652104873800764, -0.07439208966825293, -0.07228887415780377, -0.07021210431794814, -0.06816243932063405, -0.06614049563985842, -0.06414684735508742, -0.062182026514543326, -0.06024652355611375, -0.05834078778356931, -0.056465227895713205, -0.05462021256603093, -0.05280607107036159, -0.05102309396007226, -0.049271533778185314, -0.04755160581588301, -0.04586348890679734, -0.04420732625648208, -0.04258322630446035, -0.040991263616245374, -0.03943147980274092, -0.03790388446444469, -0.03640845615790006, -0.03494514338186967, -0.033513865580738045, -0.032114514162689456, -0.03074695353025116, -0.029411022120841204, -0.02810653345501263, -0.026833277190144025, -0.025591020177387177, -0.024379507519747327, -0.023198463629239992, -0.022047593281139036, -0.020926582663404407, -0.019835100419454146, -0.018772798682523163, -0.01773931409993139, -0.01673426884566489, -0.01575727161975638, -0.014807918633035, -0.013885794575898704, -0.01299047356984816, -0.012121520100604296, -0.01127848993171731, -0.010460930997658057, -0.009668384275466811, -0.008900384634116923, -0.008156461660832389, -0.007436140463679165, -0.006738942449828773, -0.006064386078970505, -0.005411987591424359, -0.0047812617105805165, -0.004171722319363438, -0.003582883110488157, -0.0030142582103441905, -0.0024653627764073902, -0.0019357135681431891, -0.00142482949142461, -0.0009322321165464668, -0.00045744616997189964] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
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
            "samples": [0.0010431184086790637, 0.001297437087971483, 0.001579419271390326, 0.0018906571247472115, 0.0022327747859784914, 0.0026074265218423314, 0.0030162947658382232, 0.003461088038651809, 0.003943538752722474, 0.004465400902827129, 0.005028447644869812, 0.005634468765363369, 0.00628526804438481, 0.006982660515079928, 0.007728469623084345, 0.00852452428951689, 0.009372655881485822, 0.010274695094328934, 0.011232468750083296, 0.012247796516949913, 0.013322487554780361, 0.014458337091867734, 0.01565712293857104, 0.016920601943539695, 0.018250506398533706, 0.019648540398052795, 0.02111637616019582, 0.02265565031536685, 0.024267960169629045, 0.02595485994967802, 0.027717857036564576, 0.029558408195441106, 0.03147791580873541, 0.03347772412027163, 0.03555911549795721, 0.03772330672274012, 0.03997144531160804, 0.042304605882454244, 0.044723786568669904, 0.04722990549134098, 0.04982379729692978, 0.05250620976830496, 0.05527780051695001, 0.058139133764130296, 0.06109067721872816, 0.06413279905937112, 0.06726576502837225, 0.07048973564488095, 0.07380476354450223, 0.07721079095248568, 0.08070764729741242, 0.08429504697211393, 0.0879725872483519, 0.09173974635156179, 0.09559588170172308, 0.09954022832616044, 0.10357189744981242, 0.10768987526821235, 0.11189302190813086, 0.11618007058050804, 0.12054962692998235, 0.12500016858497545, 0.12953004491194683, 0.13413747697706035, 0.13882055771813773, 0.14357725232938434, 0.1484053988609816, 0.15330270903523802, 0.15826676928058409, 0.16329504198427403, 0.16838486696424743, 0.1735334631601626, 0.1787379305432009, 0.18399525224379068, 0.1893022968959787, 0.1946558211967324, 0.2000524726780225, 0.20548879268910147, 0.21096121958595615, 0.21646609212448611, 0.22199965305352734, 0.22755805290342507, 0.23313735396543173, 0.23873353445681147, 0.24434249286611068, 0.24996005247267947, 0.2555819660341269, 0.26120392063503095, 0.2668215426898536, 0.2724304030926589, 0.27802602250590464, 0.28360387678023474, 0.2891594024969082, 0.29468800262419026, 0.3001850522787632, 0.30564590458294194, 0.3110658966082452, 0.31644035539563287, 0.32176460404252344, 0.32703396784650657, 0.33224378049550174, 0.33738939029395826, 0.3424661664145676, 0.34746950516484454, 0.35239483625785073, 0.3572376290762628, 0.3619933989189455, 0.36665771321916907, 0.3712261977236015, 0.37569454262123525, 0.38005850861144863, 0.3843139329004605, 0.3884567351155389, 0.3924829231264168, 0.39638859876350385, 0.40016996342264993, 0.40382332354636, 0.4073450959715863, 0.4107318131344117, 0.41398012812219737, 0.4170868195639962, 0.4200487963503368, 0.42286310217374873, 0.42552691988172936, 0.42803757563417577, 0.43039254285763634, 0.4325894459891301, 0.4346260640026206, 0.43650033371165115, 0.4382103528420395, 0.4397543828689488, 0.4411308516130899, 0.4423383555912364, 0.44337566211670193, 0.44424171114587985, 0.4449356168674101, 0.44545666903102915, 0.44580433401362796] + [0.44597825562053467] * 2 + [0.44580433401362796, 0.44545666903102915, 0.4449356168674101, 0.44424171114587985, 0.44337566211670193, 0.4423383555912364, 0.4411308516130899, 0.4397543828689488, 0.4382103528420395, 0.43650033371165115, 0.4346260640026206, 0.4325894459891301, 0.43039254285763634, 0.42803757563417577, 0.42552691988172936, 0.42286310217374873, 0.4200487963503368, 0.4170868195639962, 0.41398012812219737, 0.4107318131344117, 0.4073450959715863, 0.40382332354636, 0.40016996342264993, 0.39638859876350385, 0.3924829231264168, 0.3884567351155389, 0.3843139329004605, 0.38005850861144863, 0.37569454262123525, 0.3712261977236015, 0.36665771321916907, 0.3619933989189455, 0.3572376290762628, 0.35239483625785073, 0.34746950516484454, 0.3424661664145676, 0.33738939029395826, 0.33224378049550174, 0.32703396784650657, 0.32176460404252344, 0.31644035539563287, 0.3110658966082452, 0.30564590458294194, 0.3001850522787632, 0.29468800262419026, 0.2891594024969082, 0.28360387678023474, 0.27802602250590464, 0.2724304030926589, 0.2668215426898536, 0.26120392063503095, 0.2555819660341269, 0.24996005247267947, 0.24434249286611068, 0.23873353445681147, 0.23313735396543173, 0.22755805290342507, 0.22199965305352734, 0.21646609212448611, 0.21096121958595615, 0.20548879268910147, 0.2000524726780225, 0.1946558211967324, 0.1893022968959787, 0.18399525224379068, 0.1787379305432009, 0.1735334631601626, 0.16838486696424743, 0.16329504198427403, 0.15826676928058409, 0.15330270903523802, 0.1484053988609816, 0.14357725232938434, 0.13882055771813773, 0.13413747697706035, 0.12953004491194683, 0.12500016858497545, 0.12054962692998235, 0.11618007058050804, 0.11189302190813086, 0.10768987526821235, 0.10357189744981242, 0.09954022832616044, 0.09559588170172308, 0.09173974635156179, 0.0879725872483519, 0.08429504697211393, 0.08070764729741242, 0.07721079095248568, 0.07380476354450223, 0.07048973564488095, 0.06726576502837225, 0.06413279905937112, 0.06109067721872816, 0.058139133764130296, 0.05527780051695001, 0.05250620976830496, 0.04982379729692978, 0.04722990549134098, 0.044723786568669904, 0.042304605882454244, 0.03997144531160804, 0.03772330672274012, 0.03555911549795721, 0.03347772412027163, 0.03147791580873541, 0.029558408195441106, 0.027717857036564576, 0.02595485994967802, 0.024267960169629045, 0.02265565031536685, 0.02111637616019582, 0.019648540398052795, 0.018250506398533706, 0.016920601943539695, 0.01565712293857104, 0.014458337091867734, 0.013322487554780361, 0.012247796516949913, 0.011232468750083296, 0.010274695094328934, 0.009372655881485822, 0.00852452428951689, 0.007728469623084345, 0.006982660515079928, 0.00628526804438481, 0.005634468765363369, 0.005028447644869812, 0.004465400902827129, 0.003943538752722474, 0.003461088038651809, 0.0030162947658382232, 0.0026074265218423314, 0.0022327747859784914, 0.0018906571247472115, 0.001579419271390326, 0.001297437087971483, 0.0010431184086790637] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0] * 2,
        },
        "x180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 280,
        },
        "x180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "x180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "x180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "x180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0005215592043395318, 0.0006487185439857415, 0.000789709635695163, 0.0009453285623736057, 0.0011163873929892457, 0.0013037132609211657, 0.0015081473829191116, 0.0017305440193259045, 0.001971769376361237, 0.0022327004514135643, 0.002514223822434906, 0.0028172343826816846, 0.003142634022192405, 0.003491330257539964, 0.0038642348115421727, 0.004262262144758445, 0.004686327940742911, 0.005137347547164467, 0.005616234375041648, 0.006123898258474957, 0.006661243777390181, 0.007229168545933867, 0.00782856146928552, 0.008460300971769847, 0.009125253199266853, 0.009824270199026397, 0.01055818808009791, 0.011327825157683425, 0.012133980084814523, 0.01297742997483901, 0.013858928518282288, 0.014779204097720553, 0.015738957904367704, 0.016738862060135817, 0.017779557748978606, 0.01886165336137006, 0.01998572265580402, 0.021152302941227122, 0.022361893284334952, 0.02361495274567049, 0.02491189864846489, 0.02625310488415248, 0.027638900258475006, 0.029069566882065148, 0.03054533860936408, 0.03206639952968556, 0.03363288251418613, 0.035244867822440476, 0.036902381772251115, 0.03860539547624284, 0.04035382364870621, 0.042147523486056965, 0.04398629362417595, 0.045869873175780895, 0.04779794085086154, 0.04977011416308022, 0.05178594872490621, 0.05384493763410617, 0.05594651095406543, 0.05809003529025402, 0.060274813464991174, 0.06250008429248773, 0.06476502245597342, 0.06706873848853018, 0.06941027885906886, 0.07178862616469217, 0.0742026994304908, 0.07665135451761901, 0.07913338464029204, 0.08164752099213701, 0.08419243348212371, 0.0867667315800813, 0.08936896527160045, 0.09199762612189534, 0.09465114844798934, 0.0973279105983662, 0.10002623633901125, 0.10274439634455074, 0.10548060979297808, 0.10823304606224306, 0.11099982652676367, 0.11377902645171253, 0.11656867698271586, 0.11936676722840574, 0.12217124643305534, 0.12498002623633973, 0.12779098301706346, 0.13060196031751548, 0.1334107713449268, 0.13621520154632946, 0.13901301125295232, 0.14180193839011737, 0.1445797012484541, 0.14734400131209513, 0.1500925261393816, 0.15282295229147097, 0.1555329483041226, 0.15822017769781643, 0.16088230202126172, 0.16351698392325328, 0.16612189024775087, 0.16869469514697913, 0.1712330832072838, 0.17373475258242227, 0.17619741812892536, 0.1786188145381314, 0.18099669945947275, 0.18332885660958453, 0.18561309886180075, 0.18784727131061763, 0.19002925430572432, 0.19215696645023025, 0.19422836755776945, 0.1962414615632084, 0.19819429938175193, 0.20008498171132497, 0.20191166177318, 0.20367254798579315, 0.20536590656720585, 0.20699006406109868, 0.2085434097819981, 0.2100243981751684, 0.21143155108687436, 0.21276345994086468, 0.21401878781708789, 0.21519627142881817, 0.21629472299456504, 0.2173130320013103, 0.21825016685582557, 0.21910517642101976, 0.2198771914344744, 0.22056542580654495, 0.2211691777956182, 0.22168783105835096, 0.22212085557293992, 0.22246780843370506, 0.22272833451551458, 0.22290216700681398] + [0.22298912781026733] * 2 + [0.22290216700681398, 0.22272833451551458, 0.22246780843370506, 0.22212085557293992, 0.22168783105835096, 0.2211691777956182, 0.22056542580654495, 0.2198771914344744, 0.21910517642101976, 0.21825016685582557, 0.2173130320013103, 0.21629472299456504, 0.21519627142881817, 0.21401878781708789, 0.21276345994086468, 0.21143155108687436, 0.2100243981751684, 0.2085434097819981, 0.20699006406109868, 0.20536590656720585, 0.20367254798579315, 0.20191166177318, 0.20008498171132497, 0.19819429938175193, 0.1962414615632084, 0.19422836755776945, 0.19215696645023025, 0.19002925430572432, 0.18784727131061763, 0.18561309886180075, 0.18332885660958453, 0.18099669945947275, 0.1786188145381314, 0.17619741812892536, 0.17373475258242227, 0.1712330832072838, 0.16869469514697913, 0.16612189024775087, 0.16351698392325328, 0.16088230202126172, 0.15822017769781643, 0.1555329483041226, 0.15282295229147097, 0.1500925261393816, 0.14734400131209513, 0.1445797012484541, 0.14180193839011737, 0.13901301125295232, 0.13621520154632946, 0.1334107713449268, 0.13060196031751548, 0.12779098301706346, 0.12498002623633973, 0.12217124643305534, 0.11936676722840574, 0.11656867698271586, 0.11377902645171253, 0.11099982652676367, 0.10823304606224306, 0.10548060979297808, 0.10274439634455074, 0.10002623633901125, 0.0973279105983662, 0.09465114844798934, 0.09199762612189534, 0.08936896527160045, 0.0867667315800813, 0.08419243348212371, 0.08164752099213701, 0.07913338464029204, 0.07665135451761901, 0.0742026994304908, 0.07178862616469217, 0.06941027885906886, 0.06706873848853018, 0.06476502245597342, 0.06250008429248773, 0.060274813464991174, 0.05809003529025402, 0.05594651095406543, 0.05384493763410617, 0.05178594872490621, 0.04977011416308022, 0.04779794085086154, 0.045869873175780895, 0.04398629362417595, 0.042147523486056965, 0.04035382364870621, 0.03860539547624284, 0.036902381772251115, 0.035244867822440476, 0.03363288251418613, 0.03206639952968556, 0.03054533860936408, 0.029069566882065148, 0.027638900258475006, 0.02625310488415248, 0.02491189864846489, 0.02361495274567049, 0.022361893284334952, 0.021152302941227122, 0.01998572265580402, 0.01886165336137006, 0.017779557748978606, 0.016738862060135817, 0.015738957904367704, 0.014779204097720553, 0.013858928518282288, 0.01297742997483901, 0.012133980084814523, 0.011327825157683425, 0.01055818808009791, 0.009824270199026397, 0.009125253199266853, 0.008460300971769847, 0.00782856146928552, 0.007229168545933867, 0.006661243777390181, 0.006123898258474957, 0.005616234375041648, 0.005137347547164467, 0.004686327940742911, 0.004262262144758445, 0.0038642348115421727, 0.003491330257539964, 0.003142634022192405, 0.0028172343826816846, 0.002514223822434906, 0.0022327004514135643, 0.001971769376361237, 0.0017305440193259045, 0.0015081473829191116, 0.0013037132609211657, 0.0011163873929892457, 0.0009453285623736057, 0.000789709635695163, 0.0006487185439857415, 0.0005215592043395318] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0] * 2,
        },
        "x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 280,
        },
        "x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "minus_x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0005215592043395318, -0.0006487185439857415, -0.000789709635695163, -0.0009453285623736057, -0.0011163873929892457, -0.0013037132609211657, -0.0015081473829191116, -0.0017305440193259045, -0.001971769376361237, -0.0022327004514135643, -0.002514223822434906, -0.0028172343826816846, -0.003142634022192405, -0.003491330257539964, -0.0038642348115421727, -0.004262262144758445, -0.004686327940742911, -0.005137347547164467, -0.005616234375041648, -0.006123898258474957, -0.006661243777390181, -0.007229168545933867, -0.00782856146928552, -0.008460300971769847, -0.009125253199266853, -0.009824270199026397, -0.01055818808009791, -0.011327825157683425, -0.012133980084814523, -0.01297742997483901, -0.013858928518282288, -0.014779204097720553, -0.015738957904367704, -0.016738862060135817, -0.017779557748978606, -0.01886165336137006, -0.01998572265580402, -0.021152302941227122, -0.022361893284334952, -0.02361495274567049, -0.02491189864846489, -0.02625310488415248, -0.027638900258475006, -0.029069566882065148, -0.03054533860936408, -0.03206639952968556, -0.03363288251418613, -0.035244867822440476, -0.036902381772251115, -0.03860539547624284, -0.04035382364870621, -0.042147523486056965, -0.04398629362417595, -0.045869873175780895, -0.04779794085086154, -0.04977011416308022, -0.05178594872490621, -0.05384493763410617, -0.05594651095406543, -0.05809003529025402, -0.060274813464991174, -0.06250008429248773, -0.06476502245597342, -0.06706873848853018, -0.06941027885906886, -0.07178862616469217, -0.0742026994304908, -0.07665135451761901, -0.07913338464029204, -0.08164752099213701, -0.08419243348212371, -0.0867667315800813, -0.08936896527160045, -0.09199762612189534, -0.09465114844798934, -0.0973279105983662, -0.10002623633901125, -0.10274439634455074, -0.10548060979297808, -0.10823304606224306, -0.11099982652676367, -0.11377902645171253, -0.11656867698271586, -0.11936676722840574, -0.12217124643305534, -0.12498002623633973, -0.12779098301706346, -0.13060196031751548, -0.1334107713449268, -0.13621520154632946, -0.13901301125295232, -0.14180193839011737, -0.1445797012484541, -0.14734400131209513, -0.1500925261393816, -0.15282295229147097, -0.1555329483041226, -0.15822017769781643, -0.16088230202126172, -0.16351698392325328, -0.16612189024775087, -0.16869469514697913, -0.1712330832072838, -0.17373475258242227, -0.17619741812892536, -0.1786188145381314, -0.18099669945947275, -0.18332885660958453, -0.18561309886180075, -0.18784727131061763, -0.19002925430572432, -0.19215696645023025, -0.19422836755776945, -0.1962414615632084, -0.19819429938175193, -0.20008498171132497, -0.20191166177318, -0.20367254798579315, -0.20536590656720585, -0.20699006406109868, -0.2085434097819981, -0.2100243981751684, -0.21143155108687436, -0.21276345994086468, -0.21401878781708789, -0.21519627142881817, -0.21629472299456504, -0.2173130320013103, -0.21825016685582557, -0.21910517642101976, -0.2198771914344744, -0.22056542580654495, -0.2211691777956182, -0.22168783105835096, -0.22212085557293992, -0.22246780843370506, -0.22272833451551458, -0.22290216700681398] + [-0.22298912781026733] * 2 + [-0.22290216700681398, -0.22272833451551458, -0.22246780843370506, -0.22212085557293992, -0.22168783105835096, -0.2211691777956182, -0.22056542580654495, -0.2198771914344744, -0.21910517642101976, -0.21825016685582557, -0.2173130320013103, -0.21629472299456504, -0.21519627142881817, -0.21401878781708789, -0.21276345994086468, -0.21143155108687436, -0.2100243981751684, -0.2085434097819981, -0.20699006406109868, -0.20536590656720585, -0.20367254798579315, -0.20191166177318, -0.20008498171132497, -0.19819429938175193, -0.1962414615632084, -0.19422836755776945, -0.19215696645023025, -0.19002925430572432, -0.18784727131061763, -0.18561309886180075, -0.18332885660958453, -0.18099669945947275, -0.1786188145381314, -0.17619741812892536, -0.17373475258242227, -0.1712330832072838, -0.16869469514697913, -0.16612189024775087, -0.16351698392325328, -0.16088230202126172, -0.15822017769781643, -0.1555329483041226, -0.15282295229147097, -0.1500925261393816, -0.14734400131209513, -0.1445797012484541, -0.14180193839011737, -0.13901301125295232, -0.13621520154632946, -0.1334107713449268, -0.13060196031751548, -0.12779098301706346, -0.12498002623633973, -0.12217124643305534, -0.11936676722840574, -0.11656867698271586, -0.11377902645171253, -0.11099982652676367, -0.10823304606224306, -0.10548060979297808, -0.10274439634455074, -0.10002623633901125, -0.0973279105983662, -0.09465114844798934, -0.09199762612189534, -0.08936896527160045, -0.0867667315800813, -0.08419243348212371, -0.08164752099213701, -0.07913338464029204, -0.07665135451761901, -0.0742026994304908, -0.07178862616469217, -0.06941027885906886, -0.06706873848853018, -0.06476502245597342, -0.06250008429248773, -0.060274813464991174, -0.05809003529025402, -0.05594651095406543, -0.05384493763410617, -0.05178594872490621, -0.04977011416308022, -0.04779794085086154, -0.045869873175780895, -0.04398629362417595, -0.042147523486056965, -0.04035382364870621, -0.03860539547624284, -0.036902381772251115, -0.035244867822440476, -0.03363288251418613, -0.03206639952968556, -0.03054533860936408, -0.029069566882065148, -0.027638900258475006, -0.02625310488415248, -0.02491189864846489, -0.02361495274567049, -0.022361893284334952, -0.021152302941227122, -0.01998572265580402, -0.01886165336137006, -0.017779557748978606, -0.016738862060135817, -0.015738957904367704, -0.014779204097720553, -0.013858928518282288, -0.01297742997483901, -0.012133980084814523, -0.011327825157683425, -0.01055818808009791, -0.009824270199026397, -0.009125253199266853, -0.008460300971769847, -0.00782856146928552, -0.007229168545933867, -0.006661243777390181, -0.006123898258474957, -0.005616234375041648, -0.005137347547164467, -0.004686327940742911, -0.004262262144758445, -0.0038642348115421727, -0.003491330257539964, -0.003142634022192405, -0.0028172343826816846, -0.002514223822434906, -0.0022327004514135643, -0.001971769376361237, -0.0017305440193259045, -0.0015081473829191116, -0.0013037132609211657, -0.0011163873929892457, -0.0009453285623736057, -0.000789709635695163, -0.0006487185439857415, -0.0005215592043395318] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0] * 2,
        },
        "minus_x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 280,
        },
        "minus_x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "minus_x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "minus_x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "minus_x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "y180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 280,
        },
        "y180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "y180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "y180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "y180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "y180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0010431184086790637, 0.001297437087971483, 0.001579419271390326, 0.0018906571247472115, 0.0022327747859784914, 0.0026074265218423314, 0.0030162947658382232, 0.003461088038651809, 0.003943538752722474, 0.004465400902827129, 0.005028447644869812, 0.005634468765363369, 0.00628526804438481, 0.006982660515079928, 0.007728469623084345, 0.00852452428951689, 0.009372655881485822, 0.010274695094328934, 0.011232468750083296, 0.012247796516949913, 0.013322487554780361, 0.014458337091867734, 0.01565712293857104, 0.016920601943539695, 0.018250506398533706, 0.019648540398052795, 0.02111637616019582, 0.02265565031536685, 0.024267960169629045, 0.02595485994967802, 0.027717857036564576, 0.029558408195441106, 0.03147791580873541, 0.03347772412027163, 0.03555911549795721, 0.03772330672274012, 0.03997144531160804, 0.042304605882454244, 0.044723786568669904, 0.04722990549134098, 0.04982379729692978, 0.05250620976830496, 0.05527780051695001, 0.058139133764130296, 0.06109067721872816, 0.06413279905937112, 0.06726576502837225, 0.07048973564488095, 0.07380476354450223, 0.07721079095248568, 0.08070764729741242, 0.08429504697211393, 0.0879725872483519, 0.09173974635156179, 0.09559588170172308, 0.09954022832616044, 0.10357189744981242, 0.10768987526821235, 0.11189302190813086, 0.11618007058050804, 0.12054962692998235, 0.12500016858497545, 0.12953004491194683, 0.13413747697706035, 0.13882055771813773, 0.14357725232938434, 0.1484053988609816, 0.15330270903523802, 0.15826676928058409, 0.16329504198427403, 0.16838486696424743, 0.1735334631601626, 0.1787379305432009, 0.18399525224379068, 0.1893022968959787, 0.1946558211967324, 0.2000524726780225, 0.20548879268910147, 0.21096121958595615, 0.21646609212448611, 0.22199965305352734, 0.22755805290342507, 0.23313735396543173, 0.23873353445681147, 0.24434249286611068, 0.24996005247267947, 0.2555819660341269, 0.26120392063503095, 0.2668215426898536, 0.2724304030926589, 0.27802602250590464, 0.28360387678023474, 0.2891594024969082, 0.29468800262419026, 0.3001850522787632, 0.30564590458294194, 0.3110658966082452, 0.31644035539563287, 0.32176460404252344, 0.32703396784650657, 0.33224378049550174, 0.33738939029395826, 0.3424661664145676, 0.34746950516484454, 0.35239483625785073, 0.3572376290762628, 0.3619933989189455, 0.36665771321916907, 0.3712261977236015, 0.37569454262123525, 0.38005850861144863, 0.3843139329004605, 0.3884567351155389, 0.3924829231264168, 0.39638859876350385, 0.40016996342264993, 0.40382332354636, 0.4073450959715863, 0.4107318131344117, 0.41398012812219737, 0.4170868195639962, 0.4200487963503368, 0.42286310217374873, 0.42552691988172936, 0.42803757563417577, 0.43039254285763634, 0.4325894459891301, 0.4346260640026206, 0.43650033371165115, 0.4382103528420395, 0.4397543828689488, 0.4411308516130899, 0.4423383555912364, 0.44337566211670193, 0.44424171114587985, 0.4449356168674101, 0.44545666903102915, 0.44580433401362796] + [0.44597825562053467] * 2 + [0.44580433401362796, 0.44545666903102915, 0.4449356168674101, 0.44424171114587985, 0.44337566211670193, 0.4423383555912364, 0.4411308516130899, 0.4397543828689488, 0.4382103528420395, 0.43650033371165115, 0.4346260640026206, 0.4325894459891301, 0.43039254285763634, 0.42803757563417577, 0.42552691988172936, 0.42286310217374873, 0.4200487963503368, 0.4170868195639962, 0.41398012812219737, 0.4107318131344117, 0.4073450959715863, 0.40382332354636, 0.40016996342264993, 0.39638859876350385, 0.3924829231264168, 0.3884567351155389, 0.3843139329004605, 0.38005850861144863, 0.37569454262123525, 0.3712261977236015, 0.36665771321916907, 0.3619933989189455, 0.3572376290762628, 0.35239483625785073, 0.34746950516484454, 0.3424661664145676, 0.33738939029395826, 0.33224378049550174, 0.32703396784650657, 0.32176460404252344, 0.31644035539563287, 0.3110658966082452, 0.30564590458294194, 0.3001850522787632, 0.29468800262419026, 0.2891594024969082, 0.28360387678023474, 0.27802602250590464, 0.2724304030926589, 0.2668215426898536, 0.26120392063503095, 0.2555819660341269, 0.24996005247267947, 0.24434249286611068, 0.23873353445681147, 0.23313735396543173, 0.22755805290342507, 0.22199965305352734, 0.21646609212448611, 0.21096121958595615, 0.20548879268910147, 0.2000524726780225, 0.1946558211967324, 0.1893022968959787, 0.18399525224379068, 0.1787379305432009, 0.1735334631601626, 0.16838486696424743, 0.16329504198427403, 0.15826676928058409, 0.15330270903523802, 0.1484053988609816, 0.14357725232938434, 0.13882055771813773, 0.13413747697706035, 0.12953004491194683, 0.12500016858497545, 0.12054962692998235, 0.11618007058050804, 0.11189302190813086, 0.10768987526821235, 0.10357189744981242, 0.09954022832616044, 0.09559588170172308, 0.09173974635156179, 0.0879725872483519, 0.08429504697211393, 0.08070764729741242, 0.07721079095248568, 0.07380476354450223, 0.07048973564488095, 0.06726576502837225, 0.06413279905937112, 0.06109067721872816, 0.058139133764130296, 0.05527780051695001, 0.05250620976830496, 0.04982379729692978, 0.04722990549134098, 0.044723786568669904, 0.042304605882454244, 0.03997144531160804, 0.03772330672274012, 0.03555911549795721, 0.03347772412027163, 0.03147791580873541, 0.029558408195441106, 0.027717857036564576, 0.02595485994967802, 0.024267960169629045, 0.02265565031536685, 0.02111637616019582, 0.019648540398052795, 0.018250506398533706, 0.016920601943539695, 0.01565712293857104, 0.014458337091867734, 0.013322487554780361, 0.012247796516949913, 0.011232468750083296, 0.010274695094328934, 0.009372655881485822, 0.00852452428951689, 0.007728469623084345, 0.006982660515079928, 0.00628526804438481, 0.005634468765363369, 0.005028447644869812, 0.004465400902827129, 0.003943538752722474, 0.003461088038651809, 0.0030162947658382232, 0.0026074265218423314, 0.0022327747859784914, 0.0018906571247472115, 0.001579419271390326, 0.001297437087971483, 0.0010431184086790637] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0] * 2,
        },
        "y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 280,
        },
        "y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0005215592043395318, 0.0006487185439857415, 0.000789709635695163, 0.0009453285623736057, 0.0011163873929892457, 0.0013037132609211657, 0.0015081473829191116, 0.0017305440193259045, 0.001971769376361237, 0.0022327004514135643, 0.002514223822434906, 0.0028172343826816846, 0.003142634022192405, 0.003491330257539964, 0.0038642348115421727, 0.004262262144758445, 0.004686327940742911, 0.005137347547164467, 0.005616234375041648, 0.006123898258474957, 0.006661243777390181, 0.007229168545933867, 0.00782856146928552, 0.008460300971769847, 0.009125253199266853, 0.009824270199026397, 0.01055818808009791, 0.011327825157683425, 0.012133980084814523, 0.01297742997483901, 0.013858928518282288, 0.014779204097720553, 0.015738957904367704, 0.016738862060135817, 0.017779557748978606, 0.01886165336137006, 0.01998572265580402, 0.021152302941227122, 0.022361893284334952, 0.02361495274567049, 0.02491189864846489, 0.02625310488415248, 0.027638900258475006, 0.029069566882065148, 0.03054533860936408, 0.03206639952968556, 0.03363288251418613, 0.035244867822440476, 0.036902381772251115, 0.03860539547624284, 0.04035382364870621, 0.042147523486056965, 0.04398629362417595, 0.045869873175780895, 0.04779794085086154, 0.04977011416308022, 0.05178594872490621, 0.05384493763410617, 0.05594651095406543, 0.05809003529025402, 0.060274813464991174, 0.06250008429248773, 0.06476502245597342, 0.06706873848853018, 0.06941027885906886, 0.07178862616469217, 0.0742026994304908, 0.07665135451761901, 0.07913338464029204, 0.08164752099213701, 0.08419243348212371, 0.0867667315800813, 0.08936896527160045, 0.09199762612189534, 0.09465114844798934, 0.0973279105983662, 0.10002623633901125, 0.10274439634455074, 0.10548060979297808, 0.10823304606224306, 0.11099982652676367, 0.11377902645171253, 0.11656867698271586, 0.11936676722840574, 0.12217124643305534, 0.12498002623633973, 0.12779098301706346, 0.13060196031751548, 0.1334107713449268, 0.13621520154632946, 0.13901301125295232, 0.14180193839011737, 0.1445797012484541, 0.14734400131209513, 0.1500925261393816, 0.15282295229147097, 0.1555329483041226, 0.15822017769781643, 0.16088230202126172, 0.16351698392325328, 0.16612189024775087, 0.16869469514697913, 0.1712330832072838, 0.17373475258242227, 0.17619741812892536, 0.1786188145381314, 0.18099669945947275, 0.18332885660958453, 0.18561309886180075, 0.18784727131061763, 0.19002925430572432, 0.19215696645023025, 0.19422836755776945, 0.1962414615632084, 0.19819429938175193, 0.20008498171132497, 0.20191166177318, 0.20367254798579315, 0.20536590656720585, 0.20699006406109868, 0.2085434097819981, 0.2100243981751684, 0.21143155108687436, 0.21276345994086468, 0.21401878781708789, 0.21519627142881817, 0.21629472299456504, 0.2173130320013103, 0.21825016685582557, 0.21910517642101976, 0.2198771914344744, 0.22056542580654495, 0.2211691777956182, 0.22168783105835096, 0.22212085557293992, 0.22246780843370506, 0.22272833451551458, 0.22290216700681398] + [0.22298912781026733] * 2 + [0.22290216700681398, 0.22272833451551458, 0.22246780843370506, 0.22212085557293992, 0.22168783105835096, 0.2211691777956182, 0.22056542580654495, 0.2198771914344744, 0.21910517642101976, 0.21825016685582557, 0.2173130320013103, 0.21629472299456504, 0.21519627142881817, 0.21401878781708789, 0.21276345994086468, 0.21143155108687436, 0.2100243981751684, 0.2085434097819981, 0.20699006406109868, 0.20536590656720585, 0.20367254798579315, 0.20191166177318, 0.20008498171132497, 0.19819429938175193, 0.1962414615632084, 0.19422836755776945, 0.19215696645023025, 0.19002925430572432, 0.18784727131061763, 0.18561309886180075, 0.18332885660958453, 0.18099669945947275, 0.1786188145381314, 0.17619741812892536, 0.17373475258242227, 0.1712330832072838, 0.16869469514697913, 0.16612189024775087, 0.16351698392325328, 0.16088230202126172, 0.15822017769781643, 0.1555329483041226, 0.15282295229147097, 0.1500925261393816, 0.14734400131209513, 0.1445797012484541, 0.14180193839011737, 0.13901301125295232, 0.13621520154632946, 0.1334107713449268, 0.13060196031751548, 0.12779098301706346, 0.12498002623633973, 0.12217124643305534, 0.11936676722840574, 0.11656867698271586, 0.11377902645171253, 0.11099982652676367, 0.10823304606224306, 0.10548060979297808, 0.10274439634455074, 0.10002623633901125, 0.0973279105983662, 0.09465114844798934, 0.09199762612189534, 0.08936896527160045, 0.0867667315800813, 0.08419243348212371, 0.08164752099213701, 0.07913338464029204, 0.07665135451761901, 0.0742026994304908, 0.07178862616469217, 0.06941027885906886, 0.06706873848853018, 0.06476502245597342, 0.06250008429248773, 0.060274813464991174, 0.05809003529025402, 0.05594651095406543, 0.05384493763410617, 0.05178594872490621, 0.04977011416308022, 0.04779794085086154, 0.045869873175780895, 0.04398629362417595, 0.042147523486056965, 0.04035382364870621, 0.03860539547624284, 0.036902381772251115, 0.035244867822440476, 0.03363288251418613, 0.03206639952968556, 0.03054533860936408, 0.029069566882065148, 0.027638900258475006, 0.02625310488415248, 0.02491189864846489, 0.02361495274567049, 0.022361893284334952, 0.021152302941227122, 0.01998572265580402, 0.01886165336137006, 0.017779557748978606, 0.016738862060135817, 0.015738957904367704, 0.014779204097720553, 0.013858928518282288, 0.01297742997483901, 0.012133980084814523, 0.011327825157683425, 0.01055818808009791, 0.009824270199026397, 0.009125253199266853, 0.008460300971769847, 0.00782856146928552, 0.007229168545933867, 0.006661243777390181, 0.006123898258474957, 0.005616234375041648, 0.005137347547164467, 0.004686327940742911, 0.004262262144758445, 0.0038642348115421727, 0.003491330257539964, 0.003142634022192405, 0.0028172343826816846, 0.002514223822434906, 0.0022327004514135643, 0.001971769376361237, 0.0017305440193259045, 0.0015081473829191116, 0.0013037132609211657, 0.0011163873929892457, 0.0009453285623736057, 0.000789709635695163, 0.0006487185439857415, 0.0005215592043395318] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0] * 2,
        },
        "minus_y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 280,
        },
        "minus_y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "minus_y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "minus_y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "minus_y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 160,
        },
        "minus_y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0005215592043395318, -0.0006487185439857415, -0.000789709635695163, -0.0009453285623736057, -0.0011163873929892457, -0.0013037132609211657, -0.0015081473829191116, -0.0017305440193259045, -0.001971769376361237, -0.0022327004514135643, -0.002514223822434906, -0.0028172343826816846, -0.003142634022192405, -0.003491330257539964, -0.0038642348115421727, -0.004262262144758445, -0.004686327940742911, -0.005137347547164467, -0.005616234375041648, -0.006123898258474957, -0.006661243777390181, -0.007229168545933867, -0.00782856146928552, -0.008460300971769847, -0.009125253199266853, -0.009824270199026397, -0.01055818808009791, -0.011327825157683425, -0.012133980084814523, -0.01297742997483901, -0.013858928518282288, -0.014779204097720553, -0.015738957904367704, -0.016738862060135817, -0.017779557748978606, -0.01886165336137006, -0.01998572265580402, -0.021152302941227122, -0.022361893284334952, -0.02361495274567049, -0.02491189864846489, -0.02625310488415248, -0.027638900258475006, -0.029069566882065148, -0.03054533860936408, -0.03206639952968556, -0.03363288251418613, -0.035244867822440476, -0.036902381772251115, -0.03860539547624284, -0.04035382364870621, -0.042147523486056965, -0.04398629362417595, -0.045869873175780895, -0.04779794085086154, -0.04977011416308022, -0.05178594872490621, -0.05384493763410617, -0.05594651095406543, -0.05809003529025402, -0.060274813464991174, -0.06250008429248773, -0.06476502245597342, -0.06706873848853018, -0.06941027885906886, -0.07178862616469217, -0.0742026994304908, -0.07665135451761901, -0.07913338464029204, -0.08164752099213701, -0.08419243348212371, -0.0867667315800813, -0.08936896527160045, -0.09199762612189534, -0.09465114844798934, -0.0973279105983662, -0.10002623633901125, -0.10274439634455074, -0.10548060979297808, -0.10823304606224306, -0.11099982652676367, -0.11377902645171253, -0.11656867698271586, -0.11936676722840574, -0.12217124643305534, -0.12498002623633973, -0.12779098301706346, -0.13060196031751548, -0.1334107713449268, -0.13621520154632946, -0.13901301125295232, -0.14180193839011737, -0.1445797012484541, -0.14734400131209513, -0.1500925261393816, -0.15282295229147097, -0.1555329483041226, -0.15822017769781643, -0.16088230202126172, -0.16351698392325328, -0.16612189024775087, -0.16869469514697913, -0.1712330832072838, -0.17373475258242227, -0.17619741812892536, -0.1786188145381314, -0.18099669945947275, -0.18332885660958453, -0.18561309886180075, -0.18784727131061763, -0.19002925430572432, -0.19215696645023025, -0.19422836755776945, -0.1962414615632084, -0.19819429938175193, -0.20008498171132497, -0.20191166177318, -0.20367254798579315, -0.20536590656720585, -0.20699006406109868, -0.2085434097819981, -0.2100243981751684, -0.21143155108687436, -0.21276345994086468, -0.21401878781708789, -0.21519627142881817, -0.21629472299456504, -0.2173130320013103, -0.21825016685582557, -0.21910517642101976, -0.2198771914344744, -0.22056542580654495, -0.2211691777956182, -0.22168783105835096, -0.22212085557293992, -0.22246780843370506, -0.22272833451551458, -0.22290216700681398] + [-0.22298912781026733] * 2 + [-0.22290216700681398, -0.22272833451551458, -0.22246780843370506, -0.22212085557293992, -0.22168783105835096, -0.2211691777956182, -0.22056542580654495, -0.2198771914344744, -0.21910517642101976, -0.21825016685582557, -0.2173130320013103, -0.21629472299456504, -0.21519627142881817, -0.21401878781708789, -0.21276345994086468, -0.21143155108687436, -0.2100243981751684, -0.2085434097819981, -0.20699006406109868, -0.20536590656720585, -0.20367254798579315, -0.20191166177318, -0.20008498171132497, -0.19819429938175193, -0.1962414615632084, -0.19422836755776945, -0.19215696645023025, -0.19002925430572432, -0.18784727131061763, -0.18561309886180075, -0.18332885660958453, -0.18099669945947275, -0.1786188145381314, -0.17619741812892536, -0.17373475258242227, -0.1712330832072838, -0.16869469514697913, -0.16612189024775087, -0.16351698392325328, -0.16088230202126172, -0.15822017769781643, -0.1555329483041226, -0.15282295229147097, -0.1500925261393816, -0.14734400131209513, -0.1445797012484541, -0.14180193839011737, -0.13901301125295232, -0.13621520154632946, -0.1334107713449268, -0.13060196031751548, -0.12779098301706346, -0.12498002623633973, -0.12217124643305534, -0.11936676722840574, -0.11656867698271586, -0.11377902645171253, -0.11099982652676367, -0.10823304606224306, -0.10548060979297808, -0.10274439634455074, -0.10002623633901125, -0.0973279105983662, -0.09465114844798934, -0.09199762612189534, -0.08936896527160045, -0.0867667315800813, -0.08419243348212371, -0.08164752099213701, -0.07913338464029204, -0.07665135451761901, -0.0742026994304908, -0.07178862616469217, -0.06941027885906886, -0.06706873848853018, -0.06476502245597342, -0.06250008429248773, -0.060274813464991174, -0.05809003529025402, -0.05594651095406543, -0.05384493763410617, -0.05178594872490621, -0.04977011416308022, -0.04779794085086154, -0.045869873175780895, -0.04398629362417595, -0.042147523486056965, -0.04035382364870621, -0.03860539547624284, -0.036902381772251115, -0.035244867822440476, -0.03363288251418613, -0.03206639952968556, -0.03054533860936408, -0.029069566882065148, -0.027638900258475006, -0.02625310488415248, -0.02491189864846489, -0.02361495274567049, -0.022361893284334952, -0.021152302941227122, -0.01998572265580402, -0.01886165336137006, -0.017779557748978606, -0.016738862060135817, -0.015738957904367704, -0.014779204097720553, -0.013858928518282288, -0.01297742997483901, -0.012133980084814523, -0.011327825157683425, -0.01055818808009791, -0.009824270199026397, -0.009125253199266853, -0.008460300971769847, -0.00782856146928552, -0.007229168545933867, -0.006661243777390181, -0.006123898258474957, -0.005616234375041648, -0.005137347547164467, -0.004686327940742911, -0.004262262144758445, -0.0038642348115421727, -0.003491330257539964, -0.003142634022192405, -0.0028172343826816846, -0.002514223822434906, -0.0022327004514135643, -0.001971769376361237, -0.0017305440193259045, -0.0015081473829191116, -0.0013037132609211657, -0.0011163873929892457, -0.0009453285623736057, -0.000789709635695163, -0.0006487185439857415, -0.0005215592043395318] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0] * 2,
        },
        "x180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0002338830512733327, 0.00041342331414452246, 0.0006490265520840418, 0.0009494369385097077, 0.001323762479540643, 0.0017813737759764942, 0.002331789745408628, 0.0029845514206982594, 0.003749085223982172, 0.004634557384785197, 0.005649721420867429, 0.00680276082544743, 0.008101129299073374, 0.009551391023757079, 0.01115906359668726, 0.012928466317204117, 0.014862576550802174, 0.016962896875620838, 0.019229335648960667, 0.02166010351355131, 0.024251628196283764, 0.026998489737573544, 0.02989337803007294, 0.03292707424467024, 0.036088457384046375, 0.03936453683476643, 0.04274051139394752, 0.04619985483256559, 0.049724427631539454, 0.05329461409633044, 0.05688948362860888, 0.06048697451734078, 0.06406409821413954, 0.06759716168638136, 0.07106200510351443, 0.07443425181377886, 0.07768956731614689, 0.08080392373085002, 0.08375386612567143, 0.0865167769675525, 0.08907113494225635, 0.09139676442001228, 0.09347507194224823, 0.0952892662626041, 0.0968245586921427, 0.09806834077071391, 0.09901033660938849, 0.09964272761743759] + [0.09996024773528736] * 2 + [0.09964272761743759, 0.09901033660938849, 0.09806834077071391, 0.0968245586921427, 0.0952892662626041, 0.09347507194224823, 0.09139676442001228, 0.08907113494225635, 0.0865167769675525, 0.08375386612567143, 0.08080392373085002, 0.07768956731614689, 0.07443425181377886, 0.07106200510351443, 0.06759716168638136, 0.06406409821413954, 0.06048697451734078, 0.05688948362860888, 0.05329461409633044, 0.049724427631539454, 0.04619985483256559, 0.04274051139394752, 0.03936453683476643, 0.036088457384046375, 0.03292707424467024, 0.02989337803007294, 0.026998489737573544, 0.024251628196283764, 0.02166010351355131, 0.019229335648960667, 0.016962896875620838, 0.014862576550802174, 0.012928466317204117, 0.01115906359668726, 0.009551391023757079, 0.008101129299073374, 0.00680276082544743, 0.005649721420867429, 0.004634557384785197, 0.003749085223982172, 0.0029845514206982594, 0.002331789745408628, 0.0017813737759764942, 0.001323762479540643, 0.0009494369385097077, 0.0006490265520840418, 0.00041342331414452246, 0.0002338830512733327] + [0] * 2,
        },
        "x180_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.00011694152563666635, 0.00020671165707226123, 0.0003245132760420209, 0.00047471846925485384, 0.0006618812397703215, 0.0008906868879882471, 0.001165894872704314, 0.0014922757103491297, 0.001874542611991086, 0.0023172786923925984, 0.0028248607104337147, 0.003401380412723715, 0.004050564649536687, 0.0047756955118785395, 0.00557953179834363, 0.006464233158602058, 0.007431288275401087, 0.008481448437810419, 0.009614667824480333, 0.010830051756775655, 0.012125814098141882, 0.013499244868786772, 0.01494668901503647, 0.01646353712233512, 0.018044228692023188, 0.019682268417383214, 0.02137025569697376, 0.023099927416282796, 0.024862213815769727, 0.02664730704816522, 0.02844474181430444, 0.03024348725867039, 0.03203204910706977, 0.03379858084319068, 0.035531002551757215, 0.03721712590688943, 0.038844783658073444, 0.04040196186542501, 0.041876933062835714, 0.04325838848377625, 0.044535567471128176, 0.04569838221000614, 0.046737535971124115, 0.04764463313130205, 0.04841227934607135, 0.04903417038535696, 0.049505168304694244, 0.049821363808718794] + [0.04998012386764368] * 2 + [0.049821363808718794, 0.049505168304694244, 0.04903417038535696, 0.04841227934607135, 0.04764463313130205, 0.046737535971124115, 0.04569838221000614, 0.044535567471128176, 0.04325838848377625, 0.041876933062835714, 0.04040196186542501, 0.038844783658073444, 0.03721712590688943, 0.035531002551757215, 0.03379858084319068, 0.03203204910706977, 0.03024348725867039, 0.02844474181430444, 0.02664730704816522, 0.024862213815769727, 0.023099927416282796, 0.02137025569697376, 0.019682268417383214, 0.018044228692023188, 0.01646353712233512, 0.01494668901503647, 0.013499244868786772, 0.012125814098141882, 0.010830051756775655, 0.009614667824480333, 0.008481448437810419, 0.007431288275401087, 0.006464233158602058, 0.00557953179834363, 0.0047756955118785395, 0.004050564649536687, 0.003401380412723715, 0.0028248607104337147, 0.0023172786923925984, 0.001874542611991086, 0.0014922757103491297, 0.001165894872704314, 0.0008906868879882471, 0.0006618812397703215, 0.00047471846925485384, 0.0003245132760420209, 0.00020671165707226123, 0.00011694152563666635] + [0] * 2,
        },
        "x90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "minus_x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.00011694152563666635, -0.00020671165707226123, -0.0003245132760420209, -0.00047471846925485384, -0.0006618812397703215, -0.0008906868879882471, -0.001165894872704314, -0.0014922757103491297, -0.001874542611991086, -0.0023172786923925984, -0.0028248607104337147, -0.003401380412723715, -0.004050564649536687, -0.0047756955118785395, -0.00557953179834363, -0.006464233158602058, -0.007431288275401087, -0.008481448437810419, -0.009614667824480333, -0.010830051756775655, -0.012125814098141882, -0.013499244868786772, -0.01494668901503647, -0.01646353712233512, -0.018044228692023188, -0.019682268417383214, -0.02137025569697376, -0.023099927416282796, -0.024862213815769727, -0.02664730704816522, -0.02844474181430444, -0.03024348725867039, -0.03203204910706977, -0.03379858084319068, -0.035531002551757215, -0.03721712590688943, -0.038844783658073444, -0.04040196186542501, -0.041876933062835714, -0.04325838848377625, -0.044535567471128176, -0.04569838221000614, -0.046737535971124115, -0.04764463313130205, -0.04841227934607135, -0.04903417038535696, -0.049505168304694244, -0.049821363808718794] + [-0.04998012386764368] * 2 + [-0.049821363808718794, -0.049505168304694244, -0.04903417038535696, -0.04841227934607135, -0.04764463313130205, -0.046737535971124115, -0.04569838221000614, -0.044535567471128176, -0.04325838848377625, -0.041876933062835714, -0.04040196186542501, -0.038844783658073444, -0.03721712590688943, -0.035531002551757215, -0.03379858084319068, -0.03203204910706977, -0.03024348725867039, -0.02844474181430444, -0.02664730704816522, -0.024862213815769727, -0.023099927416282796, -0.02137025569697376, -0.019682268417383214, -0.018044228692023188, -0.01646353712233512, -0.01494668901503647, -0.013499244868786772, -0.012125814098141882, -0.010830051756775655, -0.009614667824480333, -0.008481448437810419, -0.007431288275401087, -0.006464233158602058, -0.00557953179834363, -0.0047756955118785395, -0.004050564649536687, -0.003401380412723715, -0.0028248607104337147, -0.0023172786923925984, -0.001874542611991086, -0.0014922757103491297, -0.001165894872704314, -0.0008906868879882471, -0.0006618812397703215, -0.00047471846925485384, -0.0003245132760420209, -0.00020671165707226123, -0.00011694152563666635] + [0] * 2,
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
            "samples": [0.0002338830512733327, 0.00041342331414452246, 0.0006490265520840418, 0.0009494369385097077, 0.001323762479540643, 0.0017813737759764942, 0.002331789745408628, 0.0029845514206982594, 0.003749085223982172, 0.004634557384785197, 0.005649721420867429, 0.00680276082544743, 0.008101129299073374, 0.009551391023757079, 0.01115906359668726, 0.012928466317204117, 0.014862576550802174, 0.016962896875620838, 0.019229335648960667, 0.02166010351355131, 0.024251628196283764, 0.026998489737573544, 0.02989337803007294, 0.03292707424467024, 0.036088457384046375, 0.03936453683476643, 0.04274051139394752, 0.04619985483256559, 0.049724427631539454, 0.05329461409633044, 0.05688948362860888, 0.06048697451734078, 0.06406409821413954, 0.06759716168638136, 0.07106200510351443, 0.07443425181377886, 0.07768956731614689, 0.08080392373085002, 0.08375386612567143, 0.0865167769675525, 0.08907113494225635, 0.09139676442001228, 0.09347507194224823, 0.0952892662626041, 0.0968245586921427, 0.09806834077071391, 0.09901033660938849, 0.09964272761743759] + [0.09996024773528736] * 2 + [0.09964272761743759, 0.09901033660938849, 0.09806834077071391, 0.0968245586921427, 0.0952892662626041, 0.09347507194224823, 0.09139676442001228, 0.08907113494225635, 0.0865167769675525, 0.08375386612567143, 0.08080392373085002, 0.07768956731614689, 0.07443425181377886, 0.07106200510351443, 0.06759716168638136, 0.06406409821413954, 0.06048697451734078, 0.05688948362860888, 0.05329461409633044, 0.049724427631539454, 0.04619985483256559, 0.04274051139394752, 0.03936453683476643, 0.036088457384046375, 0.03292707424467024, 0.02989337803007294, 0.026998489737573544, 0.024251628196283764, 0.02166010351355131, 0.019229335648960667, 0.016962896875620838, 0.014862576550802174, 0.012928466317204117, 0.01115906359668726, 0.009551391023757079, 0.008101129299073374, 0.00680276082544743, 0.005649721420867429, 0.004634557384785197, 0.003749085223982172, 0.0029845514206982594, 0.002331789745408628, 0.0017813737759764942, 0.001323762479540643, 0.0009494369385097077, 0.0006490265520840418, 0.00041342331414452246, 0.0002338830512733327] + [0] * 2,
        },
        "y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.00011694152563666635, 0.00020671165707226123, 0.0003245132760420209, 0.00047471846925485384, 0.0006618812397703215, 0.0008906868879882471, 0.001165894872704314, 0.0014922757103491297, 0.001874542611991086, 0.0023172786923925984, 0.0028248607104337147, 0.003401380412723715, 0.004050564649536687, 0.0047756955118785395, 0.00557953179834363, 0.006464233158602058, 0.007431288275401087, 0.008481448437810419, 0.009614667824480333, 0.010830051756775655, 0.012125814098141882, 0.013499244868786772, 0.01494668901503647, 0.01646353712233512, 0.018044228692023188, 0.019682268417383214, 0.02137025569697376, 0.023099927416282796, 0.024862213815769727, 0.02664730704816522, 0.02844474181430444, 0.03024348725867039, 0.03203204910706977, 0.03379858084319068, 0.035531002551757215, 0.03721712590688943, 0.038844783658073444, 0.04040196186542501, 0.041876933062835714, 0.04325838848377625, 0.044535567471128176, 0.04569838221000614, 0.046737535971124115, 0.04764463313130205, 0.04841227934607135, 0.04903417038535696, 0.049505168304694244, 0.049821363808718794] + [0.04998012386764368] * 2 + [0.049821363808718794, 0.049505168304694244, 0.04903417038535696, 0.04841227934607135, 0.04764463313130205, 0.046737535971124115, 0.04569838221000614, 0.044535567471128176, 0.04325838848377625, 0.041876933062835714, 0.04040196186542501, 0.038844783658073444, 0.03721712590688943, 0.035531002551757215, 0.03379858084319068, 0.03203204910706977, 0.03024348725867039, 0.02844474181430444, 0.02664730704816522, 0.024862213815769727, 0.023099927416282796, 0.02137025569697376, 0.019682268417383214, 0.018044228692023188, 0.01646353712233512, 0.01494668901503647, 0.013499244868786772, 0.012125814098141882, 0.010830051756775655, 0.009614667824480333, 0.008481448437810419, 0.007431288275401087, 0.006464233158602058, 0.00557953179834363, 0.0047756955118785395, 0.004050564649536687, 0.003401380412723715, 0.0028248607104337147, 0.0023172786923925984, 0.001874542611991086, 0.0014922757103491297, 0.001165894872704314, 0.0008906868879882471, 0.0006618812397703215, 0.00047471846925485384, 0.0003245132760420209, 0.00020671165707226123, 0.00011694152563666635] + [0] * 2,
        },
        "minus_y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "minus_y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.00011694152563666635, -0.00020671165707226123, -0.0003245132760420209, -0.00047471846925485384, -0.0006618812397703215, -0.0008906868879882471, -0.001165894872704314, -0.0014922757103491297, -0.001874542611991086, -0.0023172786923925984, -0.0028248607104337147, -0.003401380412723715, -0.004050564649536687, -0.0047756955118785395, -0.00557953179834363, -0.006464233158602058, -0.007431288275401087, -0.008481448437810419, -0.009614667824480333, -0.010830051756775655, -0.012125814098141882, -0.013499244868786772, -0.01494668901503647, -0.01646353712233512, -0.018044228692023188, -0.019682268417383214, -0.02137025569697376, -0.023099927416282796, -0.024862213815769727, -0.02664730704816522, -0.02844474181430444, -0.03024348725867039, -0.03203204910706977, -0.03379858084319068, -0.035531002551757215, -0.03721712590688943, -0.038844783658073444, -0.04040196186542501, -0.041876933062835714, -0.04325838848377625, -0.044535567471128176, -0.04569838221000614, -0.046737535971124115, -0.04764463313130205, -0.04841227934607135, -0.04903417038535696, -0.049505168304694244, -0.049821363808718794] + [-0.04998012386764368] * 2 + [-0.049821363808718794, -0.049505168304694244, -0.04903417038535696, -0.04841227934607135, -0.04764463313130205, -0.046737535971124115, -0.04569838221000614, -0.044535567471128176, -0.04325838848377625, -0.041876933062835714, -0.04040196186542501, -0.038844783658073444, -0.03721712590688943, -0.035531002551757215, -0.03379858084319068, -0.03203204910706977, -0.03024348725867039, -0.02844474181430444, -0.02664730704816522, -0.024862213815769727, -0.023099927416282796, -0.02137025569697376, -0.019682268417383214, -0.018044228692023188, -0.01646353712233512, -0.01494668901503647, -0.013499244868786772, -0.012125814098141882, -0.010830051756775655, -0.009614667824480333, -0.008481448437810419, -0.007431288275401087, -0.006464233158602058, -0.00557953179834363, -0.0047756955118785395, -0.004050564649536687, -0.003401380412723715, -0.0028248607104337147, -0.0023172786923925984, -0.001874542611991086, -0.0014922757103491297, -0.001165894872704314, -0.0008906868879882471, -0.0006618812397703215, -0.00047471846925485384, -0.0003245132760420209, -0.00020671165707226123, -0.00011694152563666635] + [0] * 2,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_tank_circuit1": {
            "cosine": [(1.0, 20000)],
            "sine": [(0.0, 20000)],
        },
        "cosine_weights_tank_circuit2": {
            "cosine": [(1.0, 20000)],
            "sine": [(0.0, 20000)],
        },
        "sine_weights_tank_circuit1": {
            "cosine": [(0.0, 20000)],
            "sine": [(1.0, 20000)],
        },
        "sine_weights_tank_circuit2": {
            "cosine": [(0.0, 20000)],
            "sine": [(1.0, 20000)],
        },
    },
    "mixers": {
        "mixer_qubit1": [{'intermediate_frequency': 0, 'lo_frequency': 16000000000, 'correction': [1.0647488615985707, 0.21694400550069723, 0.21694400550069723, 1.0647488615985707]}],
        "mixer_qubit2": [{'intermediate_frequency': 0, 'lo_frequency': 16000000000, 'correction': [-0.22296795843987155, -1.0681012427764622, -1.0681012427764622, -0.22296795843987155]}],
        "mixer_qubit3": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qubit4": [{'intermediate_frequency': 50000000, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
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
                        "7": {
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
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {
                        "1": {
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
                            "output_mode": "direct",
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
                            "output_mode": "direct",
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
                            "output_mode": "direct",
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
                            "output_mode": "direct",
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
                            "output_mode": "direct",
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
                            "output_mode": "direct",
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
                            "output_mode": "direct",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "analog_inputs": {
                        "2": {
                            "offset": -0.007773877929687499,
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "P0": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P0_step_pulse",
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
                "port": ('con1', 3, 3),
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
                "port": ('con1', 3, 5),
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
                "port": ('con1', 3, 7),
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
                "port": ('con1', 3, 1),
            },
        },
        "P0_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P0_step_pulse",
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
                "port": ('con1', 3, 3),
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
                "port": ('con1', 3, 5),
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
                "port": ('con1', 3, 7),
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
                "port": ('con1', 3, 1),
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
                "port": ('con1', 3, 2),
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
                "port": ('con1', 3, 4),
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
                "port": ('con1', 3, 8),
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
                "port": ('con1', 3, 2),
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
                "port": ('con1', 3, 4),
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
                "port": ('con1', 3, 8),
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
                "port": ('con1', 3, 2),
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
                "port": ('con1', 3, 3),
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
                "port": ('con1', 3, 2),
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
                "port": ('con1', 3, 3),
            },
        },
        "qubit1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit1",
                "x90_square": "square_x90_pulse_qubit1",
                "-x90_square": "square_minus_x90_pulse_qubit1",
                "y180_square": "square_y180_pulse_qubit1",
                "y90_square": "square_y90_pulse_qubit1",
                "-y90_square": "square_minus_y90_pulse_qubit1",
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
                "mixer": "mixer_qubit1",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit2",
                "x90_square": "square_x90_pulse_qubit2",
                "-x90_square": "square_minus_x90_pulse_qubit2",
                "y180_square": "square_y180_pulse_qubit2",
                "y90_square": "square_y90_pulse_qubit2",
                "-y90_square": "square_minus_y90_pulse_qubit2",
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
                "mixer": "mixer_qubit2",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit3",
                "x90_square": "square_x90_pulse_qubit3",
                "-x90_square": "square_minus_x90_pulse_qubit3",
                "y180_square": "square_y180_pulse_qubit3",
                "y90_square": "square_y90_pulse_qubit3",
                "-y90_square": "square_minus_y90_pulse_qubit3",
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
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit4",
                "x90_square": "square_x90_pulse_qubit4",
                "-x90_square": "square_minus_x90_pulse_qubit4",
                "y180_square": "square_y180_pulse_qubit4",
                "y90_square": "square_y90_pulse_qubit4",
                "-y90_square": "square_minus_y90_pulse_qubit4",
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
            "intermediate_frequency": 50000000.0,
        },
        "qubit5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_qubit5",
                "x90_square": "square_x90_pulse_qubit5",
                "-x90_square": "square_minus_x90_pulse_qubit5",
                "y180_square": "square_y180_pulse_qubit5",
                "y90_square": "square_y90_pulse_qubit5",
                "-y90_square": "square_minus_y90_pulse_qubit5",
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
        "qubit1_dup1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
                "mixer": "mixer_qubit1",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit2_dup1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
                "mixer": "mixer_qubit2",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit3_dup1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
        "qubit4_dup1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
            "intermediate_frequency": 50000000.0,
        },
        "qubit5_dup1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
        "qubit1_dup2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
                "mixer": "mixer_qubit1",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit2_dup2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
                "mixer": "mixer_qubit2",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit3_dup2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
        "qubit4_dup2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
            "intermediate_frequency": 50000000.0,
        },
        "qubit5_dup2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
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
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
            "digitalInputs": {},
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
        "rf_switch": {
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
            "singleInput": {
                "port": ('con1', 5, 1),
            },
        },
        "tank_circuit1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 3, 2),
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
                "port": ('con1', 3, 8),
            },
            "smearing": 0,
            "time_of_flight": 204,
            "intermediate_frequency": 181020000.0,
        },
        "tank_circuit2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 3, 2),
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
                "port": ('con1', 3, 8),
            },
            "smearing": 0,
            "time_of_flight": 204,
            "intermediate_frequency": 139534000.0,
        },
    },
    "pulses": {
        "P0_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P0_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
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
            "length": 280,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit1",
                "Q": "x180_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit2",
                "Q": "x180_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit3",
                "Q": "x180_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit4",
                "Q": "x180_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit5",
                "Q": "x180_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit1",
                "Q": "x90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit2",
                "Q": "x90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit3",
                "Q": "x90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit4",
                "Q": "x90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit5",
                "Q": "x90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit1",
                "Q": "minus_x90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit2",
                "Q": "minus_x90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit3",
                "Q": "minus_x90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit4",
                "Q": "minus_x90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit5",
                "Q": "minus_x90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit1",
                "Q": "y180_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit2",
                "Q": "y180_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit3",
                "Q": "y180_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit4",
                "Q": "y180_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit5",
                "Q": "y180_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit1",
                "Q": "y90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit2",
                "Q": "y90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit3",
                "Q": "y90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit4",
                "Q": "y90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit5",
                "Q": "y90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit1",
                "Q": "minus_y90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit2",
                "Q": "minus_y90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit3",
                "Q": "minus_y90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit4",
                "Q": "minus_y90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit5",
                "Q": "minus_y90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit1",
                "Q": "x180_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit2",
                "Q": "x180_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit3",
                "Q": "x180_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit4",
                "Q": "x180_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit5",
                "Q": "x180_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit1",
                "Q": "x90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit2",
                "Q": "x90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit3",
                "Q": "x90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit4",
                "Q": "x90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit5",
                "Q": "x90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit1",
                "Q": "minus_x90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit2",
                "Q": "minus_x90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit3",
                "Q": "minus_x90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit4",
                "Q": "minus_x90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit5",
                "Q": "minus_x90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit1",
                "Q": "y180_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit2",
                "Q": "y180_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit3",
                "Q": "y180_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit4",
                "Q": "y180_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit5",
                "Q": "y180_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit1",
                "Q": "y90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit2",
                "Q": "y90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit3",
                "Q": "y90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit4",
                "Q": "y90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit5",
                "Q": "y90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit1": {
            "length": 280,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit1",
                "Q": "minus_y90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit2": {
            "length": 160,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit2",
                "Q": "minus_y90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit3",
                "Q": "minus_y90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit4",
                "Q": "minus_y90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit5": {
            "length": 160,
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
            "length": 20000,
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
            "length": 20000,
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
            "length": 320,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "saturation_pulse": {
            "length": 10000,
            "waveforms": {
                "I": "saturation_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_qubit1": {
            "length": 248,
            "waveforms": {
                "I": "square_x180_I_wf_qubit1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_qubit2": {
            "length": 248,
            "waveforms": {
                "I": "square_x180_I_wf_qubit2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "square_x180_I_wf_qubit3",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "square_x180_I_wf_qubit4",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "square_x180_I_wf_qubit5",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_qubit1": {
            "length": 248,
            "waveforms": {
                "I": "square_x90_I_wf_qubit1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_qubit2": {
            "length": 248,
            "waveforms": {
                "I": "square_x90_I_wf_qubit2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "square_x90_I_wf_qubit3",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "square_x90_I_wf_qubit4",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "square_x90_I_wf_qubit5",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_qubit1": {
            "length": 248,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_qubit2": {
            "length": 248,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit3",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit4",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "square_minus_x90_I_wf_qubit5",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_qubit1": {
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_qubit2": {
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_qubit1": {
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_qubit2": {
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_qubit1": {
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_qubit2": {
            "length": 248,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_qubit3": {
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_qubit4": {
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_qubit5": {
            "length": 160,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "square_x180_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "square_x90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "square_minus_x90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y180_I_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_y90_I_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "zero_wf",
                "Q": "square_minus_y90_I_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_dup1": {
            "length": 1000,
            "waveforms": {
                "I": "square_x180_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_dup1": {
            "length": 1000,
            "waveforms": {
                "I": "square_x90_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_dup1": {
            "length": 1000,
            "waveforms": {
                "I": "square_minus_x90_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_dup1": {
            "length": 1000,
            "waveforms": {
                "I": "square_y180_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_dup1": {
            "length": 1000,
            "waveforms": {
                "I": "square_y90_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_dup1": {
            "length": 1000,
            "waveforms": {
                "I": "square_minus_y90_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_dup2": {
            "length": 1000,
            "waveforms": {
                "I": "square_x180_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_dup2": {
            "length": 1000,
            "waveforms": {
                "I": "square_x90_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_dup2": {
            "length": 1000,
            "waveforms": {
                "I": "square_minus_x90_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_dup2": {
            "length": 1000,
            "waveforms": {
                "I": "square_y180_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_dup2": {
            "length": 1000,
            "waveforms": {
                "I": "square_y90_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_dup2": {
            "length": 1000,
            "waveforms": {
                "I": "square_minus_y90_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "trigger_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "zero_wf",
            },
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
            "sample": 0.3,
        },
        "saturation_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_x180_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.30671] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x180_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.1579536] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x180_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x180_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x180_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x90_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.153355] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x90_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0789768] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x90_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x90_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x90_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_x90_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.153355] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_x90_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0789768] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_x90_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_x90_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_x90_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y180_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.30671] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y180_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.1579536] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y180_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y180_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y180_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.3] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y90_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.153355] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y90_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0789768] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y90_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y90_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_y90_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_y90_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.153355] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_y90_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0789768] * 246 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_y90_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_y90_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_minus_y90_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.15] * 158 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "square_x180_I_wf": {
            "type": "constant",
            "sample": 0.4,
        },
        "square_x90_I_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "square_minus_x90_I_wf": {
            "type": "constant",
            "sample": -0.2,
        },
        "square_y180_I_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "square_y90_I_wf": {
            "type": "constant",
            "sample": 0.15,
        },
        "square_minus_y90_I_wf": {
            "type": "constant",
            "sample": -0.15,
        },
        "square_x180_I_wf_dup1": {
            "type": "constant",
            "sample": 0.26666666666666666,
        },
        "square_x90_I_wf_dup1": {
            "type": "constant",
            "sample": 0.13333333333333333,
        },
        "square_minus_x90_I_wf_dup1": {
            "type": "constant",
            "sample": -0.13333333333333333,
        },
        "square_y180_I_wf_dup1": {
            "type": "constant",
            "sample": 0.19999999999999998,
        },
        "square_y90_I_wf_dup1": {
            "type": "constant",
            "sample": 0.09999999999999999,
        },
        "square_minus_y90_I_wf_dup1": {
            "type": "constant",
            "sample": -0.09999999999999999,
        },
        "square_x180_I_wf_dup2": {
            "type": "constant",
            "sample": 0.13333333333333333,
        },
        "square_x90_I_wf_dup2": {
            "type": "constant",
            "sample": 0.06666666666666667,
        },
        "square_minus_x90_I_wf_dup2": {
            "type": "constant",
            "sample": -0.06666666666666667,
        },
        "square_y180_I_wf_dup2": {
            "type": "constant",
            "sample": 0.09999999999999999,
        },
        "square_y90_I_wf_dup2": {
            "type": "constant",
            "sample": 0.049999999999999996,
        },
        "square_minus_y90_I_wf_dup2": {
            "type": "constant",
            "sample": -0.049999999999999996,
        },
        "reflectometry_readout_wf_tank_circuit1": {
            "type": "constant",
            "sample": 0.15,
        },
        "reflectometry_readout_wf_tank_circuit2": {
            "type": "constant",
            "sample": 0.15,
        },
        "P0_step_wf": {
            "type": "constant",
            "sample": 0.25,
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
            "samples": [0.0, 0.0009148923399437993, 0.0018644642330929335, 0.00284965898284922, 0.0038714271362863782, 0.0049307255528147804, 0.006028516420688381, 0.007165766220976314, 0.008343444638726875, 0.009562523421161033, 0.010823975182848718, 0.01212877215794101, 0.013477884899657545, 0.01487228092735833, 0.016312923321664778, 0.017800769268233846, 0.019336768550933622, 0.020921861995316114, 0.02255697986343462, 0.024243040201208592, 0.02598094713969632, 0.027771589151797407, 0.02961583726607, 0.03151454323951276, 0.03346853769132978, 0.03547862819986278, 0.037545597365046326, 0.03967020083890829, 0.041853165326808814, 0.04409518656227807, 0.046396927258479985, 0.04875901503949465, 0.051182040354774354, 0.05366655438028805, 0.05621306691002526, 0.05882204424168241, 0.06149390706050232, 0.06422902832537891, 0.06702773116147609, 0.06989028676373935, 0.07281691231580012, 0.07580776892888938, 0.07886295960548184, 0.08198252723249075, 0.0851664526089207, 0.08841465251296415, 0.09172697781359468, 0.09510321163176602, 0.09854306755637063, 0.10204618792014453, 0.10561214214072318, 0.10924042513206186, 0.11293045579142641, 0.11668157556713862, 0.1204930471122275, 0.12436405302908665, 0.12829369471017485, 0.13228099127971685, 0.1363248786412681, 0.14042420863589627, 0.14457774831560755, 0.14878417933650587, 0.15304209747601527, 0.15735001227832562, 0.1617063468320342, 0.16610943768375308, 0.17055753489123626, 0.17504880221934724, 0.17958131748194273, 0.18415307303248715, 0.18876197640593897, 0.19340585111416314, 0.19808243759682406, 0.20278939432940254, 0.20752429908965656, 0.21228465038351318, 0.2170678690310354, 0.22187129991275403, 0.22669221387629673, 0.23152780980287496, 0.23637521683281865, 0.24123149674896527, 0.2460936465163277, 0.2509586009760774, 0.2558232356914874, 0.2606843699430909, 0.26553876986991826, 0.2703831517532839, 0.27521418543920934, 0.2800284978951797, 0.28482267689655494, 0.2895932748375783, 0.29433681266156153, 0.29904978390446163, 0.303728658845719, 0.3083698887598838, 0.3129699102622307, 0.31752514974124635, 0.3220320278705748, 0.32648696419271617, 0.33088638176650803, 0.33522671187016195, 0.3395043987513959, 0.34371590441598443, 0.34785771344585487, 0.35192633783767974, 0.35591832185276323, 0.35983024686888715, 0.3636587362246724, 0.3674004600469257, 0.37105214005138065, 0.374610554307203, 0.3780725419556184, 0.38143500787303103, 0.3846949272690411, 0.38784935020982825, 0.3908954060574589, 0.393830307815786, 0.39665135637374793, 0.399355944637039, 0.40194156153930644, 0.40440579592424686, 0.40674634029020573, 0.40896099438914535, 0.411047668672128, 0.4130043875737647, 0.41482929262840457, 0.4165206454111864, 0.41807683029743753, 0.4194963570342907, 0.4207778631187886, 0.4219201159771637, 0.42292201494041654, 0.42378259301175647, 0.42450101842193527, 0.4250765959689697, 0.425508768139233, 0.42579711600738496] + [0.4259413599131059] * 2 + [0.42579711600738496, 0.425508768139233, 0.4250765959689697, 0.42450101842193527, 0.42378259301175647, 0.42292201494041654, 0.4219201159771637, 0.4207778631187886, 0.4194963570342907, 0.41807683029743753, 0.4165206454111864, 0.41482929262840457, 0.4130043875737647, 0.411047668672128, 0.40896099438914535, 0.40674634029020573, 0.40440579592424686, 0.40194156153930644, 0.399355944637039, 0.39665135637374793, 0.393830307815786, 0.3908954060574589, 0.38784935020982825, 0.3846949272690411, 0.38143500787303103, 0.3780725419556184, 0.374610554307203, 0.37105214005138065, 0.3674004600469257, 0.3636587362246724, 0.35983024686888715, 0.35591832185276323, 0.35192633783767974, 0.34785771344585487, 0.34371590441598443, 0.3395043987513959, 0.33522671187016195, 0.33088638176650803, 0.32648696419271617, 0.3220320278705748, 0.31752514974124635, 0.3129699102622307, 0.3083698887598838, 0.303728658845719, 0.29904978390446163, 0.29433681266156153, 0.2895932748375783, 0.28482267689655494, 0.2800284978951797, 0.27521418543920934, 0.2703831517532839, 0.26553876986991826, 0.2606843699430909, 0.2558232356914874, 0.2509586009760774, 0.2460936465163277, 0.24123149674896527, 0.23637521683281865, 0.23152780980287496, 0.22669221387629673, 0.22187129991275403, 0.2170678690310354, 0.21228465038351318, 0.20752429908965656, 0.20278939432940254, 0.19808243759682406, 0.19340585111416314, 0.18876197640593897, 0.18415307303248715, 0.17958131748194273, 0.17504880221934724, 0.17055753489123626, 0.16610943768375308, 0.1617063468320342, 0.15735001227832562, 0.15304209747601527, 0.14878417933650587, 0.14457774831560755, 0.14042420863589627, 0.1363248786412681, 0.13228099127971685, 0.12829369471017485, 0.12436405302908665, 0.1204930471122275, 0.11668157556713862, 0.11293045579142641, 0.10924042513206186, 0.10561214214072318, 0.10204618792014453, 0.09854306755637063, 0.09510321163176602, 0.09172697781359468, 0.08841465251296415, 0.0851664526089207, 0.08198252723249075, 0.07886295960548184, 0.07580776892888938, 0.07281691231580012, 0.06989028676373935, 0.06702773116147609, 0.06422902832537891, 0.06149390706050232, 0.05882204424168241, 0.05621306691002526, 0.05366655438028805, 0.051182040354774354, 0.04875901503949465, 0.046396927258479985, 0.04409518656227807, 0.041853165326808814, 0.03967020083890829, 0.037545597365046326, 0.03547862819986278, 0.03346853769132978, 0.03151454323951276, 0.02961583726607, 0.027771589151797407, 0.02598094713969632, 0.024243040201208592, 0.02255697986343462, 0.020921861995316114, 0.019336768550933622, 0.017800769268233846, 0.016312923321664778, 0.01487228092735833, 0.013477884899657545, 0.01212877215794101, 0.010823975182848718, 0.009562523421161033, 0.008343444638726875, 0.007165766220976314, 0.006028516420688381, 0.0049307255528147804, 0.0038714271362863782, 0.00284965898284922, 0.0018644642330929335, 0.0009148923399437993] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.00045744616997189964, 0.0009322321165464668, 0.00142482949142461, 0.0019357135681431891, 0.0024653627764073902, 0.0030142582103441905, 0.003582883110488157, 0.004171722319363438, 0.0047812617105805165, 0.005411987591424359, 0.006064386078970505, 0.006738942449828773, 0.007436140463679165, 0.008156461660832389, 0.008900384634116923, 0.009668384275466811, 0.010460930997658057, 0.01127848993171731, 0.012121520100604296, 0.01299047356984816, 0.013885794575898704, 0.014807918633035, 0.01575727161975638, 0.01673426884566489, 0.01773931409993139, 0.018772798682523163, 0.019835100419454146, 0.020926582663404407, 0.022047593281139036, 0.023198463629239992, 0.024379507519747327, 0.025591020177387177, 0.026833277190144025, 0.02810653345501263, 0.029411022120841204, 0.03074695353025116, 0.032114514162689456, 0.033513865580738045, 0.03494514338186967, 0.03640845615790006, 0.03790388446444469, 0.03943147980274092, 0.040991263616245374, 0.04258322630446035, 0.04420732625648208, 0.04586348890679734, 0.04755160581588301, 0.049271533778185314, 0.05102309396007226, 0.05280607107036159, 0.05462021256603093, 0.056465227895713205, 0.05834078778356931, 0.06024652355611375, 0.062182026514543326, 0.06414684735508742, 0.06614049563985842, 0.06816243932063405, 0.07021210431794814, 0.07228887415780377, 0.07439208966825293, 0.07652104873800764, 0.07867500613916281, 0.0808531734160171, 0.08305471884187654, 0.08527876744561813, 0.08752440110967362, 0.08979065874097136, 0.09207653651624358, 0.09438098820296949, 0.09670292555708157, 0.09904121879841203, 0.10139469716470127, 0.10376214954482828, 0.10614232519175659, 0.1085339345155177, 0.11093564995637702, 0.11334610693814837, 0.11576390490143748, 0.11818760841640932, 0.12061574837448263, 0.12304682325816385, 0.1254793004880387, 0.1279116178457437, 0.13034218497154546, 0.13276938493495913, 0.13519157587664196, 0.13760709271960467, 0.14001424894758985, 0.14241133844827747, 0.14479663741878915, 0.14716840633078077, 0.14952489195223082, 0.1518643294228595, 0.1541849443799419, 0.15648495513111535, 0.15876257487062317, 0.1610160139352874, 0.16324348209635808, 0.16544319088325402, 0.16761335593508098, 0.16975219937569794, 0.17185795220799222, 0.17392885672292743, 0.17596316891883987, 0.17795916092638162, 0.17991512343444357, 0.1818293681123362, 0.18370023002346286, 0.18552607002569033, 0.1873052771536015, 0.1890362709778092, 0.19071750393651551, 0.19234746363452054, 0.19392467510491412, 0.19544770302872946, 0.196915153907893, 0.19832567818687397, 0.1996779723185195, 0.20097078076965322, 0.20220289796212343, 0.20337317014510287, 0.20448049719457267, 0.205523834336064, 0.20650219378688234, 0.20741464631420228, 0.2082603227055932, 0.20903841514871876, 0.20974817851714536, 0.2103889315593943, 0.21096005798858186, 0.21146100747020827, 0.21189129650587823, 0.21225050921096764, 0.21253829798448484, 0.2127543840696165, 0.21289855800369248] + [0.21297067995655294] * 2 + [0.21289855800369248, 0.2127543840696165, 0.21253829798448484, 0.21225050921096764, 0.21189129650587823, 0.21146100747020827, 0.21096005798858186, 0.2103889315593943, 0.20974817851714536, 0.20903841514871876, 0.2082603227055932, 0.20741464631420228, 0.20650219378688234, 0.205523834336064, 0.20448049719457267, 0.20337317014510287, 0.20220289796212343, 0.20097078076965322, 0.1996779723185195, 0.19832567818687397, 0.196915153907893, 0.19544770302872946, 0.19392467510491412, 0.19234746363452054, 0.19071750393651551, 0.1890362709778092, 0.1873052771536015, 0.18552607002569033, 0.18370023002346286, 0.1818293681123362, 0.17991512343444357, 0.17795916092638162, 0.17596316891883987, 0.17392885672292743, 0.17185795220799222, 0.16975219937569794, 0.16761335593508098, 0.16544319088325402, 0.16324348209635808, 0.1610160139352874, 0.15876257487062317, 0.15648495513111535, 0.1541849443799419, 0.1518643294228595, 0.14952489195223082, 0.14716840633078077, 0.14479663741878915, 0.14241133844827747, 0.14001424894758985, 0.13760709271960467, 0.13519157587664196, 0.13276938493495913, 0.13034218497154546, 0.1279116178457437, 0.1254793004880387, 0.12304682325816385, 0.12061574837448263, 0.11818760841640932, 0.11576390490143748, 0.11334610693814837, 0.11093564995637702, 0.1085339345155177, 0.10614232519175659, 0.10376214954482828, 0.10139469716470127, 0.09904121879841203, 0.09670292555708157, 0.09438098820296949, 0.09207653651624358, 0.08979065874097136, 0.08752440110967362, 0.08527876744561813, 0.08305471884187654, 0.0808531734160171, 0.07867500613916281, 0.07652104873800764, 0.07439208966825293, 0.07228887415780377, 0.07021210431794814, 0.06816243932063405, 0.06614049563985842, 0.06414684735508742, 0.062182026514543326, 0.06024652355611375, 0.05834078778356931, 0.056465227895713205, 0.05462021256603093, 0.05280607107036159, 0.05102309396007226, 0.049271533778185314, 0.04755160581588301, 0.04586348890679734, 0.04420732625648208, 0.04258322630446035, 0.040991263616245374, 0.03943147980274092, 0.03790388446444469, 0.03640845615790006, 0.03494514338186967, 0.033513865580738045, 0.032114514162689456, 0.03074695353025116, 0.029411022120841204, 0.02810653345501263, 0.026833277190144025, 0.025591020177387177, 0.024379507519747327, 0.023198463629239992, 0.022047593281139036, 0.020926582663404407, 0.019835100419454146, 0.018772798682523163, 0.01773931409993139, 0.01673426884566489, 0.01575727161975638, 0.014807918633035, 0.013885794575898704, 0.01299047356984816, 0.012121520100604296, 0.01127848993171731, 0.010460930997658057, 0.009668384275466811, 0.008900384634116923, 0.008156461660832389, 0.007436140463679165, 0.006738942449828773, 0.006064386078970505, 0.005411987591424359, 0.0047812617105805165, 0.004171722319363438, 0.003582883110488157, 0.0030142582103441905, 0.0024653627764073902, 0.0019357135681431891, 0.00142482949142461, 0.0009322321165464668, 0.00045744616997189964] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.00045744616997189964, -0.0009322321165464668, -0.00142482949142461, -0.0019357135681431891, -0.0024653627764073902, -0.0030142582103441905, -0.003582883110488157, -0.004171722319363438, -0.0047812617105805165, -0.005411987591424359, -0.006064386078970505, -0.006738942449828773, -0.007436140463679165, -0.008156461660832389, -0.008900384634116923, -0.009668384275466811, -0.010460930997658057, -0.01127848993171731, -0.012121520100604296, -0.01299047356984816, -0.013885794575898704, -0.014807918633035, -0.01575727161975638, -0.01673426884566489, -0.01773931409993139, -0.018772798682523163, -0.019835100419454146, -0.020926582663404407, -0.022047593281139036, -0.023198463629239992, -0.024379507519747327, -0.025591020177387177, -0.026833277190144025, -0.02810653345501263, -0.029411022120841204, -0.03074695353025116, -0.032114514162689456, -0.033513865580738045, -0.03494514338186967, -0.03640845615790006, -0.03790388446444469, -0.03943147980274092, -0.040991263616245374, -0.04258322630446035, -0.04420732625648208, -0.04586348890679734, -0.04755160581588301, -0.049271533778185314, -0.05102309396007226, -0.05280607107036159, -0.05462021256603093, -0.056465227895713205, -0.05834078778356931, -0.06024652355611375, -0.062182026514543326, -0.06414684735508742, -0.06614049563985842, -0.06816243932063405, -0.07021210431794814, -0.07228887415780377, -0.07439208966825293, -0.07652104873800764, -0.07867500613916281, -0.0808531734160171, -0.08305471884187654, -0.08527876744561813, -0.08752440110967362, -0.08979065874097136, -0.09207653651624358, -0.09438098820296949, -0.09670292555708157, -0.09904121879841203, -0.10139469716470127, -0.10376214954482828, -0.10614232519175659, -0.1085339345155177, -0.11093564995637702, -0.11334610693814837, -0.11576390490143748, -0.11818760841640932, -0.12061574837448263, -0.12304682325816385, -0.1254793004880387, -0.1279116178457437, -0.13034218497154546, -0.13276938493495913, -0.13519157587664196, -0.13760709271960467, -0.14001424894758985, -0.14241133844827747, -0.14479663741878915, -0.14716840633078077, -0.14952489195223082, -0.1518643294228595, -0.1541849443799419, -0.15648495513111535, -0.15876257487062317, -0.1610160139352874, -0.16324348209635808, -0.16544319088325402, -0.16761335593508098, -0.16975219937569794, -0.17185795220799222, -0.17392885672292743, -0.17596316891883987, -0.17795916092638162, -0.17991512343444357, -0.1818293681123362, -0.18370023002346286, -0.18552607002569033, -0.1873052771536015, -0.1890362709778092, -0.19071750393651551, -0.19234746363452054, -0.19392467510491412, -0.19544770302872946, -0.196915153907893, -0.19832567818687397, -0.1996779723185195, -0.20097078076965322, -0.20220289796212343, -0.20337317014510287, -0.20448049719457267, -0.205523834336064, -0.20650219378688234, -0.20741464631420228, -0.2082603227055932, -0.20903841514871876, -0.20974817851714536, -0.2103889315593943, -0.21096005798858186, -0.21146100747020827, -0.21189129650587823, -0.21225050921096764, -0.21253829798448484, -0.2127543840696165, -0.21289855800369248] + [-0.21297067995655294] * 2 + [-0.21289855800369248, -0.2127543840696165, -0.21253829798448484, -0.21225050921096764, -0.21189129650587823, -0.21146100747020827, -0.21096005798858186, -0.2103889315593943, -0.20974817851714536, -0.20903841514871876, -0.2082603227055932, -0.20741464631420228, -0.20650219378688234, -0.205523834336064, -0.20448049719457267, -0.20337317014510287, -0.20220289796212343, -0.20097078076965322, -0.1996779723185195, -0.19832567818687397, -0.196915153907893, -0.19544770302872946, -0.19392467510491412, -0.19234746363452054, -0.19071750393651551, -0.1890362709778092, -0.1873052771536015, -0.18552607002569033, -0.18370023002346286, -0.1818293681123362, -0.17991512343444357, -0.17795916092638162, -0.17596316891883987, -0.17392885672292743, -0.17185795220799222, -0.16975219937569794, -0.16761335593508098, -0.16544319088325402, -0.16324348209635808, -0.1610160139352874, -0.15876257487062317, -0.15648495513111535, -0.1541849443799419, -0.1518643294228595, -0.14952489195223082, -0.14716840633078077, -0.14479663741878915, -0.14241133844827747, -0.14001424894758985, -0.13760709271960467, -0.13519157587664196, -0.13276938493495913, -0.13034218497154546, -0.1279116178457437, -0.1254793004880387, -0.12304682325816385, -0.12061574837448263, -0.11818760841640932, -0.11576390490143748, -0.11334610693814837, -0.11093564995637702, -0.1085339345155177, -0.10614232519175659, -0.10376214954482828, -0.10139469716470127, -0.09904121879841203, -0.09670292555708157, -0.09438098820296949, -0.09207653651624358, -0.08979065874097136, -0.08752440110967362, -0.08527876744561813, -0.08305471884187654, -0.0808531734160171, -0.07867500613916281, -0.07652104873800764, -0.07439208966825293, -0.07228887415780377, -0.07021210431794814, -0.06816243932063405, -0.06614049563985842, -0.06414684735508742, -0.062182026514543326, -0.06024652355611375, -0.05834078778356931, -0.056465227895713205, -0.05462021256603093, -0.05280607107036159, -0.05102309396007226, -0.049271533778185314, -0.04755160581588301, -0.04586348890679734, -0.04420732625648208, -0.04258322630446035, -0.040991263616245374, -0.03943147980274092, -0.03790388446444469, -0.03640845615790006, -0.03494514338186967, -0.033513865580738045, -0.032114514162689456, -0.03074695353025116, -0.029411022120841204, -0.02810653345501263, -0.026833277190144025, -0.025591020177387177, -0.024379507519747327, -0.023198463629239992, -0.022047593281139036, -0.020926582663404407, -0.019835100419454146, -0.018772798682523163, -0.01773931409993139, -0.01673426884566489, -0.01575727161975638, -0.014807918633035, -0.013885794575898704, -0.01299047356984816, -0.012121520100604296, -0.01127848993171731, -0.010460930997658057, -0.009668384275466811, -0.008900384634116923, -0.008156461660832389, -0.007436140463679165, -0.006738942449828773, -0.006064386078970505, -0.005411987591424359, -0.0047812617105805165, -0.004171722319363438, -0.003582883110488157, -0.0030142582103441905, -0.0024653627764073902, -0.0019357135681431891, -0.00142482949142461, -0.0009322321165464668, -0.00045744616997189964] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009148923399437993, 0.0018644642330929335, 0.00284965898284922, 0.0038714271362863782, 0.0049307255528147804, 0.006028516420688381, 0.007165766220976314, 0.008343444638726875, 0.009562523421161033, 0.010823975182848718, 0.01212877215794101, 0.013477884899657545, 0.01487228092735833, 0.016312923321664778, 0.017800769268233846, 0.019336768550933622, 0.020921861995316114, 0.02255697986343462, 0.024243040201208592, 0.02598094713969632, 0.027771589151797407, 0.02961583726607, 0.03151454323951276, 0.03346853769132978, 0.03547862819986278, 0.037545597365046326, 0.03967020083890829, 0.041853165326808814, 0.04409518656227807, 0.046396927258479985, 0.04875901503949465, 0.051182040354774354, 0.05366655438028805, 0.05621306691002526, 0.05882204424168241, 0.06149390706050232, 0.06422902832537891, 0.06702773116147609, 0.06989028676373935, 0.07281691231580012, 0.07580776892888938, 0.07886295960548184, 0.08198252723249075, 0.0851664526089207, 0.08841465251296415, 0.09172697781359468, 0.09510321163176602, 0.09854306755637063, 0.10204618792014453, 0.10561214214072318, 0.10924042513206186, 0.11293045579142641, 0.11668157556713862, 0.1204930471122275, 0.12436405302908665, 0.12829369471017485, 0.13228099127971685, 0.1363248786412681, 0.14042420863589627, 0.14457774831560755, 0.14878417933650587, 0.15304209747601527, 0.15735001227832562, 0.1617063468320342, 0.16610943768375308, 0.17055753489123626, 0.17504880221934724, 0.17958131748194273, 0.18415307303248715, 0.18876197640593897, 0.19340585111416314, 0.19808243759682406, 0.20278939432940254, 0.20752429908965656, 0.21228465038351318, 0.2170678690310354, 0.22187129991275403, 0.22669221387629673, 0.23152780980287496, 0.23637521683281865, 0.24123149674896527, 0.2460936465163277, 0.2509586009760774, 0.2558232356914874, 0.2606843699430909, 0.26553876986991826, 0.2703831517532839, 0.27521418543920934, 0.2800284978951797, 0.28482267689655494, 0.2895932748375783, 0.29433681266156153, 0.29904978390446163, 0.303728658845719, 0.3083698887598838, 0.3129699102622307, 0.31752514974124635, 0.3220320278705748, 0.32648696419271617, 0.33088638176650803, 0.33522671187016195, 0.3395043987513959, 0.34371590441598443, 0.34785771344585487, 0.35192633783767974, 0.35591832185276323, 0.35983024686888715, 0.3636587362246724, 0.3674004600469257, 0.37105214005138065, 0.374610554307203, 0.3780725419556184, 0.38143500787303103, 0.3846949272690411, 0.38784935020982825, 0.3908954060574589, 0.393830307815786, 0.39665135637374793, 0.399355944637039, 0.40194156153930644, 0.40440579592424686, 0.40674634029020573, 0.40896099438914535, 0.411047668672128, 0.4130043875737647, 0.41482929262840457, 0.4165206454111864, 0.41807683029743753, 0.4194963570342907, 0.4207778631187886, 0.4219201159771637, 0.42292201494041654, 0.42378259301175647, 0.42450101842193527, 0.4250765959689697, 0.425508768139233, 0.42579711600738496] + [0.4259413599131059] * 2 + [0.42579711600738496, 0.425508768139233, 0.4250765959689697, 0.42450101842193527, 0.42378259301175647, 0.42292201494041654, 0.4219201159771637, 0.4207778631187886, 0.4194963570342907, 0.41807683029743753, 0.4165206454111864, 0.41482929262840457, 0.4130043875737647, 0.411047668672128, 0.40896099438914535, 0.40674634029020573, 0.40440579592424686, 0.40194156153930644, 0.399355944637039, 0.39665135637374793, 0.393830307815786, 0.3908954060574589, 0.38784935020982825, 0.3846949272690411, 0.38143500787303103, 0.3780725419556184, 0.374610554307203, 0.37105214005138065, 0.3674004600469257, 0.3636587362246724, 0.35983024686888715, 0.35591832185276323, 0.35192633783767974, 0.34785771344585487, 0.34371590441598443, 0.3395043987513959, 0.33522671187016195, 0.33088638176650803, 0.32648696419271617, 0.3220320278705748, 0.31752514974124635, 0.3129699102622307, 0.3083698887598838, 0.303728658845719, 0.29904978390446163, 0.29433681266156153, 0.2895932748375783, 0.28482267689655494, 0.2800284978951797, 0.27521418543920934, 0.2703831517532839, 0.26553876986991826, 0.2606843699430909, 0.2558232356914874, 0.2509586009760774, 0.2460936465163277, 0.24123149674896527, 0.23637521683281865, 0.23152780980287496, 0.22669221387629673, 0.22187129991275403, 0.2170678690310354, 0.21228465038351318, 0.20752429908965656, 0.20278939432940254, 0.19808243759682406, 0.19340585111416314, 0.18876197640593897, 0.18415307303248715, 0.17958131748194273, 0.17504880221934724, 0.17055753489123626, 0.16610943768375308, 0.1617063468320342, 0.15735001227832562, 0.15304209747601527, 0.14878417933650587, 0.14457774831560755, 0.14042420863589627, 0.1363248786412681, 0.13228099127971685, 0.12829369471017485, 0.12436405302908665, 0.1204930471122275, 0.11668157556713862, 0.11293045579142641, 0.10924042513206186, 0.10561214214072318, 0.10204618792014453, 0.09854306755637063, 0.09510321163176602, 0.09172697781359468, 0.08841465251296415, 0.0851664526089207, 0.08198252723249075, 0.07886295960548184, 0.07580776892888938, 0.07281691231580012, 0.06989028676373935, 0.06702773116147609, 0.06422902832537891, 0.06149390706050232, 0.05882204424168241, 0.05621306691002526, 0.05366655438028805, 0.051182040354774354, 0.04875901503949465, 0.046396927258479985, 0.04409518656227807, 0.041853165326808814, 0.03967020083890829, 0.037545597365046326, 0.03547862819986278, 0.03346853769132978, 0.03151454323951276, 0.02961583726607, 0.027771589151797407, 0.02598094713969632, 0.024243040201208592, 0.02255697986343462, 0.020921861995316114, 0.019336768550933622, 0.017800769268233846, 0.016312923321664778, 0.01487228092735833, 0.013477884899657545, 0.01212877215794101, 0.010823975182848718, 0.009562523421161033, 0.008343444638726875, 0.007165766220976314, 0.006028516420688381, 0.0049307255528147804, 0.0038714271362863782, 0.00284965898284922, 0.0018644642330929335, 0.0009148923399437993] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011139578471959927, 0.0023023736730072176, 0.0035687417555153225, 0.0049165912654571976, 0.006349474346888271, 0.007870953142717468, 0.009484585763728353, 0.011193911207272653, 0.013002433239926283, 0.014913603266996154, 0.016930802220817755, 0.019057321509236287, 0.0212963430754603, 0.023650918630548932, 0.026123948130068735, 0.028718157576850326, 0.03143607624220385, 0.03428001340831532, 0.0372520347447488, 0.040353938441911666, 0.043587231233895435, 0.04695310445216828, 0.05045241026005412, 0.0540856382256701, 0.057852892397895386, 0.06175386905589532, 0.0657878353076159, 0.06995360871638859, 0.07424953813724518, 0.0786734859456426, 0.083222811840959, 0.08789435840526601, 0.0926844385944517, 0.0975888253337142, 0.10260274338273095, 0.10772086362741853, 0.11293729994512569, 0.11824560877836676, 0.12363879153883095, 0.12910929994845116, 0.13464904440784756, 0.1402494054645662, 0.14590124843431646, 0.15159494120799463, 0.15732037525580642, 0.1630669898174251, 0.16882379924401278, 0.1745794234342806, 0.18032212128276165, 0.18603982703432853, 0.19172018941492253, 0.19735061338469334, 0.2029183043365048, 0.2084103145402739, 0.2138135916120975, 0.2191150287668165, 0.22430151659377898, 0.2293599960783098, 0.23427751257596194, 0.23904127043321077, 0.24363868793701127, 0.24805745226672976, 0.2522855741155109, 0.2563114416442533, 0.2601238734301302, 0.2637121700730609, 0.2670661641277441, 0.27017626803581574, 0.27303351974236306, 0.27562962569336524, 0.2779570009255619, 0.28000880597766775, 0.28177898037162064, 0.28326227243452307, 0.2844542652559221, 0.2853513986008818, 0.285950986626701] + [0.28625123127989105] * 2 + [0.285950986626701, 0.2853513986008818, 0.2844542652559221, 0.28326227243452307, 0.28177898037162064, 0.28000880597766775, 0.2779570009255619, 0.27562962569336524, 0.27303351974236306, 0.27017626803581574, 0.2670661641277441, 0.2637121700730609, 0.2601238734301302, 0.2563114416442533, 0.2522855741155109, 0.24805745226672976, 0.24363868793701127, 0.23904127043321077, 0.23427751257596194, 0.2293599960783098, 0.22430151659377898, 0.2191150287668165, 0.2138135916120975, 0.2084103145402739, 0.2029183043365048, 0.19735061338469334, 0.19172018941492253, 0.18603982703432853, 0.18032212128276165, 0.1745794234342806, 0.16882379924401278, 0.1630669898174251, 0.15732037525580642, 0.15159494120799463, 0.14590124843431646, 0.1402494054645662, 0.13464904440784756, 0.12910929994845116, 0.12363879153883095, 0.11824560877836676, 0.11293729994512569, 0.10772086362741853, 0.10260274338273095, 0.0975888253337142, 0.0926844385944517, 0.08789435840526601, 0.083222811840959, 0.0786734859456426, 0.07424953813724518, 0.06995360871638859, 0.0657878353076159, 0.06175386905589532, 0.057852892397895386, 0.0540856382256701, 0.05045241026005412, 0.04695310445216828, 0.043587231233895435, 0.040353938441911666, 0.0372520347447488, 0.03428001340831532, 0.03143607624220385, 0.028718157576850326, 0.026123948130068735, 0.023650918630548932, 0.0212963430754603, 0.019057321509236287, 0.016930802220817755, 0.014913603266996154, 0.013002433239926283, 0.011193911207272653, 0.009484585763728353, 0.007870953142717468, 0.006349474346888271, 0.0049165912654571976, 0.0035687417555153225, 0.0023023736730072176, 0.0011139578471959927] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.00045744616997189964, 0.0009322321165464668, 0.00142482949142461, 0.0019357135681431891, 0.0024653627764073902, 0.0030142582103441905, 0.003582883110488157, 0.004171722319363438, 0.0047812617105805165, 0.005411987591424359, 0.006064386078970505, 0.006738942449828773, 0.007436140463679165, 0.008156461660832389, 0.008900384634116923, 0.009668384275466811, 0.010460930997658057, 0.01127848993171731, 0.012121520100604296, 0.01299047356984816, 0.013885794575898704, 0.014807918633035, 0.01575727161975638, 0.01673426884566489, 0.01773931409993139, 0.018772798682523163, 0.019835100419454146, 0.020926582663404407, 0.022047593281139036, 0.023198463629239992, 0.024379507519747327, 0.025591020177387177, 0.026833277190144025, 0.02810653345501263, 0.029411022120841204, 0.03074695353025116, 0.032114514162689456, 0.033513865580738045, 0.03494514338186967, 0.03640845615790006, 0.03790388446444469, 0.03943147980274092, 0.040991263616245374, 0.04258322630446035, 0.04420732625648208, 0.04586348890679734, 0.04755160581588301, 0.049271533778185314, 0.05102309396007226, 0.05280607107036159, 0.05462021256603093, 0.056465227895713205, 0.05834078778356931, 0.06024652355611375, 0.062182026514543326, 0.06414684735508742, 0.06614049563985842, 0.06816243932063405, 0.07021210431794814, 0.07228887415780377, 0.07439208966825293, 0.07652104873800764, 0.07867500613916281, 0.0808531734160171, 0.08305471884187654, 0.08527876744561813, 0.08752440110967362, 0.08979065874097136, 0.09207653651624358, 0.09438098820296949, 0.09670292555708157, 0.09904121879841203, 0.10139469716470127, 0.10376214954482828, 0.10614232519175659, 0.1085339345155177, 0.11093564995637702, 0.11334610693814837, 0.11576390490143748, 0.11818760841640932, 0.12061574837448263, 0.12304682325816385, 0.1254793004880387, 0.1279116178457437, 0.13034218497154546, 0.13276938493495913, 0.13519157587664196, 0.13760709271960467, 0.14001424894758985, 0.14241133844827747, 0.14479663741878915, 0.14716840633078077, 0.14952489195223082, 0.1518643294228595, 0.1541849443799419, 0.15648495513111535, 0.15876257487062317, 0.1610160139352874, 0.16324348209635808, 0.16544319088325402, 0.16761335593508098, 0.16975219937569794, 0.17185795220799222, 0.17392885672292743, 0.17596316891883987, 0.17795916092638162, 0.17991512343444357, 0.1818293681123362, 0.18370023002346286, 0.18552607002569033, 0.1873052771536015, 0.1890362709778092, 0.19071750393651551, 0.19234746363452054, 0.19392467510491412, 0.19544770302872946, 0.196915153907893, 0.19832567818687397, 0.1996779723185195, 0.20097078076965322, 0.20220289796212343, 0.20337317014510287, 0.20448049719457267, 0.205523834336064, 0.20650219378688234, 0.20741464631420228, 0.2082603227055932, 0.20903841514871876, 0.20974817851714536, 0.2103889315593943, 0.21096005798858186, 0.21146100747020827, 0.21189129650587823, 0.21225050921096764, 0.21253829798448484, 0.2127543840696165, 0.21289855800369248] + [0.21297067995655294] * 2 + [0.21289855800369248, 0.2127543840696165, 0.21253829798448484, 0.21225050921096764, 0.21189129650587823, 0.21146100747020827, 0.21096005798858186, 0.2103889315593943, 0.20974817851714536, 0.20903841514871876, 0.2082603227055932, 0.20741464631420228, 0.20650219378688234, 0.205523834336064, 0.20448049719457267, 0.20337317014510287, 0.20220289796212343, 0.20097078076965322, 0.1996779723185195, 0.19832567818687397, 0.196915153907893, 0.19544770302872946, 0.19392467510491412, 0.19234746363452054, 0.19071750393651551, 0.1890362709778092, 0.1873052771536015, 0.18552607002569033, 0.18370023002346286, 0.1818293681123362, 0.17991512343444357, 0.17795916092638162, 0.17596316891883987, 0.17392885672292743, 0.17185795220799222, 0.16975219937569794, 0.16761335593508098, 0.16544319088325402, 0.16324348209635808, 0.1610160139352874, 0.15876257487062317, 0.15648495513111535, 0.1541849443799419, 0.1518643294228595, 0.14952489195223082, 0.14716840633078077, 0.14479663741878915, 0.14241133844827747, 0.14001424894758985, 0.13760709271960467, 0.13519157587664196, 0.13276938493495913, 0.13034218497154546, 0.1279116178457437, 0.1254793004880387, 0.12304682325816385, 0.12061574837448263, 0.11818760841640932, 0.11576390490143748, 0.11334610693814837, 0.11093564995637702, 0.1085339345155177, 0.10614232519175659, 0.10376214954482828, 0.10139469716470127, 0.09904121879841203, 0.09670292555708157, 0.09438098820296949, 0.09207653651624358, 0.08979065874097136, 0.08752440110967362, 0.08527876744561813, 0.08305471884187654, 0.0808531734160171, 0.07867500613916281, 0.07652104873800764, 0.07439208966825293, 0.07228887415780377, 0.07021210431794814, 0.06816243932063405, 0.06614049563985842, 0.06414684735508742, 0.062182026514543326, 0.06024652355611375, 0.05834078778356931, 0.056465227895713205, 0.05462021256603093, 0.05280607107036159, 0.05102309396007226, 0.049271533778185314, 0.04755160581588301, 0.04586348890679734, 0.04420732625648208, 0.04258322630446035, 0.040991263616245374, 0.03943147980274092, 0.03790388446444469, 0.03640845615790006, 0.03494514338186967, 0.033513865580738045, 0.032114514162689456, 0.03074695353025116, 0.029411022120841204, 0.02810653345501263, 0.026833277190144025, 0.025591020177387177, 0.024379507519747327, 0.023198463629239992, 0.022047593281139036, 0.020926582663404407, 0.019835100419454146, 0.018772798682523163, 0.01773931409993139, 0.01673426884566489, 0.01575727161975638, 0.014807918633035, 0.013885794575898704, 0.01299047356984816, 0.012121520100604296, 0.01127848993171731, 0.010460930997658057, 0.009668384275466811, 0.008900384634116923, 0.008156461660832389, 0.007436140463679165, 0.006738942449828773, 0.006064386078970505, 0.005411987591424359, 0.0047812617105805165, 0.004171722319363438, 0.003582883110488157, 0.0030142582103441905, 0.0024653627764073902, 0.0019357135681431891, 0.00142482949142461, 0.0009322321165464668, 0.00045744616997189964] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005569789235979963, 0.0011511868365036088, 0.0017843708777576612, 0.0024582956327285988, 0.0031747371734441353, 0.003935476571358734, 0.004742292881864177, 0.0055969556036363265, 0.006501216619963141, 0.007456801633498077, 0.008465401110408877, 0.009528660754618144, 0.01064817153773015, 0.011825459315274466, 0.013061974065034367, 0.014359078788425163, 0.015718038121101924, 0.01714000670415766, 0.0186260173723744, 0.020176969220955833, 0.021793615616947717, 0.02347655222608414, 0.02522620513002706, 0.02704281911283505, 0.028926446198947693, 0.03087693452794766, 0.03289391765380795, 0.034976804358194294, 0.03712476906862259, 0.0393367429728213, 0.0416114059204795, 0.043947179202633004, 0.04634221929722585, 0.0487944126668571, 0.05130137169136548, 0.05386043181370927, 0.056468649972562845, 0.05912280438918338, 0.061819395769415475, 0.06455464997422558, 0.06732452220392378, 0.0701247027322831, 0.07295062421715823, 0.07579747060399732, 0.07866018762790321, 0.08153349490871255, 0.08441189962200639, 0.0872897117171403, 0.09016106064138082, 0.09301991351716427, 0.09586009470746126, 0.09867530669234667, 0.1014591521682524, 0.10420515727013695, 0.10690679580604875, 0.10955751438340824, 0.11215075829688949, 0.1146799980391549, 0.11713875628798097, 0.11952063521660539, 0.12181934396850563, 0.12402872613336488, 0.12614278705775545, 0.12815572082212665, 0.1300619367150651, 0.13185608503653046, 0.13353308206387204, 0.13508813401790787, 0.13651675987118153, 0.13781481284668262, 0.13897850046278096, 0.14000440298883388, 0.14088949018581032, 0.14163113621726153, 0.14222713262796105, 0.1426756993004409, 0.1429754933133505] + [0.14312561563994552] * 2 + [0.1429754933133505, 0.1426756993004409, 0.14222713262796105, 0.14163113621726153, 0.14088949018581032, 0.14000440298883388, 0.13897850046278096, 0.13781481284668262, 0.13651675987118153, 0.13508813401790787, 0.13353308206387204, 0.13185608503653046, 0.1300619367150651, 0.12815572082212665, 0.12614278705775545, 0.12402872613336488, 0.12181934396850563, 0.11952063521660539, 0.11713875628798097, 0.1146799980391549, 0.11215075829688949, 0.10955751438340824, 0.10690679580604875, 0.10420515727013695, 0.1014591521682524, 0.09867530669234667, 0.09586009470746126, 0.09301991351716427, 0.09016106064138082, 0.0872897117171403, 0.08441189962200639, 0.08153349490871255, 0.07866018762790321, 0.07579747060399732, 0.07295062421715823, 0.0701247027322831, 0.06732452220392378, 0.06455464997422558, 0.061819395769415475, 0.05912280438918338, 0.056468649972562845, 0.05386043181370927, 0.05130137169136548, 0.0487944126668571, 0.04634221929722585, 0.043947179202633004, 0.0416114059204795, 0.0393367429728213, 0.03712476906862259, 0.034976804358194294, 0.03289391765380795, 0.03087693452794766, 0.028926446198947693, 0.02704281911283505, 0.02522620513002706, 0.02347655222608414, 0.021793615616947717, 0.020176969220955833, 0.0186260173723744, 0.01714000670415766, 0.015718038121101924, 0.014359078788425163, 0.013061974065034367, 0.011825459315274466, 0.01064817153773015, 0.009528660754618144, 0.008465401110408877, 0.007456801633498077, 0.006501216619963141, 0.0055969556036363265, 0.004742292881864177, 0.003935476571358734, 0.0031747371734441353, 0.0024582956327285988, 0.0017843708777576612, 0.0011511868365036088, 0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.00045744616997189964, -0.0009322321165464668, -0.00142482949142461, -0.0019357135681431891, -0.0024653627764073902, -0.0030142582103441905, -0.003582883110488157, -0.004171722319363438, -0.0047812617105805165, -0.005411987591424359, -0.006064386078970505, -0.006738942449828773, -0.007436140463679165, -0.008156461660832389, -0.008900384634116923, -0.009668384275466811, -0.010460930997658057, -0.01127848993171731, -0.012121520100604296, -0.01299047356984816, -0.013885794575898704, -0.014807918633035, -0.01575727161975638, -0.01673426884566489, -0.01773931409993139, -0.018772798682523163, -0.019835100419454146, -0.020926582663404407, -0.022047593281139036, -0.023198463629239992, -0.024379507519747327, -0.025591020177387177, -0.026833277190144025, -0.02810653345501263, -0.029411022120841204, -0.03074695353025116, -0.032114514162689456, -0.033513865580738045, -0.03494514338186967, -0.03640845615790006, -0.03790388446444469, -0.03943147980274092, -0.040991263616245374, -0.04258322630446035, -0.04420732625648208, -0.04586348890679734, -0.04755160581588301, -0.049271533778185314, -0.05102309396007226, -0.05280607107036159, -0.05462021256603093, -0.056465227895713205, -0.05834078778356931, -0.06024652355611375, -0.062182026514543326, -0.06414684735508742, -0.06614049563985842, -0.06816243932063405, -0.07021210431794814, -0.07228887415780377, -0.07439208966825293, -0.07652104873800764, -0.07867500613916281, -0.0808531734160171, -0.08305471884187654, -0.08527876744561813, -0.08752440110967362, -0.08979065874097136, -0.09207653651624358, -0.09438098820296949, -0.09670292555708157, -0.09904121879841203, -0.10139469716470127, -0.10376214954482828, -0.10614232519175659, -0.1085339345155177, -0.11093564995637702, -0.11334610693814837, -0.11576390490143748, -0.11818760841640932, -0.12061574837448263, -0.12304682325816385, -0.1254793004880387, -0.1279116178457437, -0.13034218497154546, -0.13276938493495913, -0.13519157587664196, -0.13760709271960467, -0.14001424894758985, -0.14241133844827747, -0.14479663741878915, -0.14716840633078077, -0.14952489195223082, -0.1518643294228595, -0.1541849443799419, -0.15648495513111535, -0.15876257487062317, -0.1610160139352874, -0.16324348209635808, -0.16544319088325402, -0.16761335593508098, -0.16975219937569794, -0.17185795220799222, -0.17392885672292743, -0.17596316891883987, -0.17795916092638162, -0.17991512343444357, -0.1818293681123362, -0.18370023002346286, -0.18552607002569033, -0.1873052771536015, -0.1890362709778092, -0.19071750393651551, -0.19234746363452054, -0.19392467510491412, -0.19544770302872946, -0.196915153907893, -0.19832567818687397, -0.1996779723185195, -0.20097078076965322, -0.20220289796212343, -0.20337317014510287, -0.20448049719457267, -0.205523834336064, -0.20650219378688234, -0.20741464631420228, -0.2082603227055932, -0.20903841514871876, -0.20974817851714536, -0.2103889315593943, -0.21096005798858186, -0.21146100747020827, -0.21189129650587823, -0.21225050921096764, -0.21253829798448484, -0.2127543840696165, -0.21289855800369248] + [-0.21297067995655294] * 2 + [-0.21289855800369248, -0.2127543840696165, -0.21253829798448484, -0.21225050921096764, -0.21189129650587823, -0.21146100747020827, -0.21096005798858186, -0.2103889315593943, -0.20974817851714536, -0.20903841514871876, -0.2082603227055932, -0.20741464631420228, -0.20650219378688234, -0.205523834336064, -0.20448049719457267, -0.20337317014510287, -0.20220289796212343, -0.20097078076965322, -0.1996779723185195, -0.19832567818687397, -0.196915153907893, -0.19544770302872946, -0.19392467510491412, -0.19234746363452054, -0.19071750393651551, -0.1890362709778092, -0.1873052771536015, -0.18552607002569033, -0.18370023002346286, -0.1818293681123362, -0.17991512343444357, -0.17795916092638162, -0.17596316891883987, -0.17392885672292743, -0.17185795220799222, -0.16975219937569794, -0.16761335593508098, -0.16544319088325402, -0.16324348209635808, -0.1610160139352874, -0.15876257487062317, -0.15648495513111535, -0.1541849443799419, -0.1518643294228595, -0.14952489195223082, -0.14716840633078077, -0.14479663741878915, -0.14241133844827747, -0.14001424894758985, -0.13760709271960467, -0.13519157587664196, -0.13276938493495913, -0.13034218497154546, -0.1279116178457437, -0.1254793004880387, -0.12304682325816385, -0.12061574837448263, -0.11818760841640932, -0.11576390490143748, -0.11334610693814837, -0.11093564995637702, -0.1085339345155177, -0.10614232519175659, -0.10376214954482828, -0.10139469716470127, -0.09904121879841203, -0.09670292555708157, -0.09438098820296949, -0.09207653651624358, -0.08979065874097136, -0.08752440110967362, -0.08527876744561813, -0.08305471884187654, -0.0808531734160171, -0.07867500613916281, -0.07652104873800764, -0.07439208966825293, -0.07228887415780377, -0.07021210431794814, -0.06816243932063405, -0.06614049563985842, -0.06414684735508742, -0.062182026514543326, -0.06024652355611375, -0.05834078778356931, -0.056465227895713205, -0.05462021256603093, -0.05280607107036159, -0.05102309396007226, -0.049271533778185314, -0.04755160581588301, -0.04586348890679734, -0.04420732625648208, -0.04258322630446035, -0.040991263616245374, -0.03943147980274092, -0.03790388446444469, -0.03640845615790006, -0.03494514338186967, -0.033513865580738045, -0.032114514162689456, -0.03074695353025116, -0.029411022120841204, -0.02810653345501263, -0.026833277190144025, -0.025591020177387177, -0.024379507519747327, -0.023198463629239992, -0.022047593281139036, -0.020926582663404407, -0.019835100419454146, -0.018772798682523163, -0.01773931409993139, -0.01673426884566489, -0.01575727161975638, -0.014807918633035, -0.013885794575898704, -0.01299047356984816, -0.012121520100604296, -0.01127848993171731, -0.010460930997658057, -0.009668384275466811, -0.008900384634116923, -0.008156461660832389, -0.007436140463679165, -0.006738942449828773, -0.006064386078970505, -0.005411987591424359, -0.0047812617105805165, -0.004171722319363438, -0.003582883110488157, -0.0030142582103441905, -0.0024653627764073902, -0.0019357135681431891, -0.00142482949142461, -0.0009322321165464668, -0.00045744616997189964] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005569789235979963, -0.0011511868365036088, -0.0017843708777576612, -0.0024582956327285988, -0.0031747371734441353, -0.003935476571358734, -0.004742292881864177, -0.0055969556036363265, -0.006501216619963141, -0.007456801633498077, -0.008465401110408877, -0.009528660754618144, -0.01064817153773015, -0.011825459315274466, -0.013061974065034367, -0.014359078788425163, -0.015718038121101924, -0.01714000670415766, -0.0186260173723744, -0.020176969220955833, -0.021793615616947717, -0.02347655222608414, -0.02522620513002706, -0.02704281911283505, -0.028926446198947693, -0.03087693452794766, -0.03289391765380795, -0.034976804358194294, -0.03712476906862259, -0.0393367429728213, -0.0416114059204795, -0.043947179202633004, -0.04634221929722585, -0.0487944126668571, -0.05130137169136548, -0.05386043181370927, -0.056468649972562845, -0.05912280438918338, -0.061819395769415475, -0.06455464997422558, -0.06732452220392378, -0.0701247027322831, -0.07295062421715823, -0.07579747060399732, -0.07866018762790321, -0.08153349490871255, -0.08441189962200639, -0.0872897117171403, -0.09016106064138082, -0.09301991351716427, -0.09586009470746126, -0.09867530669234667, -0.1014591521682524, -0.10420515727013695, -0.10690679580604875, -0.10955751438340824, -0.11215075829688949, -0.1146799980391549, -0.11713875628798097, -0.11952063521660539, -0.12181934396850563, -0.12402872613336488, -0.12614278705775545, -0.12815572082212665, -0.1300619367150651, -0.13185608503653046, -0.13353308206387204, -0.13508813401790787, -0.13651675987118153, -0.13781481284668262, -0.13897850046278096, -0.14000440298883388, -0.14088949018581032, -0.14163113621726153, -0.14222713262796105, -0.1426756993004409, -0.1429754933133505] + [-0.14312561563994552] * 2 + [-0.1429754933133505, -0.1426756993004409, -0.14222713262796105, -0.14163113621726153, -0.14088949018581032, -0.14000440298883388, -0.13897850046278096, -0.13781481284668262, -0.13651675987118153, -0.13508813401790787, -0.13353308206387204, -0.13185608503653046, -0.1300619367150651, -0.12815572082212665, -0.12614278705775545, -0.12402872613336488, -0.12181934396850563, -0.11952063521660539, -0.11713875628798097, -0.1146799980391549, -0.11215075829688949, -0.10955751438340824, -0.10690679580604875, -0.10420515727013695, -0.1014591521682524, -0.09867530669234667, -0.09586009470746126, -0.09301991351716427, -0.09016106064138082, -0.0872897117171403, -0.08441189962200639, -0.08153349490871255, -0.07866018762790321, -0.07579747060399732, -0.07295062421715823, -0.0701247027322831, -0.06732452220392378, -0.06455464997422558, -0.061819395769415475, -0.05912280438918338, -0.056468649972562845, -0.05386043181370927, -0.05130137169136548, -0.0487944126668571, -0.04634221929722585, -0.043947179202633004, -0.0416114059204795, -0.0393367429728213, -0.03712476906862259, -0.034976804358194294, -0.03289391765380795, -0.03087693452794766, -0.028926446198947693, -0.02704281911283505, -0.02522620513002706, -0.02347655222608414, -0.021793615616947717, -0.020176969220955833, -0.0186260173723744, -0.01714000670415766, -0.015718038121101924, -0.014359078788425163, -0.013061974065034367, -0.011825459315274466, -0.01064817153773015, -0.009528660754618144, -0.008465401110408877, -0.007456801633498077, -0.006501216619963141, -0.0055969556036363265, -0.004742292881864177, -0.003935476571358734, -0.0031747371734441353, -0.0024582956327285988, -0.0017843708777576612, -0.0011511868365036088, -0.0005569789235979963] + [0.0] * 3,
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
            "samples": [0.0010431184086790637, 0.001297437087971483, 0.001579419271390326, 0.0018906571247472115, 0.0022327747859784914, 0.0026074265218423314, 0.0030162947658382232, 0.003461088038651809, 0.003943538752722474, 0.004465400902827129, 0.005028447644869812, 0.005634468765363369, 0.00628526804438481, 0.006982660515079928, 0.007728469623084345, 0.00852452428951689, 0.009372655881485822, 0.010274695094328934, 0.011232468750083296, 0.012247796516949913, 0.013322487554780361, 0.014458337091867734, 0.01565712293857104, 0.016920601943539695, 0.018250506398533706, 0.019648540398052795, 0.02111637616019582, 0.02265565031536685, 0.024267960169629045, 0.02595485994967802, 0.027717857036564576, 0.029558408195441106, 0.03147791580873541, 0.03347772412027163, 0.03555911549795721, 0.03772330672274012, 0.03997144531160804, 0.042304605882454244, 0.044723786568669904, 0.04722990549134098, 0.04982379729692978, 0.05250620976830496, 0.05527780051695001, 0.058139133764130296, 0.06109067721872816, 0.06413279905937112, 0.06726576502837225, 0.07048973564488095, 0.07380476354450223, 0.07721079095248568, 0.08070764729741242, 0.08429504697211393, 0.0879725872483519, 0.09173974635156179, 0.09559588170172308, 0.09954022832616044, 0.10357189744981242, 0.10768987526821235, 0.11189302190813086, 0.11618007058050804, 0.12054962692998235, 0.12500016858497545, 0.12953004491194683, 0.13413747697706035, 0.13882055771813773, 0.14357725232938434, 0.1484053988609816, 0.15330270903523802, 0.15826676928058409, 0.16329504198427403, 0.16838486696424743, 0.1735334631601626, 0.1787379305432009, 0.18399525224379068, 0.1893022968959787, 0.1946558211967324, 0.2000524726780225, 0.20548879268910147, 0.21096121958595615, 0.21646609212448611, 0.22199965305352734, 0.22755805290342507, 0.23313735396543173, 0.23873353445681147, 0.24434249286611068, 0.24996005247267947, 0.2555819660341269, 0.26120392063503095, 0.2668215426898536, 0.2724304030926589, 0.27802602250590464, 0.28360387678023474, 0.2891594024969082, 0.29468800262419026, 0.3001850522787632, 0.30564590458294194, 0.3110658966082452, 0.31644035539563287, 0.32176460404252344, 0.32703396784650657, 0.33224378049550174, 0.33738939029395826, 0.3424661664145676, 0.34746950516484454, 0.35239483625785073, 0.3572376290762628, 0.3619933989189455, 0.36665771321916907, 0.3712261977236015, 0.37569454262123525, 0.38005850861144863, 0.3843139329004605, 0.3884567351155389, 0.3924829231264168, 0.39638859876350385, 0.40016996342264993, 0.40382332354636, 0.4073450959715863, 0.4107318131344117, 0.41398012812219737, 0.4170868195639962, 0.4200487963503368, 0.42286310217374873, 0.42552691988172936, 0.42803757563417577, 0.43039254285763634, 0.4325894459891301, 0.4346260640026206, 0.43650033371165115, 0.4382103528420395, 0.4397543828689488, 0.4411308516130899, 0.4423383555912364, 0.44337566211670193, 0.44424171114587985, 0.4449356168674101, 0.44545666903102915, 0.44580433401362796] + [0.44597825562053467] * 2 + [0.44580433401362796, 0.44545666903102915, 0.4449356168674101, 0.44424171114587985, 0.44337566211670193, 0.4423383555912364, 0.4411308516130899, 0.4397543828689488, 0.4382103528420395, 0.43650033371165115, 0.4346260640026206, 0.4325894459891301, 0.43039254285763634, 0.42803757563417577, 0.42552691988172936, 0.42286310217374873, 0.4200487963503368, 0.4170868195639962, 0.41398012812219737, 0.4107318131344117, 0.4073450959715863, 0.40382332354636, 0.40016996342264993, 0.39638859876350385, 0.3924829231264168, 0.3884567351155389, 0.3843139329004605, 0.38005850861144863, 0.37569454262123525, 0.3712261977236015, 0.36665771321916907, 0.3619933989189455, 0.3572376290762628, 0.35239483625785073, 0.34746950516484454, 0.3424661664145676, 0.33738939029395826, 0.33224378049550174, 0.32703396784650657, 0.32176460404252344, 0.31644035539563287, 0.3110658966082452, 0.30564590458294194, 0.3001850522787632, 0.29468800262419026, 0.2891594024969082, 0.28360387678023474, 0.27802602250590464, 0.2724304030926589, 0.2668215426898536, 0.26120392063503095, 0.2555819660341269, 0.24996005247267947, 0.24434249286611068, 0.23873353445681147, 0.23313735396543173, 0.22755805290342507, 0.22199965305352734, 0.21646609212448611, 0.21096121958595615, 0.20548879268910147, 0.2000524726780225, 0.1946558211967324, 0.1893022968959787, 0.18399525224379068, 0.1787379305432009, 0.1735334631601626, 0.16838486696424743, 0.16329504198427403, 0.15826676928058409, 0.15330270903523802, 0.1484053988609816, 0.14357725232938434, 0.13882055771813773, 0.13413747697706035, 0.12953004491194683, 0.12500016858497545, 0.12054962692998235, 0.11618007058050804, 0.11189302190813086, 0.10768987526821235, 0.10357189744981242, 0.09954022832616044, 0.09559588170172308, 0.09173974635156179, 0.0879725872483519, 0.08429504697211393, 0.08070764729741242, 0.07721079095248568, 0.07380476354450223, 0.07048973564488095, 0.06726576502837225, 0.06413279905937112, 0.06109067721872816, 0.058139133764130296, 0.05527780051695001, 0.05250620976830496, 0.04982379729692978, 0.04722990549134098, 0.044723786568669904, 0.042304605882454244, 0.03997144531160804, 0.03772330672274012, 0.03555911549795721, 0.03347772412027163, 0.03147791580873541, 0.029558408195441106, 0.027717857036564576, 0.02595485994967802, 0.024267960169629045, 0.02265565031536685, 0.02111637616019582, 0.019648540398052795, 0.018250506398533706, 0.016920601943539695, 0.01565712293857104, 0.014458337091867734, 0.013322487554780361, 0.012247796516949913, 0.011232468750083296, 0.010274695094328934, 0.009372655881485822, 0.00852452428951689, 0.007728469623084345, 0.006982660515079928, 0.00628526804438481, 0.005634468765363369, 0.005028447644869812, 0.004465400902827129, 0.003943538752722474, 0.003461088038651809, 0.0030162947658382232, 0.0026074265218423314, 0.0022327747859784914, 0.0018906571247472115, 0.001579419271390326, 0.001297437087971483, 0.0010431184086790637] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0005215592043395318, 0.0006487185439857415, 0.000789709635695163, 0.0009453285623736057, 0.0011163873929892457, 0.0013037132609211657, 0.0015081473829191116, 0.0017305440193259045, 0.001971769376361237, 0.0022327004514135643, 0.002514223822434906, 0.0028172343826816846, 0.003142634022192405, 0.003491330257539964, 0.0038642348115421727, 0.004262262144758445, 0.004686327940742911, 0.005137347547164467, 0.005616234375041648, 0.006123898258474957, 0.006661243777390181, 0.007229168545933867, 0.00782856146928552, 0.008460300971769847, 0.009125253199266853, 0.009824270199026397, 0.01055818808009791, 0.011327825157683425, 0.012133980084814523, 0.01297742997483901, 0.013858928518282288, 0.014779204097720553, 0.015738957904367704, 0.016738862060135817, 0.017779557748978606, 0.01886165336137006, 0.01998572265580402, 0.021152302941227122, 0.022361893284334952, 0.02361495274567049, 0.02491189864846489, 0.02625310488415248, 0.027638900258475006, 0.029069566882065148, 0.03054533860936408, 0.03206639952968556, 0.03363288251418613, 0.035244867822440476, 0.036902381772251115, 0.03860539547624284, 0.04035382364870621, 0.042147523486056965, 0.04398629362417595, 0.045869873175780895, 0.04779794085086154, 0.04977011416308022, 0.05178594872490621, 0.05384493763410617, 0.05594651095406543, 0.05809003529025402, 0.060274813464991174, 0.06250008429248773, 0.06476502245597342, 0.06706873848853018, 0.06941027885906886, 0.07178862616469217, 0.0742026994304908, 0.07665135451761901, 0.07913338464029204, 0.08164752099213701, 0.08419243348212371, 0.0867667315800813, 0.08936896527160045, 0.09199762612189534, 0.09465114844798934, 0.0973279105983662, 0.10002623633901125, 0.10274439634455074, 0.10548060979297808, 0.10823304606224306, 0.11099982652676367, 0.11377902645171253, 0.11656867698271586, 0.11936676722840574, 0.12217124643305534, 0.12498002623633973, 0.12779098301706346, 0.13060196031751548, 0.1334107713449268, 0.13621520154632946, 0.13901301125295232, 0.14180193839011737, 0.1445797012484541, 0.14734400131209513, 0.1500925261393816, 0.15282295229147097, 0.1555329483041226, 0.15822017769781643, 0.16088230202126172, 0.16351698392325328, 0.16612189024775087, 0.16869469514697913, 0.1712330832072838, 0.17373475258242227, 0.17619741812892536, 0.1786188145381314, 0.18099669945947275, 0.18332885660958453, 0.18561309886180075, 0.18784727131061763, 0.19002925430572432, 0.19215696645023025, 0.19422836755776945, 0.1962414615632084, 0.19819429938175193, 0.20008498171132497, 0.20191166177318, 0.20367254798579315, 0.20536590656720585, 0.20699006406109868, 0.2085434097819981, 0.2100243981751684, 0.21143155108687436, 0.21276345994086468, 0.21401878781708789, 0.21519627142881817, 0.21629472299456504, 0.2173130320013103, 0.21825016685582557, 0.21910517642101976, 0.2198771914344744, 0.22056542580654495, 0.2211691777956182, 0.22168783105835096, 0.22212085557293992, 0.22246780843370506, 0.22272833451551458, 0.22290216700681398] + [0.22298912781026733] * 2 + [0.22290216700681398, 0.22272833451551458, 0.22246780843370506, 0.22212085557293992, 0.22168783105835096, 0.2211691777956182, 0.22056542580654495, 0.2198771914344744, 0.21910517642101976, 0.21825016685582557, 0.2173130320013103, 0.21629472299456504, 0.21519627142881817, 0.21401878781708789, 0.21276345994086468, 0.21143155108687436, 0.2100243981751684, 0.2085434097819981, 0.20699006406109868, 0.20536590656720585, 0.20367254798579315, 0.20191166177318, 0.20008498171132497, 0.19819429938175193, 0.1962414615632084, 0.19422836755776945, 0.19215696645023025, 0.19002925430572432, 0.18784727131061763, 0.18561309886180075, 0.18332885660958453, 0.18099669945947275, 0.1786188145381314, 0.17619741812892536, 0.17373475258242227, 0.1712330832072838, 0.16869469514697913, 0.16612189024775087, 0.16351698392325328, 0.16088230202126172, 0.15822017769781643, 0.1555329483041226, 0.15282295229147097, 0.1500925261393816, 0.14734400131209513, 0.1445797012484541, 0.14180193839011737, 0.13901301125295232, 0.13621520154632946, 0.1334107713449268, 0.13060196031751548, 0.12779098301706346, 0.12498002623633973, 0.12217124643305534, 0.11936676722840574, 0.11656867698271586, 0.11377902645171253, 0.11099982652676367, 0.10823304606224306, 0.10548060979297808, 0.10274439634455074, 0.10002623633901125, 0.0973279105983662, 0.09465114844798934, 0.09199762612189534, 0.08936896527160045, 0.0867667315800813, 0.08419243348212371, 0.08164752099213701, 0.07913338464029204, 0.07665135451761901, 0.0742026994304908, 0.07178862616469217, 0.06941027885906886, 0.06706873848853018, 0.06476502245597342, 0.06250008429248773, 0.060274813464991174, 0.05809003529025402, 0.05594651095406543, 0.05384493763410617, 0.05178594872490621, 0.04977011416308022, 0.04779794085086154, 0.045869873175780895, 0.04398629362417595, 0.042147523486056965, 0.04035382364870621, 0.03860539547624284, 0.036902381772251115, 0.035244867822440476, 0.03363288251418613, 0.03206639952968556, 0.03054533860936408, 0.029069566882065148, 0.027638900258475006, 0.02625310488415248, 0.02491189864846489, 0.02361495274567049, 0.022361893284334952, 0.021152302941227122, 0.01998572265580402, 0.01886165336137006, 0.017779557748978606, 0.016738862060135817, 0.015738957904367704, 0.014779204097720553, 0.013858928518282288, 0.01297742997483901, 0.012133980084814523, 0.011327825157683425, 0.01055818808009791, 0.009824270199026397, 0.009125253199266853, 0.008460300971769847, 0.00782856146928552, 0.007229168545933867, 0.006661243777390181, 0.006123898258474957, 0.005616234375041648, 0.005137347547164467, 0.004686327940742911, 0.004262262144758445, 0.0038642348115421727, 0.003491330257539964, 0.003142634022192405, 0.0028172343826816846, 0.002514223822434906, 0.0022327004514135643, 0.001971769376361237, 0.0017305440193259045, 0.0015081473829191116, 0.0013037132609211657, 0.0011163873929892457, 0.0009453285623736057, 0.000789709635695163, 0.0006487185439857415, 0.0005215592043395318] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0005215592043395318, -0.0006487185439857415, -0.000789709635695163, -0.0009453285623736057, -0.0011163873929892457, -0.0013037132609211657, -0.0015081473829191116, -0.0017305440193259045, -0.001971769376361237, -0.0022327004514135643, -0.002514223822434906, -0.0028172343826816846, -0.003142634022192405, -0.003491330257539964, -0.0038642348115421727, -0.004262262144758445, -0.004686327940742911, -0.005137347547164467, -0.005616234375041648, -0.006123898258474957, -0.006661243777390181, -0.007229168545933867, -0.00782856146928552, -0.008460300971769847, -0.009125253199266853, -0.009824270199026397, -0.01055818808009791, -0.011327825157683425, -0.012133980084814523, -0.01297742997483901, -0.013858928518282288, -0.014779204097720553, -0.015738957904367704, -0.016738862060135817, -0.017779557748978606, -0.01886165336137006, -0.01998572265580402, -0.021152302941227122, -0.022361893284334952, -0.02361495274567049, -0.02491189864846489, -0.02625310488415248, -0.027638900258475006, -0.029069566882065148, -0.03054533860936408, -0.03206639952968556, -0.03363288251418613, -0.035244867822440476, -0.036902381772251115, -0.03860539547624284, -0.04035382364870621, -0.042147523486056965, -0.04398629362417595, -0.045869873175780895, -0.04779794085086154, -0.04977011416308022, -0.05178594872490621, -0.05384493763410617, -0.05594651095406543, -0.05809003529025402, -0.060274813464991174, -0.06250008429248773, -0.06476502245597342, -0.06706873848853018, -0.06941027885906886, -0.07178862616469217, -0.0742026994304908, -0.07665135451761901, -0.07913338464029204, -0.08164752099213701, -0.08419243348212371, -0.0867667315800813, -0.08936896527160045, -0.09199762612189534, -0.09465114844798934, -0.0973279105983662, -0.10002623633901125, -0.10274439634455074, -0.10548060979297808, -0.10823304606224306, -0.11099982652676367, -0.11377902645171253, -0.11656867698271586, -0.11936676722840574, -0.12217124643305534, -0.12498002623633973, -0.12779098301706346, -0.13060196031751548, -0.1334107713449268, -0.13621520154632946, -0.13901301125295232, -0.14180193839011737, -0.1445797012484541, -0.14734400131209513, -0.1500925261393816, -0.15282295229147097, -0.1555329483041226, -0.15822017769781643, -0.16088230202126172, -0.16351698392325328, -0.16612189024775087, -0.16869469514697913, -0.1712330832072838, -0.17373475258242227, -0.17619741812892536, -0.1786188145381314, -0.18099669945947275, -0.18332885660958453, -0.18561309886180075, -0.18784727131061763, -0.19002925430572432, -0.19215696645023025, -0.19422836755776945, -0.1962414615632084, -0.19819429938175193, -0.20008498171132497, -0.20191166177318, -0.20367254798579315, -0.20536590656720585, -0.20699006406109868, -0.2085434097819981, -0.2100243981751684, -0.21143155108687436, -0.21276345994086468, -0.21401878781708789, -0.21519627142881817, -0.21629472299456504, -0.2173130320013103, -0.21825016685582557, -0.21910517642101976, -0.2198771914344744, -0.22056542580654495, -0.2211691777956182, -0.22168783105835096, -0.22212085557293992, -0.22246780843370506, -0.22272833451551458, -0.22290216700681398] + [-0.22298912781026733] * 2 + [-0.22290216700681398, -0.22272833451551458, -0.22246780843370506, -0.22212085557293992, -0.22168783105835096, -0.2211691777956182, -0.22056542580654495, -0.2198771914344744, -0.21910517642101976, -0.21825016685582557, -0.2173130320013103, -0.21629472299456504, -0.21519627142881817, -0.21401878781708789, -0.21276345994086468, -0.21143155108687436, -0.2100243981751684, -0.2085434097819981, -0.20699006406109868, -0.20536590656720585, -0.20367254798579315, -0.20191166177318, -0.20008498171132497, -0.19819429938175193, -0.1962414615632084, -0.19422836755776945, -0.19215696645023025, -0.19002925430572432, -0.18784727131061763, -0.18561309886180075, -0.18332885660958453, -0.18099669945947275, -0.1786188145381314, -0.17619741812892536, -0.17373475258242227, -0.1712330832072838, -0.16869469514697913, -0.16612189024775087, -0.16351698392325328, -0.16088230202126172, -0.15822017769781643, -0.1555329483041226, -0.15282295229147097, -0.1500925261393816, -0.14734400131209513, -0.1445797012484541, -0.14180193839011737, -0.13901301125295232, -0.13621520154632946, -0.1334107713449268, -0.13060196031751548, -0.12779098301706346, -0.12498002623633973, -0.12217124643305534, -0.11936676722840574, -0.11656867698271586, -0.11377902645171253, -0.11099982652676367, -0.10823304606224306, -0.10548060979297808, -0.10274439634455074, -0.10002623633901125, -0.0973279105983662, -0.09465114844798934, -0.09199762612189534, -0.08936896527160045, -0.0867667315800813, -0.08419243348212371, -0.08164752099213701, -0.07913338464029204, -0.07665135451761901, -0.0742026994304908, -0.07178862616469217, -0.06941027885906886, -0.06706873848853018, -0.06476502245597342, -0.06250008429248773, -0.060274813464991174, -0.05809003529025402, -0.05594651095406543, -0.05384493763410617, -0.05178594872490621, -0.04977011416308022, -0.04779794085086154, -0.045869873175780895, -0.04398629362417595, -0.042147523486056965, -0.04035382364870621, -0.03860539547624284, -0.036902381772251115, -0.035244867822440476, -0.03363288251418613, -0.03206639952968556, -0.03054533860936408, -0.029069566882065148, -0.027638900258475006, -0.02625310488415248, -0.02491189864846489, -0.02361495274567049, -0.022361893284334952, -0.021152302941227122, -0.01998572265580402, -0.01886165336137006, -0.017779557748978606, -0.016738862060135817, -0.015738957904367704, -0.014779204097720553, -0.013858928518282288, -0.01297742997483901, -0.012133980084814523, -0.011327825157683425, -0.01055818808009791, -0.009824270199026397, -0.009125253199266853, -0.008460300971769847, -0.00782856146928552, -0.007229168545933867, -0.006661243777390181, -0.006123898258474957, -0.005616234375041648, -0.005137347547164467, -0.004686327940742911, -0.004262262144758445, -0.0038642348115421727, -0.003491330257539964, -0.003142634022192405, -0.0028172343826816846, -0.002514223822434906, -0.0022327004514135643, -0.001971769376361237, -0.0017305440193259045, -0.0015081473829191116, -0.0013037132609211657, -0.0011163873929892457, -0.0009453285623736057, -0.000789709635695163, -0.0006487185439857415, -0.0005215592043395318] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0010431184086790637, 0.001297437087971483, 0.001579419271390326, 0.0018906571247472115, 0.0022327747859784914, 0.0026074265218423314, 0.0030162947658382232, 0.003461088038651809, 0.003943538752722474, 0.004465400902827129, 0.005028447644869812, 0.005634468765363369, 0.00628526804438481, 0.006982660515079928, 0.007728469623084345, 0.00852452428951689, 0.009372655881485822, 0.010274695094328934, 0.011232468750083296, 0.012247796516949913, 0.013322487554780361, 0.014458337091867734, 0.01565712293857104, 0.016920601943539695, 0.018250506398533706, 0.019648540398052795, 0.02111637616019582, 0.02265565031536685, 0.024267960169629045, 0.02595485994967802, 0.027717857036564576, 0.029558408195441106, 0.03147791580873541, 0.03347772412027163, 0.03555911549795721, 0.03772330672274012, 0.03997144531160804, 0.042304605882454244, 0.044723786568669904, 0.04722990549134098, 0.04982379729692978, 0.05250620976830496, 0.05527780051695001, 0.058139133764130296, 0.06109067721872816, 0.06413279905937112, 0.06726576502837225, 0.07048973564488095, 0.07380476354450223, 0.07721079095248568, 0.08070764729741242, 0.08429504697211393, 0.0879725872483519, 0.09173974635156179, 0.09559588170172308, 0.09954022832616044, 0.10357189744981242, 0.10768987526821235, 0.11189302190813086, 0.11618007058050804, 0.12054962692998235, 0.12500016858497545, 0.12953004491194683, 0.13413747697706035, 0.13882055771813773, 0.14357725232938434, 0.1484053988609816, 0.15330270903523802, 0.15826676928058409, 0.16329504198427403, 0.16838486696424743, 0.1735334631601626, 0.1787379305432009, 0.18399525224379068, 0.1893022968959787, 0.1946558211967324, 0.2000524726780225, 0.20548879268910147, 0.21096121958595615, 0.21646609212448611, 0.22199965305352734, 0.22755805290342507, 0.23313735396543173, 0.23873353445681147, 0.24434249286611068, 0.24996005247267947, 0.2555819660341269, 0.26120392063503095, 0.2668215426898536, 0.2724304030926589, 0.27802602250590464, 0.28360387678023474, 0.2891594024969082, 0.29468800262419026, 0.3001850522787632, 0.30564590458294194, 0.3110658966082452, 0.31644035539563287, 0.32176460404252344, 0.32703396784650657, 0.33224378049550174, 0.33738939029395826, 0.3424661664145676, 0.34746950516484454, 0.35239483625785073, 0.3572376290762628, 0.3619933989189455, 0.36665771321916907, 0.3712261977236015, 0.37569454262123525, 0.38005850861144863, 0.3843139329004605, 0.3884567351155389, 0.3924829231264168, 0.39638859876350385, 0.40016996342264993, 0.40382332354636, 0.4073450959715863, 0.4107318131344117, 0.41398012812219737, 0.4170868195639962, 0.4200487963503368, 0.42286310217374873, 0.42552691988172936, 0.42803757563417577, 0.43039254285763634, 0.4325894459891301, 0.4346260640026206, 0.43650033371165115, 0.4382103528420395, 0.4397543828689488, 0.4411308516130899, 0.4423383555912364, 0.44337566211670193, 0.44424171114587985, 0.4449356168674101, 0.44545666903102915, 0.44580433401362796] + [0.44597825562053467] * 2 + [0.44580433401362796, 0.44545666903102915, 0.4449356168674101, 0.44424171114587985, 0.44337566211670193, 0.4423383555912364, 0.4411308516130899, 0.4397543828689488, 0.4382103528420395, 0.43650033371165115, 0.4346260640026206, 0.4325894459891301, 0.43039254285763634, 0.42803757563417577, 0.42552691988172936, 0.42286310217374873, 0.4200487963503368, 0.4170868195639962, 0.41398012812219737, 0.4107318131344117, 0.4073450959715863, 0.40382332354636, 0.40016996342264993, 0.39638859876350385, 0.3924829231264168, 0.3884567351155389, 0.3843139329004605, 0.38005850861144863, 0.37569454262123525, 0.3712261977236015, 0.36665771321916907, 0.3619933989189455, 0.3572376290762628, 0.35239483625785073, 0.34746950516484454, 0.3424661664145676, 0.33738939029395826, 0.33224378049550174, 0.32703396784650657, 0.32176460404252344, 0.31644035539563287, 0.3110658966082452, 0.30564590458294194, 0.3001850522787632, 0.29468800262419026, 0.2891594024969082, 0.28360387678023474, 0.27802602250590464, 0.2724304030926589, 0.2668215426898536, 0.26120392063503095, 0.2555819660341269, 0.24996005247267947, 0.24434249286611068, 0.23873353445681147, 0.23313735396543173, 0.22755805290342507, 0.22199965305352734, 0.21646609212448611, 0.21096121958595615, 0.20548879268910147, 0.2000524726780225, 0.1946558211967324, 0.1893022968959787, 0.18399525224379068, 0.1787379305432009, 0.1735334631601626, 0.16838486696424743, 0.16329504198427403, 0.15826676928058409, 0.15330270903523802, 0.1484053988609816, 0.14357725232938434, 0.13882055771813773, 0.13413747697706035, 0.12953004491194683, 0.12500016858497545, 0.12054962692998235, 0.11618007058050804, 0.11189302190813086, 0.10768987526821235, 0.10357189744981242, 0.09954022832616044, 0.09559588170172308, 0.09173974635156179, 0.0879725872483519, 0.08429504697211393, 0.08070764729741242, 0.07721079095248568, 0.07380476354450223, 0.07048973564488095, 0.06726576502837225, 0.06413279905937112, 0.06109067721872816, 0.058139133764130296, 0.05527780051695001, 0.05250620976830496, 0.04982379729692978, 0.04722990549134098, 0.044723786568669904, 0.042304605882454244, 0.03997144531160804, 0.03772330672274012, 0.03555911549795721, 0.03347772412027163, 0.03147791580873541, 0.029558408195441106, 0.027717857036564576, 0.02595485994967802, 0.024267960169629045, 0.02265565031536685, 0.02111637616019582, 0.019648540398052795, 0.018250506398533706, 0.016920601943539695, 0.01565712293857104, 0.014458337091867734, 0.013322487554780361, 0.012247796516949913, 0.011232468750083296, 0.010274695094328934, 0.009372655881485822, 0.00852452428951689, 0.007728469623084345, 0.006982660515079928, 0.00628526804438481, 0.005634468765363369, 0.005028447644869812, 0.004465400902827129, 0.003943538752722474, 0.003461088038651809, 0.0030162947658382232, 0.0026074265218423314, 0.0022327747859784914, 0.0018906571247472115, 0.001579419271390326, 0.001297437087971483, 0.0010431184086790637] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.000701649153819998, 0.0010159571126778081, 0.0013907423165435595, 0.0018320196697535899, 0.0023459935169274186, 0.0029390338564037307, 0.003617650216413644, 0.004388463268933603, 0.0052581742748428265, 0.0062335324725631275, 0.007321300540638395, 0.00852821828257141, 0.009860964699533133, 0.011326118633149638, 0.01293011817631418, 0.014679219064728626, 0.016579452275517693, 0.0186365810716535, 0.020856057741958194, 0.023242980296007108, 0.025802049381231023, 0.028537525695821846, 0.031453188175600305, 0.03455229323573553, 0.037837535349060654, 0.041311009241657634, 0.04497417398336164, 0.04882781924584117, 0.05287203399394496, 0.05710617786708141, 0.06152885549653901, 0.06613789399190939, 0.07093032381519439, 0.07590236324483655, 0.0810494066138928, 0.08636601648697459, 0.091845919919515, 0.09748200892051599, 0.10326634521631788, 0.10919016938826173, 0.11524391443153494, 0.12141722375617628, 0.12769897362432925, 0.1340772999905569, 0.14053962968455128, 0.14707271584806286, 0.15366267751054916, 0.16029504316105583, 0.16695479814742795, 0.17362643570824945, 0.1802940114181382, 0.18694120080335544, 0.1935513598622827, 0.2001075882043579, 0.20659279450169943, 0.21298976393001356, 0.21928122725963997, 0.22544993124384313, 0.23147870993982203, 0.23735055658848553, 0.2430486956719127, 0.2485566547626275, 0.2538583357764537, 0.2589380852407734, 0.26378076319253674, 0.2683718103253363, 0.27269731301227307, 0.2767440658411379, 0.2804996313105908, 0.28395239635044295, 0.28709162534576393, 0.28990750936325177, 0.29239121129897194, 0.29453490668910687, 0.29633181994956703, 0.29777625583609013, 0.29886362594358246, 0.2995904700917974] + [0.2999544724737967] * 2 + [0.2995904700917974, 0.29886362594358246, 0.29777625583609013, 0.29633181994956703, 0.29453490668910687, 0.29239121129897194, 0.28990750936325177, 0.28709162534576393, 0.28395239635044295, 0.2804996313105908, 0.2767440658411379, 0.27269731301227307, 0.2683718103253363, 0.26378076319253674, 0.2589380852407734, 0.2538583357764537, 0.2485566547626275, 0.2430486956719127, 0.23735055658848553, 0.23147870993982203, 0.22544993124384313, 0.21928122725963997, 0.21298976393001356, 0.20659279450169943, 0.2001075882043579, 0.1935513598622827, 0.18694120080335544, 0.1802940114181382, 0.17362643570824945, 0.16695479814742795, 0.16029504316105583, 0.15366267751054916, 0.14707271584806286, 0.14053962968455128, 0.1340772999905569, 0.12769897362432925, 0.12141722375617628, 0.11524391443153494, 0.10919016938826173, 0.10326634521631788, 0.09748200892051599, 0.091845919919515, 0.08636601648697459, 0.0810494066138928, 0.07590236324483655, 0.07093032381519439, 0.06613789399190939, 0.06152885549653901, 0.05710617786708141, 0.05287203399394496, 0.04882781924584117, 0.04497417398336164, 0.041311009241657634, 0.037837535349060654, 0.03455229323573553, 0.031453188175600305, 0.028537525695821846, 0.025802049381231023, 0.023242980296007108, 0.020856057741958194, 0.0186365810716535, 0.016579452275517693, 0.014679219064728626, 0.01293011817631418, 0.011326118633149638, 0.009860964699533133, 0.00852821828257141, 0.007321300540638395, 0.0062335324725631275, 0.0052581742748428265, 0.004388463268933603, 0.003617650216413644, 0.0029390338564037307, 0.0023459935169274186, 0.0018320196697535899, 0.0013907423165435595, 0.0010159571126778081, 0.000701649153819998] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0005215592043395318, 0.0006487185439857415, 0.000789709635695163, 0.0009453285623736057, 0.0011163873929892457, 0.0013037132609211657, 0.0015081473829191116, 0.0017305440193259045, 0.001971769376361237, 0.0022327004514135643, 0.002514223822434906, 0.0028172343826816846, 0.003142634022192405, 0.003491330257539964, 0.0038642348115421727, 0.004262262144758445, 0.004686327940742911, 0.005137347547164467, 0.005616234375041648, 0.006123898258474957, 0.006661243777390181, 0.007229168545933867, 0.00782856146928552, 0.008460300971769847, 0.009125253199266853, 0.009824270199026397, 0.01055818808009791, 0.011327825157683425, 0.012133980084814523, 0.01297742997483901, 0.013858928518282288, 0.014779204097720553, 0.015738957904367704, 0.016738862060135817, 0.017779557748978606, 0.01886165336137006, 0.01998572265580402, 0.021152302941227122, 0.022361893284334952, 0.02361495274567049, 0.02491189864846489, 0.02625310488415248, 0.027638900258475006, 0.029069566882065148, 0.03054533860936408, 0.03206639952968556, 0.03363288251418613, 0.035244867822440476, 0.036902381772251115, 0.03860539547624284, 0.04035382364870621, 0.042147523486056965, 0.04398629362417595, 0.045869873175780895, 0.04779794085086154, 0.04977011416308022, 0.05178594872490621, 0.05384493763410617, 0.05594651095406543, 0.05809003529025402, 0.060274813464991174, 0.06250008429248773, 0.06476502245597342, 0.06706873848853018, 0.06941027885906886, 0.07178862616469217, 0.0742026994304908, 0.07665135451761901, 0.07913338464029204, 0.08164752099213701, 0.08419243348212371, 0.0867667315800813, 0.08936896527160045, 0.09199762612189534, 0.09465114844798934, 0.0973279105983662, 0.10002623633901125, 0.10274439634455074, 0.10548060979297808, 0.10823304606224306, 0.11099982652676367, 0.11377902645171253, 0.11656867698271586, 0.11936676722840574, 0.12217124643305534, 0.12498002623633973, 0.12779098301706346, 0.13060196031751548, 0.1334107713449268, 0.13621520154632946, 0.13901301125295232, 0.14180193839011737, 0.1445797012484541, 0.14734400131209513, 0.1500925261393816, 0.15282295229147097, 0.1555329483041226, 0.15822017769781643, 0.16088230202126172, 0.16351698392325328, 0.16612189024775087, 0.16869469514697913, 0.1712330832072838, 0.17373475258242227, 0.17619741812892536, 0.1786188145381314, 0.18099669945947275, 0.18332885660958453, 0.18561309886180075, 0.18784727131061763, 0.19002925430572432, 0.19215696645023025, 0.19422836755776945, 0.1962414615632084, 0.19819429938175193, 0.20008498171132497, 0.20191166177318, 0.20367254798579315, 0.20536590656720585, 0.20699006406109868, 0.2085434097819981, 0.2100243981751684, 0.21143155108687436, 0.21276345994086468, 0.21401878781708789, 0.21519627142881817, 0.21629472299456504, 0.2173130320013103, 0.21825016685582557, 0.21910517642101976, 0.2198771914344744, 0.22056542580654495, 0.2211691777956182, 0.22168783105835096, 0.22212085557293992, 0.22246780843370506, 0.22272833451551458, 0.22290216700681398] + [0.22298912781026733] * 2 + [0.22290216700681398, 0.22272833451551458, 0.22246780843370506, 0.22212085557293992, 0.22168783105835096, 0.2211691777956182, 0.22056542580654495, 0.2198771914344744, 0.21910517642101976, 0.21825016685582557, 0.2173130320013103, 0.21629472299456504, 0.21519627142881817, 0.21401878781708789, 0.21276345994086468, 0.21143155108687436, 0.2100243981751684, 0.2085434097819981, 0.20699006406109868, 0.20536590656720585, 0.20367254798579315, 0.20191166177318, 0.20008498171132497, 0.19819429938175193, 0.1962414615632084, 0.19422836755776945, 0.19215696645023025, 0.19002925430572432, 0.18784727131061763, 0.18561309886180075, 0.18332885660958453, 0.18099669945947275, 0.1786188145381314, 0.17619741812892536, 0.17373475258242227, 0.1712330832072838, 0.16869469514697913, 0.16612189024775087, 0.16351698392325328, 0.16088230202126172, 0.15822017769781643, 0.1555329483041226, 0.15282295229147097, 0.1500925261393816, 0.14734400131209513, 0.1445797012484541, 0.14180193839011737, 0.13901301125295232, 0.13621520154632946, 0.1334107713449268, 0.13060196031751548, 0.12779098301706346, 0.12498002623633973, 0.12217124643305534, 0.11936676722840574, 0.11656867698271586, 0.11377902645171253, 0.11099982652676367, 0.10823304606224306, 0.10548060979297808, 0.10274439634455074, 0.10002623633901125, 0.0973279105983662, 0.09465114844798934, 0.09199762612189534, 0.08936896527160045, 0.0867667315800813, 0.08419243348212371, 0.08164752099213701, 0.07913338464029204, 0.07665135451761901, 0.0742026994304908, 0.07178862616469217, 0.06941027885906886, 0.06706873848853018, 0.06476502245597342, 0.06250008429248773, 0.060274813464991174, 0.05809003529025402, 0.05594651095406543, 0.05384493763410617, 0.05178594872490621, 0.04977011416308022, 0.04779794085086154, 0.045869873175780895, 0.04398629362417595, 0.042147523486056965, 0.04035382364870621, 0.03860539547624284, 0.036902381772251115, 0.035244867822440476, 0.03363288251418613, 0.03206639952968556, 0.03054533860936408, 0.029069566882065148, 0.027638900258475006, 0.02625310488415248, 0.02491189864846489, 0.02361495274567049, 0.022361893284334952, 0.021152302941227122, 0.01998572265580402, 0.01886165336137006, 0.017779557748978606, 0.016738862060135817, 0.015738957904367704, 0.014779204097720553, 0.013858928518282288, 0.01297742997483901, 0.012133980084814523, 0.011327825157683425, 0.01055818808009791, 0.009824270199026397, 0.009125253199266853, 0.008460300971769847, 0.00782856146928552, 0.007229168545933867, 0.006661243777390181, 0.006123898258474957, 0.005616234375041648, 0.005137347547164467, 0.004686327940742911, 0.004262262144758445, 0.0038642348115421727, 0.003491330257539964, 0.003142634022192405, 0.0028172343826816846, 0.002514223822434906, 0.0022327004514135643, 0.001971769376361237, 0.0017305440193259045, 0.0015081473829191116, 0.0013037132609211657, 0.0011163873929892457, 0.0009453285623736057, 0.000789709635695163, 0.0006487185439857415, 0.0005215592043395318] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.000350824576909999, 0.0005079785563389041, 0.0006953711582717798, 0.0009160098348767949, 0.0011729967584637093, 0.0014695169282018653, 0.001808825108206822, 0.0021942316344668016, 0.0026290871374214132, 0.0031167662362815637, 0.0036606502703191977, 0.004264109141285705, 0.004930482349766566, 0.005663059316574819, 0.00646505908815709, 0.007339609532364313, 0.008289726137758847, 0.00931829053582675, 0.010428028870979097, 0.011621490148003554, 0.012901024690615511, 0.014268762847910923, 0.015726594087800153, 0.017276146617867767, 0.018918767674530327, 0.020655504620828817, 0.02248708699168082, 0.024413909622920584, 0.02643601699697248, 0.028553088933540704, 0.030764427748269506, 0.033068946995954696, 0.035465161907597194, 0.03795118162241828, 0.0405247033069464, 0.043183008243487295, 0.0459229599597575, 0.048741004460257996, 0.05163317260815894, 0.054595084694130866, 0.05762195721576747, 0.06070861187808814, 0.06384948681216462, 0.06703864999527845, 0.07026981484227564, 0.07353635792403143, 0.07683133875527458, 0.08014752158052792, 0.08347739907371397, 0.08681321785412473, 0.0901470057090691, 0.09347060040167772, 0.09677567993114135, 0.10005379410217895, 0.10329639725084971, 0.10649488196500678, 0.10964061362981999, 0.11272496562192157, 0.11573935496991102, 0.11867527829424276, 0.12152434783595635, 0.12427832738131375, 0.12692916788822686, 0.1294690426203867, 0.13189038159626837, 0.13418590516266815, 0.13634865650613653, 0.13837203292056896, 0.1402498156552954, 0.14197619817522147, 0.14354581267288197, 0.14495375468162588, 0.14619560564948597, 0.14726745334455343, 0.14816590997478352, 0.14888812791804507, 0.14943181297179123, 0.1497952350458987] + [0.14997723623689835] * 2 + [0.1497952350458987, 0.14943181297179123, 0.14888812791804507, 0.14816590997478352, 0.14726745334455343, 0.14619560564948597, 0.14495375468162588, 0.14354581267288197, 0.14197619817522147, 0.1402498156552954, 0.13837203292056896, 0.13634865650613653, 0.13418590516266815, 0.13189038159626837, 0.1294690426203867, 0.12692916788822686, 0.12427832738131375, 0.12152434783595635, 0.11867527829424276, 0.11573935496991102, 0.11272496562192157, 0.10964061362981999, 0.10649488196500678, 0.10329639725084971, 0.10005379410217895, 0.09677567993114135, 0.09347060040167772, 0.0901470057090691, 0.08681321785412473, 0.08347739907371397, 0.08014752158052792, 0.07683133875527458, 0.07353635792403143, 0.07026981484227564, 0.06703864999527845, 0.06384948681216462, 0.06070861187808814, 0.05762195721576747, 0.054595084694130866, 0.05163317260815894, 0.048741004460257996, 0.0459229599597575, 0.043183008243487295, 0.0405247033069464, 0.03795118162241828, 0.035465161907597194, 0.033068946995954696, 0.030764427748269506, 0.028553088933540704, 0.02643601699697248, 0.024413909622920584, 0.02248708699168082, 0.020655504620828817, 0.018918767674530327, 0.017276146617867767, 0.015726594087800153, 0.014268762847910923, 0.012901024690615511, 0.011621490148003554, 0.010428028870979097, 0.00931829053582675, 0.008289726137758847, 0.007339609532364313, 0.00646505908815709, 0.005663059316574819, 0.004930482349766566, 0.004264109141285705, 0.0036606502703191977, 0.0031167662362815637, 0.0026290871374214132, 0.0021942316344668016, 0.001808825108206822, 0.0014695169282018653, 0.0011729967584637093, 0.0009160098348767949, 0.0006953711582717798, 0.0005079785563389041, 0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 280,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 160,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0005215592043395318, -0.0006487185439857415, -0.000789709635695163, -0.0009453285623736057, -0.0011163873929892457, -0.0013037132609211657, -0.0015081473829191116, -0.0017305440193259045, -0.001971769376361237, -0.0022327004514135643, -0.002514223822434906, -0.0028172343826816846, -0.003142634022192405, -0.003491330257539964, -0.0038642348115421727, -0.004262262144758445, -0.004686327940742911, -0.005137347547164467, -0.005616234375041648, -0.006123898258474957, -0.006661243777390181, -0.007229168545933867, -0.00782856146928552, -0.008460300971769847, -0.009125253199266853, -0.009824270199026397, -0.01055818808009791, -0.011327825157683425, -0.012133980084814523, -0.01297742997483901, -0.013858928518282288, -0.014779204097720553, -0.015738957904367704, -0.016738862060135817, -0.017779557748978606, -0.01886165336137006, -0.01998572265580402, -0.021152302941227122, -0.022361893284334952, -0.02361495274567049, -0.02491189864846489, -0.02625310488415248, -0.027638900258475006, -0.029069566882065148, -0.03054533860936408, -0.03206639952968556, -0.03363288251418613, -0.035244867822440476, -0.036902381772251115, -0.03860539547624284, -0.04035382364870621, -0.042147523486056965, -0.04398629362417595, -0.045869873175780895, -0.04779794085086154, -0.04977011416308022, -0.05178594872490621, -0.05384493763410617, -0.05594651095406543, -0.05809003529025402, -0.060274813464991174, -0.06250008429248773, -0.06476502245597342, -0.06706873848853018, -0.06941027885906886, -0.07178862616469217, -0.0742026994304908, -0.07665135451761901, -0.07913338464029204, -0.08164752099213701, -0.08419243348212371, -0.0867667315800813, -0.08936896527160045, -0.09199762612189534, -0.09465114844798934, -0.0973279105983662, -0.10002623633901125, -0.10274439634455074, -0.10548060979297808, -0.10823304606224306, -0.11099982652676367, -0.11377902645171253, -0.11656867698271586, -0.11936676722840574, -0.12217124643305534, -0.12498002623633973, -0.12779098301706346, -0.13060196031751548, -0.1334107713449268, -0.13621520154632946, -0.13901301125295232, -0.14180193839011737, -0.1445797012484541, -0.14734400131209513, -0.1500925261393816, -0.15282295229147097, -0.1555329483041226, -0.15822017769781643, -0.16088230202126172, -0.16351698392325328, -0.16612189024775087, -0.16869469514697913, -0.1712330832072838, -0.17373475258242227, -0.17619741812892536, -0.1786188145381314, -0.18099669945947275, -0.18332885660958453, -0.18561309886180075, -0.18784727131061763, -0.19002925430572432, -0.19215696645023025, -0.19422836755776945, -0.1962414615632084, -0.19819429938175193, -0.20008498171132497, -0.20191166177318, -0.20367254798579315, -0.20536590656720585, -0.20699006406109868, -0.2085434097819981, -0.2100243981751684, -0.21143155108687436, -0.21276345994086468, -0.21401878781708789, -0.21519627142881817, -0.21629472299456504, -0.2173130320013103, -0.21825016685582557, -0.21910517642101976, -0.2198771914344744, -0.22056542580654495, -0.2211691777956182, -0.22168783105835096, -0.22212085557293992, -0.22246780843370506, -0.22272833451551458, -0.22290216700681398] + [-0.22298912781026733] * 2 + [-0.22290216700681398, -0.22272833451551458, -0.22246780843370506, -0.22212085557293992, -0.22168783105835096, -0.2211691777956182, -0.22056542580654495, -0.2198771914344744, -0.21910517642101976, -0.21825016685582557, -0.2173130320013103, -0.21629472299456504, -0.21519627142881817, -0.21401878781708789, -0.21276345994086468, -0.21143155108687436, -0.2100243981751684, -0.2085434097819981, -0.20699006406109868, -0.20536590656720585, -0.20367254798579315, -0.20191166177318, -0.20008498171132497, -0.19819429938175193, -0.1962414615632084, -0.19422836755776945, -0.19215696645023025, -0.19002925430572432, -0.18784727131061763, -0.18561309886180075, -0.18332885660958453, -0.18099669945947275, -0.1786188145381314, -0.17619741812892536, -0.17373475258242227, -0.1712330832072838, -0.16869469514697913, -0.16612189024775087, -0.16351698392325328, -0.16088230202126172, -0.15822017769781643, -0.1555329483041226, -0.15282295229147097, -0.1500925261393816, -0.14734400131209513, -0.1445797012484541, -0.14180193839011737, -0.13901301125295232, -0.13621520154632946, -0.1334107713449268, -0.13060196031751548, -0.12779098301706346, -0.12498002623633973, -0.12217124643305534, -0.11936676722840574, -0.11656867698271586, -0.11377902645171253, -0.11099982652676367, -0.10823304606224306, -0.10548060979297808, -0.10274439634455074, -0.10002623633901125, -0.0973279105983662, -0.09465114844798934, -0.09199762612189534, -0.08936896527160045, -0.0867667315800813, -0.08419243348212371, -0.08164752099213701, -0.07913338464029204, -0.07665135451761901, -0.0742026994304908, -0.07178862616469217, -0.06941027885906886, -0.06706873848853018, -0.06476502245597342, -0.06250008429248773, -0.060274813464991174, -0.05809003529025402, -0.05594651095406543, -0.05384493763410617, -0.05178594872490621, -0.04977011416308022, -0.04779794085086154, -0.045869873175780895, -0.04398629362417595, -0.042147523486056965, -0.04035382364870621, -0.03860539547624284, -0.036902381772251115, -0.035244867822440476, -0.03363288251418613, -0.03206639952968556, -0.03054533860936408, -0.029069566882065148, -0.027638900258475006, -0.02625310488415248, -0.02491189864846489, -0.02361495274567049, -0.022361893284334952, -0.021152302941227122, -0.01998572265580402, -0.01886165336137006, -0.017779557748978606, -0.016738862060135817, -0.015738957904367704, -0.014779204097720553, -0.013858928518282288, -0.01297742997483901, -0.012133980084814523, -0.011327825157683425, -0.01055818808009791, -0.009824270199026397, -0.009125253199266853, -0.008460300971769847, -0.00782856146928552, -0.007229168545933867, -0.006661243777390181, -0.006123898258474957, -0.005616234375041648, -0.005137347547164467, -0.004686327940742911, -0.004262262144758445, -0.0038642348115421727, -0.003491330257539964, -0.003142634022192405, -0.0028172343826816846, -0.002514223822434906, -0.0022327004514135643, -0.001971769376361237, -0.0017305440193259045, -0.0015081473829191116, -0.0013037132609211657, -0.0011163873929892457, -0.0009453285623736057, -0.000789709635695163, -0.0006487185439857415, -0.0005215592043395318] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.000350824576909999, -0.0005079785563389041, -0.0006953711582717798, -0.0009160098348767949, -0.0011729967584637093, -0.0014695169282018653, -0.001808825108206822, -0.0021942316344668016, -0.0026290871374214132, -0.0031167662362815637, -0.0036606502703191977, -0.004264109141285705, -0.004930482349766566, -0.005663059316574819, -0.00646505908815709, -0.007339609532364313, -0.008289726137758847, -0.00931829053582675, -0.010428028870979097, -0.011621490148003554, -0.012901024690615511, -0.014268762847910923, -0.015726594087800153, -0.017276146617867767, -0.018918767674530327, -0.020655504620828817, -0.02248708699168082, -0.024413909622920584, -0.02643601699697248, -0.028553088933540704, -0.030764427748269506, -0.033068946995954696, -0.035465161907597194, -0.03795118162241828, -0.0405247033069464, -0.043183008243487295, -0.0459229599597575, -0.048741004460257996, -0.05163317260815894, -0.054595084694130866, -0.05762195721576747, -0.06070861187808814, -0.06384948681216462, -0.06703864999527845, -0.07026981484227564, -0.07353635792403143, -0.07683133875527458, -0.08014752158052792, -0.08347739907371397, -0.08681321785412473, -0.0901470057090691, -0.09347060040167772, -0.09677567993114135, -0.10005379410217895, -0.10329639725084971, -0.10649488196500678, -0.10964061362981999, -0.11272496562192157, -0.11573935496991102, -0.11867527829424276, -0.12152434783595635, -0.12427832738131375, -0.12692916788822686, -0.1294690426203867, -0.13189038159626837, -0.13418590516266815, -0.13634865650613653, -0.13837203292056896, -0.1402498156552954, -0.14197619817522147, -0.14354581267288197, -0.14495375468162588, -0.14619560564948597, -0.14726745334455343, -0.14816590997478352, -0.14888812791804507, -0.14943181297179123, -0.1497952350458987] + [-0.14997723623689835] * 2 + [-0.1497952350458987, -0.14943181297179123, -0.14888812791804507, -0.14816590997478352, -0.14726745334455343, -0.14619560564948597, -0.14495375468162588, -0.14354581267288197, -0.14197619817522147, -0.1402498156552954, -0.13837203292056896, -0.13634865650613653, -0.13418590516266815, -0.13189038159626837, -0.1294690426203867, -0.12692916788822686, -0.12427832738131375, -0.12152434783595635, -0.11867527829424276, -0.11573935496991102, -0.11272496562192157, -0.10964061362981999, -0.10649488196500678, -0.10329639725084971, -0.10005379410217895, -0.09677567993114135, -0.09347060040167772, -0.0901470057090691, -0.08681321785412473, -0.08347739907371397, -0.08014752158052792, -0.07683133875527458, -0.07353635792403143, -0.07026981484227564, -0.06703864999527845, -0.06384948681216462, -0.06070861187808814, -0.05762195721576747, -0.054595084694130866, -0.05163317260815894, -0.048741004460257996, -0.0459229599597575, -0.043183008243487295, -0.0405247033069464, -0.03795118162241828, -0.035465161907597194, -0.033068946995954696, -0.030764427748269506, -0.028553088933540704, -0.02643601699697248, -0.024413909622920584, -0.02248708699168082, -0.020655504620828817, -0.018918767674530327, -0.017276146617867767, -0.015726594087800153, -0.014268762847910923, -0.012901024690615511, -0.011621490148003554, -0.010428028870979097, -0.00931829053582675, -0.008289726137758847, -0.007339609532364313, -0.00646505908815709, -0.005663059316574819, -0.004930482349766566, -0.004264109141285705, -0.0036606502703191977, -0.0031167662362815637, -0.0026290871374214132, -0.0021942316344668016, -0.001808825108206822, -0.0014695169282018653, -0.0011729967584637093, -0.0009160098348767949, -0.0006953711582717798, -0.0005079785563389041, -0.000350824576909999] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0002338830512733327, 0.00041342331414452246, 0.0006490265520840418, 0.0009494369385097077, 0.001323762479540643, 0.0017813737759764942, 0.002331789745408628, 0.0029845514206982594, 0.003749085223982172, 0.004634557384785197, 0.005649721420867429, 0.00680276082544743, 0.008101129299073374, 0.009551391023757079, 0.01115906359668726, 0.012928466317204117, 0.014862576550802174, 0.016962896875620838, 0.019229335648960667, 0.02166010351355131, 0.024251628196283764, 0.026998489737573544, 0.02989337803007294, 0.03292707424467024, 0.036088457384046375, 0.03936453683476643, 0.04274051139394752, 0.04619985483256559, 0.049724427631539454, 0.05329461409633044, 0.05688948362860888, 0.06048697451734078, 0.06406409821413954, 0.06759716168638136, 0.07106200510351443, 0.07443425181377886, 0.07768956731614689, 0.08080392373085002, 0.08375386612567143, 0.0865167769675525, 0.08907113494225635, 0.09139676442001228, 0.09347507194224823, 0.0952892662626041, 0.0968245586921427, 0.09806834077071391, 0.09901033660938849, 0.09964272761743759] + [0.09996024773528736] * 2 + [0.09964272761743759, 0.09901033660938849, 0.09806834077071391, 0.0968245586921427, 0.0952892662626041, 0.09347507194224823, 0.09139676442001228, 0.08907113494225635, 0.0865167769675525, 0.08375386612567143, 0.08080392373085002, 0.07768956731614689, 0.07443425181377886, 0.07106200510351443, 0.06759716168638136, 0.06406409821413954, 0.06048697451734078, 0.05688948362860888, 0.05329461409633044, 0.049724427631539454, 0.04619985483256559, 0.04274051139394752, 0.03936453683476643, 0.036088457384046375, 0.03292707424467024, 0.02989337803007294, 0.026998489737573544, 0.024251628196283764, 0.02166010351355131, 0.019229335648960667, 0.016962896875620838, 0.014862576550802174, 0.012928466317204117, 0.01115906359668726, 0.009551391023757079, 0.008101129299073374, 0.00680276082544743, 0.005649721420867429, 0.004634557384785197, 0.003749085223982172, 0.0029845514206982594, 0.002331789745408628, 0.0017813737759764942, 0.001323762479540643, 0.0009494369385097077, 0.0006490265520840418, 0.00041342331414452246, 0.0002338830512733327] + [0.0] * 2,
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
            "samples": [0.00011694152563666635, 0.00020671165707226123, 0.0003245132760420209, 0.00047471846925485384, 0.0006618812397703215, 0.0008906868879882471, 0.001165894872704314, 0.0014922757103491297, 0.001874542611991086, 0.0023172786923925984, 0.0028248607104337147, 0.003401380412723715, 0.004050564649536687, 0.0047756955118785395, 0.00557953179834363, 0.006464233158602058, 0.007431288275401087, 0.008481448437810419, 0.009614667824480333, 0.010830051756775655, 0.012125814098141882, 0.013499244868786772, 0.01494668901503647, 0.01646353712233512, 0.018044228692023188, 0.019682268417383214, 0.02137025569697376, 0.023099927416282796, 0.024862213815769727, 0.02664730704816522, 0.02844474181430444, 0.03024348725867039, 0.03203204910706977, 0.03379858084319068, 0.035531002551757215, 0.03721712590688943, 0.038844783658073444, 0.04040196186542501, 0.041876933062835714, 0.04325838848377625, 0.044535567471128176, 0.04569838221000614, 0.046737535971124115, 0.04764463313130205, 0.04841227934607135, 0.04903417038535696, 0.049505168304694244, 0.049821363808718794] + [0.04998012386764368] * 2 + [0.049821363808718794, 0.049505168304694244, 0.04903417038535696, 0.04841227934607135, 0.04764463313130205, 0.046737535971124115, 0.04569838221000614, 0.044535567471128176, 0.04325838848377625, 0.041876933062835714, 0.04040196186542501, 0.038844783658073444, 0.03721712590688943, 0.035531002551757215, 0.03379858084319068, 0.03203204910706977, 0.03024348725867039, 0.02844474181430444, 0.02664730704816522, 0.024862213815769727, 0.023099927416282796, 0.02137025569697376, 0.019682268417383214, 0.018044228692023188, 0.01646353712233512, 0.01494668901503647, 0.013499244868786772, 0.012125814098141882, 0.010830051756775655, 0.009614667824480333, 0.008481448437810419, 0.007431288275401087, 0.006464233158602058, 0.00557953179834363, 0.0047756955118785395, 0.004050564649536687, 0.003401380412723715, 0.0028248607104337147, 0.0023172786923925984, 0.001874542611991086, 0.0014922757103491297, 0.001165894872704314, 0.0008906868879882471, 0.0006618812397703215, 0.00047471846925485384, 0.0003245132760420209, 0.00020671165707226123, 0.00011694152563666635] + [0.0] * 2,
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
            "samples": [-0.00011694152563666635, -0.00020671165707226123, -0.0003245132760420209, -0.00047471846925485384, -0.0006618812397703215, -0.0008906868879882471, -0.001165894872704314, -0.0014922757103491297, -0.001874542611991086, -0.0023172786923925984, -0.0028248607104337147, -0.003401380412723715, -0.004050564649536687, -0.0047756955118785395, -0.00557953179834363, -0.006464233158602058, -0.007431288275401087, -0.008481448437810419, -0.009614667824480333, -0.010830051756775655, -0.012125814098141882, -0.013499244868786772, -0.01494668901503647, -0.01646353712233512, -0.018044228692023188, -0.019682268417383214, -0.02137025569697376, -0.023099927416282796, -0.024862213815769727, -0.02664730704816522, -0.02844474181430444, -0.03024348725867039, -0.03203204910706977, -0.03379858084319068, -0.035531002551757215, -0.03721712590688943, -0.038844783658073444, -0.04040196186542501, -0.041876933062835714, -0.04325838848377625, -0.044535567471128176, -0.04569838221000614, -0.046737535971124115, -0.04764463313130205, -0.04841227934607135, -0.04903417038535696, -0.049505168304694244, -0.049821363808718794] + [-0.04998012386764368] * 2 + [-0.049821363808718794, -0.049505168304694244, -0.04903417038535696, -0.04841227934607135, -0.04764463313130205, -0.046737535971124115, -0.04569838221000614, -0.044535567471128176, -0.04325838848377625, -0.041876933062835714, -0.04040196186542501, -0.038844783658073444, -0.03721712590688943, -0.035531002551757215, -0.03379858084319068, -0.03203204910706977, -0.03024348725867039, -0.02844474181430444, -0.02664730704816522, -0.024862213815769727, -0.023099927416282796, -0.02137025569697376, -0.019682268417383214, -0.018044228692023188, -0.01646353712233512, -0.01494668901503647, -0.013499244868786772, -0.012125814098141882, -0.010830051756775655, -0.009614667824480333, -0.008481448437810419, -0.007431288275401087, -0.006464233158602058, -0.00557953179834363, -0.0047756955118785395, -0.004050564649536687, -0.003401380412723715, -0.0028248607104337147, -0.0023172786923925984, -0.001874542611991086, -0.0014922757103491297, -0.001165894872704314, -0.0008906868879882471, -0.0006618812397703215, -0.00047471846925485384, -0.0003245132760420209, -0.00020671165707226123, -0.00011694152563666635] + [0.0] * 2,
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
            "samples": [0.0002338830512733327, 0.00041342331414452246, 0.0006490265520840418, 0.0009494369385097077, 0.001323762479540643, 0.0017813737759764942, 0.002331789745408628, 0.0029845514206982594, 0.003749085223982172, 0.004634557384785197, 0.005649721420867429, 0.00680276082544743, 0.008101129299073374, 0.009551391023757079, 0.01115906359668726, 0.012928466317204117, 0.014862576550802174, 0.016962896875620838, 0.019229335648960667, 0.02166010351355131, 0.024251628196283764, 0.026998489737573544, 0.02989337803007294, 0.03292707424467024, 0.036088457384046375, 0.03936453683476643, 0.04274051139394752, 0.04619985483256559, 0.049724427631539454, 0.05329461409633044, 0.05688948362860888, 0.06048697451734078, 0.06406409821413954, 0.06759716168638136, 0.07106200510351443, 0.07443425181377886, 0.07768956731614689, 0.08080392373085002, 0.08375386612567143, 0.0865167769675525, 0.08907113494225635, 0.09139676442001228, 0.09347507194224823, 0.0952892662626041, 0.0968245586921427, 0.09806834077071391, 0.09901033660938849, 0.09964272761743759] + [0.09996024773528736] * 2 + [0.09964272761743759, 0.09901033660938849, 0.09806834077071391, 0.0968245586921427, 0.0952892662626041, 0.09347507194224823, 0.09139676442001228, 0.08907113494225635, 0.0865167769675525, 0.08375386612567143, 0.08080392373085002, 0.07768956731614689, 0.07443425181377886, 0.07106200510351443, 0.06759716168638136, 0.06406409821413954, 0.06048697451734078, 0.05688948362860888, 0.05329461409633044, 0.049724427631539454, 0.04619985483256559, 0.04274051139394752, 0.03936453683476643, 0.036088457384046375, 0.03292707424467024, 0.02989337803007294, 0.026998489737573544, 0.024251628196283764, 0.02166010351355131, 0.019229335648960667, 0.016962896875620838, 0.014862576550802174, 0.012928466317204117, 0.01115906359668726, 0.009551391023757079, 0.008101129299073374, 0.00680276082544743, 0.005649721420867429, 0.004634557384785197, 0.003749085223982172, 0.0029845514206982594, 0.002331789745408628, 0.0017813737759764942, 0.001323762479540643, 0.0009494369385097077, 0.0006490265520840418, 0.00041342331414452246, 0.0002338830512733327] + [0.0] * 2,
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
            "samples": [0.00011694152563666635, 0.00020671165707226123, 0.0003245132760420209, 0.00047471846925485384, 0.0006618812397703215, 0.0008906868879882471, 0.001165894872704314, 0.0014922757103491297, 0.001874542611991086, 0.0023172786923925984, 0.0028248607104337147, 0.003401380412723715, 0.004050564649536687, 0.0047756955118785395, 0.00557953179834363, 0.006464233158602058, 0.007431288275401087, 0.008481448437810419, 0.009614667824480333, 0.010830051756775655, 0.012125814098141882, 0.013499244868786772, 0.01494668901503647, 0.01646353712233512, 0.018044228692023188, 0.019682268417383214, 0.02137025569697376, 0.023099927416282796, 0.024862213815769727, 0.02664730704816522, 0.02844474181430444, 0.03024348725867039, 0.03203204910706977, 0.03379858084319068, 0.035531002551757215, 0.03721712590688943, 0.038844783658073444, 0.04040196186542501, 0.041876933062835714, 0.04325838848377625, 0.044535567471128176, 0.04569838221000614, 0.046737535971124115, 0.04764463313130205, 0.04841227934607135, 0.04903417038535696, 0.049505168304694244, 0.049821363808718794] + [0.04998012386764368] * 2 + [0.049821363808718794, 0.049505168304694244, 0.04903417038535696, 0.04841227934607135, 0.04764463313130205, 0.046737535971124115, 0.04569838221000614, 0.044535567471128176, 0.04325838848377625, 0.041876933062835714, 0.04040196186542501, 0.038844783658073444, 0.03721712590688943, 0.035531002551757215, 0.03379858084319068, 0.03203204910706977, 0.03024348725867039, 0.02844474181430444, 0.02664730704816522, 0.024862213815769727, 0.023099927416282796, 0.02137025569697376, 0.019682268417383214, 0.018044228692023188, 0.01646353712233512, 0.01494668901503647, 0.013499244868786772, 0.012125814098141882, 0.010830051756775655, 0.009614667824480333, 0.008481448437810419, 0.007431288275401087, 0.006464233158602058, 0.00557953179834363, 0.0047756955118785395, 0.004050564649536687, 0.003401380412723715, 0.0028248607104337147, 0.0023172786923925984, 0.001874542611991086, 0.0014922757103491297, 0.001165894872704314, 0.0008906868879882471, 0.0006618812397703215, 0.00047471846925485384, 0.0003245132760420209, 0.00020671165707226123, 0.00011694152563666635] + [0.0] * 2,
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
            "samples": [-0.00011694152563666635, -0.00020671165707226123, -0.0003245132760420209, -0.00047471846925485384, -0.0006618812397703215, -0.0008906868879882471, -0.001165894872704314, -0.0014922757103491297, -0.001874542611991086, -0.0023172786923925984, -0.0028248607104337147, -0.003401380412723715, -0.004050564649536687, -0.0047756955118785395, -0.00557953179834363, -0.006464233158602058, -0.007431288275401087, -0.008481448437810419, -0.009614667824480333, -0.010830051756775655, -0.012125814098141882, -0.013499244868786772, -0.01494668901503647, -0.01646353712233512, -0.018044228692023188, -0.019682268417383214, -0.02137025569697376, -0.023099927416282796, -0.024862213815769727, -0.02664730704816522, -0.02844474181430444, -0.03024348725867039, -0.03203204910706977, -0.03379858084319068, -0.035531002551757215, -0.03721712590688943, -0.038844783658073444, -0.04040196186542501, -0.041876933062835714, -0.04325838848377625, -0.044535567471128176, -0.04569838221000614, -0.046737535971124115, -0.04764463313130205, -0.04841227934607135, -0.04903417038535696, -0.049505168304694244, -0.049821363808718794] + [-0.04998012386764368] * 2 + [-0.049821363808718794, -0.049505168304694244, -0.04903417038535696, -0.04841227934607135, -0.04764463313130205, -0.046737535971124115, -0.04569838221000614, -0.044535567471128176, -0.04325838848377625, -0.041876933062835714, -0.04040196186542501, -0.038844783658073444, -0.03721712590688943, -0.035531002551757215, -0.03379858084319068, -0.03203204910706977, -0.03024348725867039, -0.02844474181430444, -0.02664730704816522, -0.024862213815769727, -0.023099927416282796, -0.02137025569697376, -0.019682268417383214, -0.018044228692023188, -0.01646353712233512, -0.01494668901503647, -0.013499244868786772, -0.012125814098141882, -0.010830051756775655, -0.009614667824480333, -0.008481448437810419, -0.007431288275401087, -0.006464233158602058, -0.00557953179834363, -0.0047756955118785395, -0.004050564649536687, -0.003401380412723715, -0.0028248607104337147, -0.0023172786923925984, -0.001874542611991086, -0.0014922757103491297, -0.001165894872704314, -0.0008906868879882471, -0.0006618812397703215, -0.00047471846925485384, -0.0003245132760420209, -0.00020671165707226123, -0.00011694152563666635] + [0.0] * 2,
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
            "cosine": [(1.0, 20000)],
            "sine": [(0.0, 20000)],
        },
        "cosine_weights_tank_circuit2": {
            "cosine": [(1.0, 20000)],
            "sine": [(0.0, 20000)],
        },
        "sine_weights_tank_circuit1": {
            "cosine": [(0.0, 20000)],
            "sine": [(1.0, 20000)],
        },
        "sine_weights_tank_circuit2": {
            "cosine": [(0.0, 20000)],
            "sine": [(1.0, 20000)],
        },
    },
    "mixers": {
        "mixer_qubit1": [{'intermediate_frequency': 0, 'lo_frequency': 16000000000.0, 'correction': (1.0647488615985707, 0.21694400550069723, 0.21694400550069723, 1.0647488615985707)}],
        "mixer_qubit2": [{'intermediate_frequency': 0, 'lo_frequency': 16000000000.0, 'correction': (-0.22296795843987155, -1.0681012427764622, -1.0681012427764622, -0.22296795843987155)}],
        "mixer_qubit3": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit4": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit5": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qp_control_c3t2": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
    },
}


