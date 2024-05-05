[![Python application test with Github Actions](https://github.com/preetamjumech/Python-microservices/actions/workflows/mlops.yml/badge.svg)](https://github.com/preetamjumech/Python-microservices/actions/workflows/mlops.yml)


# Python-microservices
CI/CD MLOps series

## Scaffold - 
1. make file
2. requirements.txt
3. source code
4. test file
5. docker file
6. [IAC - Infrastructure as Code] // Configuration file

## steps
1. create virtual environment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`
`vim ~/.bashrc`
//edit the file # sourcing virtual env
`source ~/.venv/bin/activate`

2. create empty files
`touch Makefile`, `touch Dockerfile`, `touch requirements.txt`, `touch main.py`

3. Populate Makefile
`make install`

`pip freeze | less`

![image](https://github.com/preetamjumech/Python-microservices/assets/82079602/3ccab2d0-1fed-403a-845a-1b6f10018115)
