@ECHO OFF
SET WAS_HOME=%WAS_HOME%
SET WAS_PROFILE=AppSrv01
SET WAS_SERVER=server1
SET WAS_USER=""
SET WAS_PWD=""

:MENU
ECHO [0] SAIR
ECHO [1] INICIAR WAS
ECHO [2] PARAR WAS
ECHO [3] REINICIAR WAS
SET /P X="O QUE DESEJA FAZER? "
IF /I "%X%" == "0" GOTO END
IF /I "%X%" == "1" GOTO START
IF /I "%X%" == "2" GOTO STOP
IF /I "%X%" == "3" GOTO RESTART
ECHO "OPÇÃO INVÁLIDA"
GOTO END

:START
ECHO .
ECHO :--------------------------
ECHO ::::: INICIANDO SERVIDOR ::
ECHO :--------------------------
ECHO .
%WAS_HOME%\bin\startServer.bat -profileName %WAS_PROFILE% %WAS_SERVER%
START https://localhost:9043/ibm/console/unsecureLogon.jsp
GOTO END

:STOP
ECHO .
ECHO :--------------------------
ECHO ::::::: PARANDO SERVIDOR ::
ECHO :--------------------------
ECHO .
%WAS_HOME%\bin\stopServer.bat -profileName %WAS_PROFILE% %WAS_SERVER% -username %WAS_USER% -password %WAS_PWD%
GOTO END

:RESTART
ECHO .
ECHO :--------------------------
ECHO ::: REINICIANDO SERVIDOR ::
ECHO :--------------------------
ECHO .
%WAS_HOME%\bin\stopServer.bat -profileName %WAS_PROFILE% %WAS_SERVER% -username %WAS_USER% -password %WAS_PWD%
%WAS_HOME%\bin\startServer.bat -profileName %WAS_PROFILE% %WAS_SERVER%
START https://localhost:9043/ibm/console/unsecureLogon.jsp
GOTO END

:END
EXIT 0
