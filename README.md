## Problema

**Escenario:** Estás desarrollando una API para un blog. La API debe permitir a los usuarios crear, leer, actualizar y eliminar entradas de blog y comentarios.

### Requisitos

1. Definir al menos dos modelos: uno para post, y otro para comentarios (o para usuarios).
2. Implementa serializadores para los modelos utilizados.
3. Configura las rutas para que la API permita realizar las operaciones CRUD sobre las entradas del blog y los comentarios, utilizando JSON.
4. Implementa una funcionalidad que permita listar todos los comentarios de un `Post` específico.

### Resultado

- Especificación del API
- Repositorio de código

### Respuesta 

1. Se genero uan API con Django Rest Framework con autentificacion por token
2. Se Realizaron los modeslos, vista y rutas para Post(publicaciones) y commnets (Comentarios)
3. se Incluyo django_filters para realizar filtrado de comentarios por publicacion



## Instrucciones

Crea entorno virtual
```
python -m venv .venv
```

Activarlo antes de correr django
```
source .venv/bin/activate
```

Crea migraciones necesarias
```
python manage.py makemigrations
python manage.py migrate
```

Genera un usuario admin con
```
python manage.py createsuperuser
```

Corre el servidor de desarrollo
```
python manage.py runserver
```

El servidor esta disponible en `http://localhost:8000`, el admin en `http://localhost:8000/admin` y el auth en `http://localhost:8000/api-auth/login`



### Instrucciones de USO de respesta

### registro
1.  realizar una peticion para generar un registro en base de datos de un autor o usuario

POST http://localhost:8000/register
{
  "email":"test1@email.com",
  "password":"password",
  "username":"test"  
}

### LOGN
2. Realizar una peticion acceder a la aplicacion y para generar un Token de autorizacion
POST http://localhost:8000/login
{
  "username":"test1",  
  "password":"test"
}

response:
{
  "token": "fd97c6d3c20280437a1eda4e4ebcb9756c08896a"
}


### post
3. ruta de Post(Publicaciones) para el uso del Django REST FRAMEWORK 
"api/post": "http://127.0.0.1:8000/api/post/"

3.1. ruta para el uso de filto para realizar una peticion de publicaciones filtradas por autor
http://localhost:8000/api/post/?id_author=1


### comment
4. ruta para Comment(Comentarios) el uso del Django REST FRAMEWORK
[http://localhost:8000/api/comment/?id_author=1&post=2

