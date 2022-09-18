
# script para preparar e rodar ambiente do programa analisador_lexico.py

# windows

# cria ambiente virtual
python -m venv venv

# ativa ambiente virtual
.\venv\Scripts\Activate

# instala dependencias
pip install -r requirements.txt

# roda o analisador 
py analisador_lexico.py