#!/bin/sh

socat TCP-LISTEN:10000,fork EXEC:"timeout 3600 python3 /chal/Cut\&Paste0/server.py" &
socat TCP-LISTEN:10001,fork EXEC:"timeout 3600 python3 /chal/Cut\&Paste1/server.py" &
socat TCP-LISTEN:10002,fork EXEC:"timeout 3600 python3 /chal/Bit_Flipping0/server.py" &
socat TCP-LISTEN:10003,fork EXEC:"timeout 3600 python3 /chal/Bit_Flipping1/server.py" &
socat TCP-LISTEN:10004,fork EXEC:"timeout 3600 python3 /chal/Padding_Oracle0/server.py" &
socat TCP-LISTEN:10005,fork EXEC:"timeout 3600 python3 /chal/Padding_Oracle1/server.py" &
socat TCP-LISTEN:10006,fork EXEC:"timeout 3600 python3 /chal/LCG/server.py" &
socat TCP-LISTEN:10007,fork EXEC:"timeout 3600 python3 /chal/MT19937/server.py" &
socat TCP-LISTEN:10008,fork EXEC:"timeout 3600 python3 /chal/Where_Is_My_Bit/server.py" &
exec socat TCP-LISTEN:10009,fork EXEC:"timeout 3600 python3 /chal/Length_Extension_Attack/server.py"