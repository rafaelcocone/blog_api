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
