# Servidor Web con Docker en Linux Mint

Este documento describe el proceso para crear un **servidor web sencillo** utilizando Docker en Linux Mint.
El objetivo es ejecutar el servidor de forma aislada para evitar que utilice todos los recursos del computador.

---

# 1️⃣ Actualizar el sistema

Primero se actualiza el sistema operativo para asegurar que todos los paquetes estén al día.

```bash
sudo apt update
sudo apt upgrade
```

---

# 2️⃣ Instalar Docker

Docker permitirá crear servidores aislados dentro del computador.

Instalar Docker:

```bash
sudo apt install docker.io
```

Activar el servicio de Docker:

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

Verificar la instalación:

```bash
docker --version
```

---

# 3️⃣ Crear una carpeta para el servidor

Se crea una carpeta dedicada para el servidor, lo que ayuda a organizar los archivos y evitar el uso innecesario de todo el disco.

```bash
mkdir ~/servidor
cd ~/servidor
```

---

# 4️⃣ Descargar la imagen de Nginx

Antes de ejecutar el contenedor, se descarga manualmente la imagen del servidor web.

```bash
sudo docker pull nginx
```

---

# 5️⃣ Crear un servidor web sencillo

Se crea un servidor web utilizando **Nginx** dentro de un contenedor Docker.

```bash
sudo docker run -d \
--name servidor_web \
-p 8080:80 \
--memory="1g" \
--cpus="1.0" \
nginx
```

Explicación de los parámetros:

* `-d` ejecuta el contenedor en segundo plano
* `--name` asigna un nombre al contenedor
* `-p 8080:80` conecta el puerto 8080 del PC con el puerto 80 del contenedor
* `--memory` limita el uso de memoria RAM
* `--cpus` limita el uso de CPU

El servidor quedará disponible en:

```
http://localhost:8080
```

---

# 6️⃣ Ver los contenedores activos

Para verificar que el servidor está en ejecución:

```bash
sudo docker ps
```

---

# 7️⃣ Detener el servidor

Para detener el contenedor:

```bash
sudo docker stop servidor_web
```

---

# 8️⃣ Crear almacenamiento separado (Opcional)

Para separar los archivos del servidor del sistema principal se puede crear una carpeta dedicada.

```bash
mkdir ~/servidor/web
```

Luego ejecutar el contenedor montando la carpeta como volumen:

```bash
sudo docker run -d \
--name servidor_web \
-p 8080:80 \
--memory="1g" \
--cpus="1.0" \
-v ~/servidor/web:/usr/share/nginx/html \
nginx
```

Esto permite que los archivos del sitio web se guarden directamente en la carpeta:

```
~/servidor/web
```

De esta manera el servidor utiliza almacenamiento separado del sistema principal.

---

# Conclusión

Con este procedimiento se logra:

* Crear un servidor web sencillo en Linux Mint.
* Ejecutar el servidor dentro de un contenedor Docker.
* Limitar el uso de CPU y memoria.
* Separar los archivos del servidor del sistema operativo.

Esto permite utilizar el computador como un pequeño entorno de pruebas para servidores y servicios web.
