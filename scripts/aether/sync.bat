echo Pulling all repos to 'C:\workspace'

SET startdir=%CD%

cd C:\workspace

cd aether
call git pull origin master

cd ..\pyaether
call git pull origin master

cd ..\aetherpp
call git pull origin master

cd %startdir%