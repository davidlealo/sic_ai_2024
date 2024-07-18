# Ejercicios de preprocesamiento

El día de hoy realizaremos un ejercicio de trabajo en grupos. Cada grupo tendrá una subunidad asignada la que deberá explicar generando un archivo de práctica con ejemplos y ejercicios para resolver en el curso.

Debes dejar tu ejercicio en la carpeta de tu capítulo, según corresponda, recuerda que debemos ignorar los archivos que no son código. 

# Instrucciones para colaborar en este repositorio utilizando Google Colab

Sigue estos pasos para hacer un fork de este repositorio, trabajar en él desde Google Colab y enviar tus cambios mediante un pull request.

## 1. Hacer Fork del Repositorio

1. Ve al repositorio original en GitHub.
2. Haz clic en el botón "Fork" en la esquina superior derecha para crear una copia del repositorio en tu cuenta de GitHub.

## 2. Clonar el Repositorio Fork en Google Colab

1. Ve a [Google Colab](https://colab.research.google.com/) e inicia sesión con tu cuenta de Google.
2. Abre una nueva libreta en Colab.
3. En la primera celda, ejecuta el siguiente código para clonar tu repositorio fork:

    ```python
    !git clone https://github.com/tu-usuario/nombre-del-repositorio.git
    %cd nombre-del-repositorio
    ```

4. Reemplaza `tu-usuario` con tu nombre de usuario de GitHub y `nombre-del-repositorio` con el nombre del repositorio que has forked.

## 3. Crear una Nueva Rama

1. Antes de hacer cualquier cambio, crea una nueva rama para trabajar en tu tema específico:

    ```python
    !git checkout -b nombre-de-la-rama
    ```

2. Reemplaza `nombre-de-la-rama` con un nombre descriptivo para tu rama.

## 4. Trabajar en los Archivos

1. Abre y edita los archivos `.ipynb` dentro del repositorio clonado.
2. Puedes usar el navegador de archivos en la parte izquierda de la interfaz de Colab para abrir un notebook específico.

## 5. Guardar y Hacer Commits

1. Una vez que hayas hecho los cambios necesarios, guarda los cambios y haz commits directamente desde Colab usando los siguientes comandos:

    ```python
    !git add nombre-del-archivo.ipynb
    !git commit -m "Descripción de los cambios"
    ```

2. Reemplaza `nombre-del-archivo.ipynb` con el nombre del archivo que has editado y proporciona una descripción adecuada de los cambios en el commit.

## 6. Empujar los Cambios a tu Repositorio Fork

1. Empuja los cambios a tu repositorio fork en GitHub:

    ```python
    !git push origin nombre-de-la-rama
    ```

2. Asegúrate de reemplazar `nombre-de-la-rama` con el nombre de la rama que has creado.

## 7. Crear un Pull Request

1. Ve a tu repositorio fork en GitHub.
2. Haz clic en el botón "Compare & pull request" para iniciar el proceso de creación del pull request.
3. Proporciona una descripción detallada de los cambios y envía el pull request para revisión.