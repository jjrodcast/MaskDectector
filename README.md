# Mask Detector

Proyecto Final de fin de curso de *_Python para Ciencia de Datos_* del Diplomado de Inteligencia Artificial de la PUCP.

## Objetivo 🚀

Este proyecto contiene una implementación para detectar en una imagen o un video qué personas están usando una máscara que le ayude a prevenir contagiarse del COVID-19.


## Pre-requisitos 📋

Este proyecto inicialmente ha sido diseñado para poder ser ejecutado en Colab y para una optimización se activó el entorno de ejecución en GPU.
Colab ya trae consigo muchas de las librería ya utilizadas, aunque fue necesario instalar:
- mtcnn

```
!pip install mtcnn
```


## Archivos necesarios para la ejecución ⌨️

**- MODELOS:**

**_model/mask_net.hdf5_** : Model CNN entrenado desde cero con Keras.

**_model/best_model_conv_ft2.model_** : Modelo CNN pre-entrenado de ResNet18 en Pytorch, del cual se mantuvo la estructura de la red y se volvieron a entrenar los pesos en todas las capas.

**- UTILITARIOS:**

**_utils/bounding_box.py_** : Utilitario para incrementar en un porcentaje dato el cuadro delimitador de una imagen que contiene un rostro.

**_utils/predictor_keras.py_** : Utilitario para generar las predicciones con el modelo entrenado de Keras.

**_utils/predictor_pytorch.py_** : Utilitario para generar las predicciones con el modelo entrenado con Pytorch.

**- ARCHIVO PRINCIPAL:**

**_MaskDetector.ipynb_** : Notebook con las pruebas end-to-end para generar sobre imágenes y videos las predicciones de si una persona está usando o no una mascarilla.

## Instalación 🔧 --- Se piensa omitir

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Dí cómo será ese paso_

```
Da un ejemplo
```

_Y repite_

```
hasta finalizar
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_


## Autores ✒️

* **David Fosca Gamarra** - [linkedin](https://www.linkedin.com/in/jorge-rodr%C3%ADguez-castillo/) - [github](https://github.com/jjrodcast)
* **Keven Fernández Carrillo** - [linkedin](https://www.linkedin.com/in/keven-fern%C3%A1ndez-carrillo-50b07aa2/) - [github](https://github.com/KevenRFC)
* **David Fosca Gamarra** - [linkedin](https://www.linkedin.com/in/davidfoscagamarra/) - [github](https://github.com/DavidFosca)


## Licencia 📄

Este proyecto está bajo la Licencia (XYZW) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

