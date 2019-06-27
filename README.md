## was-deploy.py
#### Configurar
- Abra o script e configure as constantes de acordo do seu projeto:
	- PROJETO_BASE_LOCAL
		-  O caminho do projeto, exemplo `C:\\Desenvolvimento\\Projetos\\AppCorporativo\\`
	- EAR_NOME
		- O nome do aplicativo a ser feito do deploy, sem a extensão, exemplo: `app-corporativo`
	- EAR_LOCAL
		- O local do aplicativo gerado pelo Maven (geralmente em /target), exemplo: `\\AppCorporativoEAR\\target\\`
	- PROJETOS
		- O caminho/pastas a serem compiladas pelo Maven. Essas pastas serão executadas na ordem em que estão descritas. Caso alguma seja dependente de outra, coloque-a antes.
		- `PROJETOS [ ModuloEJB, ModuloWAR, ModuloEAR ]`
		- Neste caso, o `ModuloEAR` empacota o `ModuloWAR` e `ModuloEJB`, por isso ele ficou por último.
#### Executar
- Entrar na pasta `bin` do WebSphere:
	- `$ cd <CAMINHO_WAS>\WebSphere\AppServer\bin`
- Executar o comando dentro da pasta `bin`:
	- `$ wsadmin.bat -language jython -f <CAMINHO_SCRIPT>\was-deploy.py -username wasadmin -password wasadmin`
	- Caso queira utilizar outro usuário para execução do deploy, troque o parâmetro `-username` e `-password`

## was-fix-composition-unit.py
#### Configurar
- Abra o script e configure as constantes de acordo do seu projeto:
	- WAS_CELL_CAMINHO
		-  O caminho da célula, exemplo `C:\\IBM\\WebSphere\\AppServer\\profiles\\AppSrv01\\config\\cells\\cell01\\'`
	- APP_NOME
		-  `app-corporativo`
#### Executar
- Executar onde o script for baixado
	- `$ python was-fix-composition-unit.py`
