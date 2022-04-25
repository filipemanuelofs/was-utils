@ECHO OFF
SET WAS_USER=""
SET WAS_PWD=""
ECHO [0] SAIR
ECHO [1] INICIAR WAS
ECHO [2] PARAR WAS
ECHO [3] REINICIAR WAS
SET /P X="O QUE DESEJA FAZER? "
IF /I "%X%" == "0" GOTO 0
IF /I "%X%" == "1" GOTO 1
IF /I "%X%" == "2" GOTO 2
IF /I "%X%" == "3" GOTO 3
ECHO "OPCAO INVALIDA"
GOTO END
:0
EXIT 0
:1
ECHO .
ECHO :--------------------------
ECHO ::::: INICIANDO SERVIDOR ::
ECHO :--------------------------
ECHO .
%WAS_HOME%\bin\startServer.bat -profileName AppSrv01 server1 && START https://localhost:9043/ibm/console/unsecureLogon.jsp
GOTO END
:2
ECHO .
ECHO :--------------------------
ECHO ::::::: PARANDO SERVIDOR ::
ECHO :--------------------------
ECHO .
%WAS_HOME%\bin\stopServer.bat -profileName AppSrv01 server1 -username $WAS_USER -password $WAS_PWD
GOTO END
:3
ECHO .
ECHO :--------------------------
ECHO ::: REINICIANDO SERVIDOR ::
ECHO :--------------------------
ECHO .
%WAS_HOME%\bin\stopServer.bat -profileName AppSrv01 server1 -username wasadmin -password wasadmin && %WAS_HOME%\bin\startServer.bat -profileName AppSrv01 server1 && START https://localhost:9043/ibm/console/unsecureLogon.jsp
:END
PAUSE
