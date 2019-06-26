#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Script responsavel por realizar o undeploy e deploy do aplicativo no WAS.

Execucao:
	$ cd C:\\<CAMINHO_WAS>\\WebSphere\\AppServer\\bin
	$ wsadmin.bat -language jython -f <CAMINHO_SCRIPT> -username wasadmin -password wasadmin
	
'''
import time
import os
import sys
import string
import subprocess

# Caminho do projeto
PROJETO_BASE_LOCAL = '<CAMINHO_DO_PROJETO>'

# Nome do aplicativo
EAR_NOME = '<NOME_DO_APLICATIVO-EAR>'

# Caminho do EAR
EAR_LOCAL = PROJETO_BASE_LOCAL + '<CAMINHO_DA_PASTA_TARGET>'

'''
Resposavel por compilar o projeto pelo Maven
'''
def compilar_maven():
	if os.path.exists(PROJETO_BASE_LOCAL):
		os.chdir(PROJETO_BASE_LOCAL)
		print '###\n### Entrando na pasta {} ###\n###'.format(PROJETO_BASE_LOCAL)
	
		codigo = subprocess.call(["mvn", "clean", "install", "-DskipTests=true", "-o", "-Pwas"], shell=True)

		if codigo == 0 or codigo is None:
			print '###\n### Projeto compilado com sucesso ###\n###'
		else:
			print '###\n### Não foi possível compilar o projeto ###\n###'

'''
Responsavel por realizar o deploy do aplicativo no WAS
'''
def deploy():
	print '###\n### Realizando deploy do aplicativo: {} ###\n###'.format(EAR_NOME)
	AdminApp.install(EAR_LOCAL + EAR_NOME + '.ear','[-node nd1 -cell cell01 -server server1]')
	AdminConfig.save()
	appMan = AdminControl.queryNames('cell=cell01,node=nd1,type=ApplicationManager,process=server1,*')
	AdminControl.invoke(appMan, 'startApplication', EAR_NOME)
	print '###\n### Deploy realizado com sucesso ###\n###'

'''
Responsavel por realizar o undeploy do aplicativo no WAS
'''
def undeploy(): 
	print '###\n### Realizando undeploy do aplicativo: {} ###\n###'.format(EAR_NOME)
	AdminApp.uninstall(EAR_NOME)
	AdminConfig.save()
	print '###\n### Undeploy realizado com sucesso ###\n###'

'''
Responsavel por recuperar o status do aplicativo no WAS
'''
def __app_status(aplicativo):
	objeto = AdminControl.completeObjectName('type=Application,name=' + aplicativo + ',*')
	if objeto == "":
		status = 'Parado'
	else:
		status = 'Rodando'
	
	return status

'''
Responsavel por montar a informacao dos aplicativos no WAS
'''
def app_status_info():
	appsString = AdminApp.list()
	print appsString
	appList = string.split(appsString, '\r\n')
	print '###\n### Status\t| Aplicativo ###\n###'

	for app in appList:
		print '### ' + __app_status(app) + '\t| ' + app

if __name__ == '__main__':
	app_status_info()
	undeploy()
	compilar_maven()
	deploy()