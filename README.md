# Mask Detector

Proyecto Final de fin de curso de *_Python para Ciencia de Datos_* del Diplomado de Inteligencia Artificial de la PUCP.

Puedes ver la versión usando YOLOv4 en el siguiente enlace: [MaskDetector-YoloV4](https://github.com/jjrodcast/MaskDetector-YoloV4)

## Objetivo 🚀

Este proyecto contiene una implementación para detectar en una imagen o un video qué personas están usando una mascarilla que le ayude a prevenir contagiarse del COVID-19.

<p align="center"> 
    <img src="https://user-images.githubusercontent.com/7152507/81436296-da95e080-912e-11ea-9c2f-5280e12aea95.png" alt="Resultado">
</p>

## Procedimiento 🛠️

El proceso general para obtener las detecciones de rostros con o sin mascarillas es el siguiente:

1. **Leer** la imagen o frame de video.
2. **Aplicar modelo CNN_Face_Detector** para detectar todos los rostros en la imagen.
3. **Aplicar modelo CNN_Mask_Class** para determinar si el rostro tiene o no mascarilla.
4. **Insertar recuadro clasificador** en rostro de imagen original.
5. **Repetir el proceso** para todos los rostros en la imagen.

Conoce más sobre la arquitectura, el funcionamiento y los resultados obtenidos del proyecto en la siguiente [presentación](https://github.com/jjrodcast/MaskDectector/blob/master/presentacion/Proyecto_Final_PFDS.pdf).

## Pre-Requisitos 📋

Este proyecto inicialmente ha sido diseñado para poder ser ejecutado en Colab y para una optimización se activó el entorno de ejecución en GPU.
Colab ya trae instaladas muchas de las librerías utilizadas en este proyecto, solo fue necesario instalar adicionalmente:
- mtcnn (Detector de rostros: Multi-Task Cascaded Convolutional Neural Network)

```
!pip install mtcnn
```

## Archivos necesarios para la ejecución 🛠️

📌 **MODELOS:**

* **_models/mask_net.hdf5_** : Model CNN entrenado desde cero con Keras.

* **_models/best_model_conv_ft2.model_** : Modelo CNN pre-entrenado de ResNet18 en Pytorch, del cual se mantuvo la estructura de la red y se volvieron a entrenar los pesos en todas las capas.

📌 **UTILITARIOS:**

* **_utils/bounding_box.py_** : Utilitario para incrementar en un porcentaje dato el cuadro delimitador de un rostro en una imagen.

* **_utils/detect_faces.py_** : Utilitario para detectar las caras en las imágenes o frames de videos.

* **_utils/predictor_keras.py_** : Utilitario para generar las predicciones con el modelo entrenado de Keras.

* **_utils/predictor_pytorch.py_** : Utilitario para generar las predicciones con el modelo entrenado con Pytorch.

📌 **ARCHIVO PRINCIPAL:**

* **_MaskDetector.ipynb_** : Notebook con las pruebas end-to-end para generar sobre imágenes y videos las predicciones de si una persona está usando o no una mascarilla.

📌 **ARCHIVOS MULTIMEDIA:**

Básicamente puedes cargar imágenes o videos propios, pero por defecto puedes utilizar las imágenes presentes en la carpeta **"multimedia/"**.

## Proceso de Ejecución ⚙️ 

* Levantar el notebook principal en Colab
* Cargar los archivos necesarios al notebook
* Validar que el Tipo de Entorno de Ejecución está en **GPU**
* Ejecutar todo el notebook

## Archivos Adicionales 📁

* **notebooks/CNN_Zero_ProyectoFinal.ipynb** : Notebook para generar el modelo entrenado desde cero con Keras para predecir si un rostro en una imagen tiene una mascarilla o no.

* **notebooks/VC_MaskDetector_Transfer Learning.ipynb** : Notebook con Transfer Learning del modelo pre-entrenado de ResNet18 con Pytorch para predecir si un rostro en una imagen tiene una mascarilla o no.

* **dataset/** : Este folder contiene los datasets utilizados para entrenar y validar los modelos clasificadores del uso de la mascarilla. _Repositorio Fuente:_ facial_mask_classifier (https://bit.ly/3beau7v)

## Documentación de apoyo 📚

Face Detection with Deep Learning using Multi Tasked Cascased CNN: https://towardsdatascience.com/face-detection-with-deep-learning-using-multi-tasked-cascased-cnn-8721435531d5

Basic classification: Classify images of clothing: https://www.tensorflow.org/tutorials/keras/classification

Train and evaluate with Keras: https://www.tensorflow.org/guide/keras/train_and_evaluate

Image classification from scratch in keras: https://towardsdatascience.com/image-detection-from-scratch-in-keras-f314872006c9

Transfer Learning for Computer Vision Tutorial: https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html

## Autores ✒️

* **Jorge Rodríguez Castillo** - [Linkedin](https://www.linkedin.com/in/jorge-rodr%C3%ADguez-castillo/) - [Github](https://github.com/jjrodcast)
* **Keven Fernández Carrillo** - [Linkedin](https://www.linkedin.com/in/keven-fern%C3%A1ndez-carrillo-50b07aa2/) - [Github](https://github.com/KevenRFC)
* **David Fosca Gamarra** - [Linkedin](https://www.linkedin.com/in/davidfoscagamarra/) - [Github](https://github.com/DavidFosca)

## Licencia 📄

Este proyecto está bajo la Licencia **GNU General Public License v3.0** - mira el archivo [LICENSE.md](LICENSE.md) para más detalles.

