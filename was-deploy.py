#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Versão: 2.0
Script responsavel por realizar o undeploy e deploy do aplicativo no WAS, alem de compilar atraves do Maven.

Execução:
	$ cd C:\<CAMINHO_WAS>\WebSphere\AppServer\bin
	$ wsadmin.bat -language jython -f <CAMINHO_SCRIPT> -username wasadmin -password wasadmin

Autor: Filipe Manuel
'''
import time
import os
import sys
import string
import subprocess

# Caminho do projeto
# Ex: C:\\Desenvolvimento\\Projetos\\AppCorporativo\\
PROJETO_BASE_LOCAL = '<CAMINHO_DO_PROJETO>'

# Nome do aplicativo
# Ex: app-corporativo
APP_NOME = '<NOME_DO_APLICATIVO_EAR>'

# Caminho do EAR
# Ex: \\AppCorporativoEAR\\target\\
APP_LOCAL = PROJETO_BASE_LOCAL + '<CAMINHO_DA_PASTA_TARGET>'

# Caminho dos projetos/pastas a serem compilados em ordem, portanto, os projetos de EAR e WAR devem ser os ultimos
PROJETOS = [
	'ModuloEJB',
	'ModuloWAR',
	'ModuloEAR'
]

'''
Resposavel por compilar o projeto pelo Maven
'''
def compilar_maven():
	projetos_compilados = []
	if os.path.exists(PROJETO_BASE_LOCAL):
		os.chdir(PROJETO_BASE_LOCAL)
		print '###\n### Entrando na pasta {} ###\n###'.format(PROJETO_BASE_LOCAL)

		for projeto in PROJETOS:
			caminho_completo = PROJETO_BASE_LOCAL + projeto
			if os.path.exists(caminho_completo):
				os.chdir(caminho_completo)
				print '###\n### Entrando na pasta {} ###\n###'.format(caminho_completo)

				codigo = subprocess.call(["mvn", "clean", "install", "-DskipTests", "-Pwas", "-o"], shell=True)

				if codigo == 0:
					projetos_compilados.append(projeto)
				else:
					print '###\n### Projeto {} NAO compilado corretamente ###\n###'.format(projeto)
					break
			else:
				print '###\n### Projeto NAO existente {} ###\n###'.format(projeto)
		
		if codigo == 0 or codigo is None:
			print '###\n### Projetos compilados com sucesso ###\n###'
		else:
			raise Exception('###\n### Não foi possível compilar o projeto ###\n###')

'''
Responsavel por realizar o deploy do aplicativo no WAS
'''
def deploy():
	print '###\n### Realizando deploy do aplicativo: {} ###\n###'.format(APP_NOME)
	AdminApp.install(APP_LOCAL + APP_NOME + '.ear','[-node nd1 -cell cell01 -server server1]')
	AdminConfig.save()
	appMan = AdminControl.queryNames('cell=cell01,node=nd1,type=ApplicationManager,process=server1,*')
	AdminControl.invoke(appMan, 'startApplication', APP_NOME)
	print '###\n### Deploy realizado com sucesso ###\n###'

'''
Responsavel por realizar o undeploy do aplicativo no WAS
'''
def undeploy(): 
	print '###\n### Realizando undeploy do aplicativo: {} ###\n###'.format(APP_NOME)
	AdminApp.uninstall(APP_NOME)
	AdminConfig.save()
	print '###\n### Undeploy realizado com sucesso ###\n###'

'''
Responsavel por recuperar o status do aplicativo no WAS
'''
def __app_status(aplicativo):
	objeto = AdminControl.completeObjectName('type=Application,name=' + aplicativo + ',*')
	
	status = ''
	if objeto != '':
		status = 'Iniciado'
	
	return status

'''
Responsavel por montar a informacao dos aplicativos no WAS
'''
def app_status_info():
	appsString = AdminApp.list()
	appList = string.split(appsString, '\r\n')
	print '###\n### Status\t| Aplicativo ###'

	for app in appList:
		print '### ' + __app_status(app) + '\t| ' + app

if __name__ == '__main__':
	inicio = time.time()
	
	try:
		app_status_info()
		compilar_maven()
		undeploy()
		deploy()
	except Exception as ex:
		print 'Erro: {}'.format(ex)

	minutos = ((time.time() - inicio) / 60)
	print u'###\n### Tempo total: {} min ###'.format(minutos)
