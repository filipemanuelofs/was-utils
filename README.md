## was-deploy.py
#### Configuração
- Abra o script e configure as constantes de acordo do seu projeto:
	- PROJETO_BASE_LOCAL
		-  O caminho do projeto, exemplo `C:\\Desenvolvimento\\Projetos\\AppCorporativo\\`
	- APP_NOME
		- O nome do aplicativo a ser feito do deploy, sem a extensão, exemplo: `app-corporativo`
	- APP_LOCAL
		- O local do aplicativo gerado pelo Maven (geralmente em /target), exemplo: `\\AppCorporativoEAR\\target\\`
	- PROJETOS
		- O caminho/pastas a serem compiladas pelo Maven. Essas pastas serão executadas na ordem em que estão descritas. Caso alguma seja dependente de outra, coloque-a antes.
		- `PROJETOS [ ModuloEJB, ModuloWAR, ModuloEAR ]`
		- Neste caso, o `ModuloEAR` empacota o `ModuloWAR` e `ModuloEJB`, por isso ele ficou por último.
		- Caso seja vazio, a compilação irá ocorrer no projeto completo, de acordo com a variável PROJETO_BASE_LOCAL
#### Execução
- Entrar na pasta `bin` do WebSphere:
	- `$ cd <CAMINHO_WAS>\WebSphere\AppServer\bin`
- Executar o comando dentro da pasta `bin`:
	- `$ wsadmin.bat -f <CAMINHO_SCRIPT>\was-deploy.py -lang jython -username <USER> -password <PWD>`
	- Caso queira utilizar outro usuário para execução do deploy, troque o parâmetro `-username` e `-password`
	- Caso queira iniciar o aplicativo após a instalação, passe o argumento `start`
		- `$ wsadmin.bat -f <CAMINHO_SCRIPT>\was-deploy.py start -lang jython -username <USER> -password <PWD>`

## was-fix-composition-unit.py
#### Configuração
- Abra o script e configure as constantes de acordo do seu projeto:
	- WAS_CELL_CAMINHO
		-  O caminho da célula, exemplo `C:\\IBM\\WebSphere\\AppServer\\profiles\\AppSrv01\\config\\cells\\cell01\\'`
	- APP_NOME
		-  O nome do aplicativo, exemplo `app-corporativo`
#### Execução
- Parar o servidor
- Executar onde o script for baixado
	- `$ python was-fix-composition-unit.py`
- Iniciar o servidor

## was-start.bat
#### Configuração
- Abra o script e configure as constantes de acordo do servidor:
	- WAS_USER
		-  usuário de conexão com o console do servidor
	- WAS_PWD
		-  senha de conexão com o console do servidor
- Caso não esteja configurada, é necessário configurar a variável de ambiente `WAS_HOME` apontando para o local de instalação do seu servidor, por exemplo:
	- `WAS_HOME=C:\"Program Files"\IBM\WebSphere\AppServer`

#### Execução
- Iniciar o arquivo
- Escolher uma opção 
	- (0) Sair; 
	- (1) Iniciar servidor; 
	- (2) Parar servidor;
	- (3) Reiniciar servidor.
