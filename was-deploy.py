#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Versão: 2.0
Script responsavel por realizar o undeploy e deploy do aplicativo no WAS, alem de compilar atraves do Maven.

Execução:
	$ cd C:\<CAMINHO_WAS>\WebSphere\AppServer\bin
	$ wsadmin.bat -lang jython -f <CAMINHO_SCRIPT> -username <USUARIO> -password <SENHA>

Autor: Filipe Manuel
'''
import time
import os
import sys
import string
import subprocess

# Lista de argumentos possiveis
ARGUMENTOS = [
    'start'
]

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

class CompilarApp:

    def __init__(self):
        pass

    def executar_maven(self):
        codigo = None
        try:
           codigo = subprocess.call(["mvn", "clean", "install", "-DskipTests", "-P<PROFILE>", "-o"], shell=True)
        except Exception as ex:
            print 'Excecao: ', ex
        
        return codigo

    def compilar(self):
        projetos_compilados = []
        if os.path.exists(PROJETO_BASE_LOCAL):
            os.chdir(PROJETO_BASE_LOCAL)
            exibir_mensagem('Entrando na pasta {}'.format(PROJETO_BASE_LOCAL))

            if len(PROJETOS) >= 1:
                for projeto in PROJETOS:
                    caminho_completo = PROJETO_BASE_LOCAL + projeto
                    if os.path.exists(caminho_completo):
                        os.chdir(caminho_completo)
                        exibir_mensagem('Entrando na pasta {}'.format(caminho_completo))

                        codigo = self.executar_maven()

                        if codigo == 0:
                            projetos_compilados.append(projeto)
                        else:
                            exibir_mensagem('Projeto {} NAO compilado corretamente'.format(projeto))
                            break
                    else:
                        exibir_mensagem('Projeto NAO existente {}'.format(projeto))
            else:
                if os.path.exists(PROJETO_BASE_LOCAL):
                    os.chdir(PROJETO_BASE_LOCAL)
                    exibir_mensagem('Entrando na pasta {}'.format(PROJETO_BASE_LOCAL))
                    
                    codigo = self.executar_maven()
                    if codigo != 0:
                        exibir_mensagem('Projeto {} NAO compilado corretamente'.format(projeto))

            if codigo == 0 or codigo is None:
                exibir_mensagem('Projetos compilados com sucesso')
            else:
                raise Exception(u'NAO foi possível compilar o projeto')

class GerenciarApp:

    def __init__(self):
        pass

    def deploy(self, argumento):
        exibir_mensagem('Realizando deploy do aplicativo: {}'.format(APP_NOME))
        AdminApp.install(APP_LOCAL + APP_NOME + '.ear','[-node nd1 -cell cell01 -server server1 -MapWebModToVH [[.* .* default_host]]]')
        AdminConfig.save()
        appMan = AdminControl.queryNames('cell=cell01,node=nd1,type=ApplicationManager,process=server1,*')
        
        if argumento in ARGUMENTOS:
            if argumento == 'start':
                exibir_mensagem('Iniciando aplicativo')
                AdminControl.invoke(appMan, 'startApplication', APP_NOME)
        else:
            raise Exception('Argumento invalido')

        exibir_mensagem('Deploy realizado com sucesso')

    def undeploy(self):
        exibir_mensagem('Realizando undeploy do aplicativo: {}'.format(APP_NOME))
        AdminApp.uninstall(APP_NOME)
        AdminConfig.save()
        exibir_mensagem('Undeploy realizado com sucesso')

    def __app_status(self, aplicativo):
        objeto = AdminControl.completeObjectName('type=Application,name=' + aplicativo + ',*')
        
        if objeto != '':
            status = 'Iniciado'
        else:
            status = 'Parado'
        
        return status

    def app_status_info(self):
        appsString = AdminApp.list()
        appList = string.split(appsString, '\r\n')
        exibir_mensagem('Status | Aplicativo')

        for app in appList:
            exibir_mensagem(self.__app_status(app) + ' | ' + app)

def exibir_mensagem(msg):
    print '###\n### {} \n###'.format(msg)

if __name__ == '__main__':
    inicio = time.time()
    gerenciarApp = GerenciarApp()
    compilarApp = CompilarApp()

    try:
        gerenciarApp.app_status_info()
        compilarApp.compilar()
        gerenciarApp.undeploy()
        gerenciarApp.deploy(sys.argv[0])
    except Exception as ex:
        exibir_mensagem('Erro: {}'.format(ex))

    minutos = ((time.time() - inicio) / 60)
    exibir_mensagem('Tempo total: {} min'.format(minutos))
