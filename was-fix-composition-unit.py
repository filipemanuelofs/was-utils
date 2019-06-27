#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Script referente ao erro:
	com.ibm.websphere.management.exception.AdminException: A composition unit with name <APLICATIVO> already exists. 
	Select a different application name.

Referência:
	https://www-01.ibm.com/support/docview.wss?uid=swg21590141

Execução:
	$ python was-fix-composition-unit.py
'''
import os
import shutil

# Caminho da célula
WAS_CELL_CAMINHO = '<CAMINHO_DO_WAS>\\AppServer\\profiles\\AppSrv01\\config\\cells\\cell01\\'

# Fixo
DIRETORIOS = ['applications', 'blas', 'cus']

# Nome do aplicativo 
APP_NOME = '<NOME_APLICATIVO>'

def apagar_diretorios():
	if os.path.exists(WAS_CELL_CAMINHO):
		os.chdir(WAS_CELL_CAMINHO)
		print('###\n### Entrando na pasta {0} ###\n###'.format(WAS_CELL_CAMINHO))

		for diretorio in DIRETORIOS:
			caminho_completo = WAS_CELL_CAMINHO + diretorio
			if os.path.exists(caminho_completo):
				os.chdir(caminho_completo)
				print('###\n### Entrando na pasta {} ###\n###'.format(caminho_completo))

				if diretorio == 'applications':
					caminho_diretorio = caminho_completo + '\\' + APP_NOME + '.ear'
				else:
					caminho_diretorio = caminho_completo + '\\' + APP_NOME
				
				if os.path.exists(caminho_diretorio):
					shutil.rmtree(caminho_diretorio)
					#os.rmdir(caminho_diretorio)
					print('###\n### Arquivo deletado em {} ###\n###'.format(caminho_diretorio))
				else:
					print('###\n### Caminho NAO existente {} ###\n###'.format(caminho_diretorio))
			else:
				print('###\n### Caminho NAO existente {} ###\n###'.format(caminho_completo))

if __name__ == '__main__':
	apagar_diretorios()
