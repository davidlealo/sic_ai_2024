@echo off
echo Instalando dependencias para el proyecto de procesamiento de audio...

REM Actualizar pip
python -m pip install --upgrade pip

REM Instalar dependencias
pip install tensorflow
pip install scikit-learn
pip install pandas
pip install matplotlib
pip install seaborn
pip install numpy
pip install librosa
pip install gc
pip install yt-dlp
pip install pydub

echo Instalación completada.
pause